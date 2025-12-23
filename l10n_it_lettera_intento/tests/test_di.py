# -*- coding: utf-8 -*-
import logging
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)


# Record data for base models


TEST_SETUP_LIST = [
    "account.account",
    "account.tax",
    "account.journal",
    "account.fiscal.position",
    "account.payment.term",
    "account.payment.term.line",
    "product.template",
    "res.partner",
    "account.invoice",
    "account.invoice.line",
]


class TestDichiarazioneIntento(SingleTransactionCase):
    def setUp(self):
        super(TestDichiarazioneIntento, self).setUp()
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
        super(TestDichiarazioneIntento, self).tearDown()

    def _test_di_1_sale(self):
        xref = "z0bug.invoice_Z0_9"
        invoice = self.resource_browse(xref=xref)
        self.resource_edit(resource=invoice, actions="action_invoice_open")
        invoice = self.resource_browse(xref=xref)
        self.assertEqual(
            invoice.state,
            "open",
            msg="action_invoice_open() FAILED: no state changed!"
        )
        self.assertEqual(round(invoice.amount_tax, 2), 10.91)
        self.assertEqual(invoice.amount_total, 160.50)
        self.assertEqual(invoice.amount_di, 100.00)

    def test_di(self):
        _logger.info("🎺 Testing Dichiarazione Intento")
        self._test_di_1_sale()
