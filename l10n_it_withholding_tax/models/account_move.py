# -*- coding: utf-8 -*-
# Copyright 2015 Alessandro Camilli (<http://www.openforce.it>)
# Copyright 2018 Lorenzo Battistini - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AccountPartialReconcile(models.Model):
    _inherit = "account.partial.reconcile"

    @api.model
    def create(self, vals):
        # In case of WT The amount of reconcile mustn't exceed the tot net
        # amount. The amount residual will be full reconciled with amount net
        # and amount wt created with payment
        invoice = False
        ml_ids = []
        if vals.get("debit_move_id"):
            ml_ids.append(vals.get("debit_move_id"))
        if vals.get("credit_move_id"):
            ml_ids.append(vals.get("credit_move_id"))
        for ml in self.env["account.move.line"].browse(ml_ids):
            domain = [("move_id", "=", ml.move_id.id)]
            invoice = self.env["account.invoice"].search(domain)
            if invoice:
                break
        # Limit value of reconciliation
        if invoice and invoice.withholding_tax and invoice.amount_net_pay:
            # We must consider amount in foreign currency, if present
            # Note that this is always executed, for every reconciliation.
            # Thus, we must not change amount when not in withholding tax case
            amount = vals.get("amount_currency") or vals.get("amount")
            if amount > invoice.amount_net_pay:
                vals.update({"amount": invoice.amount_net_pay})

        # Create reconciliation
        reconcile = super(AccountPartialReconcile, self).create(vals)
        # Avoid re-generate wt moves if the move line is an wt move.
        # It's possible if the user unreconciles a wt move under invoice
        ld = self.env["account.move.line"].browse(vals.get("debit_move_id"))
        lc = self.env["account.move.line"].browse(vals.get("credit_move_id"))

        if (
            lc.withholding_tax_generated_by_move_id
            or ld.withholding_tax_generated_by_move_id
        ):
            is_wt_move = True
        else:
            is_wt_move = False
        # Wt moves creation
        if (
            invoice.withholding_tax_line_ids
            and not self._context.get("no_generate_wt_move")
            and not is_wt_move
        ):
            # and not wt_existing_moves\
            reconcile.generate_wt_moves()

        return reconcile

    def _prepare_wt_move(self, vals):
        """
        Hook to change values before wt move creation
        """
        return vals

    @api.model
    def generate_wt_moves(self):
        wt_statement_obj = self.env["withholding.tax.statement"]
        # Reconcile lines
        line_payment_ids = []
        line_payment_ids.append(self.debit_move_id.id)
        line_payment_ids.append(self.credit_move_id.id)
        domain = [("id", "in", line_payment_ids)]
        rec_lines = self.env["account.move.line"].search(domain)

        # Search statements of competence
        wt_statements = False
        rec_line_statement = False
        for rec_line in rec_lines:
            domain = [("move_id", "=", rec_line.move_id.id)]
            wt_statements = wt_statement_obj.search(domain)
            if wt_statements:
                rec_line_statement = rec_line
                break
        # Search payment move
        rec_line_payment = False
        for rec_line in rec_lines:
            if rec_line.id != rec_line_statement.id:
                rec_line_payment = rec_line
        # Generate wt moves
        wt_moves = []
        for wt_st in wt_statements:
            amount_wt = wt_st.get_wt_competence(self.amount)
            # Date maturity
            p_date_maturity = False
            payment_lines = wt_st.withholding_tax_id.payment_term.compute(
                amount_wt, rec_line_payment.date or False
            )
            if payment_lines and payment_lines[0]:
                p_date_maturity = payment_lines[0][0][0]
            wt_move_vals = {
                "statement_id": wt_st.id,
                "date": rec_line_payment.date,
                "partner_id": rec_line_statement.partner_id.id,
                "reconcile_partial_id": self.id,
                "payment_line_id": rec_line_payment.id,
                "credit_debit_line_id": rec_line_statement.id,
                "withholding_tax_id": wt_st.withholding_tax_id.id,
                "account_move_id": rec_line_payment.move_id.id or False,
                "date_maturity": p_date_maturity or rec_line_payment.date_maturity,
                "amount": amount_wt,
            }
            wt_move_vals = self._prepare_wt_move(wt_move_vals)
            wt_move = self.env["withholding.tax.move"].create(wt_move_vals)
            wt_moves.append(wt_move)
            # Generate account move
            wt_move.generate_account_move()
        return wt_moves

    @api.multi
    def unlink(self):
        statements = []
        for rec in self:
            # To avoid delete if the wt move are paid
            domain = [("reconcile_partial_id", "=", rec.id), ("state", "!=", "due")]
            wt_moves = self.env["withholding.tax.move"].search(domain)
            if wt_moves:
                raise ValidationError(
                    _(
                        "Warning! Only Withholding Tax moves in Due status \
                    can be deleted"
                    )
                )
            # Statement to recompute
            domain = [("reconcile_partial_id", "=", rec.id)]
            wt_moves = self.env["withholding.tax.move"].search(domain)
            for wt_move in wt_moves:
                if wt_move.statement_id not in statements:
                    statements.append(wt_move.statement_id)

        res = super(AccountPartialReconcile, self).unlink()
        # Recompute statement values
        for st in statements:
            st._compute_total()
        return res


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.one
    def _prepare_wt_values(self):
        partner = False
        wt_competence = {}
        # First : Partner and WT competence
        for line in self.line_id:
            if line.partner_id:
                partner = line.partner_id
                if partner.property_account_position:
                    for wt in partner.property_account_position.withholding_tax_ids:
                        wt_competence[wt.id] = {
                            "withholding_tax_id": wt.id,
                            "partner_id": partner.id,
                            "date": self.date,
                            "account_move_id": self.id,
                            "wt_account_move_line_id": False,
                            "base": 0,
                            "amount": 0,
                        }
                break
        # After : Looking for WT lines
        wt_amount = 0
        for line in self.line_id:
            domain = []
            # WT line
            if line.credit:
                domain.append(("account_payable_id", "=", line.account_id.id))
                amount = line.credit
            else:
                domain.append(("account_receivable_id", "=", line.account_id.id))
                amount = line.debit
            wt_ids = self.pool["withholding.tax"].search(
                self.env.cr, self.env.uid, domain
            )
            if wt_ids:
                wt_amount += amount
                if (
                    wt_competence
                    and wt_competence[wt_ids[0]]
                    and "amount" in wt_competence[wt_ids[0]]
                ):
                    wt_competence[wt_ids[0]]["wt_account_move_line_id"] = line.id
                    wt_competence[wt_ids[0]]["amount"] = wt_amount
                    wt_competence[wt_ids[0]]["base"] = self.pool[
                        "withholding.tax"
                    ].get_base_from_tax(self.env.cr, self.env.uid, wt_ids[0], wt_amount)

        wt_codes = []
        if wt_competence:
            for _key, val in wt_competence.items():
                wt_codes.append(val)
        res = {
            "partner_id": partner and partner.id or False,
            "move_id": self.id,
            "invoice_id": False,
            "date": self.date,
            "base": wt_codes and wt_codes[0]["base"] or 0,
            "tax": wt_codes and wt_codes[0]["amount"] or 0,
            "withholding_tax_id": (
                wt_codes and wt_codes[0]["withholding_tax_id"] or False
            ),
            "wt_account_move_line_id": (
                wt_codes and wt_codes[0]["wt_account_move_line_id"] or False
            ),
            "amount": wt_codes[0]["amount"],
        }
        return res


