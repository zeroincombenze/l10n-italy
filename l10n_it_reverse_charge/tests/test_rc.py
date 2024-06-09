# -*- coding: utf-8 -*-
import logging
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)


# Record data for base models


TEST_SETUP_LIST = [
    "account.account",
    "account.tax",
    "account.journal",
    "account.rc.type",
    "account.rc.type.tax",
    "account.fiscal.position",
    "account.payment.term",
    "account.payment.term.line",
    "product.template",
    "res.partner",
    "account.invoice",
    "account.invoice.line",
]


class TestReverseCharge(SingleTransactionCase):
    def setUp(self):
        super(TestReverseCharge, self).setUp()
        # Add following statement just for get debug information
        self.debug_level = 0
        self.odoo_commit_test = True
        self.setup_company(
            self.default_company(),
            xref="z0bug.mycompany",
            partner_xref="z0bug.partner_mycompany",
            recv_xref="z0bug.coa_recv",
            values={
                "name": "Test Company",
                "vat": "IT05111810015",
                "country_id": "base.it",
            },
        )
        self.setup_env()  # Create test environment

    def tearDown(self):
        super(TestReverseCharge, self).tearDown()

    def _test_rc_1_purchase(self):
        xref = "z0bug.invoice_ZI_6"
        invoice = self.resource_browse(xref=xref)
        self.resource_edit(resource=invoice, actions="action_invoice_open")
        invoice = self.resource_browse(xref=xref)
        self.assertEqual(
            invoice.state,
            "open",
            msg="action_invoice_open() FAILED: no state changed!"
        )
        self.assertEqual(invoice.amount_tax, 32.97)
        self.assertEqual(invoice.amount_total, 182.85)
        self.assertEqual(invoice.amount_net_pay, 160.85)
        self.assertEqual(invoice.residual, 160.85)
        self.assertEqual(invoice.amount_rc, -22.0)
        self_invoice = invoice.rc_self_invoice_id
        self.assertTrue(self_invoice)
        self.assertEqual(
            self_invoice.state,
            "paid",
            msg="Invalid self-invoice status"
        )
        self.assertEqual(self_invoice.amount_tax, 22.0)
        self.assertEqual(self_invoice.amount_total, 122.0)

    def _test_rc_1_sale(self):
        xref = "z0bug.invoice_Z0_9"
        invoice = self.resource_browse(xref=xref)
        self.resource_edit(resource=invoice, actions="action_invoice_open")
        invoice = self.resource_browse(xref=xref)
        self.assertEqual(
            invoice.state,
            "open",
            msg="action_invoice_open() FAILED: no state changed!"
        )
        self.assertEqual(round(invoice.amount_tax, 2), 32.91)
        self.assertEqual(invoice.amount_total, 182.50)
        self.assertEqual(invoice.amount_net_pay, 160.50)
        self.assertEqual(invoice.residual, 160.50)
        self.assertEqual(invoice.amount_rc, -22.0)

        template = []
        tmpl_move = []
        vals = {
            "account_id": invoice.account_id.id,
            "debit": 182.50,
            "credit": 0.0,
            "tax_line_id": False,
            "tax_ids": [],
        }
        tmpl_move.append(vals)
        vals = {
            "account_id": invoice.account_id.id,
            "debit": 0.0,
            "credit": 22.0,
            "tax_line_id": self.env.ref("z0bug.tax_a17c6cv"),
            "tax_ids": [],
        }
        tmpl_move.append(vals)
        template.append({"line_ids": tmpl_move})
        self.validate_records(template, invoice.move_id)

    def test_rc(self):
        _logger.info("🎺 Testing Reverse Charge")
        self._test_rc_1_purchase()
        self._test_rc_1_sale()

