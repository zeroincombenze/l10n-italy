# -*- coding: utf-8 -*-
from odoo import api, models, fields
# from odoo.exceptions import UserError
# from odoo.tools.float_utils import float_compare, float_is_zero


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def generate_ddt_espresso(self, shipping=None):

        def exec_wizard(action):
            res_model = action['res_model']
            ctx = action['context'] or {}
            wiz = self.env[res_model].browse(action['res_id']).with_context(ctx)
            fct = 'process'
            if hasattr(wiz, fct):
                return getattr(wiz, fct)()
            return False

        ddt_model = self.env["stock.picking.package.preparation"]
        orders = []
        ddts = {}
        # shippings = {}
        for order in self:
            if (
                order.state != "sale" or
                not order.order_line.filtered(
                    lambda ln: ln.line_with_product_espresso(shipping=shipping)
                )
            ):
                # Sale Order without espresso products
                continue
            if order.carrier_id:
                ship_prod = order.carrier_id.product_id
            else:
                ship_prod = shipping
            hash_key = '%d|%d|%d' % (
                order.partner_id.id,
                order.partner_shipping_id.id,
                order.payment_term_id.id)
            for picking in order.picking_ids:
                if len(picking.ddt_ids) or not picking.move_lines.filtered(
                    lambda ln: ln.line_with_product_espresso(shipping=ship_prod)
                ):
                    # Picking without espresso products
                    continue
                nro_lines = 0
                if picking.state in ("draft",
                                     "waiting",
                                     "partially_available",
                                     "confirmed"):
                    picking.action_assign()
                if picking.state != "assigned":
                    picking.force_assign()
                if picking.state == "assigned":
                    for pack in picking.pack_operation_ids:
                        if pack.product_id in (ship_prod, shipping):
                            # if hash_key not in shippings:
                            #     shippings[hash_key] = pack.product_id
                            #     pack.write({'qty_done': pack.product_qty})
                            # else:
                            #     pack.unlink()
                            pack.write(
                                {
                                    {'qty_done': pack.product_qty}
                                }
                            )
                        elif pack.product_id.espresso and pack.product_qty > 0:
                            pack.write({'qty_done': pack.product_qty})
                            nro_lines += 1
                        else:
                            pack.unlink()
                if nro_lines:
                    action = picking.do_new_transfer()
                    if isinstance(action, dict):
                        exec_wizard(action)
                    if hash_key not in ddts:
                        ddts[hash_key] = self.env["stock.picking"]
                    ddts[hash_key] += picking
                    if picking.sale_id not in orders:
                        orders.append(picking.sale_id)
        ddt_ids = []
        for hash_key in ddts.keys():
            ddt = ddt_model.create(
                ddt_model.preparare_ddt_data(
                    ddts[hash_key],
                    defaults={
                        "transportation_reason_id": self.env.ref(
                            "l10n_it_ddt.transportation_reason_VEN").id,
                        "goods_description_id":
                            self.env.ref("l10n_it_ddt.goods_description_CAR"),
                    }
                )
            )
            carrier_id = False
            ship_prod = False
            for line in ddt.line_ids:
                if not ship_prod and line.sale_id and line.sale_id.carrier_id:
                    carrier_id = line.sale_id.carrier_id
                    ship_prod = line.sale_id.carrier_id.product_id
                    break
            if not ship_prod:
                ship_prod = shipping
                carrier_id = self.env["delivery.carrier"].search(
                    [("name", "=", shipping.name)])[0]
            ship_line = False
            for line in ddt.line_ids:
                if line.product_id and line.product_id in (ship_prod, shipping):
                    ship_line = line
                    break
            if carrier_id:
                shipping_cost = (False if ddt.untaxed_amount >= carrier_id.amount
                                 else True)
                if ship_line and not shipping_cost:
                    line.unlink()
                elif not ship_line and shipping_cost:
                    vals = {
                        'package_preparation_id': ddt.id,
                        'product_id': ship_prod.id,
                        'product_uom_id': ship_prod.uom_id,
                        'product_qty_uom': 1.0,
                        'price_unit': carrier_id.fixed_price,
                        'name': ship_prod.name,
                        'tax_ids': [6, 0, [False]],
                        'sequence': 9999,
                    }
                    self.env["stock.picking.package.preparation.line"].create(vals)
            ddt_ids.append(ddt.id)
        return ddt_ids


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    espresso = fields.Boolean(
        string="Prodotto espresso",
        related="product_id.espresso",
    )

    @api.model
    def line_with_product_espresso(self, shipping=None):
        return (self.product_id.espresso and
                self.product_id.type != "service" and
                self.product_id != shipping)


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.model
    def line_with_product_espresso(self, shipping=None):
        return (self.product_id.espresso and
                self.product_id.type != "service" and
                self.product_id != shipping)
