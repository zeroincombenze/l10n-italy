# -*- coding: utf-8 -*-
import os
import logging
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)


# Record data for base models

TEST_ACCOUNT_ACCOUNT = {
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
    "z0bug.coa_sale2": {
        "code": "200010",
        "name": "Ricavi da servizi",
        "user_type_id": "account.data_account_type_revenue",
        "reconcile": False,
    },
}

TEST_SETUP_LIST = [
    "account.account",
]


class TestReverseCharge(SingleTransactionCase):
    def setUp(self):
        super(TestReverseCharge, self).setUp()
        self.debug_level = 3
        data = {"TEST_SETUP_LIST": TEST_SETUP_LIST}
        for resource in TEST_SETUP_LIST:
            item = "TEST_%s" % resource.upper().replace(".", "_")
            data[item] = globals()[item]
        self.declare_all_data(data)
        self.setup_env()

    def tearDown(self):
        super(TestReverseCharge, self).tearDown()
        if os.environ.get("ODOO_COMMIT_TEST", ""):
            # Save test environment, so it is available to use
            self.env.cr.commit()  # pylint: disable=invalid-commit
            _logger.info("✨ Test data committed")

    def test_ddt(self):
        pass
