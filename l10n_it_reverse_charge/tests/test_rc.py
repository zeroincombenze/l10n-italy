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
        # Test old deprecated mode
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

    def _test_rc_2_purchase(self):
        # Test new mode
        self.env["account.journal"].search([("update_posted", "!=", True)]).write(
            {"update_posted": True}
        )
        xref = "z0bug.invoice_ZI_6"
        invoice = self.resource_browse(xref=xref)
        invoice.action_invoice_cancel()
        invoice.action_invoice_draft()
        # Transform old stype configuration to new configuration
        fp = invoice.fiscal_position_id
        rct = invoice.fiscal_position_id.rc_type_id
        fp.write({
            "rc_type": rct.rc_type,
            "partner_type": rct.partner_type,
            "partner_id": rct.partner_id.id,
            "self_journal_id": rct.self_journal_id.id,
            "payment_journal_id": rct.payment_journal_id.id,
            "transient_account_id": rct.transient_account_id.id,
        })
        rct.write({
            "rc_type": False,
            # "rc_type_id": False,
            "partner_type": False,
            "partner_id": False,
            "self_journal_id": False,
            "payment_journal_id": False,
            "transient_account_id": False,
        })
        for taxmap in rct.tax_ids:
            taxmap.purchase_tax_id.write({
                "rc_sale_tax_id": taxmap.sale_tax_id.id
            })

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

    def test_rc(self):
        _logger.info("🎺 Testing Reverse Charge")
        # BUG WORKAROUND
        self.resource_browse("z0bug.tax_a17c6ca").rc_sale_tax_id = self.resource_browse(
            "z0bug.tax_a17c6ca")
        self._test_rc_1_purchase()
        self._test_rc_1_sale()
        self._test_rc_2_purchase()
