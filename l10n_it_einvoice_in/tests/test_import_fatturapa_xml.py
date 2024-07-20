# -*- coding: utf-8 -*-
"""Test e-invoice import
Test various xml files with many properties.
See file ./tests/data/README.txt for furthermore information about specific
checkpoint of every xml file.
"""
# from odoo.exceptions import UserError
from .fatturapa_common import FatturapaCommon


class TestFatturaPAXMLValidation(FatturapaCommon):

    def setUp(self):
        super(TestFatturaPAXMLValidation, self).setUp()
        # Set VAT number of e-invoices
        self.env.user.company_id.vat = "IT05111810015"
        self.tax_22a = self.create_tax_22a()
        self.tax_a10a = self.create_tax_a10a()
        self.tax_a27a = self.create_tax_a27a()
        self.tax_a17c2a = self.create_tax_a17c2a()
        self.wt85 = self.create_wt_85()
        self.wt115 = self.create_wt_115()
        self.invoice_model = self.env["account.invoice"]

    def test_00_xml_import_001(self):
        # Mostly fields tests, Albo professionale, Cassa previdenziale. VAT with spaces
        self.env.user.company_id.cassa_previdenziale_product_id = self.service.id
        res = self.run_wizard("test_00_001", "IT05979361218_001.xml")
        invoice_id = res.get("domain")[0][2][0]
        invoice = self.invoice_model.browse(invoice_id)
        self.assertEqual(invoice.partner_id.register_code, "TO1258B")
        self.assertEqual(invoice.partner_id.register_fiscalpos.code, "RF02")
        self.assertEqual(invoice.reference, "FT/2024/0006")
        self.assertEqual(invoice.amount_total, 57.00)
        self.assertEqual(invoice.gross_weight, 0.00)
        self.assertEqual(invoice.net_weight, 0.00)
        # self.assertEqual(invoice.welfare_fund_ids[0].kind_id.code, "N4")
        # self.assertFalse(invoice.art73)
        # welfare_found = False
        # for line in invoice.invoice_line_ids:
        #     if line.product_id.id == self.service.id:
        #         self.assertEqual(line.price_unit, 3)
        #         welfare_found = True
        # self.assertTrue(welfare_found)
        self.assertTrue(len(invoice.e_invoice_line_ids) == 1)
        self.assertEqual(
            invoice.e_invoice_line_ids[0].name, "Prodotto di test al giorno"
        )
        self.assertEqual(invoice.e_invoice_line_ids[0].qty, 15)
        self.assertEqual(invoice.e_invoice_line_ids[0].uom, "Giorno(i)")
        self.assertEqual(invoice.e_invoice_line_ids[0].unit_price, 3.6)
        self.assertEqual(invoice.e_invoice_line_ids[0].total_price, 54)
        self.assertEqual(invoice.e_invoice_line_ids[0].tax_amount, 0)
        self.assertEqual(invoice.e_invoice_line_ids[0].tax_kind, "N4")
        self.assertTrue(len(invoice.e_invoice_line_ids[0].other_data_ids) == 2)
        self.assertEqual(
            invoice.e_invoice_line_ids[0].other_data_ids[0].text_ref, "Riferimento"
        )
