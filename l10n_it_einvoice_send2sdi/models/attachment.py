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

    def get_send_channel(self):
        company = False
        send_channel = False
        for invoice in self.out_invoice_ids:
            company = invoice.company_id
            break
        if company:
            send_channel = company.einvoice_sender_id
        return send_channel

    def send_via_json_all(self):
        # Recupero tutte le fatture in modalita send
        attachments = self.env['fatturapa.attachment.out'].search([('state', '=', 'ready')])
        for attachment in attachments:
            attachment.send_via_json()

    @api.multi
    def send_verify_all(self):
        # Recupero tutte le fatture in modalita send
        attachments = self.env['fatturapa.attachment.out'].search([('state', '=', 'sent')])
        for attachment in attachments:
            attachment.send_verify()

    @api.multi
    def reset_to_ready(self):
        for att in self:
            if att.state != 'sender_error':
                raise UserError(
                    _("You can only reset files in 'Sender Error' state.")
                )
            att.state = 'ready'

    @api.multi
    def send_verify(self):
        send_channel = self.get_send_channel()
        if send_channel.method == 'JSON':
            states = self.mapped('state')
            if set(states) != set(['sent']):
                raise UserError(_("You can only verify 'Send' files."))

            invoice = self.env['account.invoice'].search([(
                    'fatturapa_attachment_out_id', '=', self.id)])
            if len(invoice) > 1:
                raise UserError(_("Multiple invoice to one xml"))

            for att in self:
                data = {
                    'IdAzienda': int(send_channel.sender_company_id),
                    'IdArchivio': 1,
                    'Filtri': {
                        0: {
                            'NomeCampo': 'NumeroFattura',
                            'Criterio': '=',
                            'Valore': invoice.number
                        }
                    }
                }

                headers = self.header(send_channel)
                url = send_channel.sender_url + 'Cerca'
                response = requests.post(url,
                                         headers=headers,
                                         data=json.dumps(data,
                                                         ensure_ascii=False))

                data = response.json()
                if data['EsitoChiamata'] == 0:
                    for campodinamico in data['Documenti'][0]['CampiDinamici']:
                        if campodinamico['Nome'] == "StatoFattura":
                            if campodinamico['Valore'] == 'Notifica di esito: documento accettato':
                                att.state = 'validated'
                                return

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
                    "IdArchivio":3,
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
            data = response.json()

            if data['EsitoChiamata'] == 0:
                for campodinamico in data['Documenti'][0]['CampiDinamici']:
                    if campodinamico['Nome'] == "StatoInvioSdi":
                        if campodinamico['Valore'] == 'Importato':
                            att.state = 'sent'
                            att.sending_date = fields.Datetime.now()
                            att.sending_user = self.env.user.id
                            return

            att.state = 'sender_error'
            raise UserError(data['ErrorMessage'])

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
            'Host': send_channel.hub_ip_addr,
            'From': send_channel.client_id,
            'Authorization': "Bearer " + b64encode(aes.encrypt(pad_text))
        }
        return headers

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
