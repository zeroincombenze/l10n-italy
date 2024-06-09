# -*- coding: utf-8 -*-
# Copyright 2015 Alessandro Camilli (<http://www.openforce.it>)
# Copyright 2018 Lorenzo Battistini - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class AccountFiscalPosition(models.Model):
    _inherit = "account.fiscal.position"

    withholding_tax_ids = fields.Many2many(
        "withholding.tax",
        "account_fiscal_position_withholding_tax_rel",
        "fiscal_position_id",
        "withholding_tax_id",
        string="Withholding Tax",
    )


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    @api.depends(
        "invoice_line_ids.price_subtotal",
        "invoice_line_ids.invoice_line_tax_wt_ids.tax",
        "tax_line_ids.amount",
        # "withholding_tax_line_ids.tax",
        "amount_total",
        "currency_id",
        "company_id",
        "date_invoice",
    )
    def _compute_amount(self):
        super(AccountInvoice, self)._compute_amount()
        dp_obj = self.env["decimal.precision"]
        for invoice in self:
            withholding_tax_amount = 0.0
            withholding_tax = False
            for wt_line in invoice.withholding_tax_line_ids:
                withholding_tax_amount += round(
                    wt_line.tax, dp_obj.precision_get("Account")
                )
                withholding_tax = True
            if withholding_tax_amount or withholding_tax:
                invoice.withholding_tax_amount = withholding_tax_amount
                invoice.withholding_tax = withholding_tax
                invoice._compute_net_pay()

    withholding_tax = fields.Boolean("Withholding Tax",
                                     compute="_compute_amount",)
    withholding_tax_line_ids = fields.One2many(
        "account.invoice.withholding.tax",
        "invoice_id",
        "Withholding Tax",
        readonly=True,
        copy=False,
        states={"draft": [("readonly", False)]},
    )
    withholding_tax_amount = fields.Float(
        compute="_compute_amount",
        digits=dp.get_precision("Account"),
        string="Withholding tax",
        store=True,
        readonly=True,
        copy=False,
    )

    @api.model
    def create(self, vals):
        invoice = super(
            AccountInvoice, self.with_context(mail_create_nolog=True)
        ).create(vals)

        if (
            any(line.invoice_line_tax_wt_ids for line in invoice.invoice_line_ids)
            and not invoice.withholding_tax_line_ids
        ):
            invoice.compute_taxes()

        return invoice

    @api.onchange("invoice_line_ids")
    def _onchange_invoice_line_wt_ids(self):
        self.ensure_one()
        wt_taxes_grouped = self.get_wt_taxes_values()
        wt_tax_lines = [(5, 0)]
        for tax in wt_taxes_grouped.values():
            wt_tax_lines.append((0, 0, tax))
        self.withholding_tax_line_ids = wt_tax_lines
        if wt_tax_lines:
            self.withholding_tax = True
        else:
            self.withholding_tax = False

    @api.multi
    def action_move_create(self):
        """
        Split amount withholding tax on account move lines
        """
        dp_obj = self.env["decimal.precision"]
        res = super(AccountInvoice, self).action_move_create()

        for inv in self:
            # Rates
            rate_num = 0
            for move_line in inv.move_id.line_ids:
                if move_line.account_id.internal_type not in ["receivable", "payable"]:
                    continue
                rate_num += 1
            if rate_num:
                wt_rate = round(
                    inv.withholding_tax_amount / rate_num,
                    dp_obj.precision_get("Account"),
                )
            wt_residual = inv.withholding_tax_amount
            # Re-read move lines to assign the amounts of wt
            i = 0
            for move_line in inv.move_id.line_ids:
                if move_line.account_id.internal_type not in ["receivable", "payable"]:
                    continue
                i += 1
                if i == rate_num:
                    wt_amount = wt_residual
                else:
                    wt_amount = wt_rate
                wt_residual -= wt_amount
                # update line
                move_line.write({"withholding_tax_amount": wt_amount})
            # Create WT Statement
            self.create_wt_statement()
        return res

    @api.multi
    def get_wt_taxes_values(self):
        tax_grouped = {}
        for invoice in self:
            for line in invoice.invoice_line_ids:
                taxes = []
                for wt_tax in line.invoice_line_tax_wt_ids:
                    res = wt_tax.compute_tax(line.price_subtotal)
                    tax = {
                        "id": wt_tax.id,
                        "sequence": wt_tax.sequence,
                        "base": res["base"],
                        "tax": res["tax"],
                    }
                    taxes.append(tax)

                for tax in taxes:
                    val = {
                        "invoice_id": invoice.id,
                        "withholding_tax_id": tax["id"],
                        "tax": tax["tax"],
                        "base": tax["base"],
                        "sequence": tax["sequence"],
                    }

                    key = (
                        self.env["withholding.tax"]
                        .browse(tax["id"])
                        .get_grouping_key(val)
                    )

                    if key not in tax_grouped:
                        tax_grouped[key] = val
                    else:
                        tax_grouped[key]["tax"] += val["tax"]
                        tax_grouped[key]["base"] += val["base"]
        return tax_grouped

    @api.one
    def create_wt_statement(self):
        """
        Create one statement for each withholding tax
        """
        wt_statement_obj = self.env["withholding.tax.statement"]
        for inv_wt in self.withholding_tax_line_ids:
            wt_base_amount = inv_wt.base
            wt_tax_amount = inv_wt.tax
            if self.type in ["in_refund", "out_refund"]:
                wt_base_amount = -1 * wt_base_amount
                wt_tax_amount = -1 * wt_tax_amount
            val = {
                "date": self.move_id.date,
                "move_id": self.move_id.id,
                "invoice_id": self.id,
                "partner_id": self.partner_id.id,
                "withholding_tax_id": inv_wt.withholding_tax_id.id,
                "base": wt_base_amount,
                "tax": wt_tax_amount,
            }
            wt_statement_obj.create(val)


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.model
    def _default_withholding_tax(self):
        result = []
        fiscal_position_id = self._context.get("fiscal_position_id", False)
        if fiscal_position_id:
            fp = self.env["account.fiscal.position"].browse(fiscal_position_id)
            wt_ids = fp.withholding_tax_ids.mapped("id")
            result.append((6, 0, wt_ids))
        return result

    invoice_line_tax_wt_ids = fields.Many2many(
        comodel_name="withholding.tax",
        relation="account_invoice_line_tax_wt",
        column1="invoice_line_id",
        column2="withholding_tax_id",
        string="W.T.",
        default=_default_withholding_tax,
    )