class account_payment(models.Model):
    _inherit = "account.payment"

    @api.model
    def default_get(self, fields):
        """
        Redefine  amount to pay proportionally to amount total less wt
        """
        rec = super(account_payment, self).default_get(fields)
        invoice_defaults = self.resolve_2many_commands(
            "invoice_ids", rec.get("invoice_ids")
        )
        if invoice_defaults and len(invoice_defaults) == 1:
            invoice = invoice_defaults[0]
            if (
                "withholding_tax_amount" in invoice
                and invoice["withholding_tax_amount"]
            ):
                coeff_net = invoice["residual"] / invoice["amount_total"]
                rec["amount"] = invoice["amount_net_pay"] * coeff_net
        return rec


class account_register_payments(models.TransientModel):
    _inherit = "account.register.payments"

    @api.model
    def get_amount_residual(self, invoice):
        amount_residual = 0
        if invoice.withholding_tax_amount:
            coeff_net = invoice.residual / invoice.amount_total
            amount_residual = invoice.amount_net_pay * coeff_net
            return amount_residual
        return False

    @api.model
    def default_get(self, fields):
        rec = super(account_register_payments, self).default_get(fields)
        context = dict(self._context or {})
        active_model = context.get("active_model")
        active_ids = context.get("active_ids")
        invoices = self.env[active_model].browse(active_ids)
        total_amount = 0
        for inv in invoices:
            # Recompute residual amount only in case of WT
            # in the other case the standard amount(residual)
            # will be used
            amount_residual = self.get_amount_residual(inv)
            if inv.type in ["out_invoice", "in_refund"]:
                total_amount += amount_residual or inv.residual
            else:
                total_amount -= amount_residual or inv.residual
        rec["amount"] = abs(total_amount)
        return rec


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    withholding_tax_id = fields.Many2one(
        "withholding.tax",
        string="Withholding Tax",
        copy=False,
    )
    withholding_tax_base = fields.Float(
        string="Withholding Tax Base",
        copy=False,
    )
    withholding_tax_amount = fields.Float(
        string="Withholding Tax Amount",
        copy=False,
    )
    withholding_tax_generated_by_move_id = fields.Many2one(
        "account.move",
        string="Withholding Tax generated from",
        readonly=True,
        copy=False,
    )

    @api.multi
    def remove_move_reconcile(self):
        # When unreconcile a payment with a wt move linked, it will be
        # unreconciled also the wt account move
        for account_move_line in self:
            rec_move_ids = self.env["account.partial.reconcile"]
            domain = [
                (
                    "withholding_tax_generated_by_move_id",
                    "=",
                    account_move_line.move_id.id,
                )
            ]
            wt_mls = self.env["account.move.line"].search(domain)
            # Avoid wt move not in due state
            domain = [("wt_account_move_id", "in", wt_mls.mapped("move_id").ids)]
            wt_moves = self.env["withholding.tax.move"].search(domain)
            wt_moves.check_unlink()

            for wt_ml in wt_mls:
                rec_move_ids += wt_ml.matched_debit_ids
                rec_move_ids += wt_ml.matched_credit_ids
            rec_move_ids.unlink()
            # Delete wt move
            for wt_move in wt_mls.mapped("move_id"):
                wt_move.button_cancel()
                wt_move.unlink()

        return super(AccountMoveLine, self).remove_move_reconcile()

    @api.multi
    def prepare_move_lines_for_reconciliation_widget(
        self, target_currency=False, target_date=False
    ):
        """
        Net amount for invoices with withholding tax
        """
        res = super(AccountMoveLine, self).prepare_move_lines_for_reconciliation_widget(
            target_currency, target_date
        )
        for dline in res:
            if "id" in dline and dline["id"]:
                line = self.browse(dline["id"])
                if line.withholding_tax_amount:
                    dline["debit"] = (
                        line.debit - line.withholding_tax_amount if line.debit else 0
                    )
                    dline["credit"] = (
                        line.credit - line.withholding_tax_amount if line.credit else 0
                    )
                    dline["name"] += _(" (Net to pay: %s)") % (
                        dline["debit"] or dline["credit"]
                    )
        return res
