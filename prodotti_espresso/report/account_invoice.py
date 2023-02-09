# -*- coding: utf-8 -*-
from odoo import api, models, fields
# from odoo.exceptions import UserError
# from odoo.tools.float_utils import float_compare, float_is_zero


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.depends('invoice_line_ids')
    def _with_espresso(self):
        for inv in self:
            if inv.state != 'draft' or not inv.invoice_line_ids:
                continue
            espresso = False
            for line in inv.invoice_line_ids:
                if line.espresso:
                    espresso = True
                    break
            inv.espresso = espresso

    espresso = fields.Boolean(
        string="Prodotto espresso",
        computed="_with_espresso",
    )


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    espresso = fields.Boolean(
        string="Prodotto espresso",
        related="product_id.espresso",
    )


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    espresso = fields.Boolean(string="Prodotto espresso")

    def _select(self):
        return super(AccountInvoiceReport, self)._select(
        ) + ", sub.espresso"

    def _sub_select(self):
        return super(AccountInvoiceReport, self)._sub_select(
        ) + ",pt.espresso as espresso"

    def _group_by(self):
        return super(AccountInvoiceReport, self)._group_by() + ", pt.espresso"
