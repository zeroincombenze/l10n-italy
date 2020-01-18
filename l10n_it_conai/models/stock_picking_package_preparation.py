# -*- coding: utf-8 -*-
#
# Copyright 2019-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import fields, models, api
import odoo.addons.decimal_precision as dp


class StockPickingPackagePreparation(models.Model):
    _inherit = 'stock.picking.package.preparation'

    conai_category_id = fields.Many2one(
        'italy.conai.partner.category', string='CONAI Category')


class StockPickingPackagePreparationLine(models.Model):
    _inherit = 'stock.picking.package.preparation.line'

    conai_category_id = fields.Many2one(
        'italy.conai.product.category', string='CONAI Category')
    conai_amount = fields.Float(
        string='CONAI Amount',
        digits=dp.get_precision('Product Price'))

    @api.multi
    def _prepare_invoice_line(self, qty, invoice_id=None):
        self.ensure_one()
        res = super(StockPickingPackagePreparationLine,
                    self)._prepare_invoice_line(qty, invoice_id)
        res['conai_amount'] = 0.0
        if self.package_preparation_id.conai_category_id:
            percent = self.package_preparation_id.conai_category_id.conai_percent
        elif self.package_preparation_id.partner_id.conai_category_id:
            percent = self.package_preparation_id.partner_id.conai_category_id.conai_percent
        else:
            percent = 100.0
        category_id = False
        if self.conai_category_id:
            category_id = self.conai_category_id
            price_unit = category_id.conai_price_unit
        elif self.product_id:
            price_unit = 0.0
            if self.product_id.conai_category_id:
                category_id = self.product_id.conai_category_id
            elif self.product_id.product_tmpl_id:
                category_id = self.product_id.product_tmpl_id.conai_category_id
            if category_id:
                price_unit = category_id.conai_price_unit
                res['conai_category_id'] = category_id.id
        weight_conv = 1000
        res['conai_amount'] = self.weight * price_unit * percent / weight_conv
        return res
