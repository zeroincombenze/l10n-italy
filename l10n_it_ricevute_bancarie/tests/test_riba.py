# -*- coding: utf-8 -*-
import os
# from datetime import datetime
import logging
from .testenv import MainTest as SingleTransactionCase

import python_plus

_logger = logging.getLogger(__name__)


TEST_ACCOUNT_ACCOUNT = {
    "z0bug.coa_bnk1a": {
        "code": "101451",
        "name": "Wallet bank",
        "user_type_id": "account.data_account_type_liquidity",
    },
    "z0bug.coa_liq_tra1": {
        "code": "101710",
        "name": "Effetti attivi",
        "reconcile": True,
        "user_type_id": "account.data_account_type_receivable",
    },
    "z0bug.coa_liq_tra2": {
        "code": "101720",
        "name": "Effetti SBF",
        "reconcile": False,
        "user_type_id": "account.data_account_type_liquidity",
    },
    "z0bug.coa_tax_recv": {
        "code": "111200",
        "reconcile": False,
        "user_type_id": "account.data_account_type_current_liabilities",
        "name": "IVA n/debito",
    },
    "z0bug.coa_sale": {
        "code": "200000",
        "name": "Merci c/vendita",
        "user_type_id": "account.data_account_type_revenue",
        "reconcile": False,
    },
    "z0bug.coa_bnk_fee": {
        "code": "212300",
        "reconcile": False,
        "user_type_id": "account.data_account_type_expenses",
        "name": "Costi bancari",
    },
}

TEST_ACCOUNT_JOURNAL = {
    "external.INV": {
        "code": "INV",
        "type": "sale",
        "update_posted": True,
        "name": "Fatture di vendita",
    },
    "external.BNK1": {
        "code": "BNK1",
        "type": "bank",
        "update_posted": True,
        "name": "Banca",
    },
}

TEST_ACCOUNT_INVOICE = {
    "z0bug.invoice_Z0_1": {
        "partner_id": "z0bug.res_partner_1",
        "origin": "P1/2021/0001",
        "reference": "P1/2021/0001",
        "date_invoice": "####-<#-99",
        "type": "out_invoice",
        "journal_id": "external.INV",
        "payment_term_id": "z0bug.payment_1",
    },
    "z0bug.invoice_Z0_2": {
        "partner_id": "z0bug.res_partner_2",
        "origin": "SO123",
        "reference": "SO123",
        "date_invoice": "####-<#-99",
        "type": "out_invoice",
        "journal_id": "external.INV",
        "payment_term_id": "z0bug.payment_2",
    },
}

TEST_ACCOUNT_INVOICE_LINE = {
    "z0bug.invoice_Z0_1_1": {
        "sequence": 1,
        "invoice_id": "z0bug.invoice_Z0_1",
        "product_id": "z0bug.product_product_1",
        "name": "Prodotto Alpha",
        "quantity": 200,
        "account_id": "z0bug.coa_sale",
        "price_unit": 0.84,
        "invoice_line_tax_ids": "external.22v",
    },
    "z0bug.invoice_Z0_2_1": {
        "sequence": 1,
        "invoice_id": "z0bug.invoice_Z0_2",
        "product_id": "z0bug.product_product_1",
        "name": "Prodotto Alpha",
        "quantity": 100,
        "account_id": "z0bug.coa_sale",
        "price_unit": 0.42,
        "invoice_line_tax_ids": "external.22v",
    },
    "z0bug.invoice_Z0_2_2": {
        "sequence": 2,
        "invoice_id": "z0bug.invoice_Z0_2",
        "product_id": "z0bug.product_product_2",
        "name": "Prodotto Beta",
        "quantity": 100,
        "account_id": "z0bug.coa_sale",
        "price_unit": 1.69,
        "invoice_line_tax_ids": "external.22v",
    },
}

TEST_ACCOUNT_PAYMENT_TERM = {
    "z0bug.payment_1": {
        "name": "RiBA 30GG",
        "riba": True,
    },
    "z0bug.payment_2": {
        "name": "RiBA 30/60 GG",
        "riba": True,
    },
}

