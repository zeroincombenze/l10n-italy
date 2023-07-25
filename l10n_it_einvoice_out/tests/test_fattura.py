# -*- coding: utf-8 -*-
import os
import re
import logging
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)

# Record data for base models
TEST_ACCOUNT_ACCOUNT = {
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
}

TEST_ACCOUNT_FISCAL_POSITION = {
    "z0bug.fiscalpos_it": {
        "name": "Italia",
    },
    "z0bug.fiscalpos_eu": {
        "name": "EU",
    },
    "z0bug.fiscalpos_xx": {
        "name": "xx",
    },
}

TEST_ACCOUNT_JOURNAL = {
    "external.INV": {
        "code": "INV",
        "type": "sale",
        "update_posted": True,
        "name": "Fatture di vendita",
    },
}

TEST_ACCOUNT_PAYMENT_TERM = {
    "z0bug.payment_term_1": {
        "name": "RiBA 30 GG",
    },
    "z0bug.payment_term_2": {
        "name": "Bonifico",
    },
}

TEST_ACCOUNT_PAYMENT_TERM_LINE = {
    "z0bug.payment_term_1_1": {
        "payment_id": "z0bug.payment_term_1",
        "sequence": 1,
        "days": 30,
        "value": "balance",
    },
    "z0bug.payment_term_2_1": {
        "payment_id": "z0bug.payment_term_2",
        "sequence": 1,
        "days": 0,
        "value": "balance",
    },
}

TEST_ACCOUNT_TAX = {
    "external.22v": {
        "amount_type": "percent",
        "account_id": "z0bug.coa_tax_iva",
        "name": "IVA 22% su vendite",
        "refund_account_id": "z0bug.coa_tax_iva",
        "amount": 22,
        "type_tax_use": "sale",
        "price_include": False,
        "description": "22v",
    },
    "external.a41v": {
        "amount_type": "percent",
        "name": "vendite art. 41",
        "amount": 0,
        "type_tax_use": "sale",
        "price_include": False,
        "description": "a41v",
        "kind_id": "l10n_it_ade.n3_2",
        "law_reference": "art.41",
    },
    "external.a7tv": {
        "amount_type": "percent",
        "name": "vendite art. 7ter",
        "amount": 0,
        "type_tax_use": "sale",
        "price_include": False,
        "description": "a7tv",
        "kind_id": "l10n_it_ade.n3_1",
        "law_reference": "art.7 ter",
    },
}

# Record data for models to test
TEST_ACCOUNT_INVOICE = {
    "z0bug.invoice_Z0_1": {
        "origin": "SO123",
        "reference": "SO123",
        "type": "out_invoice",
        "payment_term_id": "z0bug.payment_1",
        "journal_id": "external.INV",
        "date_invoice": "####-<#-99",
        "partner_bank_id": "z0bug.bank_company_1",
        "partner_id": "z0bug.res_partner_1",
        "fiscal_position_id": "z0bug.fiscalpos_it",
    },
    "z0bug.invoice_Z0_2": {
        "origin": "23011214",
        "reference": "23011214",
        "type": "out_invoice",
        "payment_term_id": "z0bug.payment_2",
        "journal_id": "external.INV",
        "date_invoice": "####-<#-99",
        "partner_id": "z0bug.res_partner_2",
        "fiscal_position_id": "z0bug.fiscalpos_eu",
    },
    "z0bug.invoice_Z0_3": {
        "origin": "mail",
        "reference": "mail",
        "type": "out_invoice",
        "journal_id": "external.INV",
        "date_invoice": "####-<#-99",
        "partner_id": "z0bug.res_partner_3",
        "fiscal_position_id": "z0bug.fiscalpos_xx",
    },
}

TEST_ACCOUNT_INVOICE_LINE = {
    "z0bug.invoice_Z0_1_1": {
        "product_id": "z0bug.product_product_1",
        "invoice_id": "z0bug.invoice_Z0_1",
        "price_unit": 0.42,
        "account_id": "z0bug.coa_sale",
        "name": "Prodotto Alpha",
        "invoice_line_tax_ids": "external.22v",
        "quantity": 100,
    },
    "z0bug.invoice_Z0_1_2": {
        "product_id": "z0bug.product_product_2",
        "invoice_id": "z0bug.invoice_Z0_1",
        "price_unit": 1.69,
        "account_id": "z0bug.coa_sale",
        "name": "Prodotto Beta",
        "invoice_line_tax_ids": "external.22v",
        "quantity": 10,
    },
    "z0bug.invoice_Z0_2_1": {
        "product_id": "z0bug.product_product_2",
        "invoice_id": "z0bug.invoice_Z0_2",
        "price_unit": 1.69,
        "account_id": "z0bug.coa_sale",
        "name": "Prodotto Beta",
        "invoice_line_tax_ids": "external.a41v",
        "quantity": 50,
    },
    "z0bug.invoice_Z0_3_1": {
        "product_id": "z0bug.product_product_2",
        "invoice_id": "z0bug.invoice_Z0_2",
        "price_unit": 1.80,
        "account_id": "z0bug.coa_sale",
        "name": "Prodotto Beta",
        "invoice_line_tax_ids": "external.a7tv",
        "quantity": 20,
    },
}