class AccountInvoiceWithholdingTax(models.Model):
    """
    Withholding tax lines in the invoice
    """

    _name = "account.invoice.withholding.tax"
    _description = "Invoice Withholding Tax Line"

    def _prepare_price_unit(self, line):
        # price_unit = 0
        price_unit = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
        return price_unit

    @api.depends("base", "tax", "invoice_id.amount_untaxed")
    def _compute_coeff(self):
        for inv_wt in self:
            if inv_wt.invoice_id.amount_untaxed:
                inv_wt.base_coeff = inv_wt.base / inv_wt.invoice_id.amount_untaxed
            if inv_wt.base:
                inv_wt.tax_coeff = inv_wt.tax / inv_wt.base

    invoice_id = fields.Many2one(
        "account.invoice", string="Invoice", ondelete="cascade"
    )
    withholding_tax_id = fields.Many2one(
        "withholding.tax", string="Withholding tax", ondelete="restrict"
    )
    sequence = fields.Integer("Sequence")
    base = fields.Float("Base")
    tax = fields.Float("Tax")
    base_coeff = fields.Float(
        "Base Coeff",
        compute="_compute_coeff",
        store=True,
        help="Coeff used\
         to compute amount competence in the riconciliation",
    )
    tax_coeff = fields.Float(
        "Tax Coeff",
        compute="_compute_coeff",
        store=True,
        help="Coeff used\
         to compute amount competence in the riconciliation",
    )