TEST_ACCOUNT_PAYMENT_TERM_LINE = {
    "z0bug.payment_1_1": {
        "payment_id": "z0bug.payment_1",
        "sequence": 1,
        "days": 30,
        "value": "balance",
    },
    "z0bug.payment_2_1": {
        "payment_id": "z0bug.payment_2",
        "sequence": 1,
        "days": 30,
        "value": "percent",
        "value_amount": 50,
    },
    "z0bug.payment_2_2": {
        "payment_id": "z0bug.payment_2",
        "sequence": 2,
        "days": 60,
        "value": "balance",
    },
}

TEST_ACCOUNT_TAX = {
    "external.22v": {
        "description": "22v",
        "name": "IVA 22% su vendite",
        "amount_type": "percent",
        "account_id": "z0bug.coa_tax_recv",
        "refund_account_id": "z0bug.coa_tax_recv",
        "amount": 22,
        "type_tax_use": "sale",
        "price_include": False,
    },
}

TEST_PRODUCT_TEMPLATE = {
    "z0bug.product_template_1": {
        "property_account_income_id": "z0bug.coa_sale",
        "name": "Prodotto Alpha",
        "weight": 0.1,
        "type": "consu",
        "standard_price": 0.42,
        "uom_id": "product.product_uom_unit",
        "lst_price": 0.84,
        "default_code": "AA",
        "uom_po_id": "product.product_uom_unit",
        "taxes_id": "external.22v",
    },
    "z0bug.product_template_2": {
        "property_account_income_id": "z0bug.coa_sale",
        "name": "Prodotto Beta",
        "weight": 0.2,
        "type": "consu",
        "standard_price": 1.69,
        "uom_id": "product.product_uom_unit",
        "lst_price": 3.38,
        "default_code": "BB",
        "uom_po_id": "product.product_uom_unit",
        "taxes_id": "external.22v",
    },
}

TEST_RES_PARTNER = {
    "z0bug.res_partner_1": {
        "name": "Prima Alpha S.p.A.",
        "street": "Via I Maggio, 101",
        "country_id": "base.it",
        "zip": "20022",
        "city": "Castano Primo",
        "state_id": "base.state_it_mi",
        "customer": True,
        "supplier": True,
        "is_company": True,
        "email": "info@prima-alpha.it",
        "phone": "+39 0255582285",
        "vat": "IT00115719999",
        "website": "http://www.prima-alpha.it",
        # "property_account_position_id": "z0bug.fiscalpos_it",
        "property_payment_term_id": "z0bug.payment_1",
        "property_supplier_payment_term_id": "z0bug.payment_1",
    },
    "z0bug.res_partner_2": {
        "name": "Latte Beta Due Più s.n.c.",
        "street": "Via Dueville, 2",
        "country_id": "base.it",
        "zip": "10060",
        "city": "S. Secondo Pinerolo",
        "state_id": "base.state_it_to",
        "customer": True,
        "supplier": False,
        "is_company": True,
        "email": "agrolait2@libero.it",
        "phone": "+39 0121555123",
        "vat": "IT02345670018",
        "website": "http://www.agrolait2.it/",
        "property_payment_term_id": "z0bug.payment_2",
    },
}

TEST_RES_PARTNER_BANK = {
    "z0bug.bank_company_1": {
        "partner_id": "base.main_partner",
        "sequence": 1,
        "acc_type": "iban",
        "acc_number": "IT15A0123412345100000123456",
        "codice_sia": "A7721",
    },
    "z0bug.bank_partner_1": {
        "partner_id": "z0bug.res_partner_1",
        "acc_type": "iban",
        "acc_number": "IT73C0102001011010101987654",
    },
    "z0bug.bank_partner_2": {
        "partner_id": "z0bug.res_partner_2",
        "acc_type": "iban",
        "acc_number": "IT82B0200802002200000000022",
    },
}

