# -*- coding: utf-8 -*-
# Copyright 2017 Gianmarco Conte (gconte@dinamicheaziendali.it)

from datetime import datetime
from odoo import fields, models
import odoo.addons.decimal_precision as dp


class AccountJournalInherit(models.Model):
    _inherit = "account.journal"

    central_journal_exclude = fields.Boolean("Exclude from General Journal")


class DateRangeInherit(models.Model):
    _inherit = "date.range"

    date_last_print = fields.Date("Last printed date")
    progressive_page_number = fields.Integer("Progressive of the page", default=0)
    progressive_line_number = fields.Integer("Progressive line", default=0)
    progressive_credit = fields.Float(
        "Progressive Credit",
        digits=dp.get_precision("Account"),
        default=lambda *a: float(),
    )
    progressive_debit = fields.Float(
        "Progressive Debit",
        digits=dp.get_precision("Account"),
        default=lambda *a: float(),
    )

    def get_fiscal_daterange(self):
        fiscal_daterange = self
        if self:
            date_start = datetime.strptime(self.date_start, "%Y-%m-%d").date()
            date_end = datetime.strptime(self.date_end, "%Y-%m-%d").date()
            fiscal_daterange = self.search([
                ("type_id.fiscal_year", "=", True),
                ("date_start", "<=", date_start),
                ("date_end", ">=", date_end)])
            fiscal_daterange = fiscal_daterange[0] if fiscal_daterange else self
        return fiscal_daterange
