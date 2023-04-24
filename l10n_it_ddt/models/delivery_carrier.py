# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
from odoo import fields, models, api


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"

    partner_carrier_id = fields.Many2one(
        "res.partner",
        string="Carrier",
        oldname="ddt_carrier_id",
    )
    carriage_condition_id = fields.Many2one(
        "stock.picking.carriage_condition", string="Carriage Condition"
    )
    goods_description_id = fields.Many2one(
        "stock.picking.goods_description", string="Description of Goods"
    )
    transportation_reason_id = fields.Many2one(
        "stock.picking.transportation_reason", string="Reason for Transportation"
    )
    transportation_method_id = fields.Many2one(
        "stock.picking.transportation_method", string="Method of Transportation"
    )
    note = fields.Text(string="Note")

    @api.multi
    def get_invoice_price_available(self, invoice):
        self.ensure_one()
        if invoice.company_id.delivery_price_policy == "delivery":
            total = weight = volume = quantity = 0
            total_delivery = 0.0
            for line in invoice.invoice_line_ids:
                if line.is_delivery:
                    total_delivery += line.price_total
                if not line.product_id or line.is_delivery:
                    continue
                qty = line.uom_id._compute_quantity(
                    line.quantity, line.product_id.uom_id
                )
                weight += (line.product_id.weight or 0.0) * qty
                volume += (line.product_id.volume or 0.0) * qty
                quantity += qty
            total = (invoice.amount_total or 0.0) - total_delivery

            total = invoice.currency_id.with_context(date=invoice.date_invoice).compute(
                total, invoice.company_id.currency_id
            )

        return self.get_price_from_picking(total, weight, volume, quantity)
