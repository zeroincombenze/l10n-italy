# -*- coding: utf-8 -*-
# Copyright 2014    - Davide Corio
# Copyright 2015-16 - Lorenzo Battistini - Agile Business Group
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class FatturaPAAttachment(orm.Model):
    _name = "fatturapa.attachment.out"
    _description = "E-invoice Export File"
    _inherits = {'ir.attachment': 'ir_attachment_id'}
    _inherit = ['mail.thread']

    _columns = {
        'ir_attachment_id': fields.many2one(
            'ir.attachment', 'Attachment', required=True, ondelete="cascade"),
        'out_invoice_ids': fields.one2many(
            'account.invoice', 'fatturapa_attachment_out_id',
            string="Out Invoices", readonly=True),
        'has_pdf_invoice_print': fields.boolean(
            help="True if all the invoices have a printed "
                 "report attached in the XML, False otherwise.",
            compute='_compute_has_pdf_invoice_print', store=True),
        'invoice_partner_id': fields.many2one(
            'res.partner', string='Customer', store=True,
            compute='_compute_invoice_partner_id'),
    }


class FatturaAttachments(orm.Model):
    _inherit = "fatturapa.attachments"

    _columns = {
        'is_pdf_invoice_print': fields.boolean(
            help="This attachment contains the PDF report of the linked invoice"),
    }
