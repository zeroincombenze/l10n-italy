# -*- coding: utf-8 -*-

from odoo import fields, models, api


# class PurchaseOrder(models.Model):
#     _inherit = 'purchase.order'


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.depends('product_id')
    def _set_code(self):
        for line in self:
            if line.product_id:
                line.code = line.product_id.default_code
            else:
                line.code = False

    @api.depends('product_id', 'name')
    def _set_description(self):
        for line in self:
            line.description = line.description_2_print()

    code = fields.Char('Code',
                       compute='_set_code',
                       copy=False)
    description = fields.Char('Description',
                       compute='_set_description',
                       copy=False)
