# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ddt_invoice_exclude = fields.Boolean(
        string="Exclude from DDT invoicing",
        default=True,
        help="If flagged this service will not be automatically " "invoiced from DDT.",
    )
    is_delivery = fields.Boolean(string="Is a Delivery", default=False)

    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        for template in self:
            if not template.is_delivery and self.env['delivery.carrier'].search(
                [('product_id', 'in', template.product_variant_ids.ids)]
            ):
                template.is_delivery = True
        return res

    @api.model
    def create(self, vals):
        template = super(ProductTemplate, self).create(vals)
        if self.env['delivery.carrier'].search(
            [('product_id', 'in', template.product_variant_ids.ids)]
        ):
            if not template.is_delivery and self.env['delivery.carrier'].search(
                [('product_id', 'in', template.product_variant_ids.ids)]
            ):
                template.is_delivery = True
        return template


class ProductProduct(models.Model):
    _inherit = "product.product"

    ddt_invoice_exclude = fields.Boolean(
        related="product_tmpl_id.ddt_invoice_exclude",
        string="Exclude from DDT invoicing",
        help="If flagged this service will not be automatically " "invoiced from DDT.",
    )
    is_delivery = fields.Boolean(
        related="product_tmpl_id.is_delivery", string="Is a Delivery"
    )
