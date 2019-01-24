# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Copyright 2014    - Davide Corio
# Copyright 2015-16 - Lorenzo Battistini - Agile Business Group
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class AccountInvoice(orm.Model):
    _inherit = "account.invoice"

    _columns = {
        'fatturapa_attachment_out_id': fields.many2one(
            'fatturapa.attachment.out', 'FatturaPA Export File',
            readonly=True),
        'has_pdf_invoice_print': fields.boolean(
            related='fatturapa_attachment_out_id.has_pdf_invoice_print',
            readonly=True),
    }
