# -*- coding: utf-8 -*-
import os
import logging
from .testenv import MainTest as SingleTransactionCase

import python_plus

_logger = logging.getLogger(__name__)


TEST_ACCOUNT_ACCOUNT = {
    # The bank account is linked to demo dat: usually is 101401
    # "z0bug.coa_bnk1": {
    #     "code": "101401",
    #     "name": "Banca",
    #     "reconcile": True,
    #     "user_type_id": "account.data_account_type_liquidity",
    # },
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
    "z0bug.invoice_Z0_2": {
        "origin": "SO123",
        "reference": "SO123",
        "type": "out_invoice",
        "payment_term_id": "z0bug.payment_2",
        "journal_id": "external.INV",
        "date_invoice": "####-<#-99",
        "partner_id": "z0bug.res_partner_2",
    },
}

TEST_ACCOUNT_INVOICE_LINE = {
    "z0bug.invoice_Z0_2_1": {
        "sequence": 1,
        "product_id": "z0bug.product_product_1",
        "invoice_id": "z0bug.invoice_Z0_2",
        "price_unit": 0.42,
        "account_id": "z0bug.coa_sale",
        "name": "Prodotto Alpha",
        "invoice_line_tax_ids": "external.22v",
        "quantity": 100,
    },
    "z0bug.invoice_Z0_2_2": {
        "sequence": 2,
        "product_id": "z0bug.product_product_2",
        "invoice_id": "z0bug.invoice_Z0_2",
        "price_unit": 1.69,
        "account_id": "z0bug.coa_sale",
        "name": "Prodotto Beta",
        "invoice_line_tax_ids": "external.22v",
        "quantity": 10,
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
        "payment_method_credit": "account_banking_riba.riba",
    },
    "z0bug.payment_2_1": {
        "payment_id": "z0bug.payment_2",
        "sequence": 1,
        "days": 30,
        "value": "percent",
        "value_amount": 50,
        "payment_method_credit": "account_banking_riba.riba",
    },
    "z0bug.payment_2_2": {
        "payment_id": "z0bug.payment_2",
        "sequence": 2,
        "days": 60,
        "value": "balance",
        "payment_method_credit": "account_banking_riba.riba",
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
        # "electronic_invoice_subjected": True,
        # "codice_destinatario": "A1B2C3X",
    },
    "z0bug.res_partner_2": {
        "name": "Latte Beta Due s.n.c.",
        "street": "Via Dueville, 2",
        "country_id": "base.it",
        "property_payment_term_id": "z0bug.payment_2",
        "city": "S. Secondo Pinerolo",
        "zip": "10060",
        "supplier": False,
        "email": "agrolait2@libero.it",
        "vat": "IT02345670018",
        "website": "http://www.agrolait2.it/",
        "phone": "+39 0121555123",
        "customer": True,
        "is_company": True,
        "state_id": "base.state_it_to",
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
    "account.journal",
    "account.payment.term",
    "account.payment.term.line",
    "product.template",
    "res.partner",
    "res.partner.bank",
    "riba.configuration",
    "account.invoice",
    "account.invoice.line",
]


class TestRiba(SingleTransactionCase):
    def setUp(self):
        super(TestRiba, self).setUp()
        # Add following statement just for get debug information
        self.debug_level = 2
        data = {"TEST_SETUP_LIST": TEST_SETUP_LIST}
        for resource in TEST_SETUP_LIST:
            item = "TEST_%s" % resource.upper().replace(".", "_")
            data[item] = globals()[item]
        self.declare_all_data(data)  # TestEnv swallows the data
        # Add alias to company
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
            # Save test environment, so it is available to dump
            self.env.cr.commit()  # pylint: disable=invalid-commit
            _logger.info("✨ Test data committed")

    def _validate_cbi_file(self, riba_cbi):
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

    def _validate_accepted_moves(self, payment_order, due_records):
        acceptance_account_id = payment_order.config_id.acceptance_account_id
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

    def _validate_accreditation_moves(self, distinta, due_records):
        accreditation_account_debit_id = (
            distinta.config_id.accreditation_account_debit_id.id
        )
        accreditation_account_credit_id = (
            distinta.config_id.accreditation_account_credit_id.id
        )
        bank_amount = 0.0
        for line in due_records:
            bank_amount += line.debit - line.credit
        for line in distinta.accreditation_move_id.line_ids:
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

    def _validate_payment_moves(self, distinta, due_records):
        settlement_account_debit_id = distinta.config_id.settlement_account_debit_id.id
        settlement_account_credit_id = (
            distinta.config_id.settlement_account_credit_id.id
        )

        template = []
        for due in due_records:
            tmpl_move = []
            vals = {
                "account_id": settlement_account_debit_id,
                "debit": due.debit or due.credit,
                "credit": 0.0,
            }
            tmpl_move.append(vals)
            vals = {
                "account_id": settlement_account_credit_id,
                "debit": 0.0,
                "credit": due.credit or due.debit,
            }
            tmpl_move.append(vals)
            template.append({"line_ids": tmpl_move})

        self.validate_records(template, [ln.move_id for ln in distinta.payment_ids])

    def _validate_invoice(self):
        riba_config = self.resource_bind("z0bug.riba_config")
        self.resource_edit(
            resource=riba_config,
            web_changes=[
                ("accreditation_account_credit_id", "z0bug.coa_liq_tra2"),
                ("accreditation_account_debit_id", "z0bug.coa_bnk1"),
                ("bank_expense_account_id", "z0bug.coa_bnk_fee"),
            ],
        )

        invoices = self.env["account.invoice"]
        for xref in TEST_ACCOUNT_INVOICE.keys():
            invoice = self.resource_bind(xref)
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
            ]
        )

        date_invoice = self.compute_date("####-<#-99")
        date_due1 = self.compute_date(+30, refdate=date_invoice)
        date_due2 = self.compute_date(+60, refdate=date_invoice)
        template_dues = []
        # vals = {
        #     "account_id": invoice[0].account_id.id,
        #     "partner_id": "z0bug.res_partner_1",
        #     "date": date_invoice,
        #     "date_maturity": date_due1,
        #     "riba": True,
        # }
        # template_dues.append(vals)
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

    def _download_cbi(self, distinta):
        riba_cbi = self.resource_download(
            module=".",
            action_name="action_wizard_riba_file_export",
            records=distinta,
            button_name="act_getfile",
            field="riba_txt",
        )
        self.assertTrue(riba_cbi)
        self._validate_cbi_file(riba_cbi)

    def _payorder_accepted(self, payment_order):
        self.resource_edit(
            resource=payment_order,
            actions="confirm",
        )
        self.assertEqual(payment_order.state, "accepted")
        self.assertTrue(payment_order.acceptance_move_ids)

    def _riba_list_accreditation(self, distinta, due_records):
        bank_amount = 0.0
        for line in due_records:
            bank_amount += line.debit - line.credit
        act_windows = self.wizard(
            module=".",
            action_name="riba_accreditation_action",
            records=distinta,
            web_changes=[("bank_amount", bank_amount)],
            button_name="create_move",
        )
        self.assertTrue(self.is_action(act_windows))
        self.assertEqual(distinta.state, "accredited")
        self.assertTrue(distinta.accreditation_move_id)

    def _riba_confirm_all_payments(self, distinta):
        self.resource_edit(
            resource=distinta,
            actions="settle_all_line",
        )
        self.assertEqual(distinta.state, "paid")
        for line_distinta in distinta.line_ids:
            self.assertTrue(line_distinta.payment_ids)
        self.assertTrue(distinta.payment_ids)

    def _riba_unsolved(self, distinta):
        line_distinta = distinta.line_ids[0]
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
        self.assertEqual(distinta.state, "unsolved")
        self.assertTrue(distinta.unsolved_move_ids)

    def _riba_solved(self, distinta):
        line_distinta = distinta.line_ids[0]
        self.resource_edit(
            resource=line_distinta,
            actions="riba_line_back2solved",
        )
        self.assertEqual(line_distinta.state, "accredited")

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
        invoice, due_records = self._validate_invoice()
        payment_order = self._generate_payment_order(due_records)
        self._download_cbi(payment_order)
        self._payorder_accepted(payment_order)
        self._validate_accepted_moves(payment_order, due_records)
        self._riba_list_accreditation(payment_order, due_records)
        self._validate_accreditation_moves(payment_order, due_records)
        self._riba_confirm_all_payments(payment_order)
        self._validate_payment_moves(payment_order, due_records)

        _logger.info("🎺 Reset test_riba()")
        self._distinta_back_accreditated(payment_order)
        self._distinta_back_accepted(payment_order)
        self._distinta_back_draft(payment_order)
        self._distinta_cancel(payment_order)
        self._distinta_reset_draft(payment_order)

        _logger.info("🎺 Repeat test_riba()")
        self._download_cbi(payment_order)
        self._payorder_accepted(payment_order)
        self._validate_accepted_moves(payment_order, due_records)
        self._riba_list_accreditation(payment_order, due_records)
        self._validate_accreditation_moves(payment_order, due_records)
        self._riba_confirm_all_payments(payment_order)
        self._validate_payment_moves(payment_order, due_records)

        _logger.info("🎺 Test unsolved and pay test_riba()")
        self._riba_unsolved(payment_order)
        self._riba_solved(payment_order)
        self._riba_unsolved(payment_order)

        self.pay_invoice(invoice, payment_order)