TEST_RIBA_CONFIGURATION = {
    "z0bug.riba_config": {
        "name": "RIBA SBF",
        "type": "sbf",
        "bank_id": "z0bug.bank_company_1",
        "acceptance_journal_id": "external.BNK1",
        "acceptance_account_id": "z0bug.coa_liq_tra1",
    },
}

TEST_SETUP_LIST = [
    "account.account",
    "account.tax",
    "account.payment.term",
    "account.payment.term.line",
    "product.template",
    "res.partner",
    "res.partner.bank",
    "account.journal",
    "riba.configuration",
    "account.invoice",
    "account.invoice.line",
]


class TestRiba(SingleTransactionCase):
    def setUp(self):
        super(TestRiba, self).setUp()
        self.debug_level = 0
        data = {"TEST_SETUP_LIST": TEST_SETUP_LIST}
        for resource in TEST_SETUP_LIST:
            item = "TEST_%s" % resource.upper().replace(".", "_")
            data[item] = globals()[item]
        self.declare_all_data(data)
        self.setup_company(
            self.default_company(),
            xref="z0bug.mycompany",
            partner_xref="z0bug.partner_mycompany",
            bnk1_xref="z0bug.coa_bnk1",
            values={
                "name": "Test Company",
                "street": "Via dei Matti, 0",
                "country_id": "base.it",
                "zip": "20080",
                "city": "Ozzero",
                "state_id": "base.state_it_mi",
                "customer": False,
                "supplier": False,
                "is_company": True,
                "email": "info@testcompany.org",
                "phone": "+39 025551234",
                "vat": "IT05111810015",
                "website": "https://www.testcompany.org",
            },
        )
        self.setup_env()  # Create test environment

    def tearDown(self):
        super(TestRiba, self).tearDown()
        if os.environ.get("ODOO_COMMIT_TEST", ""):
            self.env.cr.commit()  # pylint: disable=invalid-commit
            _logger.info("✨ Test data committed")

    def _validate_cbi_file(self, riba_cbi, due_records):
        # Simple file validator
        state = ""
        ctr_recs = ctr_dues = 0
        for ln in python_plus._u(riba_cbi).split("\n"):
            if not ln:
                self.assertFalse(state, "Empty line in CBI file")
                continue
            line_id = ln[:3]
            self.assertTrue(
                line_id
                in (" IB", " 14", " 20", " 30", " 40", " 50", " 51", " 70", " EF"),
                "Invalid CBI contents!",
            )
            ctr_recs += 1
            if line_id.startswith(" IB"):
                state = "body"
            elif line_id.startswith(" 14"):
                ctr_dues += 1
            elif line_id.startswith(" EF"):
                state = ""
                self.assertEqual(
                    int(ln[46:52]), ctr_dues, "Invalid # of dues in CBI file"
                )
                self.assertEqual(
                    int(ln[83:89]), ctr_recs, "Invalid # of records in CBI file"
                )
                self.assertEqual(
                    ctr_dues, len(due_records), "Invalid # of dues in CBI file"
                )

    def _edit_riba_config(self):
        riba_config = self.resource_browse("z0bug.riba_config")
        self.resource_edit(
            resource=riba_config,
            web_changes=[
                ("accreditation_account_debit_id", "z0bug.coa_liq_tra2"),
                ("accreditation_account_credit_id", "z0bug.coa_bnk1a"),
                ("bank_expense_account_id", "z0bug.coa_bnk_fee"),
                ("liquidity_account_id", "z0bug.coa_bnk1"),
            ],
        )

        self.assertEqual(riba_config["accreditation_account_debit_id"],
                         self.env.ref("z0bug.coa_liq_tra2"))
        self.assertEqual(riba_config["accreditation_account_credit_id"],
                         self.env.ref("z0bug.coa_bnk1a"))
        self.assertEqual(riba_config["liquidity_account_id"],
                         self.env.ref("z0bug.coa_bnk1"))

    def _validate_invoice(self):
        invoices = self.env["account.invoice"]
        for xref in TEST_ACCOUNT_INVOICE.keys():
            invoice = self.resource_browse(xref)
            invoice.compute_taxes()
            invoice.action_invoice_open()
            invoices |= invoice

        due_records = self.env["account.move.line"].search(
            [
                ("invoice_id", "in", [x.id for x in invoices]),
                (
                    "account_id.user_type_id",
                    "=",
                    self.env.ref("account.data_account_type_receivable").id,
                ),
            ],
            order="date_maturity,partner_id",
        )

        # We have 2 invoices: the 1.st one has just 1 due date, the 2.nd is split
        # into 2 due dates. The 1.st due date is equal for all invoices.
        date_invoice = self.compute_date("####-<#-99")
        date_due1 = self.compute_date(+30, refdate=date_invoice)
        date_due2 = self.compute_date(+60, refdate=date_invoice)
        template_dues = []
        vals = {
            "account_id": invoice[0].account_id.id,
            "partner_id": "z0bug.res_partner_1",
            "date": date_invoice,
            "date_maturity": date_due1,
            "riba": True,
        }
        template_dues.append(vals)
        vals = {
            "account_id": invoice[0].account_id.id,
            "partner_id": "z0bug.res_partner_2",
            "date": date_invoice,
            "date_maturity": date_due1,
            "riba": True,
        }
        template_dues.append(vals)
        vals = {
            "account_id": invoice[0].account_id.id,
            "partner_id": "z0bug.res_partner_2",
            "date": date_invoice,
            "date_maturity": date_due2,
            "riba": True,
        }
        template_dues.append(vals)
        self.validate_records(template_dues, due_records)

        return invoices, due_records

    def _generate_payment_order(self, due_records):
        act_windows = self.wizard(
            module=".",
            action_name="riba_issue_action",
            records=due_records,
            default={"configuration_id": "z0bug.riba_config"},
            button_name="create_list",
        )
        self.assertTrue(self.is_action(act_windows))
        return self.get_records_from_act_windows(act_windows)

    def _download_cbi(self, payment_order, due_records):
        riba_cbi = self.resource_download(
            module=".",
            action_name="action_wizard_riba_file_export",
            records=payment_order,
            button_name="act_getfile",
            field="riba_txt",
        )
        self.assertTrue(riba_cbi)
        self._validate_cbi_file(riba_cbi, due_records)
        return riba_cbi

    def _payorder_accepted(self, payment_order):
        self.resource_edit(
            resource=payment_order,
            actions="confirm",
        )
        self.assertEqual(payment_order.state, "accepted")
        self.assertTrue(payment_order.acceptance_move_ids)

    def _validate_accepted_moves(self, payment_order, due_records):
        # acceptance_account_id = payment_order.config_id.acceptance_account_id
        acceptance_account_id = self.env.ref("z0bug.coa_liq_tra1")
        template = []
        for due in due_records:
            tmpl_move = []
            vals = {
                "account_id": acceptance_account_id.id,
                "debit": due.debit or due.credit,
                "credit": 0.0,
            }
            tmpl_move.append(vals)
            vals = {
                "account_id": due.account_id.id,
                "debit": 0.0,
                "credit": due.credit or due.debit,
            }
            tmpl_move.append(vals)
            template.append({"line_ids": tmpl_move})

        self.validate_records(template, payment_order.acceptance_move_ids)

    def _payorder_accreditation(self, payment_order, due_records):
        bank_amount = 0.0
        for line in due_records:
            bank_amount += line.debit - line.credit
        act_windows = self.wizard(
            module=".",
            action_name="riba_accreditation_action",
            records=payment_order,
            web_changes=[("bank_amount", bank_amount)],
            button_name="create_move",
        )
        self.assertTrue(self.is_action(act_windows))
        self.assertEqual(payment_order.state, "accredited")
        self.assertTrue(payment_order.accreditation_move_id)

    def _validate_accreditation_moves(self, payment_order, due_records):
        accreditation_account_debit_id = self.env.ref("z0bug.coa_liq_tra2").id
        accreditation_account_credit_id = self.env.ref("z0bug.coa_bnk1a").id
        bank_amount = 0.0
        for line in due_records:
            bank_amount += line.debit - line.credit
        for line in payment_order.accreditation_move_id.line_ids:
            if line.credit > 0.0:
                self.assertEqual(
                    line.account_id.id,
                    accreditation_account_credit_id,
                )
                self.assertEqual(
                    line.credit,
                    bank_amount,
                )
            else:
                self.assertEqual(
                    line.account_id.id,
                    accreditation_account_debit_id,
                )
                self.assertEqual(
                    line.debit,
                    bank_amount,
                )

    def _confirm_all_payments(self, payment_order, due_records):
        self.resource_edit(
            resource=payment_order,
            actions="settle_all_line",
        )
        self.assertEqual(payment_order.state, "paid")
        for line_distinta in payment_order.line_ids:
            self.assertTrue(line_distinta.payment_ids)
        self.assertTrue(payment_order.payment_ids)

    def _validate_payment_moves(self, payment_order, due_records):
        acceptance_account_id = self.env.ref("z0bug.coa_liq_tra1")
        accreditation_account_debit_id = self.env.ref("z0bug.coa_liq_tra2").id
        accreditation_account_credit_id = self.env.ref("z0bug.coa_bnk1a").id
        liquidity_account_id = self.env.ref("z0bug.coa_bnk1").id

        template = []
        for due in due_records:
            tmpl_move = []
            vals = {
                "account_id": liquidity_account_id,
                "debit": due.debit or due.credit,
                "credit": 0.0,
            }
            tmpl_move.append(vals)
            vals = {
                "account_id": acceptance_account_id,
                "debit": 0.0,
                "credit": due.credit or due.debit,
                "reconciled": True,
            }
            tmpl_move.append(vals)
            vals = {
                "account_id": accreditation_account_credit_id,
                "debit": due.debit or due.credit,
                "credit": 0.0,
            }
            tmpl_move.append(vals)
            vals = {
                "account_id": accreditation_account_debit_id ,
                "debit": 0.0,
                "credit": due.credit or due.debit,
            }
            tmpl_move.append(vals)
            template.append({"line_ids": tmpl_move})

        self.validate_records(
            template, [ln.move_id for ln in payment_order.payment_ids])

    def _validate_payment_moves_with_unsolved(self, payment_order, due_records):
        acceptance_account_id = self.env.ref("z0bug.coa_liq_tra1")
        accreditation_account_debit_id = self.env.ref("z0bug.coa_liq_tra2").id
        accreditation_account_credit_id = self.env.ref("z0bug.coa_bnk1a").id
        liquidity_account_id = self.env.ref("z0bug.coa_bnk1").id

        template = []
        for due in due_records:
            if due == payment_order.line_ids[0].move_line_ids.move_line_id:
                continue
            tmpl_move = []
            vals = {
                "account_id": liquidity_account_id,
                "debit": due.debit or due.credit,
                "credit": 0.0,
            }
            tmpl_move.append(vals)
            vals = {
                "account_id": acceptance_account_id,
                "debit": 0.0,
                "credit": due.credit or due.debit,
                "reconciled": True,
            }
            tmpl_move.append(vals)
            vals = {
                "account_id": accreditation_account_credit_id,
                "debit": due.debit or due.credit,
                "credit": 0.0,
            }
            tmpl_move.append(vals)
            vals = {
                "account_id": accreditation_account_debit_id,
                "debit": 0.0,
                "credit": due.credit or due.debit,
            }
            tmpl_move.append(vals)
            template.append({"line_ids": tmpl_move})

        self.validate_records(
            template, [ln.move_id for ln in payment_order.payment_ids])

    def _riba_unsolved(self, payment_order):
        line_distinta = payment_order.line_ids[0]
        self.resource_edit(
            resource=line_distinta,
            actions="riba_line_back2accredited",
        )
        self.assertEqual(line_distinta.state, "accredited")
        act_windows = self.wizard(
            module=".",
            action_name="riba_unsolved_action",
            records=line_distinta,
            default={
                "bank_amount": line_distinta.amount,
            },
            button_name="create_move",
        )
        self.assertTrue(self.is_action(act_windows))
        self.assertEqual(line_distinta.state, "unsolved")
        self.assertTrue(line_distinta.unsolved_move_id)
        self.assertEqual(payment_order.state, "unsolved")
        self.assertTrue(payment_order.unsolved_move_ids)

    def _riba_solved(self, distinta):
        line_distinta = distinta.line_ids[0]
        self.resource_edit(
            resource=line_distinta,
            actions="riba_line_back2solved",
        )
        self.assertEqual(line_distinta.state, "accredited")

        self.resource_edit(
            resource=line_distinta,
            actions="riba_line_settlement",
        )
        self.assertEqual(line_distinta.state, "paid")

    def _distinta_back_accreditated(self, distinta):
        self.resource_edit(
            resource=distinta,
            actions="back_to_accredited",
        )
        self.assertEqual(distinta.state, "accredited")
        self.assertFalse(distinta.payment_ids)

    def _distinta_back_accepted(self, distinta):
        self.resource_edit(
            resource=distinta,
            actions="back_to_accepted",
        )
        self.assertEqual(distinta.state, "accepted")
        self.assertFalse(distinta.accreditation_move_id)

    def _distinta_back_draft(self, distinta):
        self.resource_edit(
            resource=distinta,
            actions="back_to_draft",
        )
        self.assertEqual(distinta.state, "draft")
        self.assertFalse(distinta.acceptance_move_ids)

    def _distinta_cancel(self, distinta):
        self.resource_edit(
            resource=distinta,
            actions="riba_cancel",
        )
        self.assertEqual(distinta.state, "cancel")

    def _distinta_reset_draft(self, distinta):
        self.resource_edit(
            resource=distinta,
            actions="action_draft",
        )
        self.assertEqual(distinta.state, "draft")

    def pay_invoice(self, invoice, distinta):
        act_windows = self.resource_edit(
            resource=invoice,
            actions="account.action_account_invoice_payment",
        )
        if self.is_action(act_windows):
            self.wizard(
                act_windows=act_windows,
                default={
                    "journal_id": "external.BNK1",
                },
                button_name="post",
            )
        self.assertEqual(distinta.state, "paid")
        for line_distinta in distinta.line_ids:
            self.assertTrue(
                line_distinta.payment_ids or line_distinta.extra_payment_ids
            )
        self.assertTrue(distinta.payment_ids)

    def test_riba(self):
        _logger.info("🎺 Starting test_riba()")
        self._edit_riba_config()
        invoices, due_records = self._validate_invoice()
        payment_order = self._generate_payment_order(due_records)
        self._download_cbi(payment_order, due_records)
        self._payorder_accepted(payment_order)
        self._validate_accepted_moves(payment_order, due_records)
        self._payorder_accreditation(payment_order, due_records)
        self._validate_accreditation_moves(payment_order, due_records)
        self._confirm_all_payments(payment_order, due_records)
        self._validate_payment_moves(payment_order, due_records)
        #
        _logger.info("🎺 Reset test_riba()")
        self._distinta_back_accreditated(payment_order)
        self._distinta_back_accepted(payment_order)
        self._distinta_back_draft(payment_order)
        self._distinta_cancel(payment_order)
        self._distinta_reset_draft(payment_order)
        #
        _logger.info("🎺 Repeat test_riba()")
        self._download_cbi(payment_order, due_records)
        self._payorder_accepted(payment_order)
        self._validate_accepted_moves(payment_order, due_records)
        self._payorder_accreditation(payment_order, due_records)
        self._validate_accreditation_moves(payment_order, due_records)
        self._confirm_all_payments(payment_order, due_records)
        self._validate_payment_moves(payment_order, due_records)
        #
        _logger.info("🎺 Test unsolved and pay test_riba()")
        self._riba_unsolved(payment_order)
        # Unsolve riba does not update payments
        self._validate_payment_moves_with_unsolved(payment_order, due_records)
        self._riba_solved(payment_order)
        # Payments still remian unchanged
        self._validate_payment_moves(payment_order, due_records)
        self._riba_unsolved(payment_order)
        # Pay unsolved invoice
        self.pay_invoice(invoices[0], payment_order)

