# -*- coding: utf-8 -*-
# Copyright (C) 2012 Andrea Cometa.
# Email: info@andreacometa.it
# Web site: http://www.andreacometa.it
# Copyright (C) 2012 Associazione OpenERP Italia
# (<http://www.odoo-italia.org>).
# Copyright (C) 2012-2017 Lorenzo Battistini - Agile Business Group
# Copyright 2018-22 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date

from odoo import _, api, fields, models, workflow
from odoo.exceptions import Warning as UserError

import odoo.addons.decimal_precision as dp


class RibaList(models.Model):
    _name = "riba.distinta"
    _description = "Riba list"

    @api.multi
    def _compute_acceptance_move_ids(self):
        for riba in self:
            move_ids = self.env["account.move"]
            for line in riba.line_ids:
                move_ids |= line.acceptance_move_id
            riba.acceptance_move_ids = move_ids

    @api.multi
    def _compute_unsolved_move_ids(self):
        for riba in self:
            move_ids = self.env["account.move"]
            for line in riba.line_ids:
                move_ids |= line.unsolved_move_id
            riba.unsolved_move_ids = move_ids

    @api.multi
    @api.depends("line_ids")
    def _compute_payment_ids(self):
        for riba in self:
            payment_lines = self.env["account.move.line"]
            extra_lines = self.env["account.move.line"]
            for line in riba.line_ids:
                payment_lines |= line.payment_ids
                extra_lines |= line.extra_payment_ids
            riba.payment_ids = payment_lines
            riba.extra_payment_ids = extra_lines

    name = fields.Char(
        "Reference",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=(lambda self: self.env["ir.sequence"].next_by_code("riba.distinta")),
    )
    config_id = fields.Many2one(
        "riba.configuration",
        string="Configuration",
        index=True,
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Riba configuration to be used",
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("accepted", "Accepted"),
            ("accredited", "Accredited"),
            ("paid", "Full Paid"),
            ("unsolved", "Unsolved"),
            ("cancel", "Canceled"),
        ],
        "State",
        readonly=True,
        default="draft",
    )
    line_ids = fields.One2many(
        "riba.distinta.line",
        "distinta_id",
        "Riba deadlines",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    user_id = fields.Many2one(
        "res.users",
        "User",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=lambda self: self.env.user,
    )
    date_created = fields.Date(
        "Creation date",
        readonly=True,
        default=lambda self: fields.Date.context_today(self),
    )
    date_accepted = fields.Date("Acceptance date")
    date_accreditation = fields.Date("Accreditation date")
    date_paid = fields.Date("Paid date", readonly=True)
    date_unsolved = fields.Date("Unsolved date", readonly=True)
    company_id = fields.Many2one(
        "res.company",
        "Company",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=lambda self: self.env["res.company"]._company_default_get(
            "riba.distinta"
        ),
    )
    acceptance_move_ids = fields.Many2many(
        "account.move",
        compute="_compute_acceptance_move_ids",
        string="Acceptance Entries",
    )
    accreditation_move_id = fields.Many2one(
        "account.move", "Accreditation Entry", readonly=True
    )
    payment_ids = fields.Many2many(
        "account.move.line", compute="_compute_payment_ids", string="Payments"
    )
    extra_payment_ids = fields.Many2many(
        "account.move.line", compute="_compute_payment_ids", string="Extra Payments"
    )
    unsolved_move_ids = fields.Many2many(
        "account.move", compute="_compute_unsolved_move_ids", string="Unsolved Entries"
    )
    type = fields.Selection(string="Type", related="config_id.type", readonly=True)
    registration_date = fields.Date(
        "Registration Date",
        states={
            "draft": [("readonly", False)],
            "cancel": [("readonly", False)],
        },
        readonly=True,
        required=True,
        default=lambda self: fields.Date.context_today(self),
        help="Keep empty to use the current date",
    )

    @api.onchange("date_accepted", "date_accreditation")
    def _onchange_date(self):
        if self.date_accepted and self.date_accreditation:
            if self.date_accepted > self.date_accreditation:
                raise UserError(
                    _(
                        "Date accreditation must be greater or equal to"
                        " date acceptance"
                    )
                )

    @api.multi
    def unlink(self):
        for riba_list in self:
            if riba_list.state not in ("draft", "cancel"):
                raise UserError(
                    _(
                        "List %s is in state %s. You can only delete documents"
                        " in state draft or canceled"
                    )
                    % (riba_list.name, riba_list.state)
                )
        super(RibaList, self).unlink()

    @api.multi
    def confirm(self):
        for ribalist in self:
            for line in ribalist.line_ids:
                line.confirm()
            ribalist.signal_workflow("accepted")

    @api.multi
    def back_to_draft(self):
        for riba_list in self:
            riba_list.date_accepted = False
            if riba_list.acceptance_move_ids:
                for move in riba_list.acceptance_move_ids:
                    move.line_ids.remove_move_reconcile()
                    move.button_cancel()
                    move.unlink()
            riba_list.action_draft()

    @api.multi
    def back_to_accepted(self):
        for riba_list in self:
            riba_list.date_accreditation = False
            if riba_list.accreditation_move_id:
                riba_list.accreditation_move_id.line_ids.remove_move_reconcile()
                riba_list.accreditation_move_id.button_cancel()
                riba_list.accreditation_move_id.unlink()
            for line in riba_list.line_ids:
                line.riba_line_back2accepted(harmless=True)
            riba_list.signal_workflow("accepted")

    @api.multi
    def back_to_accredited(self):
        for riba_list in self:
            riba_list.date_paid = False
            for line in riba_list.line_ids:
                line.riba_line_back2accredited(harmless=True)
            riba_list.signal_workflow("accredited")

    @api.multi
    def settle_all_line(self):
        for riba_list in self:
            for line in riba_list.line_ids:
                if line.state == "accredited":
                    line.riba_line_settlement()
            riba_list.signal_workflow("paid")

    @api.multi
    def action_draft(self):
        for riba_list in self:
            workflow.trg_delete(
                self.env.user.id, "riba.distinta", riba_list.id, self._cr
            )
            workflow.trg_create(
                self.env.user.id, "riba.distinta", riba_list.id, self._cr
            )
            riba_list.state = "draft"
            for line in riba_list.line_ids:
                line.riba_line_back2draft(harmless=True)

    #
    # --- WORKFLOW ---
    #

    @api.multi
    def riba_new(self):
        for riba_list in self:
            riba_list.state = "draft"

    @api.multi
    def riba_accepted(self):
        # Workflow internal function
        for riba_list in self:
            riba_list.state = "accepted"
            if not riba_list.date_accepted:
                riba_list.date_accepted = fields.Date.context_today(riba_list)
            for line in riba_list.line_ids:
                line.state = "accepted"

    @api.multi
    def riba_accredited(self):
        # Workflow internal function
        for riba_list in self:
            riba_list.state = "accredited"
            if not riba_list.date_accreditation:
                riba_list.date_accreditation = fields.Date.context_today(self)
            for line in riba_list.line_ids:
                line.state = "paid" if line.payment_ids else "accredited"

    @api.multi
    def riba_paid(self):
        # Workflow internal function
        for riba_list in self:
            riba_list.state = "paid"
            riba_list.date_paid = fields.Date.context_today(self)

    @api.multi
    def riba_unsolved(self):
        # Workflow internal function
        for riba_list in self:
            riba_list.state = "unsolved"
            riba_list.date_unsolved = fields.Date.context_today(self)

    @api.multi
    def riba_cancel(self):
        # Workflow internal function
        for riba_list in self:
            riba_list.state = "cancel"
            for line in riba_list.line_ids:
                line.state = "cancel"

    @api.multi
    def test_state(self, states):
        if not iter(states):
            states = [states]
        for riba_list in self:
            for line in riba_list.line_ids:
                if line.state not in states:
                    return False
        return True

    @api.multi
    def test_accepted(self):
        return self.test_state("accepted")

    @api.multi
    def test_unsolved(self):
        return self.test_state(["unsolved", "paid"])

    @api.multi
    def test_paid(self):
        return self.test_state("paid")


class RibaListLine(models.Model):
    _name = "riba.distinta.line"
    _description = "Riba details"
    _rec_name = "sequence"

    @api.multi
    def _compute_line_values(self):
        for line in self:
            line.amount = 0.0
            line.invoice_date = ""
            line.invoice_number = ""
            for move_line in line.move_line_ids:
                line.amount += move_line.amount
                if move_line.move_line_id.invoice_id:
                    invoice_date = fields.Date.from_string(
                        move_line.move_line_id.invoice_id.date_invoice
                    ).strftime("%d/%m/%Y")
                    invoice_number = move_line.move_line_id.invoice_id.move_name
                else:  # pragma: no cover
                    # Avoid crash in some case which the invoice is deleted
                    invoice_date = "???"
                    invoice_number = "???"
                if not line.invoice_date:
                    line.invoice_date = invoice_date
                else:
                    line.invoice_date = "%s, %s" % (line.invoice_date, invoice_date)
                if not line.invoice_number:
                    line.invoice_number = invoice_number
                else:
                    line.invoice_number = "%s, %s" % (
                        line.invoice_number,
                        invoice_number,
                    )

    @api.multi
    def _compute_extra_payments(self):
        for riba_line in self:
            if all([x.move_line_id.reconciled for x in riba_line.move_line_ids]):
                reconciled_lines = [
                    x.move_line_id.full_reconcile_id.reconciled_line_ids
                    for x in riba_line.move_line_ids
                ][0]
                reconciled_ids = [x.id for x in reconciled_lines]
                inv_ids = [x.move_line_id.id for x in riba_line.move_line_ids]
                riba_ids = riba_line.acceptance_move_id.line_ids.ids
                extra_ids = list((set(reconciled_ids) - set(inv_ids)) - set(riba_ids))
                extra_payments = [x for x in reconciled_lines if x.id in extra_ids]
                if extra_payments:
                    extra_payment_ids = self.env["account.move.line"]
                    for line in extra_payments[0]:
                        for ln in line.move_id.line_ids:
                            if ln != line and ln.user_type_id == self.env.ref(
                                "account.data_account_type_liquidity"
                            ):
                                extra_payment_ids |= ln
                    riba_line.extra_payment_ids = extra_payment_ids

    def _compute_has_unsolved(self):
        for riba_line in self:
            riba_line.has_unsolved = bool(riba_line.unsolved_move_id)

    amount = fields.Float(compute="_compute_line_values", string="Amount")
    invoice_date = fields.Char(
        compute="_compute_line_values", string="Invoice Date", size=256
    )
    invoice_number = fields.Char(
        compute="_compute_line_values", string="Invoice Number", size=256
    )

    @api.multi
    def move_line_id_payment_get(self):
        # return the move line ids with the same account as the distinta line
        if not self.id:  # pragma: no cover
            return []
        query = """ SELECT l.id
                    FROM account_move_line l, riba_distinta_line rdl
                    WHERE rdl.id = %s AND l.move_id = rdl.acceptance_move_id
                    AND l.account_id = rdl.acceptance_account_id
                """
        self._cr.execute(query, (self.id,))
        return [row[0] for row in self._cr.fetchall()]

    @api.multi
    def test_reconciled(self):
        # check whether all corresponding account move lines are reconciled
        line_ids = self.move_line_id_payment_get()
        if not line_ids:  # pragma: no cover
            return False
        move_lines = self.env["account.move.line"].browse(line_ids)
        reconcilied = all(line.reconciled for line in move_lines)
        return reconcilied

    sequence = fields.Integer("Number")
    move_line_ids = fields.One2many(
        "riba.distinta.move.line", "riba_line_id", string="Credit move lines"
    )
    acceptance_move_id = fields.Many2one(
        "account.move", string="Acceptance Entry", readonly=True
    )
    unsolved_move_id = fields.Many2one(
        "account.move", string="Unsolved Entry", readonly=True
    )
    has_unsolved = fields.Boolean(
        string="Has Unsolved", compute="_compute_has_unsolved"
    )
    acceptance_account_id = fields.Many2one(
        "account.account", string="Acceptance Account"
    )
    bank_id = fields.Many2one("res.partner.bank", string="Debitor Bank")
    iban = fields.Char(
        related="bank_id.acc_number", string="IBAN", store=False, readonly=True
    )
    distinta_id = fields.Many2one(
        "riba.distinta", string="List", required=True, ondelete="cascade"
    )
    partner_id = fields.Many2one("res.partner", string="Cliente", readonly=True)
    due_date = fields.Date("Due date", readonly=True)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("accepted", "Confirmed"),
            ("accredited", "Accredited"),
            ("paid", "Paid"),
            ("unsolved", "Unsolved"),
            ("cancel", "Canceled"),
        ],
        "State",
        readonly=True,
        track_visibility="onchange",
    )
    payment_ids = fields.Many2many("account.move.line", string="Payments")
    extra_payment_ids = fields.Many2many(
        "account.move.line", string="Extra Payments", compute="_compute_extra_payments"
    )
    type = fields.Selection(string="Type", related="distinta_id.type", readonly=True)

    @api.multi
    def confirm(self):
        move_model = self.env["account.move"]
        move_line_model = self.env["account.move.line"]
        for line in self:
            journal = line.distinta_id.config_id.acceptance_journal_id
            total_credit = 0.0
            move = move_model.create(
                {
                    "ref": "Ri.Ba. %s - line %s"
                    % (line.distinta_id.name, line.sequence),
                    "journal_id": journal.id,
                    "date": line.distinta_id.registration_date,
                }
            )
            to_be_reconciled = self.env["account.move.line"]
            for riba_move_line in line.move_line_ids:
                total_credit += riba_move_line.amount
                move_line = move_line_model.with_context(
                    {"check_move_validity": False}
                ).create(
                    {
                        "name": (
                            riba_move_line.move_line_id.invoice_id
                            and riba_move_line.move_line_id.invoice_id.number
                            or riba_move_line.move_line_id.name
                        ),
                        "partner_id": line.partner_id.id,
                        "account_id": (riba_move_line.move_line_id.account_id.id),
                        "credit": riba_move_line.amount,
                        "debit": 0.0,
                        "move_id": move.id,
                    }
                )
                if move_line.account_id == riba_move_line.move_line_id.account_id:
                    to_be_reconciled |= move_line
                    to_be_reconciled |= riba_move_line.move_line_id
            move_line_model.with_context({"check_move_validity": False}).create(
                {
                    "name": "Ri.Ba. %s - line %s"
                    % (line.distinta_id.name, line.sequence),
                    "account_id": (
                        line.acceptance_account_id.id
                        or line.distinta_id.config_id.acceptance_account_id.id
                    ),
                    "partner_id": line.partner_id.id,
                    "date_maturity": line.due_date,
                    "credit": 0.0,
                    "debit": total_credit,
                    "move_id": move.id,
                }
            )
            move.post()
            if to_be_reconciled:
                to_be_reconciled.reconcile()
            line.write(
                {
                    "acceptance_move_id": move.id,
                    "state": "accepted",
                }
            )

    def _open_items__init(self):
        # open_items is managed like an object
        return {
            "config": {},
            "account_ids": {},
            "move_line_ids": {},
        }

    def _open_items__load_config(self, this, riba_line):
        # this is the open_items object created by _init__open_items()
        # Load configuration accounts
        config = riba_line.distinta_id.config_id
        this["config"]["bank_id"] = config.bank_id
        this["config"]["acceptance_account_id"] = riba_line.acceptance_account_id
        this["config"][
            "accreditation_account_debit_id"
        ] = config.accreditation_account_debit_id
        this["config"][
            "accreditation_account_credit_id"
        ] = config.accreditation_account_credit_id
        this["config"]["overdue_account_debit_id"] = config.overdue_account_debit_id
        this["config"]["overdue_account_credit_id"] = config.overdue_account_credit_id
        this["config"][
            "settlement_account_debit_id"
        ] = config.settlement_account_debit_id
        this["config"][
            "settlement_account_credit_id"
        ] = config.settlement_account_credit_id
        this["config"]["settlement_journal_id"] = config.settlement_journal_id
        this["config"]["distinta_name"] = riba_line.distinta_id.name
        this["config"]["partner_id"] = riba_line.partner_id

        for line in riba_line.acceptance_move_id.line_ids:
            this = self._open_items__add_move_line(this, line, "acceptance")
        for line in riba_line.distinta_id.accreditation_move_id.line_ids:
            this = self._open_items__add_move_line(this, line, "accreditation")
        # remove debit/credit pair lines
        for account in this["account_ids"].keys():
            if this["account_ids"].get("debit") and this["account_ids"].get("credit"):
                for move_type in ("acceptance", "accreditation"):
                    for move_line in this["move_line_ids"][move_type].copy().keys():
                        if this["move_line_ids"][move_line].account_id == account:
                            del this["move_line_ids"][move_line]
                del this["account_ids"][account]
        return this

    def _open_items__add_move_line(self, this, move_line, move_type):
        # this is the open_items object created by _init__open_items()
        # Process move line and data in internal structure
        side = ""
        if not move_line.reconciled:
            if move_line.debit > 0.0:
                side = "debit"
            elif move_line.credit > 0.0:
                side = "credit"
            acc_type = move_line.account_id.user_type_id.type
            if (
                side
                and move_line.account_id != this["config"]["overdue_account_credit_id"]
                and move_line.account_id.user_type_id
                in (
                    self.env.ref("account.data_account_type_current_assets"),
                    self.env.ref("account.data_account_type_current_liabilities"),
                    self.env.ref("account.data_account_type_liquidity"),
                    self.env.ref("account.data_account_type_receivable"),
                    self.env.ref("account.data_account_type_payable"),
                )
            ):
                if move_line.account_id not in this["account_ids"]:
                    this["account_ids"][move_line.account_id] = {}
                this["account_ids"][move_line.account_id][side] = acc_type

                if move_type in ("acceptance", "accreditation"):
                    if move_type not in this["move_line_ids"]:
                        this["move_line_ids"][move_type] = {}
                    this["move_line_ids"][move_type][side] = move_line
                else:
                    raise UserError(
                        "Invalid %s value: must be 'acceptance' or 'accreditation'"
                        % side
                    )
        return this

    def _open_items__load_line_values(self, this, account, side, amount):
        if side not in ("debit", "credit"):
            raise UserError("Invalid %s value: must be 'debit' or 'credit'" % side)
        opposite_side = "debit" if side == "credit" else "credit"
        move_ref = _("Settlement RIBA {} - {}").format(
            this["config"]["distinta_name"],
            this["config"]["partner_id"].name,
        )
        return {
            "name": move_ref,
            "partner_id": this["config"]["partner_id"].id,
            "account_id": account.id,
            side: 0.0,
            opposite_side: amount,
        }

    def _open_items__get_move_vals(self, this):
        # this is the open_items object created by _init__open_items()
        # Return dict for create settlement move from internal data
        move_ref = _("Settlement RIBA {} - {}").format(
            this["config"]["distinta_name"],
            this["config"]["partner_id"].name,
        )
        vals = {
            "journal_id": this["config"]["settlement_journal_id"].id,
            "date": date.today().strftime("%Y-%m-%d"),
            "ref": move_ref,
            "line_ids": [],
        }

        # Prepare line values. All lines must close acceptance and accreditation lines.
        totals = {"debit": 0.0, "credit": 0.0}
        for account in this["account_ids"].keys():
            side = this["account_ids"][account].keys()[0]
            line_vals = self._open_items__load_line_values(
                this, account, side, this["move_line_ids"]["acceptance"]["debit"].debit
            )
            vals["line_ids"].append((0, 0, line_vals))
            totals["debit"] += line_vals["credit"]
            totals["credit"] += line_vals["debit"]

        if totals["debit"] > totals["credit"]:
            line_vals = self._open_items__load_line_values(
                this,
                this["config"]["overdue_account_credit_id"],
                "credit",
                totals["debit"] - totals["credit"],
            )
            vals["line_ids"].append((0, 0, line_vals))
        elif totals["debit"] < totals["credit"]:
            line_vals = self._open_items__load_line_values(
                this,
                this["config"]["settlement_account_credit_id"],
                "debit",
                totals["credit"] - totals["debit"],
            )
            vals["line_ids"].append((0, 0, line_vals))
        return vals

    def _open_items__do_reconciles(self, this):
        reconciles = {}
        for move_type in this["move_line_ids"]:
            for side in this["move_line_ids"][move_type]:
                for move_line in this["move_line_ids"][move_type][side]:
                    account = move_line.account_id
                    if account in this["account_ids"] and account.reconcile:
                        if account not in reconciles:
                            reconciles[account] = {}
                        reconciles[account][side] = move_line
        for account in reconciles:
            if reconciles[account].get("debit") and reconciles[account].get("credit"):
                to_be_reconciled = self.env["account.move.line"]
                to_be_reconciled |= reconciles[account]["debit"]
                to_be_reconciled |= reconciles[account]["credit"]
                to_be_reconciled.reconcile()

    @api.multi
    def riba_line_settlement(self):
        for riba_line in self:
            if (
                not riba_line.distinta_id.config_id.settlement_journal_id
            ):  # pragma: no cover
                raise UserError(_("Please define a Settlement journal"))

            if not riba_line.extra_payment_ids:
                move_model = self.env["account.move"]
                open_items = self._open_items__init()
                open_items = self._open_items__load_config(open_items, riba_line)
                settlement_move = move_model.create(
                    self._open_items__get_move_vals(open_items)
                )
                settlement_move.post()
                move_line_debit = False
                for move_line in settlement_move.line_ids:
                    if move_line.debit > 0.0:
                        if not move_line_debit:
                            move_line_debit = move_line
                        elif (
                            move_line.account_id
                            == open_items["config"]["settlement_account_debit_id"]
                        ):
                            move_line_debit = move_line
                riba_line.payment_ids = [(4, move_line_debit.id)]
                self._open_items__do_reconciles(open_items)
            self.riba_line_set_state("paid")

    @api.multi
    def riba_line_set_state(self, state, harmless=None):
        if state not in (
            "draft",
            "accepted",
            "accredited",
            "cancel",
            "paid",
            "unsolved",
        ):
            return  # pragma: no cover
        states = {}
        for line in self:
            if state == "paid":
                if all([x.move_line_id.reconciled for x in line.move_line_ids]):
                    line.state = state
            elif state == "unsolved":
                if line.unsolved_move_id:
                    line.state = state
            else:
                line.riba_line_back2solved(harmless=True)
                if line.payment_ids:
                    for move_line in line.payment_ids:
                        line.payment_ids = [(3, move_line.id)]
                        for ln in move_line.move_id.line_ids:
                            if ln.reconciled:
                                ln.remove_move_reconcile()
                        move_line.move_id.button_cancel()
                        move_line.move_id.unlink()
                    line.state = state
            if not harmless:
                if line.distinta_id not in states:
                    states[line.distinta_id] = []
                    for ln in line.distinta_id.line_ids:
                        if ln.state not in states[line.distinta_id]:
                            states[line.distinta_id].append(ln.state)
        for (distinta, state) in states.items():
            if len(state) == 1:
                distinta.state = state[0]
            elif "unsolved" in state:
                distinta.state = "unsolved"

    @api.multi
    def riba_line_back2solved(self, harmless=None):
        for line in self:
            if line.unsolved_move_id:
                for move in line.unsolved_move_id:
                    move.line_ids.remove_move_reconcile()
                    move.button_cancel()
                    move.unlink()
            if line.payment_ids:
                line.state = "paid"
            else:
                line.state = "accredited"

    @api.multi
    def riba_line_back2accredited(self, harmless=None):
        self.riba_line_set_state("accredited", harmless=harmless)

    @api.multi
    def riba_line_back2accepted(self, harmless=None):
        self.riba_line_set_state("accepted", harmless=harmless)

    @api.multi
    def riba_line_back2draft(self, harmless=None):
        self.riba_line_set_state("draft", harmless=harmless)

    @api.multi
    def riba_line_back2cancel(self, harmless=None):
        self.riba_line_set_state("cancel", harmless=harmless)


class RibaListMoveLine(models.Model):

    _name = "riba.distinta.move.line"
    _description = "Riba details"
    _rec_name = "amount"

    amount = fields.Float("Amount", digits=dp.get_precision("Account"))
    move_line_id = fields.Many2one("account.move.line", string="Credit move line")
    riba_line_id = fields.Many2one(
        "riba.distinta.line", string="List line", ondelete="cascade"
    )
