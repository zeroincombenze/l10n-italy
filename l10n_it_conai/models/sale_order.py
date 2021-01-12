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


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    conai_exemption_id = fields.Many2one(
        'italy.conai.partner.category', string='CONAI Exemption')
    amount_goods_service = fields.Monetary(
        string='Goods & Service Amount',
        currency_field='company_id',
        store=True, readonly=True)
    amount_conai = fields.Monetary(string='CONAI Amount',
                                   currency_field='company_id',
                                   store=True, readonly=True)

    @api.multi
    def action_confirm(self):

        def _calc_conai_value(conai_category, weight):
            conai_amount = conai_category.evaluate_conai_amount(weight)
            conai_struct[conai_category]['amount'] = conai_amount
            conai_struct[conai_category]['weight'] += weight
            return conai_amount

        def _process_category(conai_category):
            if not conai_category:
                return
            weight_conv, uom = conai_category.evaluate_weight_conv()
            category2 = weight2 = False
            if conai_category not in conai_struct:
                conai = {}
                conai['name'] = conai_category.name
                conai['weight'] = 0.0
                conai['um'] = uom
                conai['price'] = conai_category.get_price()
                conai['amount'] = 0.0
                conai['tax'] = line.tax_id
                conai_struct[conai_category] = conai
            if line.product_id:
                weight2 = ((line.product_id.weight2 or
                            line.product_id.product_tmpl_id.weight2) *
                           line.product_uom_qty)
                category2 = (line.product_id.conai_category2_id or
                             line.product_id.product_tmpl_id.conai_category2_id)
            if weight2 and category2:
                if conai_category == category2:
                    _calc_conai_value(conai_category, weight2)
                else:
                    _calc_conai_value(conai_category, line.weight - weight2)
            else:
                conai_amount = _calc_conai_value(conai_category, line.weight)
                line.write({'conai_amount': conai_amount,
                            'weight': line.weight})

        order_line_model = self.env['sale.order.line']
        for order in self:
            conai_product = order.company_id.conai_product_id
            conai_struct = {}
            if (order.conai_exemption_id and
                    order.conai_exemption_id.conai_percent):
                percent = order.conai_exemption_id.conai_percent
                p_name = order.conai_exemption_id.name
                ii = p_name.lower().find('vs')
                if ii >= 0:
                    p_name = p_name[ii:]
                p_name = 'Esenzione %s%% %s' % (percent, p_name)
            else:
                percent = 0.0
                p_name = ''
            supplemental_line_ids = []
            for line in order.order_line:
                if line.name.startswith('Contributo ambientale'):
                    supplemental_line_ids.append(line.id)
                    continue
                if not line.conai_category_id:
                    continue
                if not line.weight and line.product_id:
                    line.weight = (
                            (line.product_id.weight or
                             line.product_id.product_tmpl_id.weight) *
                            line.product_uom_qty)
                _process_category(line.conai_category_id)
                if line.product_id:
                    _process_category(
                        line.product_id.conai_category2_id or
                        line.product_id.product_tmpl_id.conai_category2_id)

            if conai_product:
                for nr, conai_category in enumerate(conai_struct):
                    if p_name:
                        conai_name = 'Contributo ambientale %s (%s %s)\n%s' % (
                            conai_struct[conai_category]['name'],
                            conai_struct[conai_category]['weight'],
                            conai_struct[conai_category]['um'].name,
                            p_name)
                    else:
                        conai_name = 'Contributo ambientale %s (%s %s)' % (
                            conai_struct[conai_category]['name'],
                            conai_struct[conai_category]['weight'],
                            conai_struct[conai_category]['um'].name)
                    line_vals = {
                        'product_id': conai_product.id,
                        'name': conai_name,
                        'order_id': order.id,
                        'product_uom': conai_struct[conai_category]['um'].id,
                        'product_uom_qty': conai_category.get_qty(
                            conai_struct[conai_category]['weight'],
                            percent=percent),
                        'price_unit': conai_struct[conai_category]['price'],
                        'tax_id': [
                            (6, 0,
                             [x.id for x in
                              conai_struct[conai_category]['tax']])],
                        'sequence': 99999,
                    }
                    if nr < len(supplemental_line_ids):
                        order_line_model.browse(
                            supplemental_line_ids[nr]).write(line_vals)
                    else:
                        inv_line = order_line_model.create(line_vals)
                nr = len(conai_struct)
                while nr < len(supplemental_line_ids):
                    order_line_model.browse(
                        supplemental_line_ids[nr]).unlink()
                    nr += 1
                if len(conai_struct):
                    order._amount_all()
        return super(SaleOrder, self).action_confirm()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    date_order = fields.Datetime(
        string='Date',
        related='order_id.date_order', store=True, readonly=True)
    conai_category_id = fields.Many2one(
        'italy.conai.product.category', string='CONAI Category')
    conai_amount = fields.Float(
        string='CONAI Amount',
        digits=dp.get_precision('Product Price'))
    conai_exemption_id = fields.Many2one(
        string='CONAI Exemption',
        related='order_id.conai_exemption_id', store=True, readonly=True)

    @api.multi
    @api.onchange('product_id')
    def _set_conai_category(self):
        if self.product_id:
            if self.product_id.conai_category_id:
                self.conai_category_id = self.product_id.conai_category_id.id
            elif self.product_id.product_tmpl_id.conai_category_id:
                self.conai_category_id = \
                    self.product_id.product_tmpl_id.conai_category_id.id
            self.evaluate_conai_amount()

    @api.multi
    @api.onchange('product_uom_qty', 'conai_category_id')
    def _set_conai_amount(self):
        self.evaluate_conai_amount()

    @api.model
    def evaluate_conai_amount(self):
        if not self.weight and self.product_id and self.product_uom_qty:
            self.weight = (
                    (self.product_id.weight or
                     self.product_id.product_tmpl_id.weight) *
                    self.product_uom_qty)
        if self.weight and self.conai_category_id:
            self.conai_amount = self.conai_category_id.evaluate_conai_amount(
                self.weight)

    @api.model
    def create(self, vals):
        if 'conai_category_id' not in vals and 'product_id' in vals:
            weight = vals.get('weight', 0.0)
            conai_category_id = False
            product = self.env['product.product'].browse(vals['product_id'])
            if product.conai_category_id:
                conai_category_id = product.conai_category_id.id
                if not weight:
                    weight = product.weight
            else:
                if (product.product_tmpl_id and
                        product.product_tmpl_id.conai_category_id):
                    conai_category_id = \
                        product.product_tmpl_id.conai_category_id.id
                    if not weight:
                        weight = product.weight
            if conai_category_id:
                vals['conai_category_id'] = conai_category_id
            if weight:
                vals['weight'] = weight
        return super(SaleOrderLine, self).create(vals)
