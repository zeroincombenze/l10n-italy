# -*- coding: utf-8 -*-
# Copyright 2016 Davide Corio
# Copyright 2017 Alex Comba - Agile Business Group
# Copyright 2017 Lorenzo Battistini - Agile Business Group
# Copyright 2017 Marco Calcagni - Dinamiche Aziendali srl
# Copyright 2019-24 Antonio M. Vigliotti - SHS-Av srl

from odoo import fields, models


class AccountFiscalPosition(models.Model):
    _inherit = "account.fiscal.position"

    # Old deprected style field
    rc_type_id = fields.Many2one("account.rc.type", "RC Type (Deprecated)")
    rc_type = fields.Selection(
        selection=[
            ("", "No RC"),
            # ("local", "RC domestic"),
            ("self", "RC with self.invoice"),
        ],
        string="Reverse Charge Policy",
        default="",
    )
    partner_type = fields.Selection(
        selection=[("supplier", "Supplier"), ("other", "Company")],
        string="Self-Invoice Partner Type",
        default="",
    )
    self_journal_id = fields.Many2one(
        "account.journal",
        string="Self-Invoice Journal",
        domain=[("type", "=", "sale")],
        default="",
    )
    payment_journal_id = fields.Many2one(
        "account.journal",
        string="Self Invoice Payment Journal",
        help="Journal used to pay RC self invoices.",
    )
    transient_account_id = fields.Many2one(
        "account.account",
        string="Self Invoice Transitory Account",
        help="Transitory account used on self invoices.",
    )
