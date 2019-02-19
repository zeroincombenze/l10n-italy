# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm, osv


class ResCompany(orm.Model):
    _inherit = 'res.company'


    _columns = {
        'sconto_maggiorazione_product_id': fields.many2one(
            'product.product', 'Discount Supplement Product',
            help="Product used to model ScontoMaggiorazione XML element on bills."),
    }

class AccountConfigSettings(osv.TransientModel):
    _inherit = 'account.config.settings'
    _columns = {
            'sconto_maggiorazione_product_id': fields.many2one(
                related='company_id.sconto_maggiorazione_product_id',
                string="Discount Supplement Product",
                help="Product used to model ScontoMaggiorazione XML element on bills."
            ),
    }

    def onchange_company_id(self, cr, uid, ids, company_id, context=None):
        res = super(AccountConfigSettings, self).onchange_company_id(cr, uid, ids, company_id, context)
        company_id = self.pool.get('res.company').browse(cr, uid, company_id)
        if company_id:
            res['value']['sconto_maggiorazione_product_id'] = (
                company_id.sconto_maggiorazione_product_id and
                company_id.sconto_maggiorazione_product_id.id or False
                )
        else:
            res['value']['sconto_maggiorazione_product_id'] = False
        return res
