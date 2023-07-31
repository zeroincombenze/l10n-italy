# -*- coding: utf-8 -*-
# Copyright 2017 Gianmarco Conte (gconte@dinamicheaziendali.it)

from datetime import datetime, timedelta

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError
from odoo.tools.misc import flatten


class WizardGiornale(models.TransientModel):
    _name = "wizard.giornale"
    _description = "Wizard journal report"

    @api.model
    def _get_journal(self):
        journal_obj = self.env["account.journal"]
        if self.company_id:
            journal_ids = journal_obj.search(
                [
                    ("central_journal_exclude", "=", False),
                    ("company_id", "=", self.company_id.id),
                ]
            )
        else:
            journal_ids = journal_obj.search(
                [
                    ("central_journal_exclude", "=", False),
                ]
            )
        return journal_ids

    @api.model
    def _get_default_daterange(self):
        daterange_cls = self.env["date.range"]
        def_daterange = daterange_cls.search([
            ("type_id.fiscal_year", "=", True),
            ("date_last_print", "!=", False)],
            order="date_last_print desc", limit=1)
        if not def_daterange:
            # Never printed
            def_daterange = daterange_cls.search([("type_id.fiscal_year", "=", True)],
                                                 order="date_start", limit=1)
        elif def_daterange[0].date_last_print == def_daterange[0].date_end:
            # Printed until end of year
            def_daterange = daterange_cls.search([
                ("type_id.fiscal_year", "=", True),
                ("date_start", ">", def_daterange[0].date_end)],
                order="date_start", limit=1)
        return def_daterange[0].id if def_daterange else False

    date_move_line_from = fields.Date("From date", required=True)
    date_move_line_from_view = fields.Date("From date")
    last_def_date_print = fields.Date("Last definitive date print")
    first_date_print = fields.Date("First date to print")
    date_move_line_to = fields.Date("To date", required=True)
    daterange = fields.Many2one(
        "date.range", "Date Range",
        required=True,
        default=_get_default_daterange)
    company_id = fields.Many2one(
        related="daterange.company_id", readonly=True, store=True
    )
    progressive_credit = fields.Float("Progressive Credit")
    progressive_debit = fields.Float("Progressive debit")
    print_state = fields.Selection(
        [("print", "Ready for printing"), ("printed", "Printed")],
        "State",
        default="print",
        readonly=True,
    )
    journal_ids = fields.Many2many(
        "account.journal",
        "giornale_journals_rel",
        "journal_id",
        "giornale_id",
        default=_get_journal,
        string="Journals",
        required=True,
    )
    target_move = fields.Selection(
        [("all", "All"), ("posted", "Posted"), ("draft", "Draft")],
        "Target Move",
        default="posted",
    )
    fiscal_page_base = fields.Integer("Last printed page", required=True)
    start_row = fields.Integer("Start row", required=True)
    year_footer = fields.Char(
        string="Year for Footer", help="Value printed near number of page in the footer"
    )

    @api.onchange("daterange")
    def on_change_daterange(self):
        if self.daterange:
            fiscal_daterange = self.daterange.get_fiscal_daterange()
            self.load_values_from_fiscalyear(fiscal_daterange)

    @api.onchange("date_move_line_from")
    def on_change_date_start(self):
        if self.date_move_line_from:
            self.year_footer = str(
                datetime.strptime(self.date_move_line_from, "%Y-%m-%d").year
            )

    def load_values_from_fiscalyear(self, fiscal_daterange):
        date_start = datetime.strptime(
            fiscal_daterange.date_start, "%Y-%m-%d").date()
        if fiscal_daterange.date_last_print and (
                self.daterange.date_start
                <= fiscal_daterange.date_last_print
                <= self.daterange.date_end
        ):
            # Selected valid fiscal year
            date_last_print = datetime.strptime(
                fiscal_daterange.date_last_print, "%Y-%m-%d"
            ).date()
            # First valid date to print final journal
            self.last_def_date_print = date_last_print
            # Read-only field does not pass to wizard, so we do backup
            self.date_move_line_from_view = self.last_def_date_print
            self.date_move_line_from = self.first_date_print = (date_last_print
                                                                + timedelta(days=1))
            if self.daterange.date_end > fiscal_daterange.date_last_print:
                self.date_move_line_to = self.daterange.date_end
            else:
                self.date_move_line_to = fiscal_daterange.date_end
        else:
            self.last_def_date_print = None
            self.first_date_print = date_start
            self.date_move_line_from = date_start
            self.date_move_line_to = self.daterange.date_end
        if fiscal_daterange.progressive_line_number != 0:
            self.start_row = fiscal_daterange.progressive_line_number + 1
        else:
            self.start_row = fiscal_daterange.progressive_line_number
        self.progressive_debit = fiscal_daterange.progressive_debit
        self.progressive_credit = fiscal_daterange.progressive_credit
        self.fiscal_page_base = fiscal_daterange.progressive_page_number
        self.year_footer = str(date_start.year)
        self.journal_ids = self._get_journal()

    def get_line_ids(self):
        wizard = self
        if wizard.target_move == "all":
            target_type = ["posted", "draft"]
        else:
            target_type = [wizard.target_move]
        sql = """
            SELECT aml.id FROM account_move_line aml
            LEFT JOIN account_move am ON (am.id = aml.move_id)
            WHERE
            aml.date >= %(date_from)s
            AND aml.date <= %(date_to)s
            AND am.state in %(target_type)s
            ORDER BY am.date, am.name, am.id
        """
        params = {
            "date_from": wizard.date_move_line_from,
            "date_to": wizard.date_move_line_to,
            "target_type": tuple(target_type),
            "journal_ids": tuple(self.journal_ids.ids),
        }
        self.env.cr.execute(sql, params)
        res = self.env.cr.fetchall()
        move_line_ids = flatten(res)
        return move_line_ids

    def _prepare_datas_form(self):
        wizard = self
        datas_form = {}
        datas_form["date_move_line_from"] = wizard.date_move_line_from
        datas_form["last_def_date_print"] = wizard.last_def_date_print
        datas_form["date_move_line_to"] = wizard.date_move_line_to
        datas_form["l10n_it_count_fiscal_page_base"] = wizard.fiscal_page_base
        datas_form["progressive_debit"] = wizard.progressive_debit
        datas_form["progressive_credit"] = wizard.progressive_credit
        datas_form["start_row"] = wizard.start_row
        datas_form["daterange"] = wizard.daterange.id
        datas_form["year_footer"] = wizard.year_footer
        return datas_form

    @api.multi
    def print_giornale(self):
        self.ensure_one()
        move_line_ids = self.get_line_ids()
        if not move_line_ids:
            raise UserError(_("No documents found in the current selection"))
        datas_form = self._prepare_datas_form()
        datas_form["print_state"] = "draft"
        report_name = "l10n_it_central_journal.report_giornale"
        datas = {"ids": move_line_ids, "model": "account.move", "form": datas_form}
        return self.env["report"].get_action([], report_name, data=datas)

    @api.multi
    def print_giornale_final(self):
        self.ensure_one()
        res_company_obj = self.env["res.company"]
        if self.target_move != "posted":
            raise UserError(_("Only posted records"))
        fiscal_daterange = self.daterange.get_fiscal_daterange()
        if not fiscal_daterange.type_id.fiscal_year:
            raise UserError(_("No fiscal date range found! Please create one"))

        if not self.first_date_print:
            raise UserError(_("Missing records"))
        if self.date_move_line_from < self.first_date_print:
            raise UserError(_("Date already printed"))
        elif self.date_move_line_from > self.first_date_print:
            raise UserError(_("Missing records"))

        move_line_ids = self.get_line_ids()
        if not move_line_ids:
            raise UserError(_("No documents found in the current selection"))
        datas_form = self._prepare_datas_form()
        datas_form["print_state"] = "def"
        report_name = "l10n_it_central_journal.report_giornale"
        datas = {"ids": move_line_ids, "model": "account.move", "form": datas_form}
        company = res_company_obj.search([("id", "=", self.company_id.id)])
        if (
            not company.period_lock_date
            or company.period_lock_date < self.date_move_line_to
        ):
            company.sudo().period_lock_date = self.date_move_line_to
        return self.env["report"].get_action([], report_name, data=datas)
