# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import os
import logging
import re
from datetime import timedelta
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
    u'Inviato': 'sent',
    u'Inviata a Sdi': 'sent',
    u'In attesa di risposta dopo aver inviato il documento': 'sent',
    u'Importato': 'sent',
    u'Controlli validazione': 'sent',
    u'Notifica di scarto': 'rejected',
    u'Il documento non può essere preso in carico': 'rejected',
    u'Il documento non ha superato i controlli di validazione': 'rejected',
    u'Ricevuta di consegna': 'validated',
    u'Notifica di mancata consegna': 'recipient_error',
    u'Notifica di esito: documento rifiutato dalla PA': 'discarted',
    u'Notifica di esito: documento accettato': 'accepted',
    u'Notifica di decorrenza termini': 'recipient_error',
    u'ERRORE SCONOSCIUTO': 'sender_error',
}


class FatturaPAAttachmentIn(models.Model):

    _inherit = "fatturapa.attachment.in"

    @api.multi
    def import_xml_invoice(self):
        send_channel = self.env.user.company_id.einvoice_sender_id
        if send_channel is False:
            _logger.error('Undefined SDI channel')
            return
        if not send_channel.sender_url:
            _logger.error('Undefined URL of SDI channel')
            return

        headers = Evolve.header(send_channel)
        url = os.path.join(send_channel.sender_url, 'Cerca')
        archive = int(send_channel.param2) if send_channel.param2 else 2
        domain_mode = int(send_channel.param4) if send_channel.param4 else 0

        data = {
            'IdAzienda': int(send_channel.sender_company_id),
            'IdArchivio': archive,
            'Filtri': [],
        }
        if 0 < domain_mode <= 60:
            limit_date = (datetime.datetime.now() - timedelta(days=domain_mode)
                          ).strftime('%Y-%m-%dT%H:%M:%S')
            data['Filtri'] = [
                {
                    'NomeCampo': 'DataRicezione',
                    'Criterio': '>',
                    'FromValue': limit_date,
                }
            ]
        elif domain_mode == 0:
            data['Filtri'] = [
                {
                    'NomeCampo': 'DataDownload',
                    'Criterio': 'nullo',
                }
            ]

        _logger.info(json.dumps(data,
                        ensure_ascii=False))

        try:
            response = requests.post(url,
                                     headers=headers,
                                     data=json.dumps(data,
                                                     ensure_ascii=False))
        except BaseException:
            _logger.error('request.post FAILED')
            return
        if not (200 <= response.status_code < 300):
            _logger.error('FAILED request.post: %s' % response.status_code)
            return

        try:
            documenti = response.json()
            if documenti['EsitoChiamata'] > 0:
                _logger.info(response.text.replace(r'\r\n', '\n'))
                return
        except BaseException:
            return

        for value in documenti['Documenti']:
            documento = Evolve.parse_documento(value)
            self.import_xml_invoice_single(documento, send_channel, headers)

    # Import singolo documento
    def import_xml_invoice_single(self, documento, send_channel, headers):

        attach_model = self.env['fatturapa.attachment.in']

        attachments = attach_model.search([('uid', '=', documento["Uid"])])
        if (len(attachments)>0):
            return
        archive = int(send_channel.param2) if send_channel.param2 else 2

        data = {
            'Documento': {
                'IdAzienda': int(send_channel.sender_company_id),
                'IdArchivio': archive,
                'CampiDinamici': [
                    {
                        'Nome': 'Uid',
                        'Valore': documento["Uid"]
                    }
                ]
            },
            'Recupera': 2
        }

        url = os.path.join(send_channel.sender_url, 'Recupera')

        _logger.info(json.dumps(data,
                        ensure_ascii=False))

        try:
            response = requests.post(url,
                                     headers=headers,
                                     data=json.dumps(data,
                                                     ensure_ascii=False))
        except BaseException:
            _logger.error('request.post FAILED')
            return
        if not (200 <= response.status_code < 300):
            _logger.error('FAILED request.post: %s' % response.status_code)
            return

        try:
            documenti = response.json()
            if documenti['EsitoChiamata'] > 0:
                _logger.info(response.text.replace(r'\r\n', '\n'))
                return
        except BaseException:
            _logger.error(response.text.replace(r'\r\n', '\n'))
            return

        documento = Evolve.parse_documento(documenti["Documenti"][0])

        # Recupero il file xml
        for file in documenti["Files"]:
            if file["Nome"] == documento["NomeFile"]:
                filein = file
                break

        attach_vals = {
            'name': filein["Nome"],
            'datas_fname': filein["Nome"],
            'datas': filein["Bytes"],
            'uid': documento["Uid"]
        }

        try:
            attach_model.create(attach_vals)
        except BaseException as e:
            _logger.error('Error <%s> creating XML attachment' % e)


