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

    def invoice_from_xml(self, mesg, xml_fn):
        return self.invoice_model.browse(
            self.run_wizard(mesg, xml_fn).get("domain")[0][2][0])

    def test_00_xml_import_001(self):
        # Mostly fields tests, Albo professionale, Cassa previdenziale. VAT with spaces
        invoice = self.invoice_from_xml("test_00_001", "IT05979361218_001.xml")
        self.assertEqual(invoice.partner_id.register_code, "TO1258B")
        self.assertEqual(invoice.partner_id.register_fiscalpos.code, "RF02")
        self.assertEqual(invoice.reference, "FT/2024/0006")
        self.assertEqual(invoice.amount_total, 57.0)
        self.assertEqual(invoice.gross_weight, 0.0)
        self.assertEqual(invoice.net_weight, 0.0)
        self.assertEqual(invoice.welfare_fund_ids[0].tax_kind_id.code, "N4")
        self.assertFalse(invoice.art73)
        welfare_found = False
        for line in invoice.invoice_line_ids:
            if line.product_id.id == self.service.id:
                self.assertEqual(line.price_unit, 3)
                welfare_found = True
        self.assertTrue(welfare_found)
        self.assertTrue(len(invoice.e_invoice_line_ids) == 1)
        self.assertEqual(
            invoice.e_invoice_line_ids[0].name, "Prodotto di test al giorno"
        )
        self.assertEqual(invoice.e_invoice_line_ids[0].qty, 15)
        self.assertEqual(invoice.e_invoice_line_ids[0].uom, "Giorno(i)")
        self.assertEqual(invoice.e_invoice_line_ids[0].unit_price, 3.6)
        self.assertEqual(invoice.e_invoice_line_ids[0].total_price, 54.0)
        self.assertEqual(invoice.e_invoice_line_ids[0].tax_amount, 0.0)
        self.assertEqual(invoice.e_invoice_line_ids[0].tax_kind, "N4")
        self.assertTrue(len(invoice.e_invoice_line_ids[0].other_data_ids) == 2)
        self.assertEqual(
            invoice.e_invoice_line_ids[0].other_data_ids[0].text_ref, "Riferimento"
        )
        self.assertEqual(invoice. e_invoice_amount_untaxed, 57.0)
        self.assertEqual(invoice. e_invoice_amount_tax, 0.0)
        self.assertEqual(invoice.e_invoice_amount_total, 57.0)

    def test_01_xml_import_11004(self):
        # Supplier name like previous, rappresentante fiscale
        invoice = self.invoice_from_xml("test_01_11004", "IT02780790107_11004.xml")
        self.assertEqual(invoice.reference, "123")
        self.assertEqual(invoice.date_invoice, "2024-07-18")
        self.assertEqual(invoice.amount_untaxed, 34.00)
        self.assertEqual(invoice.amount_tax, 7.48)
        self.assertEqual(len(invoice.invoice_line_ids[0].invoice_line_tax_ids), 1)
        self.assertEqual(
            invoice.invoice_line_ids[0].invoice_line_tax_ids[0].name, "22% e-bill"
        )
        self.assertEqual(invoice.fatturapa_summary_ids[0].amount_untaxed, 34.00)
        self.assertEqual(invoice.fatturapa_summary_ids[0].amount_tax, 7.48)
        self.assertEqual(invoice.fatturapa_summary_ids[0].payability, "D")
        self.assertEqual(invoice.partner_id.name, "SOCIETA' ALPHA SRL")
        self.assertEqual(invoice.partner_id.street, "VIALE ROMA 543")
        self.assertEqual(invoice.partner_id.state_id.code, "SS")
        self.assertEqual(invoice.partner_id.country_id.code, "IT")
        self.assertEqual(invoice.tax_representative_id.name, "Rappresentante fiscale")
        self.assertEqual(invoice.welfare_fund_ids[0].welfare_rate_tax, 0.04)
        order_related_doc = invoice.related_documents.filtered(
            lambda rd: rd.type == "order"
        )
        self.assertTrue(order_related_doc)
        self.assertEqual(order_related_doc.cig, "456def")
        self.assertEqual(order_related_doc.cup, "123abc")
        self.assertEqual(invoice.welfare_fund_ids[0].welfare_amount_tax, 9.0)
        self.assertFalse(invoice.welfare_fund_ids[0].welfare_taxable)
        self.assertEqual(invoice.unit_weight, "KGM")
        self.assertEqual(invoice.ftpa_incoterms, "DAP")
        self.assertEqual(invoice.fiscal_document_type_id.code, "TD01")
        self.assertTrue(invoice.art73)
        self.assertEqual(invoice. e_invoice_amount_untaxed, 34.0)
        self.assertEqual(invoice. e_invoice_amount_tax, 7.48)
        self.assertEqual(invoice.e_invoice_amount_total, 41.48)

    def test_02_xml_import_011(self):
        # Intermediary
        invoice = self.invoice_from_xml("test_02_011", "IT05979361218_011.xml")
        self.assertEqual(invoice.intermediary.vat, "IT02886610241")

    def test_04_xml_import_11005(self):
        invoice = self.invoice_from_xml("test_04_11005", "IT02780790107_11005.xml")
        self.assertEqual(invoice.reference, "124")
        self.assertEqual(invoice.partner_id.name, "SOCIETA' ALPHA SRL")
        self.assertEqual(
            invoice.invoice_line_ids[0].invoice_line_tax_ids[0].name, "22% e-bill"
        )
        self.assertEqual(
            invoice.invoice_line_ids[1].invoice_line_tax_ids[0].name, "22% e-bill"
        )
        self.assertEqual(
            invoice.invoice_line_ids[0].invoice_line_tax_ids[0].amount, 22.0)
        self.assertEqual(
            invoice.invoice_line_ids[1].invoice_line_tax_ids[0].amount, 22.0)
        self.assertEqual(invoice.invoice_line_ids[1].price_unit, 2.0)
        self.assertTrue(len(invoice.e_invoice_line_ids) == 2)
        for e_line in invoice.e_invoice_line_ids:
            self.assertTrue(e_line.line_number in (1, 2))
            if e_line.line_number == 1:
                self.assertEqual(e_line.cod_article_ids[0].name, "EAN")
                self.assertEqual(e_line.cod_article_ids[0].code_val, "12345")
        # TODD> CHeck for language
        # self.assertEqual(
        #     invoice.inconsistencies,
        #     "Company Name field contains 'Societa' Alpha SRL'. "
        #     "Your System contains 'SOCIETA' ALPHA SRL'\n\n",
        # )

    def test_00002_xml_import(self):
        # Invoice with WH tax
        res = self.run_wizard("🎺 test002", "IT10242670015_00002.xml")
        invoice_id = res.get("domain")[0][2][0]
        invoice = self.invoice_model.browse(invoice_id)
        self.assertEqual(invoice.partner_id.register_code, "SS1234")
        self.assertEqual(invoice.partner_id.register_fiscalpos.code, "RF02")
        self.assertEqual(invoice.reference, "FT/2022/0006")
        self.assertEqual(invoice.amount_total, 57.00)
        self.assertEqual(invoice.gross_weight, 0.00)
        self.assertEqual(invoice.net_weight, 0.00)
        # TODO> Must add welfare fund
        # self.assertEqual(invoice.welfare_fund_ids[0].kind_id.code, "N4")
        self.assertFalse(invoice.art73)
        # welfare_found = False
        for line in invoice.invoice_line_ids:
            if line.product_id.id == self.service.id:
                self.assertEqual(line.price_unit, 3)
                # welfare_found = True
        # TODO> Must add welfare fund
        # self.assertTrue(welfare_found)
        self.assertTrue(len(invoice.e_invoice_line_ids) == 1)
        self.assertEqual(
            invoice.e_invoice_line_ids[0].name, "Prodotto di test al giorno"
        )
        self.assertEqual(invoice.e_invoice_line_ids[0].qty, 15.0)
        self.assertEqual(invoice.e_invoice_line_ids[0].uom, "Giorno(i)")
        self.assertEqual(invoice.e_invoice_line_ids[0].unit_price, 3.6)
        self.assertEqual(invoice.e_invoice_line_ids[0].total_price, 54.0)
        self.assertEqual(invoice.e_invoice_line_ids[0].tax_amount, 0.0)
        self.assertEqual(invoice.e_invoice_line_ids[0].tax_kind, "N2.2")
        self.assertTrue(len(invoice.e_invoice_line_ids[0].other_data_ids) == 2)
        self.assertEqual(
            invoice.e_invoice_line_ids[0].other_data_ids[0].text_ref, "Riferimento"
        )

    def test_00003_xml_import(self):
        # Invoice from RSM
        res = self.run_wizard("🎺 test003", "SM00000004298_00003.xml")
        invoice_id = res.get("domain")[0][2][0]
        invoice = self.invoice_model.browse(invoice_id)
        for line in invoice.invoice_line_ids:
            self.assertEqual(line.invoice_line_tax_ids[0].kind_id.code, "N6.9")

    def test_00004_xml_import(self):
        # Invoice with WH tax
        self.run_wizard("🎺 test004", "ITNREGCM80H30D612D_00004.xml")

    def test_00014_xml_import(self):
        # Invoice with wrong e-mail
        self.run_wizard("🎺 test014", "IT00488410010_00014.xml")

    def test_00015_xml_import(self):
        # Invoice with wrong e-mail
        self.run_wizard("🎺 test015", "IT01641790702_00015.xml")
