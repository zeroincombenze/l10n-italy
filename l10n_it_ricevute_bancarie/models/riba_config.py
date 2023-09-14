# -*- coding: utf-8 -*-
# Copyright (C) 2012 Andrea Cometa.
# Email: info@andreacometa.it
# Web site: http://www.andreacometa.it
# Copyright (C) 2012 Associazione OpenERP Italia
# (<http://www.odoo-italia.org>).
# Copyright (C) 2012-2017 Lorenzo Battistini - Agile Business Group
# Copyright 2018-23 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class RibaConfiguration(models.Model):

    _name = "riba.configuration"
    _description = "Configuration parameters for Ricevute Bancarie"

    name = fields.Char("Description", size=64, required=True)
    type = fields.Selection(
        (("sbf", "Salvo buon fine"), ("incasso", "Al dopo incasso")),
        "Emission mode",
        required=True,
    )
    bank_id = fields.Many2one(
        "res.partner.bank",
        "Banca",
        required=True,
        help="Bank account used for Ri.Ba. issuing",
    )
    acceptance_journal_id = fields.Many2one(
        "account.journal",
        "Acceptance journal",
        domain=[("type", "=", "bank")],
        help="Journal used when Ri.Ba. is accepted by the bank",
    )
    acceptance_account_id = fields.Many2one(
        "account.account",
        "Acceptance account",
        domain=[("internal_type", "=", "receivable")],
        help="Account used when Ri.Ba. is accepted by the bank",
    )
    company_id = fields.Many2one(
        "res.company",
        "Company",
        required=True,
        default=lambda self: self.env["res.company"]._company_default_get(
            "riba.configuration"
        ),
    )
    accreditation_journal_id = fields.Many2one(
        "account.journal",
        "Accreditation journal",
        domain=[("type", "=", "bank")],
        help="Journal used when Ri.Ba. amount is accredited by the bank",
    )
    accreditation_account_debit_id = fields.Many2one(
        "account.account",
        "Accreditation account (debit side - Subject To Collection C/O)",
        oldname="bank_account_id",
        help="Account receiving amount when list is accepted by the bank.\n"
        "May be the liquidity bank account or a transitory account.",
        # domain=[("internal_type", "=", "liquidity")],
    )
    accreditation_account_credit_id = fields.Many2one(
        "account.account",
        "Accreditation account (credit side - C/O portfolio bank)",
        oldname="accreditation_account_id",
        help="Account used when Ri.Ba. is accepted by the bank",
        # domain=[("internal_type", "!=", "liquidity")],
    )
    accreditation2_account_debit_id = fields.Many2one(
        string="Accreditation account (debit side – supplemental)",
        comodel_name="account.account",
    )
    accreditation2_account_credit_id = fields.Many2one(
        string="Accreditation account (credit side – supplemental)",
        comodel_name="account.account",
    )
    liquidity_account_id = fields.Many2one(
        "account.account",
        "A/C Bank Account",
    )
    bank_expense_account_id = fields.Many2one(
        "account.account", "Bank Expenses account"
    )
    unsolved_journal_id = fields.Many2one(
        "account.journal",
        "Unsolved journal",
        domain=[("type", "=", "bank")],
        help="Journal used when Ri.Ba. is unsolved",
    )
    overdue_account_debit_id = fields.Many2one(
        "account.account",
        "Overdue Effects account (receivable)",
        oldname="overdue_account_credit_id",
        domain=[("internal_type", "=", "receivable")],
    )
    # overdue_account_credit_id = fields.Many2one(
    #     "account.account",
    #     "Overdue Bank account",
    # )
    overdue_expenses_account_id = fields.Many2one(
        "account.account", "Protest charge account"
    )
    settlement_journal_id = fields.Many2one(
        "account.journal",
        "Settlement Journal",
        help="Journal used when the clients finally pays the invoice to bank",
    )

    def get_default_value_by_list(self, field_name):
        if not self.env.context.get("active_id", False):             # pragma: no cover
            return False
        ribalist_model = self.env["riba.distinta"]
        ribalist = ribalist_model.browse(self.env.context["active_id"])
        return (
            ribalist.config_id[field_name]
            and ribalist.config_id[field_name].id
            or False
        )

    def get_default_value_by_list_line(self, field_name):
        if not self.env.context.get("active_id", False):             # pragma: no cover
            return False
        ribalist_line = self.env["riba.distinta.line"].browse(
            self.env.context["active_id"]
        )
        return (
            ribalist_line.distinta_id.config_id[field_name]
            and ribalist_line.distinta_id.config_id[field_name].id
            or False
        )

    def get_default_account_receivable(self, company):
        code = company.chart_template_id.property_account_receivable_id.code
        digits = company.chart_template_id.code_digits
        if len(code) < digits:
            code = (code + ("0" * digits))[:digits]
        res = self.env["account.account"].search(
            [
                ("company_id", "=", company.id),
                ("code", "=", code)
            ]
        )
        return res[0] if res else False

    @api.onchange("acceptance_journal_id",
                  "acceptance_account_id",
                  "accreditation_journal_id",
                  "accreditation_account_debit_id",
                  "accreditation_account_credit_id",
                  "bank_expense_account_id")
    def onchange_some_fields(self):
        if self.bank_expense_account_id and not self.overdue_expenses_account_id:
            self.overdue_expenses_account_id = self.bank_expense_account_id
        # if self.accreditation_account_debit_id and not self.overdue_account_credit_id:
        #     self.overdue_account_credit_id = self.accreditation_account_debit_id
        if self.acceptance_journal_id and not self.settlement_journal_id:
            self.settlement_journal_id = self.acceptance_journal_id
        if self.acceptance_journal_id and not self.accreditation_journal_id:
            self.accreditation_journal_id = self.acceptance_journal_id
        if self.acceptance_journal_id and not self.unsolved_journal_id:
            self.unsolved_journal_id = self.acceptance_journal_id
        if not self.overdue_account_debit_id:
            self.overdue_account_debit_id = self.get_default_account_receivable(
                self.company_id)
