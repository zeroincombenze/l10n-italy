# -*- coding: utf-8 -*-
from odoo import api, models, fields
# from odoo.exceptions import UserError
# from odoo.tools.float_utils import float_compare, float_is_zero


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def generate_ddt_espresso(self):
        import pdb; pdb.set_trace()
        ddt_model = self.env["stock.picking.package.preparation"]
        orders = []
        ddts = {}
        for order in self:
            if (
                orders.state != "sale" or
                not order.order_line.filtered(
                    lambda x: (
                        x.product_id.product_espresso and
                        x.product_id.type != "service"
                    )
                )
            ):
                # Sale Order without espresso products
                continue
            for picking in order.picking_ids:
                if not picking.move_line.filtered(
                    lambda x: (
                        x.product_id.product_espresso and
                        x.product_id.type != "service"
                    )
                ):
                    # Picking without espresso products
                    continue
                nro_lines = 0
                if picking.state in ("draft",
                                     "waiting",
                                     "partially_available",
                                     "confirmed"):
                    picking.action_assign()
                if (
                    picking.state == "assigned"
                    and len(picking.mapped("ddt_ids")) == 0
                ):
                    for pack in picking.pack_operation_ids:
                        if pack.product_id.product_espresso and pack.product_qty > 0:
                            pack.write({'qty_done': pack.product_qty})
                            nro_lines += 1
                        else:
                            pack.unlink()
                if nro_lines:
                    hash_key = '%s|%d|%d|%d|%d' % (
                        order.name,
                        order.id,
                        order.partner_id.id,
                        order.partner_shipping_id.id,
                        order.payment_term_id.id)
                    if hash_key not in ddts:
                        ddts[hash_key] = []
                    ddts[hash_key].append(picking)
                    if picking.sale_id not in orders:
                        orders.append(picking.sale_id)
        for hash_key in ddts.keys():
            items = hash_key.split("|")
            order = self.browse(items[1])
            ddt = ddt_model.create(
                ddt_model.preparare_ddt_data(
                    ddts[hash_key],
                    order=order,
                )
            )
        return ddt


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_espresso = fields.Boolean(
        string="Prodotto espresso",
        related="product_id.espresso",
    )