TEST_PRODUCT_TEMPLATE = {
    # Consumable product
    "z0bug.product_template_1": {
        "default_code": "AA",
        "name": "Prodotto Alpha",
        "lst_price": 0.84,
        "standard_price": 0.42,
        "type": "consu",
        "uom_id": "product.product_uom_unit",
        "uom_po_id": "product.product_uom_unit",
        "property_account_income_id": "z0bug.coa_sale",
    },
    "z0bug.product_template_2": {
        "default_code": "BB",
        "name": "Prodotto Beta",
        "lst_price": 3.38,
        "standard_price": 1.69,
        "type": "consu",
        "uom_id": "product.product_uom_unit",
        "uom_po_id": "product.product_uom_unit",
        "property_account_income_id": "z0bug.coa_sale",
    },
    # Product on stock
    "z0bug.product_template_18": {
        "default_code": "RR",
        "name": "Prodotto Rho",
        "lst_price": 1.19,
        "standard_price": 0.59,
        "type": "product",
        "uom_id": "product.product_uom_unit",
        "uom_po_id": "product.product_uom_unit",
        "property_account_income_id": "z0bug.coa_sale",
    },
    # Service
    "z0bug.product_template_23": {
        "default_code": "WW",
        "name": "Special Worldwide service",
        "lst_price": 1.88,
        "standard_price": 0,
        "type": "service",
        "uom_id": "product.product_uom_unit",
        "uom_po_id": "product.product_uom_unit",
        "property_account_income_id": "z0bug.coa_sale2",
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
        "property_payment_term_id": "z0bug.payment_1",
        "property_account_position_id": "z0bug.fiscalpos_it",
        "electronic_invoice_subjected": True,
        "codice_destinatario": "A1B2C3X",
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
        "property_payment_term_id": "z0bug.payment_2",
        "property_account_position_id": "z0bug.fiscalpos_eu",
        "electronic_invoice_subjected": True,
        "codice_destinatario": "XXXXXXX",
    },
    "z0bug.res_partner_3": {
        "name": "Antonio La Pacchia",
        "street": "Kaiserswerther Straße 12-24",
        "country_id": "base.ch",
        "city": "Zurich",
        "customer": True,
        "supplier": False,
        "is_company": True,
        "fiscalcode": "VGLNTN59H26B963V",
        "property_account_position_id": "z0bug.fiscalpos_xx",
        "electronic_invoice_subjected": True,
        "codice_destinatario": "XXXXXXX",
    },
}

TEST_RES_PARTNER_BANK = {
    "z0bug.bank_company_1": {
        "acc_number": "IT15A0123412345100000123456",
        "partner_id": "base.main_partner",
        # "acc_type": "iban",
    },
}

TEST_SETUP_LIST = [
    "account.account",
    "account.fiscal.position",
    "account.journal",
    "account.tax",
    "account.payment.term",
    "account.payment.term.line",
    "res.partner",
    "res.partner.bank",
    "product.template",
    "res.company",
    "account.invoice",
    "account.invoice.line",
]


class AccountInvoice(SingleTransactionCase):

    def setUp(self):
        super(AccountInvoice, self).setUp()
        # Add following statement just for get debug information
        self.debug_level = 0
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
            "DatiGenerali/DatiGeneraliDocumento/Data": invoice.date_invoice,
            "DatiGenerali/DatiGeneraliDocumento/Numero": invoice.number,
            "ImportoTotaleDocumento": "%1.2f" % invoice.amount_total,
            "TipoDocumento": "TD01",
        })
    def _validate_xml_vat(self, invoice, xml, vat=None):
        vat = vat or invoice.partner_id.vat
        self._test_file_xml(xml, {
            "CessionarioCommittente/DatiAnagrafici/IdFiscaleIVA/IdPaese": vat[: 2],
            "CessionarioCommittente/DatiAnagrafici/IdFiscaleIVA/IdCodice": vat[2:],
        })

    def test_account_invoice(self):
        model = "account.invoice"
        for xref in TEST_ACCOUNT_INVOICE.keys():
            self.log_lvl_1(u"🎺 Testing %s[%s]" % (model, xref))
            invoice = self.resource_browse(xref=xref)
            self.resource_edit(resource=invoice, actions="action_invoice_open")
            self.assertEqual(
                invoice.state, "open", "action_invoice_open() FAILED: no state changed!"
            )
            self.wizard(module=".",
                        action_name="action_wizard_export_fatturapa",
                        records=invoice,
                        button_name="exportFatturaPA")
            xml = self.field_download(invoice.fatturapa_attachment_out_id, "datas")
            self._validate_xml_common(invoice, xml)
            if xref == "z0bug.invoice_Z0_3":
                self._validate_xml_vat(invoice, xml, vat="CH99999999999")
            else:
                self._validate_xml_vat(invoice, xml)
