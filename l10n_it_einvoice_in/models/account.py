# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import decimal_precision as dp
from openerp.osv import fields, orm


class AccountInvoice(orm.Model):
    _inherit = "account.invoice"


    _columns = {
        'fatturapa_attachment_in_id': fields.many2one(
                'fatturapa.attachment.in', 'E-bill Import File',
                ondelete='restrict'),
        'inconsistencies': fields.text('Import Inconsistencies'),
        'e_invoice_line_ids': fields.one2many(
                "einvoice.line", "invoice_id", string="Lines Detail",
                readonly=True),
    }

    def name_get(self, cr, uid, ids, context={}):
        result = super(AccountInvoice, self).name_get(cr, uid, ids, context)
        res = []
        for tup in result:
            invoice = self.browse(cr, uid, tup[0])
            if invoice.type in ('in_invoice', 'in_refund'):
                name = "%s, %s" % (tup[1], invoice.partner_id.name)
                if invoice.origin:
                    name += ', %s' % invoice.origin
                res.append((invoice.id, name))
            else:
                res.append(tup)
            return res

    def remove_attachment_link(self, cr, uid, ids, context={}):
        self.write(cr, uid, ids, {'fatturapa_attachment_in_id': False}, context)
        return {'type': 'ir.actions.client', 'tag': 'reload'}


class fatturapa_article_code(orm.Model):
    # _position = ['2.2.1.3']
    _name = "fatturapa.article.code"
    _description = 'E-bill Article Code'

    _columns = {
        'name': fields.char('Cod Type', size=35),
        'code_val': fields.char('Code Value', size=35),
        'invoice_line_id': fields.many2one(
            'account.invoice.line', 'Related Invoice line',
            ondelete='cascade', select=True
        )
    }


class AccountInvoiceLine(orm.Model):
    # _position = [
    #     '2.2.1.3', '2.2.1.6', '2.2.1.7',
    #     '2.2.1.8', '2.1.1.10'
    # ]
    _inherit = "account.invoice.line"

    _columns = {
        'fatturapa_attachment_in_id': fields.many2one(
             'fatturapa.attachment.in', 'E-bill Import File',
             readonly=True,
             related='invoice_id.fatturapa_attachment_in_id'),
    }


class DiscountRisePrice(orm.Model):
    _inherit = "discount.rise.price"
    _columns = {
        'e_invoice_line_id': fields.many2one(
            'einvoice.line',
            'Related E-bill Line', readonly=True)
    }


class EInvoiceLine(orm.Model):
    _name = 'einvoice.line'
    _columns = {
        'invoice_id': fields.many2one(
            "account.invoice", "Bill", readonly=True),
        'line_number': fields.integer('Line Number', readonly=True),
        'service_type': fields.char('Sale Provision Type', readonly=True),
        'cod_article_ids': fields.one2many(
            'fatturapa.article.code', 'e_invoice_line_id',
            'Articles Code', readonly=True),
        'name': fields.char("Description", readonly=True),
        'qty': fields.float(
            'Quantity', readonly=True,
            digits_compute=dp.get_precision('Product Unit of Measure'),),
        'uom': fields.char("Unit of measure", readonly=True),
        'period_start_date': fields.date("Period Start Date", readonly=True),
        'period_end_date': fields.date("Period End Date", readonly=True),
        'price_unit': fields.float(
            'Unit Price', readonly=True,
            digits_compute=dp.get_precision('Product Price')),
        'discount_rise_price_ids': fields.one2many(
            'discount.rise.price', 'e_invoice_line_id',
            'Discount and Supplement Details', readonly=True),
        'total_price': fields.float("Total Price", readonly=True),
        'tax_amount': fields.float("VAT Rate", readonly=True),
        'wt_amount': fields.char("Tax Withholding", readonly=True),
        'tax_nature': fields.char("Nature", readonly=True),
        'admin_ref': fields.char("Administration Reference", readonly=True),
        'other_data_ids': fields.one2many(
            "einvoice.line.other.data", "e_invoice_line_id",
            string="Other Administrative Data", readonly=True),
    }


class EInvoiceLineOtherData(orm.Model):
    _name = 'einvoice.line.other.data'
    _columns = {
        'e_invoice_line_id': fields.many2one(
                'einvoice.line', 'Related E-bill Line', readonly=True
        ),
        'name': fields.char("Data Type", readonly=True),
        'text_ref': fields.char("Text Reference", readonly=True),
        'num_ref': fields.float("Number Reference", readonly=True),
        'date_ref': fields.char("Date Reference", readonly=True),
    }
