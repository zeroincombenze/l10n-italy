# -*- coding: utf-8 -*-
import os
import re
import logging
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)

# Record data for base models
TEST_ACCOUNT_ACCOUNT = {
    # Output (paid) VAT account
    "z0bug.coa_tax_ova": {
        "code": "101300",
        "reconcile": False,
        "user_type_id": "account.data_account_type_current_assets",
        "name": "IVA n/credito",
    },
    # Input (received) VAT account
    "z0bug.coa_tax_iva": {
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
    "z0bug.coa_cog": {
        "code": "210000",
        "name": "Merci conto vendita",
        "user_type_id": "account.data_account_type_direct_costs",
        "reconcile": False,
    },
    "external.490050": {
        "code": "490050",
        "name": "G/C RC",
        "user_type_id": "account.data_account_type_current_liabilities",
        "reconcile": False,
    },
}

TEST_ACCOUNT_FISCAL_POSITION = {
    "z0bug.fiscalpos_it": {
        "name": "Italia",
    },
    "z0bug.fiscalpos_rc": {
        "name": "RC locale",
        # "rc_type_id": "z0bug.rc_type_local",
    },
}

TEST_ACCOUNT_JOURNAL = {
    "external.CG": {
        "code": "CG",
        "type": "general",
        "update_posted": True,
        "name": "Giroconti tecnici",
        "default_debit_account_id": "external.490050",
        "default_credit_account_id": "external.490050",
        "sequence": 100,
    },
}

TEST_ACCOUNT_RC_TYPE = {
    "z0bug.rc_type_local": {
        "name": "Reverse charge locale",
        "method": "selfinvoice",
        "partner_type": "other",
        "journal_id": "external.INV",
        "payment_journal_id": "external.GC",
        "transitory_account_id": "external.490050",
    },
}

TEST_ACCOUNT_RC_TYPE_TAX = {
    "z0bug.rc_type_local_external.a41a": {
        "rc_type_id": "rc_type_local",
        "purchase_tax_id": "external.a41a",
        "sale_tax_id": "external.aa41v",
    },
}

TEST_ACCOUNT_TAX = {
    "external.a41a": {
        "amount_type": "percent",
        "name": "Acquisti art. 41",
        "amount": 22,
        "account_id": "z0bug.coa_tax_ova",
        "refund_account_id": "z0bug.coa_tax_ova",
        "type_tax_use": "purchase",
        "price_include": False,
        "description": "a41a",
    },
    "external.aa41v": {
        "amount_type": "percent",
        "name": "R/C art. 41",
        "amount": 22,
        "account_id": "z0bug.coa_tax_iva",
        "refund_account_id": "z0bug.coa_tax_iva",
        "type_tax_use": "sale",
        "price_include": False,
        "description": "a41v",
        "kind_id": "l10n_it_ade.n3_2",
        "law_reference": "art.41",
    },
}

TEST_ACCOUNT_INVOICE = {
    "z0bug.invoice_Z0_1": {
        "type": "in_invoice",
        "journal_id": "external.BILL",
        "date_invoice": "####-##-<#",
        "date": "####-##-##",
        "partner_id": "z0bug.res_partner_1",
        "fiscal_position_id": "z0bug.fiscalpos_rc",
    },
}

TEST_ACCOUNT_INVOICE_LINE = {
    "z0bug.invoice_Z0_1_1": {
        "invoice_id": "z0bug.invoice_Z0_1",
        "price_unit": 100,
        "account_id": "z0bug.coa_cog",
        "name": "Prodotto Alpha",
        "invoice_line_tax_ids": "external.a41a",
        "quantity": 1,
    },
}

TEST_RES_COMPANY = {
    "z0bug.mycompany": {
        "fatturapa_fiscal_position_id": "l10n_it_einvoice_base.fatturapa_RF01",
        "fatturapa_sequence_id": "l10n_it_einvoice_base.seq_fatturapa",
        "fatturapa_rea_office": "base.state_it_mi",
        "fatturapa_rea_number": "123456",
        "fatturapa_rea_capital": 10000,
        "fatturapa_rea_partner": "SU",
    }
}

TEST_RES_PARTNER = {
    "z0bug.partner_mycompany": {
        "name": "Test Company",
        "street": "Via dei Matti, 0",
        "zip": "20080",
        "city": "Ozzero",
        "state_id": "base.state_it_mi",
        "customer": False,
        "supplier": False,
        "is_company": True,
        "email": "info@testcompany.org",
        "phone": "+39 025551234",
        "website": "https://www.testcompany.org",
    },
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
        "vat": "IT00115719999",
        "property_account_position_id": "z0bug.fiscalpos_rc",
    },
    "z0bug.res_partner_2": {
        "name": "Freie Universität Berlin",
        "street": "Kaiserswerther Straße 12-24",
        "country_id": "base.de",
        "zip": "14195",
        "city": "Berlin",
        "customer": True,
        "supplier": False,
        "is_company": True,
        "vat": "DE123456788",
        # "property_account_position_id": "z0bug.fiscalpos_eu",
        "electronic_invoice_subjected": True,
        "codice_destinatario": "XXXXXXX",
    },
}

