# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class IrActionsReportXml(models.Model):
    _inherit = 'ir.actions.report.xml'

    pdf_watermark = fields.Binary('Watermark')
    pdf_watermark_expression = fields.Char(
        'Watermark expression',
        help='An expression yielding the base64 '
             'encoded data to be used as watermark. \n'
             'You have access to variables `env` and `docs`')
    pdf_ending_page = fields.Binary(
        'Ending Page PDF',
        help='If you want the last page of every document printed '
             'to contain some specific content such as Advertisement, '
             'your business terms and Conditions, '
             'upload a PDF with those content here and '
             'it will be appended to every document you print.')
