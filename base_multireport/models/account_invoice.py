# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models, api


class AccountInvoice(models.Model):
    _inherit = ["account.invoice"]

    pdf_model = fields.Many2one(
        'multireport.model',
        'Quote/Order Report',
        help="Select Report to use when printing the Sales Order or Quote"
    )

    # Override print_quotation method in sale module
    @api.multi
    def invoice_print(self):
        self.ensure_one()
        self.sent = True
        reportname = self.env['report'].get_reportname(self)
        return self.env['report'].get_action(
             self, reportname)


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    def description_2_print(self):
        field_name = 'name'
        style = self.company_id.report_model_style.\
            description_mode_stock_picking_package_preparation
        value = self[field_name]
        if style in ('line1', 'nocode1'):
            value = value.split('\n')[0]
        if style in ('nocode', 'nocode1'):
            i = value.find(']')
            if value[0] == '[' and i >= 0:
                value = value[i + 1:].lstrip()
        return value

    def code_2_print(self):
        field_name = 'name'
        style = self.company_id.report_model_style.\
            description_mode_stock_picking_package_preparation
        value = self[field_name]
        if style in ('nocode', 'nocode1'):
            i = value.find(']')
            if value[0] == '[' and i >= 0:
                value = value[1:i]
        return value
