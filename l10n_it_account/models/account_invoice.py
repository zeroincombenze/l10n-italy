# -*- coding: utf-8 -*-
# Copyright 2021-24 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).
from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    amount_net_pay = fields.Float(
        string="Net to pay",
        store=True,
        digits=dp.get_precision("Account"),
        readonly=True,
        compute="_compute_net_pay",
    )
    hide_net_pay = fields.Boolean(string="Hide Net to pay",
                                  store=True,
                                  readonly=True,
                                  compute="_compute_net_pay")

    @api.depends("amount_total", "amount_tax")
    def _compute_net_pay(self):
        for inv in self:
            amount_sp = inv.amount_sp if hasattr(inv, "amount_sp") else 0.0
            amount_rc = inv.amount_rc if hasattr(inv, "amount_rc") else 0.0
            withholding_tax_amount = (
                inv.withholding_tax_amount
                if hasattr(inv, "withholding_tax_amount")
                else 0.0
            )
            inv.amount_net_pay = (
                inv.amount_total
                + amount_sp
                - withholding_tax_amount
                + amount_rc
            )
            inv.hide_net_pay = inv.amount_net_pay == inv.amount_total

    @api.onchange("fiscal_position_id")
    def _onchange_fiscal_position_id(self):
        # Here function should be overridden
        pass

    def get_receivable_line_ids(self):
        if not self.id:
            return []
        query = (
            "SELECT l.id "
            "FROM account_move_line l, account_invoice i "
            "WHERE i.id = %s AND l.move_id = i.move_id "
            "AND l.account_id = i.account_id order by date_maturity,abs(balance)"
        )
        self._cr.execute(query, (self.id,))
        return [row[0] for row in self._cr.fetchall()]


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.onchange("invoice_line_tax_ids")
    def _onchange_invoice_line_tax_ids(self):
        # Here function should be overridden
        pass