TEST_SETUP_LIST = [
    "account.account",
    "account.journal",
    "account.tax",
    # "account.rc.type",
    # "account.rc.type.tax",
    "account.fiscal.position",
    "res.partner",
    "res.company",
    "account.invoice",
    "account.invoice.line",
]


class AccountInvoice(SingleTransactionCase):

    def setUp(self):
        super(AccountInvoice, self).setUp()
        # Add following statement just for get debug information
        self.debug_level = 3
        data = {"TEST_SETUP_LIST": TEST_SETUP_LIST}
        for resource in TEST_SETUP_LIST:
            item = "TEST_%s" % resource.upper().replace(".", "_")
            data[item] = globals()[item]
        self.declare_all_data(data)                 # TestEnv swallows the data
        self.setup_company(
            self.default_company(),
            xref="z0bug.mycompany",
            partner_xref="z0bug.partner_mycompany",
            recv_xref="z0bug.coa_recv",
            pay_xref="z0bug.coa_pay",
            bnk1_xref="z0bug.coa_bnk1",
            values={
                "name": "Test Company",
                "vat": "IT05111810015",
                "country_id": "base.it",
            },
        )
        self.setup_env()                            # Create test environment

    def tearDown(self):
        super(AccountInvoice, self).tearDown()
        if os.environ.get("ODOO_COMMIT_TEST", ""):  # pragma: no cover
            # Save test environment, so it is available to dump
            self.env.cr.commit()                    # pylint: disable=invalid-commit
            _logger.info("✨ Test data committed")

    def _test_file_xml(self, xml, values):
        xml = xml.replace("\n", "")
        for key, val in values.items():
            keys = key.split("/")
            begkey = ""
            for kk in keys[: -1]:
                begkey += "<%s>.*" % kk
            begkey += "<%s>" % keys[-1]
            endkey = "</%s>" % keys[-1]
            pattern = "".join([begkey, val, endkey])
            self.assertTrue(re.search(pattern, xml),
                            "Pattern %s not found in XML" % pattern)
        # _logger.info(xml)

    def _validate_xml_common(self, invoice, xml):
        self._test_file_xml(xml, {
            "DatiTrasmissione/FormatoTrasmissione": "FPR12",
            "DatiTrasmissione/IdTrasmittente/IdPaese":
                self.default_company().vat[: 2],
            "DatiTrasmissione/IdTrasmittente/IdCodice":
                self.default_company().vat[2:],
            "CodiceDestinatario": invoice.partner_id.codice_destinatario,
            "CedentePrestatore/DatiAnagrafici/IdFiscaleIVA/IdPaese":
                self.default_company().vat[: 2],
            "CedentePrestatore/DatiAnagrafici/IdFiscaleIVA/IdCodice":
                self.default_company().vat[2:],
            "CessionarioCommittente/DatiAnagrafici/IdFiscaleIVA/IdPaese":
                invoice.partner_id.vat[: 2],
            "CessionarioCommittente/DatiAnagrafici/IdFiscaleIVA/IdCodice":
                invoice.partner_id.vat[2:],
            "DatiGenerali/DatiGeneraliDocumento/Data": invoice.date_invoice,
            "DatiGenerali/DatiGeneraliDocumento/Numero": invoice.number,
            "ImportoTotaleDocumento": "%1.2f" % invoice.amount_total,
            "TipoDocumento": "TD01",
        })

    def test_account_invoice(self):
        model = "account.invoice"
        for xref in TEST_ACCOUNT_INVOICE.keys():
            self.log_lvl_1(u"🎺 Testing %s[%s]" % (model, xref))
            invoice = self.resource_browse(xref=xref)
            self.resource_edit(resource=invoice, actions="action_invoice_open")
            self.assertEqual(
                invoice.state, "open",
                "action_invoice_open() FAILED: no state changed!"
            )

