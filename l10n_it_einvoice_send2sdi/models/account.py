# -*- coding: utf-8 -*-

from odoo import api, fields, models

fatturapa_attachment_state_mapping = {
    'ready': 'ready',
    'sent': 'sent',
    'validated': 'delivered',
    'sender_error': 'error',
    'recipient_error': 'error',
    'rejected': 'error'
}

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    fatturapa_state = fields.Selection(
        [('ready', 'Ready to Send'),
         ('sent', 'Sent'),
         ('delivered', 'Delivered'),
         ('error', 'Error')],
        string='E-invoice State',
        compute='_compute_fatturapa_state',
        store='true',
    )

    @api.multi
    @api.depends('fatturapa_attachment_out_id.state')
    def _compute_fatturapa_state(self):
        for record in self:
            record.fatturapa_state = fatturapa_attachment_state_mapping.get(
                record.fatturapa_attachment_out_id.state)

    @api.multi
    def send_einvoice(self):
        for record in self:
            record.fatturapa_attachment_out_id.send_einvoice()