class FatturaPAAttachmentOut(models.Model):

    _inherit = "fatturapa.attachment.out"

    state = fields.Selection([('ready', 'Ready to Send'),
                              ('sent', 'Sent'),
                              ('sender_error', 'Sender Error'),
                              ('recipient_error', 'Recipient Error'),
                              ('rejected', 'Rejected'),
                              ('validated', 'Delivered'),
                              ('accepted', 'Accepted'),
                              ('discarted', 'Discarted by PA'),
                              ],
                             string='State',
                             default='ready',)

    last_sdi_response = fields.Text(
        string='Last Response from Exchange System',
        default='No response yet',
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
                        _logger.error('Error: FatturaPA {} not found.'.format(
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

    @api.model
    def get_send_channel(self):
        company = False
        send_channel = False
        for invoice in self.out_invoice_ids:
            company = invoice.company_id
            break
        if company:
            send_channel = company.einvoice_sender_id
        if send_channel is False:
            _logger.error('Undefined SDI channel')
        return send_channel

    @api.model
    def primitive_json_send(
            self, send_channel, req, chn_inv, action, attachment=None):
        if 'Documento' in req:
            req['Documento']['IdAzienda'] = int(send_channel.sender_company_id)
            req['Documento']['IdArchivio'] = chn_inv
        else:
            req['IdAzienda'] = int(send_channel.sender_company_id)
            req['IdArchivio'] = chn_inv
        headers = Evolve.header(send_channel)
        url = os.path.join(send_channel.sender_url, action)
        if send_channel.trace:
            _logger.info(
                '>>> %s.send_json(%s,%s,%s)' % (
                    send_channel.name, url, headers, req))
        try:
            response = requests.post(
                url, headers=headers, data=json.dumps(
                    req, ensure_ascii=False))
        except:
            errmsg = 'requests.post() FAILED!'
            if send_channel.trace:
                _logger.info('>>> %s' % errmsg)
            if attachment:
                attachment.state = 'sender_error'
            return False, errmsg
        if not (200 <= response.status_code < 300):
            errmsg = 'request.post FAILED: %s' % response.status_code
            _logger.error(errmsg)
            if attachment:
                attachment.state = 'sender_error'
                attachment.last_sdi_response = errmsg
            return False, errmsg
        try:
            data = response.json()
            errmsg = ''
            for item in ('ErrorStack', 'ErrorInnerExceptions', 'ErrorMessage'):
                if item in data:
                    errmsg += '%s = "%s"\n' % (item, data[item])
            if send_channel.trace:
                _logger.info(
                    '>>> response.json()=\n%s\n' % errmsg or data)
            if data['EsitoChiamata'] > 0:
                # Store response even if not trace enabled
                errmsg = response.text.replace(r'\r\n', '\n')
                if not send_channel.trace:
                    _logger.info(errmsg)
                if attachment:
                    attachment.state = 'sender_error'
                    attachment.last_sdi_response = errmsg
                return False, errmsg
        except:
            errmsg = 'response.json() FAILED!'
            if send_channel.trace:
                _logger.info('>>> %s' % errmsg)
            if attachment:
                attachment.state = 'sender_error'
            return False, errmsg
        return data, False

    @api.multi
    def send_verify_via_json(self, send_channel, invoice):
        for att in self:
            data, errmsg = self.search_via_json(send_channel, invoice.number)
            if not Evolve.has_document(data):
                limit_date = (datetime.datetime.now() - timedelta(days=1)
                              ).strftime('%Y-%m-%d %H:%M:%S')
                if not att.sending_date or (att.sending_date and
                        att.sending_date < limit_date):
                    att.state = 'ready'
                else:
                    att.state = 'sender_error'
                    if errmsg:
                        att.last_sdi_response = '%s\n%s\n%s' % (
                            'ERRORE DI COMUNICAZIONE!',
                            errmsg,
                            'Provare verifica Invio più tardi.')
                    else:
                        att.last_sdi_response = '%s\n%s' % (
                            'NO RISPOSTA DA SDI!',
                            'Fattura non (ancora) acquisita.')
                return
            history = '%-20.20s %-10.10s %-40.40s %-18.18s %-60.60s\n' % (
                'Data Caricamento', 'Data Fatt.',
                'UID', 'Stato Invio SdI', 'Note')
            last_date = '2019-01-01T00:00:00'
            last_ix = -1
            last_uid = ''
            documenti = Evolve.document_list(data['Documenti'])
            for ii, doc in enumerate(documenti):
                data_caricamento = doc.get('DataCaricamento',
                    doc['DataFattura'])
                if data_caricamento > last_date:
                    last_date = data_caricamento
                    last_uid = doc.get('Uid', '')
                    if 'Fattura duplicata' not in doc.get('Note', ''):
                        last_ix = ii
                history += '%-20.20s %-10.10s %-40.40s %-18.18s %-60.60s\n' % (
                    doc.get('DataCaricamento', ''),
                    doc['DataFattura'],
                    doc.get('Uid', ''),
                    Evolve.document_state(doc),
                    doc.get('Note', '')
                )
            limit_date = (datetime.datetime.now() - timedelta(days=10)
                          ).strftime('%Y-%m-%d %H:%M:%S')
            att_state = evolve_stato_mapping[
                Evolve.document_state(documenti[last_ix])]
            if (att_state == 'sent' and
                    att.sending_date and
                    att.sending_date < limit_date):
                att_state = 'recipient_error'
            att.state = att_state
            att.last_sdi_response = '%s\n\n%s\n' % (
                documenti[last_ix].get('Note', ''), history)

            documenti = Evolve.document_list(data['Documenti'])
            if len(documenti) == 0:
                att.state = 'sender_error'
                att.last_sdi_response = '%s\n\n%s\n' % (
                    'ERRORE DI SINCRONIZZAZIONE', history)
                return
            if att_state != 'sender_error':
                last_ix = -1
                valid_ix = -1
                for ii, doc in enumerate(documenti):
                    if evolve_stato_mapping[Evolve.document_state(
                            doc)] in ('accepted', 'discarted'):
                        last_ix = ii
                        break
                    elif doc.get('Uid', '') == last_uid:
                        last_ix = ii
                    elif evolve_stato_mapping[Evolve.document_state(
                            doc)] == 'validated':
                        valid_ix = ii
                    elif ('disponibile in consultazione nell\'area riservata'
                          in doc.get('Note', '')):
                        valid_ix = ii
                doc = documenti[last_ix]
                att_state = evolve_stato_mapping[Evolve.document_state(doc)]
                if valid_ix >= 0 and att_state in (
                        'sender_error', 'sent', 'rejected'):
                    last_ix = valid_ix
                    doc = documenti[last_ix]
                    if doc.get('StatoFattura'):
                        att_state = evolve_stato_mapping[doc['StatoFattura']]
                    else:
                        att_state = 'validated'

                if att_state == 'recipient_error':
                    delivered_date = datetime.datetime.strptime(
                        doc['DataFattura'], '%Y-%m-%dT%H:%M:%S') + timedelta(
                        days=120)
                    if delivered_date <  datetime.datetime.today():
                        att_state = 'validated'
                att.state = att_state
                att.last_sdi_response = (
                        'Tipo Documento=%s\n'
                        'Numero Fattura="%s"\n'
                        'Destinatario="%s"\n'
                        'P.IVA destinatario="%s"\n'
                        'Stato invio fattura="%s"\n'
                        'Note="%s"\n'
                        '\nCronologia invii\n'
                        '%s\n' % (doc.get('TipoDocumento'),
                                  doc.get('NumeroFattura'),
                                  doc.get('Destinatario'),
                                  doc.get('DestinatarioPartitaIva', ''),
                                  Evolve.document_state(doc),
                                  doc.get('Note', ''),
                                  history))

    @api.multi
    def send_verify_via_pec(self, send_channel, invoice):
        pass

    @api.multi
    def send_verify(self):
        send_channel = self.get_send_channel()
        if send_channel is False:
            raise UserError(_('Undefined SDI channel'))

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
        date_limit_no_pa = (datetime.datetime.now() - timedelta(
            days=30)).strftime('%Y-%m-%d')
        date_limit_pa = (datetime.datetime.now() - timedelta(
            days=150)).strftime('%Y-%m-%d')
        attachments = self.env['fatturapa.attachment.out'].search(
            ['|', '|',
             ('state', '=', 'sent'),
             '&',
             ('state', 'in', ['recipient_error', 'sender_error']),
             ('sending_date', '>=', date_limit_no_pa),
             '&',
             ('sending_date', '>=', date_limit_pa),
             ('invoice_partner_id.is_pa', '=', True)])
        for attachment in attachments:
            attachment.send_verify()
            # commit every table to avoid too big transaction
            self.env.cr.commit()  # pylint: disable=invalid-commit

    @api.multi
    def reset_to_ready(self):
        for att in self:
            if att.state == 'validated':
                raise UserError(
                    _("You can not reset files in 'Delivered' state.")
                )
            att.state = 'ready'

    @api.multi
    def set_to_delivered(self):
        for att in self:
            if att.state != 'recipient_error':
                raise UserError(
                    _("You can not reset files in 'recipient_error' state.")
                )
            att.state = 'validated'

    @api.model
    def search_via_json(self, send_channel, invoice_number):
        chn_inv_out = int(send_channel.param1) if send_channel.param1 else 1
        chn_inv_sent = int(send_channel.param3) if send_channel.param3 else 3
        request = {
            'Filtri': [
                {
                    'NomeCampo': 'NumeroFattura',
                    'Criterio': '=',
                    'FromValue': invoice_number
                }
            ]
        }
        data, errmsg = self.primitive_json_send(
            send_channel, request, chn_inv_out, 'Cerca')
        if data and data['EsitoChiamata'] > 0:
            data, errmsg = self.primitive_json_send(
                send_channel, request, chn_inv_sent, 'Cerca')
        return data, errmsg

    @api.multi
    def send_via_json(self, send_channel):
        # Recupero i dati della fattura
        invoice = self.out_invoice_ids
        if len(invoice) > 1:
            raise UserError(_("Multiple invoice to one xml"))

        chn_inv_sent = int(send_channel.param3) if send_channel.param3 else 3
        for att in self:
            data, errmsg = self.search_via_json(send_channel, invoice.number)
            if Evolve.has_document(data):
                att.state = 'sent'
                continue

            bytes = att.datas
            xml = b64decode(bytes)
            sha256 = hashlib.sha256()
            sha256.update(xml)
            request = {
                "Files": [{
                    "Bytes": bytes,
                    "MimeType": "text/xml",
                    "Nome": att.name,
                    "Extension": "XML",
                    "Hash": sha256.hexdigest()
                }],
                "Documento": {
                    "Visible": True,
                    "CampiDinamici": [{
                        "Nome": "NumeroFattura",
                        "Valore": invoice.number,
                        "CriterioPredefinito": "="
                    }, {
                        "Nome": "DataFattura",
                        "Valore": invoice.date,
                        "CriterioPredefinito": "="
                    }]
                }
            }
            data, errmsg = self.primitive_json_send(
                send_channel, request, chn_inv_sent, 'Salva', attachment=att)

            if data and data['EsitoChiamata'] == 0:
                stato = Evolve.parse_documento(data['Documenti'][-1])
                if stato["StatoInvioSdi"]:
                    att.state = evolve_stato_mapping[
                        stato['StatoInvioSdi']]
                    att.sending_date = fields.Datetime.now()
                    att.sending_user = self.env.user.id
                    att.last_sdi_response = 'Fattura Importata'
                    return True
                else:
                    if send_channel.trace:
                        _logger.info(
                            '>>>     response.json() failed: not imported!')
                    att.state = 'sender_error'
                    att.last_sdi_response = 'ERRORE IMPORTAZIONE FATTTURA'
            else:
                if send_channel.trace:
                    _logger.info('>>>     response.json() failed: esito != 0!')
                att.state = 'sender_error'
                att.last_sdi_response = 'ERRORE FATTTURA NON IMPORTATA'

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
            if att.state not in ('ready', 'rejected', 'discarted'):
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


class Evolve():

    @staticmethod
    def has_document(data):
        if data and data['EsitoChiamata'] == 0:
            return len(data['Documenti']) > 0
        return False

    @staticmethod
    def document_list(data):
        res = []
        for doc in data:
            documento = Evolve.parse_documento(doc)
            res.append(documento)
        return res

    @staticmethod
    def document_state(documento):
        if 'StatoFattura' in documento:
            return documento['StatoFattura']
        elif 'StatoInvioSdi' in documento:
            return documento['StatoInvioSdi']
        return 'ERRORE SCONOSCIUTO'

    @staticmethod
    def documenti_by_state(data):
        res = {}
        for doc in data['Documenti']:
            documento = Evolve.parse_documento(doc)
            if documento["StatoFattura"] not in res:
                res[documento["StatoFattura"]] = []
            res[documento["StatoFattura"]].append(documento)
        return res

    @staticmethod
    def parse_documento(data):
        res = {}
        for campodinamico in data["CampiDinamici"]:
            res[campodinamico["Nome"]] = campodinamico["Valore"]
        return res

    @staticmethod
    def header(send_channel):
        if send_channel is False or not send_channel.client_key:
            return False
        now = datetime.datetime.now(pytz.timezone(
            'Europe/Rome')).strftime("%Y-%m-%d %H.%M.%S")
        aes = AES.new(os0.b(send_channel.client_key),
                      AES.MODE_CBC,
                      os0.b(send_channel.client_key[:16]))
        pad_text = PKCS7Encoder().encode(now)
        headers = {
            'Content-Type': "application/json",
            'From': send_channel.client_id,
            'Authorization': "Bearer " + b64encode(aes.encrypt(pad_text))
        }
        # _logger.info(headers)
        return headers
