import logging
import re
from lxml import etree
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import datetime
import requests
import json
import hashlib
import pytz
from os0 import os0

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.addons.base.ir.ir_mail_server import MailDeliveryException

_logger = logging.getLogger(__name__)

RESPONSE_MAIL_REGEX = '[A-Z]{2}[a-zA-Z0-9]{11,16}_[a-zA-Z0-9]{,5}_[A-Z]{2}_' \
                      '[a-zA-Z0-9]{,3}'

evolve_stato_mapping = {
    "In attesa di risposta dopo aver inviato il documento": 'sent',
    "Ricevuta di consegna": 'validated',
    "Notifica di mancata consegna": 'validated',
    "Il documento non ha superato i controlli di validazione": 'validated',
    "Notifica di scarto": 'rejected'
}

class FatturaPAAttachmentOut(models.Model):

    _inherit = "fatturapa.attachment.out"

    state = fields.Selection([('ready', 'Ready to Send'),
                              ('sent', 'Sent'),
                              ('sender_error', 'Sender Error'),
                              ('recipient_error', 'Recipient Error'),
                              ('rejected', 'Rejected (PA)'),
                              ('validated', 'Delivered'),
                              ],
                             string='State',
                             default='ready',)

    last_sdi_response = fields.Text(
        string='Last Response from Exchange System', default='No response yet',
        readonly=True)
    sending_date = fields.Datetime("Sent Date", readonly=True)
    delivered_date = fields.Datetime("Delivered Date", readonly=True)
    sending_user = fields.Many2one("res.users", "Sending User", readonly=True)


    @api.multi
    def parse_pec_response(self, message_dict):
        message_dict['model'] = self._name
        message_dict['res_id'] = 0

        regex = re.compile(RESPONSE_MAIL_REGEX)
        attachments = [x for x in message_dict['attachments']
                       if regex.match(x.fname)]

        for attachment in attachments:
            response_name = attachment.fname
            message_type = response_name.split('_')[2]
            if attachment.fname.lower().endswith('.zip'):
                # not implemented, case of AT, todo
                continue
            root = etree.fromstring(attachment.content)
            file_name = root.find('NomeFile')
            fatturapa_attachment_out = False

            if file_name is not None:
                file_name = file_name.text
                fatturapa_attachment_out = self.search(
                    ['|',
                     ('datas_fname', '=', file_name),
                     ('datas_fname', '=', file_name.replace('.p7m', ''))])
                if len(fatturapa_attachment_out) > 1:
                    _logger.info('More than 1 out invoice found for incoming'
                                 'message')
                    fatturapa_attachment_out = fatturapa_attachment_out[0]
                if not fatturapa_attachment_out:
                    if message_type == 'MT':  # Metadati
                        # out invoice not found, so it is an incoming invoice
                        return message_dict
                    else:
                        _logger.info('Error: FatturaPA {} not found.'.format(
                            file_name))
                        # TODO Send a mail warning
                        return message_dict

            if fatturapa_attachment_out:
                id_sdi = root.find('IdentificativoSdI')
                receipt_dt = root.find('DataOraRicezione')
                message_id = root.find('MessageId')
                id_sdi = id_sdi.text if id_sdi is not None else False
                receipt_dt = receipt_dt.text if receipt_dt is not None \
                    else False
                message_id = message_id.text if message_id is not None \
                    else False
                if message_type == 'NS':  # 2A. Notifica di Scarto
                    error_list = root.find('ListaErrori')
                    error_str = ''
                    for error in error_list:
                        error_str += u"\n[%s] %s %s" % (
                            error.find('Codice').text if error.find(
                                'Codice') is not None else '',
                            error.find('Descrizione').text if error.find(
                                'Descrizione') is not None else '',
                            error.find('Suggerimento').text if error.find(
                                'Suggerimento') is not None else ''
                        )
                    fatturapa_attachment_out.write({
                        'state': 'sender_error',
                        'last_sdi_response': u'SdI ID: {}; '
                        u'Message ID: {}; Receipt date: {}; '
                        u'Error: {}'.format(
                            id_sdi, message_id, receipt_dt, error_str)
                    })
                elif message_type == 'MC':  # 3A. Mancata consegna
                    missed_delivery_note = root.find('Descrizione').text
                    fatturapa_attachment_out.write({
                        'state': 'recipient_error',
                        'last_sdi_response': u'SdI ID: {}; '
                        u'Message ID: {}; Receipt date: {}; '
                        u'Missed delivery note: {}'.format(
                            id_sdi, message_id, receipt_dt,
                            missed_delivery_note)
                    })
                elif message_type == 'RC':  # 3B. Ricevuta di Consegna
                    delivery_dt = root.find('DataOraConsegna').text
                    fatturapa_attachment_out.write({
                        'state': 'validated',
                        'delivered_date': fields.Datetime.now(),
                        'last_sdi_response': 'SdI ID: {}; '
                        'Message ID: {}; Receipt date: {}; '
                        'Delivery date: {}'.format(
                            id_sdi, message_id, receipt_dt, delivery_dt)
                    })
                elif message_type == 'NE':  # 4A. Notifica Esito per PA
                    esito_committente = root.find('EsitoCommittente')
                    if esito_committente is not None:
                        # more than one esito?
                        esito = esito_committente.find('Esito')
                        if esito is not None:
                            if esito.text == 'EC01':
                                state = 'validated'
                            elif esito.text == 'EC02':
                                state = 'rejected'
                            fatturapa_attachment_out.write({
                                'state': state,
                                'last_sdi_response': u'SdI ID: {}; '
                                u'Message ID: {}; Response: {}; '.format(
                                    id_sdi, message_id, esito.text)
                            })
                elif message_type == 'DT':  # 5. Decorrenza Termini per PA
                    description = root.find('Descrizione')
                    if description is not None:
                        fatturapa_attachment_out.write({
                            'state': 'validated',
                            'last_sdi_response': u'SdI ID: {}; '
                            u'Message ID: {}; Receipt date: {}; '
                            u'Description: {}'.format(
                                id_sdi, message_id, receipt_dt,
                                description.text)
                        })
                # not implemented - todo
                elif message_type == 'AT':  # 6. Avvenuta Trasmissione per PA
                    description = root.find('Descrizione')
                    if description is not None:
                        fatturapa_attachment_out.write({
                            'state': 'validated',
                            'last_sdi_response': (
                                u'SdI ID: {}; Message ID: {}; '
                                u'Receipt date: {};'
                                u' Description: {}'
                            ).format(
                                id_sdi, message_id, receipt_dt,
                                description.text)
                        })

                message_dict['res_id'] = fatturapa_attachment_out.id
        return message_dict

    def get_send_channel(self):
        company = False
        send_channel = False
        for invoice in self.out_invoice_ids:
            company = invoice.company_id
            break
        if company:
            send_channel = company.einvoice_sender_id
        return send_channel

    # Header alla chiamata Evolve
    def header(self, send_channel):
        now = datetime.datetime.now(pytz.timezone(
            'Europe/Rome')).strftime("%Y-%m-%d %H.%M.%S")
        aes = AES.new(os0.b(send_channel.client_key),
                      AES.MODE_CBC,
                      os0.b(send_channel.client_key[:16]))
        pad_text = PKCS7Encoder().encode(now)
        # print now
        headers = {
            'Content-Type': "application/json",
            # 'Host': send_channel.hub_ip_addr,
            'From': send_channel.client_id,
            'Authorization': "Bearer " + b64encode(aes.encrypt(pad_text))
        }
        _logger.info(headers)
        return headers

    @api.multi
    def send_verify_via_json(self, send_channel, invoice):

        for att in self:

            data = {
                'IdAzienda': int(send_channel.sender_company_id),
                'IdArchivio': 1 ,
                'Filtri': [
                    {
                        'NomeCampo': 'NumeroFattura',
                        'Criterio': '=',
                        'FromValue': invoice.number
                    }
                ]
            }

            _logger.info(json.dumps(data,
                            ensure_ascii=False))

            headers = self.header(send_channel)
            url = send_channel.sender_url + 'Cerca'

            response = requests.post(url,
                                     headers=headers,
                                     data=json.dumps(data,
                                                     ensure_ascii=False))

            try:
                data = response.json()
                _logger.info(response.text)
            except:
                att.state = 'sender_error'
                att.last_sdi_response = response.text
                return

            documenti = self.parse_evolve_verify(data['Documenti'])

            _logger.info(documenti)

            for k in evolve_stato_mapping.keys():
                _logger.info("Elaborazione " + k)
                if k in documenti:
                    att.state = evolve_stato_mapping[k]
                    att.last_sdi_response = json.dumps(documenti[k],
                                    ensure_ascii=False)
                    return

        return

    # Converte i valori restituiti da evolve in un array associativo
    def parse_evolve_verify(self, data):

        ret = {}

        for evolvedoc in data:
            documento = self.parse_evolve_documento(evolvedoc)

            if documento["StatoFattura"] not in ret:
                ret[documento["StatoFattura"]] = []

            ret[documento["StatoFattura"]].append(documento)

        return ret

    def parse_evolve_documento(self, data):

        ret = {}

        for campodinamico in data["CampiDinamici"]:
            ret[campodinamico["Nome"]] = campodinamico["Valore"]

        return ret

    @api.multi
    def send_verify_via_pec(self, send_channel, invoice):
        pass

    @api.multi
    def send_verify(self):
        send_channel = self.get_send_channel()
        # states = self.mapped('state')
        #if set(states) != set(['sent']):
        #    raise UserError(_("You can only verify 'Send' files."))

        invoice = self.out_invoice_ids
        if len(invoice) > 1:
            raise UserError(_("Multiple invoice to one xml"))

        if send_channel.method == 'JSON':
            return self.send_verify_via_json(send_channel, invoice)
        elif send_channel.method == 'PEC':
            return self.send_verify_via_pec(send_channel, invoice)
        else:
            raise UserError(_("Unsupported sending method"))

    @api.multi
    def send_verify_all(self):
        # Recupero tutte le fatture in modalita send
        attachments = self.env['fatturapa.attachment.out'].search([('state', '!=', 'ready'), ('state', '!=', 'validated')])
        #attachments = self.env['fatturapa.attachment.out'].search([])

        for attachment in attachments:
            attachment.send_verify()

    @api.multi
    def reset_to_ready(self):
        for att in self:
            if att.state == 'validated':
                raise UserError(
                    _("You can not reset files in 'Delivered' state.")
                )
            att.state = 'ready'

    @api.multi
    def send_via_json(self, send_channel):
        # Recupero i dati della fattura
        invoice = self.out_invoice_ids
        if len(invoice) > 1:
            raise UserError(_("Multiple invoice to one xml"))

        for att in self:
            # xml base64
            bytes = att.datas
            # xml decodificato
            xml = b64decode(bytes)
            # Hash sha256
            sha256 = hashlib.sha256()
            sha256.update(xml)

            data = {
                "Files" : [{
                    "Bytes":bytes,
                    "MimeType":"text/xml",
                    "Nome":att.name,
                    "Extension":"XML",
                    "Hash":sha256.hexdigest()
                }],
                "Documento":{
                    "Visible":True,
                    "IdAzienda": int(send_channel.sender_company_id),
                    "IdArchivio": 3,
                    "CampiDinamici":[{
                        "Nome":"NumeroFattura",
                        "Valore": invoice.number,
                        "CriterioPredefinito":"="
                    } , {
                        "Nome":"DataFattura",
                        "Valore":invoice.date,
                        "CriterioPredefinito":"="
                    }]
                }
            }

            # Header
            headers = self.header(send_channel)
            url = send_channel.sender_url + 'Salva'
            response = requests.post(url,
                                     headers=headers,
                                     data=json.dumps(data,
                                                     ensure_ascii=False))
            try:
                data = response.json()
                _logger.info(response.text)
            except:
                att.state = 'sender_error'
                att.last_sdi_response = response.text
                return

            if data['EsitoChiamata'] == 0:
                n = len(data['Documenti']) - 1
                stato = self.parse_evolve_documento(data['Documenti'][n])

                if stato["StatoInvioSdi"] == "Importato":
                    att.state = 'sent'
                    att.sending_date = fields.Datetime.now()
                    att.sending_user = self.env.user.id
                    att.last_sdi_response = response.text
                    return True
                else:
                    att.state = 'sender_error'
                    att.last_sdi_response = response.text
            else:
                att.state = 'sender_error'
                att.last_sdi_response = response.text

    @api.multi
    def send_via_pec(self, send_channel):
        self._check_fetchmail()
        for att in self:
            mail_message = self.env['mail.message'].create({
                'model': self._name,
                'res_id': att.id,
                'subject': att.name,
                'body': 'XML file for FatturaPA {} sent to Exchange System to '
                        'the email address {}.'
                .format(
                    att.name,
                    send_channel.email_exchange_system),
                'attachment_ids': [(6, 0, att.ir_attachment_id.ids)],
                'email_from': (
                    send_channel.email_from_for_fatturaPA),
                'reply_to': (
                    send_channel.email_from_for_fatturaPA),
                'mail_server_id': send_channel.pec_server_id.id,
            })

            mail = self.env['mail.mail'].create({
                'mail_message_id': mail_message.id,
                'body_html': mail_message.body,
                'email_to': send_channel.email_exchange_system,
                'headers': {
                    'Return-Path':
                    send_channel.email_from_for_fatturaPA
                }
            })

            if mail:
                try:
                    mail.send(raise_exception=True)
                    att.state = 'sent'
                    att.sending_date = fields.Datetime.now()
                    att.sending_user = self.env.user.id
                except MailDeliveryException as e:
                    att.state = 'sender_error'
                    mail.body = e[1]

    @api.multi
    def send_einvoice(self):
        states = self.mapped('state')
        if set(states) != set(['ready']):
            raise UserError(_("You can only send 'Ready to Send' files."))
        send_channel = self.get_send_channel()
        if send_channel.method == 'JSON':
            return self.send_via_json(send_channel)
        elif send_channel.method == 'PEC':
            return self.send_via_pec(send_channel)
        else:
            raise UserError(_("Unsupported sending method"))

    @api.multi
    def unlink(self):
        for att in self:
            if att.state != 'ready':
                raise UserError(_(
                    "You can only delete 'ready to send' files."
                ))
        return super(FatturaPAAttachmentOut, self).unlink()

    @api.model
    def _check_fetchmail(self):
        server = self.env['fetchmail.server'].search([
            ('is_fatturapa_pec', '=', True),
        ])
        if not server:
            raise UserError(_(
                "No incoming PEC server found. Please configure it."))
