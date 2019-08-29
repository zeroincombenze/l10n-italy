# -*- coding: utf-8 -*-
# Copyright 2016-2019 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models, api


class AccountInvoice(models.Model):
    _inherit = ["account.invoice"]

    # pdf_model = fields.Many2one(
    #     'multireport.model',
    #     'Quote/Order Report',
    #     help="Select Report to use when printing the Invoice",
    #     copy=False
    # )

    due_records = fields.One2many(
        'account.move.line', 'invoice_id',
        domain=[('account_id.user_type_id.type', '=', 'receivable')],
        string='Due Dates', copy=False,
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

    def description_2_print(self, style_mode=None):
        if not style_mode:
            style_mode = self.company_id.report_model_style.\
                description_mode
        value = self.name
        if style_mode in ('line1', 'nocode1'):
            value = value.split('\n')[0]
        if style_mode in ('nocode', 'nocode1'):
            i = value.find(']')
            if value[0] == '[' and i >= 0:
                value = value[i + 1:].lstrip()
        return value

    def code_2_print(self, style_mode=None):
        if self.product_id and (not style_mode or style_mode != 'noprint'):
            value = self.product_id.default_code
        else:
            value = ''
        return value

    @api.depends('product_id')
    def _set_code(self):
        for line in self:
            if line.product_id:
                line.code = line.product_id.default_code
            else:
                line.code = False

    @api.depends('product_id', 'name')
    def _set_description(self):
        for line in self:
            line.description = line.description_2_print()

    code = fields.Char('Code',
                       compute='_set_code',
                       copy=False)
    description = fields.Char('Description',
                       compute='_set_description',
                       copy=False)