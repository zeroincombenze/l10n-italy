# -*- coding: utf-8 -*-
# Copyright 2015    Davide Corio <davide.corio@abstract.it>
# Copyright 2015-16 Lorenzo Battistini - Agile Business Group
# Copyright 2016    Alessio Gerace - Agile Business Group
# Copyright 2018-22 Antonio M. Vigliotti - SHS-AV s.r.l.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError

import odoo.addons.decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    amount_sp = fields.Float(
        string="Split Payment",
        digits=dp.get_precision("Account"),
        store=True,
        readonly=True,
        copy=False,
        compute="_compute_amount",
    )
    split_payment = fields.Boolean(
        "Split Payment",
        related="fiscal_position_id.split_payment",
        copy=False,
    )

    @api.depends(
        "invoice_line_ids.price_subtotal",
        "tax_line_ids.amount",
        "amount_total",
        "currency_id",
        "company_id",
        "date_invoice",
    )
    def _compute_amount(self):
        super(AccountInvoice, self)._compute_amount()
        for invoice in self:
            invoice.amount_sp = 0.0
            if invoice.fiscal_position_id.split_payment:
                invoice.amount_sp = -invoice.amount_tax
                invoice._compute_net_pay()

    @api.onchange("fiscal_position_id")
    def _onchange_fiscal_position_id(self):
        res = super(AccountInvoice, self)._onchange_fiscal_position_id()
        for line in self.invoice_line_ids:
            res = line._onchange_invoice_line_tax_ids()
            if res:
                return res
        return res

    def reconcile_sp_invoice(self, invoice):
        reconcile_model = self.env["account.move.line.reconcile"]
        # move_line_model = self.env['account.move.line']
        ids = invoice.get_receivable_line_ids()
        reconcile_model.with_context(active_ids=ids).trans_rec_reconcile_full()

    def _build_sp_debit_line(self):
        if not self.company_id.sp_account_id:
            raise UserError(
                _(
                    "Please set 'Split Payment Write-off Account' field in"
                    " accounting configuration"
                )
            )
        if not self.company_id.sp_tax_id:
            raise UserError(
                _(
                    "Please set 'Split Payment Write-off Tax' field in"
                    " accounting configuration"
                )
            )
        vals = {
            "name": _("Split Payment Write Off"),
            "partner_id": self.partner_id.id,
            "account_id": self.company_id.sp_account_id.id,
            "journal_id": self.journal_id.id,
            "date": self.date_invoice,
            "date_maturity": self.date_invoice,
            "debit": abs(self.amount_sp),
            "credit": 0,
            "tax_line_id": self.company_id.sp_tax_id.id,
        }
        if self.type == "out_refund":
            vals["debit"] = 0
            vals["credit"] = abs(self.amount_sp)
        return vals

    def _build_sp_credit_line(self, invoice):
        move_line_pool = self.env["account.move.line"]
        ids = invoice.get_receivable_line_ids()
        if ids:
            account_id = move_line_pool.browse(ids[0]).account_id
        else:
            account_id = self.company_id.sp_account_id
        vals = {
            "name": _("Split Payment Write Off"),
            "partner_id": self.partner_id.id,
            "account_id": account_id.id,
            "journal_id": self.journal_id.id,
            "date": self.date_invoice,
            "date_maturity": self.date_invoice,
            "credit": abs(self.amount_sp),
            "debit": 0,
            "tax_line_id": self.company_id.sp_tax_id.id,
        }
        if self.type == "out_refund":
            vals["credit"] = 0
            vals["debit"] = abs(self.amount_sp)
        return vals

    @api.multi
    def get_vat_spl_line_ids(self):
        # return the move line ids with the split payment
        if not self.id:
            return []
        query = (
            """select id,name from account_move_line
                where invoice_id=%d and tax_line_id in
                (select x.tax_dest_id
                from account_fiscal_position f, account_fiscal_position_tax x
                where x.position_id = f.id and f.split_payment = true);"""
            % self.id
        )
        self._cr.execute(query, (self.id,))
        return [row[0] for row in self._cr.fetchall()]

    @api.multi
    def _compute_split_payments(self):
        def _revaluate_amount(receivable_line, db_cr, vat_assigned):
            receivable_line_amount = receivable_line[db_cr] - (
                invoice.amount_tax * receivable_line[db_cr] / invoice.amount_total
            )
            if not vat_assigned:
                receivable_line_amount += invoice.amount_tax
            diff = receivable_line[db_cr] - receivable_line_amount
            vals = {db_cr: receivable_line_amount}
            if not vat_assigned:
                vals["name"] = _("Importo + IVA split-payment")
            receivable_line.with_context(check_move_validity=False).write(vals)
            return diff

        for invoice in self:
            receivable_line_ids = invoice.get_receivable_line_ids()
            move_line_pool = self.env["account.move.line"]
            vat_assigned = False
            diff = 0.0
            for receivable_line in move_line_pool.browse(receivable_line_ids):
                if invoice.type == "out_invoice" and receivable_line.debit:
                    diff += _revaluate_amount(receivable_line, "debit", vat_assigned)
                elif invoice.type == "out_refund" and receivable_line.credit:
                    diff += _revaluate_amount(receivable_line, "credit", vat_assigned)
                vat_assigned = True
            if diff:
                receivable_line = move_line_pool.browse(receivable_line_ids[0])
                if invoice.type == "out_invoice" and receivable_line.debit:
                    vals = {"debit": receivable_line.debit + diff}
                elif invoice.type == "out_refund" and receivable_line.credit:
                    vals = {"credit": receivable_line.credit + diff}
                receivable_line.with_context(check_move_validity=False).write(vals)

    @api.multi
    def action_move_create(self):
        res = super(AccountInvoice, self).action_move_create()
        for invoice in self:
            if invoice.fiscal_position_id and invoice.fiscal_position_id.split_payment:
                if invoice.type in ["in_invoice", "in_refund"]:
                    raise UserError(
                        _("Can't handle supplier invoices with split payment")
                    )
                posted = False
                if invoice.move_id.state == "posted":
                    posted = True
                    invoice.move_id.state = "draft"
                self._compute_split_payments()
                line_model = self.env["account.move.line"]
                write_off_line_vals = invoice._build_sp_debit_line()
                write_off_line_vals["move_id"] = invoice.move_id.id
                line_model.with_context(check_move_validity=False).create(
                    write_off_line_vals
                )
                write_off_line_vals = invoice._build_sp_credit_line(invoice)
                write_off_line_vals["move_id"] = invoice.move_id.id
                line_model.with_context(check_move_validity=False).create(
                    write_off_line_vals
                )
                if posted:
                    invoice.move_id.state = "posted"
                self.reconcile_sp_invoice(invoice)
        return res


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.onchange("invoice_line_tax_ids")
    def _onchange_invoice_line_tax_ids(self):
        res = super(AccountInvoiceLine, self)._onchange_invoice_line_tax_ids()
        if self.invoice_id.type in ["out_invoice", "out_refund"]:
            inv_with_sp = self.invoice_id.fiscal_position_id.split_payment
        else:
            inv_with_sp = False
        for tax in self.invoice_line_tax_ids:
            if tax.payability == "S" and not inv_with_sp:
                return {
                    "warning": {
                        "title": "Invalid tax code",
                        "message": (
                            "Invalid tax code '%s' for fiscal position %s!\n"
                            "You need a Split Payment fiscal position to do this."
                            % (tax.name, self.invoice_id.fiscal_position_id.name)),
                    }
                }
            elif tax.amount and tax.payability != "S" and inv_with_sp:
                return {
                    "warning": {
                        "title": "Invalid tax code",
                        "message": (
                            "Invalid tax code '%s' for fiscal position %s!\n"
                            "Please use just Split Payment tax code."
                            % (tax.name, self.invoice_id.fiscal_position_id.name)),
                    }
                }
        return res
