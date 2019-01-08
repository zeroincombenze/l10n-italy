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
