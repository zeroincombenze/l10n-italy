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
from os0 import os0


logger = getLogger(__name__)


class Report(models.Model):
    _inherit = "report"

    RPT_BY_MODEL = {
        'sale.order': 'sale.report_saleorder',
        'account.invoice': 'account.report_invoice',
    }
    BOOL_PARAMS = ['no_header_logo',]

    @api.model
    def select_reportname(self, document):
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
    def get_doc_n_repo_params(self, document, report):
        reportname = self.select_reportname(document)
        company = False
        report_model_style = False
        if hasattr(document, 'company_id'):
            company = document.company_id or self.env.user.company_id
            report_model_style = company.report_model_style or None
        if hasattr(document, 'pdf_report'):
            pdf_report = getattr(document, 'pdf_report')
        else:
            pdf_report = False
        return reportname, company, report_model_style, pdf_report

    @api.model
    def get_report_attrib(self, param, doc, report):
        reportname, company, report_model_style, pdf_report = self.env[
            'report'].get_doc_n_repo_params(doc, report)
        model = report.model.replace('.', '_')
        value = False
        if report_model_style.origin != 'odoo':
            param_in_style = '%s_%s' % (param, model)
            template = False
            if hasattr(report, 'template'):
                template = getattr(report, 'template')
            if hasattr(report, param):
                value = getattr(report, param)
            if not value and template and hasattr(template, param):
                value = getattr(template, param)
            if not value and hasattr(report_model_style, param_in_style):
                value = getattr(report_model_style, param_in_style)
        if not value and hasattr(report_model_style, 'model_%s_id' % model):
            model_default = getattr(report, 'model_%s_id' % model)
            if hasattr(model_default, param):
                value = getattr(model_default, param)
        if not value and hasattr(report_model_style, param):
            value = getattr(report_model_style, param)
        if param == 'footer_mode' and (not value or value == 'standard'):
            if company.custom_footer:
                value = 'custom'
        if param in self.BOOL_PARAMS:
            value = os0.str2bool(value, True)
        return value or None

    @api.model
    def get_html(self, docids, report_name, data=None):
        """This method generates and returns html version of a report.
        """
        report_model_name = 'report.%s' % report_name
        report_model = self.env.get(report_model_name)
        if report_model is not None:
            return super(Report, self).get_html(
                docids, report_name, data=data)
        else:
            report = self._get_report_from_name(report_name)
            if report.model not in self.RPT_BY_MODEL:
                return super(Report, self).get_html(
                    docids, report_name, data=data)
            docs = self.env[report.model].browse(docids)
            company = docs[0].company_id or self.env.user.company_id
            docargs = {
                'doc_ids': docids,
                'doc_model': report.model,
                'docs': docs,
                'doc_opts': report,
                'doc_style': company.report_model_style,
                'def_company': self.env.user.company_id,
                'report': self,
                }
            return self.render(report.report_name, docargs)

    @api.model
    def get_pdf(self, docids, report_name, html=None, data=None):
        result = super(Report, self).get_pdf(
            docids, report_name, html=html, data=data)
        if not docids:
            return result
        report = self._get_report_from_name(report_name)
        if report.model not in self.RPT_BY_MODEL:
            return result
        recs = self.env[report.model].browse(docids)
        reportname, company, report_model_style, pdf_report = self.env[
            'report'].get_doc_n_repo_params(recs[0], report)
        if (not report_model_style or not report_model_style.origin or
                report_model_style.origin == 'odoo') and not pdf_report:
            return result
        watermark = self.get_report_attrib('pdf_watermark', recs[0], report)
        if not watermark:
            watermark = tools.safe_eval(
                 self.get_report_attrib('pdf_watermark_expression',
                                        recs[0], report) or 'None',
                dict(env=self.env, docs=recs)
            )
        if watermark:
            watermark = b64decode(watermark)
        ending_page = watermark = self.get_report_attrib('ending_page',
                                                         recs[0], report)
        report_model_style.pdf_ending_page or None
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

    def get_header_mode(self):
        model = document.__class__.__name__
        hdr_mode = 'header_%s' % model
        return self.company_id.report_model_style[hdr_mode] 
