# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from base64 import b64decode
from logging import getLogger
from pyPdf import PdfFileWriter, PdfFileReader
from pyPdf.utils import PdfReadError
from PIL import Image
from StringIO import StringIO
from odoo import api, models, tools
from PIL import PdfImagePlugin # flake8: noqa

logger = getLogger(__name__)


class Report(models.Model):
    _inherit = 'report'



class Report(models.Model):
    _inherit = "report"

    RPT_BY_MODEL = {
        'sale.order': 'sale.report_saleorder',
        'account.invoice': 'account.report_invoice',
    }

    @api.model
    def get_reportname(self, document):
        model = document.__class__.__name__
        rule_model = self.env['multireport.selection.rules']
        ir_model_model = self.env['ir.model']
        ir_ui_view_model = self.env['ir.ui.view']
        model_id = ir_model_model.search([('model', '=', model)])
        if model_id:
            where = [('active', '=', True), ('model_id', '=', model_id.id)]
        else:
            where = [('active', '=', True)]
        reportname = self.RPT_BY_MODEL.get(model, None)
        for rule in rule_model.search(where, order='sequence'):
            if rule.action == 'odoo':
                break
            elif rule.action == 'report' and rule.report_id:
                reportname = ir_ui_view_model.browse(rule.report_id.id).xml_id
                break
        return reportname

    @api.model
    def get_report_attr(self, document):
        reportname = self.get_reportname(document)
        company = document.company_id or self.env.user.company_id
        report_model_style = company.report_model_style or None
        if hasattr(document, 'pdf_report'):
            pdf_report = getattr(document, 'pdf_report')
        else:
            pdf_report = False
        return reportname, company, report_model_style, pdf_report

    # @api.noguess
    # def get_action(self, docids, report_name, data=None):
    #     import pdb
    #     pdb.set_trace()
    #     return super(Report, self).get_action(docids, report_name, data=data)

    @api.model
    def get_pdf(self, docids, report_name, html=None, data=None):
        result = super(Report, self).get_pdf(
            docids, report_name, html=html, data=data)
        report = self._get_report_from_name(report_name)
        recs = self.env[report.model].browse(docids)
        reportname, company, report_model_style, pdf_report = self.env[
            'report'].get_report_attr(recs[0])
        company = recs[0].company_id
        report_model_style = company.report_model_style or None
        if hasattr(recs, 'pdf_report'):
            pdf_report = getattr(recs, 'pdf_report')
        else:
            pdf_report = False
        if (not report_model_style or not report_model_style.origin or
                report_model_style.origin == 'odoo') and not pdf_report:
            return result
        model = recs[0].__class__.__name__
        specific_watermark = 'pdf_watermark_%s' % model.replace('.', '_')
        watermark = None
        if hasattr(report_model_style, specific_watermark):
            watermark = getattr(report_model_style, specific_watermark)
        if not watermark:
            watermark = report_model_style.pdf_watermark or None
        if not watermark:
            watermark = tools.safe_eval(
                report_model_style.pdf_watermark_expression or 'None',
                dict(env=self.env, docs=recs)
            )
        if watermark:
            watermark = b64decode(watermark)
        ending_page = report_model_style.pdf_ending_page or None
        if ending_page:
            ending_page = b64decode(ending_page)
        if not watermark and not ending_page:
            return result

        pdf = PdfFileWriter()
        pdf_watermark = None
        try:
            pdf_watermark = PdfFileReader(StringIO(watermark))
        except PdfReadError:
            # let's see if we can convert this with pillow
            try:
                Image.init()
                image = Image.open(StringIO(watermark))
                pdf_buffer = StringIO()
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                resolution = image.info.get(
                    'dpi', report.paperformat_id.dpi or 90
                )
                if isinstance(resolution, tuple):
                    resolution = resolution[0]
                image.save(pdf_buffer, 'pdf', resolution=resolution)
                pdf_watermark = PdfFileReader(pdf_buffer)
            except:
                logger.exception('Failed to load watermark')

        if not pdf_watermark:
            logger.error(
                'No usable watermark found, got %s...', watermark[:100]
            )
            return result

        if pdf_watermark.numPages < 1:
            logger.error('Your watermark pdf does not contain any pages')
            return result
        if pdf_watermark.numPages > 1:
            logger.debug('Your watermark pdf contains more than one page, '
                         'all but the first one will be ignored')

        for page in PdfFileReader(StringIO(result)).pages:
            watermark_page = pdf.addBlankPage(
                page.mediaBox.getWidth(), page.mediaBox.getHeight()
            )
            watermark_page.mergePage(pdf_watermark.getPage(0))
            watermark_page.mergePage(page)

        pdf_content = StringIO()
        pdf.write(pdf_content)

        return pdf_content.getvalue()
