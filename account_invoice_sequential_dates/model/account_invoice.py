#
# Copyright 2017-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import datetime

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def _check_4_inv_date(self):

        def _check_date(invoice, date_invoice, date_name):
            if date_invoice and invoice.state == 'draft':
                # Check for then last date (1.st validation)
                msg = _(r'Invalid invoice date. '
                        'Found invoice with date next to this one. '
                        'Please use date since %s')
                if not invoice.move_name:
                    domain = [('type', '=', invoice.type),
                              ('journal_id', '=', invoice.journal_id.id),
                              (date_name, '>', date_invoice),
                              ('state', 'not in', [
                                  'draft', 'cancel', 'proforma', 'proforma2'])]
                    res = invoice.search(domain, limit=1)
                    if res:
                        return res, msg
                # Check for interval date, if re-validation
                if invoice.move_name:
                    domain = [('type', '=', invoice.type),
                              ('journal_id', '=', invoice.journal_id.id),
                              (date_name, '>', date_invoice),
                              ('state', 'not in', [
                                  'draft', 'cancel', 'proforma', 'proforma2']),
                              ('number', '<', invoice.move_name)]
                    res = invoice.search(domain, limit=1)
                    if res:
                        return res, msg
                    msg = _(r'Invalid invoice date. '
                            'Found invoice with date prior to this one. '
                            'Please set date %s')
                    domain = [('type', '=', invoice.type),
                              ('journal_id', '=', invoice.journal_id.id),
                              (date_name, '<', date_invoice),
                              ('state', 'not in', [
                                  'draft', 'cancel', 'proforma', 'proforma2']),
                              ('number', '>', invoice.move_name)]
                    res = invoice.search(domain, limit=1)
                    if res:
                        return res, msg
            return [], ''

        for invoice in self:
            if not invoice.journal_id.check_4_sequence:
                continue
            res = False
            if invoice.type in ('in_invoice', 'in_refund'):
                date_invoice = invoice.date
                date_name = 'date'
            elif invoice.type in ('out_invoice', 'out_refund'):
                date_invoice = invoice.date_invoice
                date_name = 'date_invoice'
            if date_invoice:
                res, msg = _check_date(invoice, date_invoice, date_name)
            if res:
                raise UserError(msg % datetime.datetime.strftime(
                    fields.Date.from_string(res[0][date_name]),
                    self.env['res.lang'].search(

                        [('code', '=', self.env.user.lang)]).date_format))
        return True

    @api.multi
    def action_move_create(self):
        res = super(AccountInvoice, self).action_move_create()
        self._check_4_inv_date()
        return res

