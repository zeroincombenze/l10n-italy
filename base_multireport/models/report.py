
from base64 import b64decode
from logging import getLogger
from StringIO import StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.utils import PdfReadError
from PIL import Image
from odoo import api, models, _
LOGGER = getLogger(__name__)


class Report(models.Model):
    _inherit = 'report'

    @api.model
    def get_pdf(self, docids, report_name, html=None, data=None):
        return super(
            Report,
            self).get_pdf(
                docids,
                report_name,
                html=html,
                data=data)
