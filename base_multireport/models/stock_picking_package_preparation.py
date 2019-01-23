# -*- coding: utf-8 -*-


from base64 import b64decode
from StringIO import StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader
from odoo import models, fields, api


class StockPickingPackagePreparation(models.Model):
    _inherit = ["stock.picking.package.preparation"]

    report_doc_ids = fields.Many2many(
        'ir.attachment',
        'stock_picking_package_preparation_rel',
        'picking_id',
        'ir_attachment_id',
        string="Documents to be appended to DdT (PDF only):",
        copy=False)

    @api.multi
    def get_docs_to_attach(self):
        """Returns a merged PDF document from a list of all attached PDFs."""
        self.ensure_one()
        new_pdf = PdfFileWriter()
        for pdf_doc in self.report_doc_ids.filtered(
                lambda d: d.mimetype == 'application/pdf').sorted(
                    key='attach_seq'):
            pdf = PdfFileReader(
                StringIO(b64decode(pdf_doc.datas)))
            for page in pdf.pages:
                new_pdf.addPage(page)
        pdf_content = StringIO()
        new_pdf.write(pdf_content)
        return pdf_content.getvalue()

    def get_header_mode(self):
        return self.company_id.report_model_style.header_stock_picking_package_preparation


class StockPickingPackagePreparationLine(models.Model):
    _inherit = 'stock.picking.package.preparation.line'

    def description_2_print(self):
        field_name = 'name'
        style = self.package_preparation_id.company_id.report_model_style.\
            description_mode_stock_picking_package_preparation
        value = self[field_name]
        if style in ('line1', 'nocode1'):
            value = value.split('\n')[0]
        if style in ('nocode', 'nocode1'):
            i = value.find(']')
            if value[0] == '[' and i >= 0:
                value = value[i + 1:].lstrip()
        return value

    def code_2_print(self):
        field_name = 'name'
        style = self.package_preparation_id.company_id.report_model_style.\
            description_mode_stock_picking_package_preparation
        value = self[field_name]
        if style in ('nocode', 'nocode1'):
            i = value.find(']')
            if value[0] == '[' and i >= 0:
                value = value[1:i]
        return value
