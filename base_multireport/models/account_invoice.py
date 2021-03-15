# -*- coding: utf-8 -*-
#
# Copyright 2016-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from datetime import datetime

from odoo import fields, models, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


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
        reportname = self.env['report'].select_reportname(self)
        return self.env['report'].get_action(
             self, reportname)


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    def get_order_ref_text(self, doc, report, line):
        order_ref_text = self.env[
            'report'].get_report_attrib('order_ref_text', doc, report)
        if not order_ref_text:
            return ''
        lang = self.env['res.lang'].search(
            [('code', '=', line.invoice_id.partner_id.lang)])
        if not lang:
            lang = self.env.user.company_id.partner_id.lang
        date_format = lang.date_format
        client_order_ref = ''
        order_name = ''
        date_order = ''
        if line.sale_line_ids:
            date_order = line.sale_line_ids[0].order_id.date_order
            if date_order:
                date_order = datetime.strptime(
                    date_order,
                    DEFAULT_SERVER_DATETIME_FORMAT).strftime(date_format)
            else:
                date_order = ''
            client_order_ref = line.sale_line_ids[
                0].order_id.client_order_ref or ''
            order_name = line.sale_line_ids.order_id.name
        ctx = {
            'order_name': order_name,
            'date_order': date_order,
            'client_order_ref': client_order_ref,
        }
        return order_ref_text % ctx

    def get_ddt_ref_text(self, doc, report, line):
        ddt_ref_text = self.env[
            'report'].get_report_attrib('ddt_ref_text', doc, report)
        if not ddt_ref_text:
            return ''
        lang = self.env['res.lang'].search(
            [('code', '=', line.invoice_id.partner_id.lang)])
        if not lang:
            lang = self.env.user.company_id.partner_id.lang
        date_format = lang.date_format
        date_ddt = ''
        date_done = ''
        ddt_number = ''
        if line.ddt_line_id:
            date_ddt = line.ddt_line_id.package_preparation_id.date
            if date_ddt:
                date_ddt = datetime.strptime(
                    date_ddt,
                    DEFAULT_SERVER_DATETIME_FORMAT).strftime(date_format)
            else:
                date_ddt = ''
            date_done = line.ddt_line_id.package_preparation_id.date
            if date_done:
                date_done = datetime.strptime(
                    date_done,
                    DEFAULT_SERVER_DATETIME_FORMAT).strftime(date_format)
            else:
                date_done = ''
            ddt_number = \
                line.ddt_line_id.package_preparation_id.ddt_number or ''
        ctx = {
            'ddt_number': ddt_number,
            'date_ddt': date_ddt,
            'date_done': date_done,
        }
        return ddt_ref_text % ctx

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
