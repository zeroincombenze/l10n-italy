# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from xml.sax.saxutils import escape
import logging

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

try:
    from unidecode import unidecode
except ImportError as err:
    _logger.debug(err)


XML_ESCAPE = {
    u'\'': u' ',
    u'\n': u' ',
    u'\r': u' ',
    u'\t': u' ',
    u'€': u'EUR',
    u'©': u'(C)',
    u'®': u'(R)',
    u'«': u'&laquo;',
    u'»': u'&raquo;',
    u'Ø': u'&Oslash;',
    u'ø': u'&oslash;',
    u'ß': u'ss',
}

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def wep_text(self, text):
        """"Do xml escape to avoid error StringLatinType"""
        if text:
            return escape(unidecode(text), XML_ESCAPE).strip()
        return text
