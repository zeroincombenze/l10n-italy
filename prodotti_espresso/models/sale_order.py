# -*- coding: utf-8 -*-
from odoo import api, models, fields
# from odoo.exceptions import UserError
# from odoo.tools.float_utils import float_compare, float_is_zero


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def generate_ddt_espresso(self):

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
        for order in self:
            if (
                order.state != "sale" or
                not order.order_line.filtered(
                    lambda x: (
                        x.product_id.espresso and
                        x.product_id.type != "service"
                    )
                )
            ):
                # Sale Order without espresso products
                continue
            for picking in order.picking_ids:
                if len(picking.ddt_ids) or not picking.move_lines.filtered(
                    lambda x: (
                        x.product_id.espresso and
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
                if picking.state != "assigned":
                    picking.force_assign()
                if picking.state == "assigned":
                    for pack in picking.pack_operation_ids:
                        if pack.product_id.espresso and pack.product_qty > 0:
                            pack.write({'qty_done': pack.product_qty})
                            nro_lines += 1
                        else:
                            pack.unlink()
                if nro_lines:
                    action = picking.do_new_transfer()
                    if isinstance(action, dict):
                        exec_wizard(action)
                    hash_key = '%d|%d|%d' % (
                        order.partner_id.id,
                        order.partner_shipping_id.id,
                        order.payment_term_id.id)
                    if hash_key not in ddts:
                        ddts[hash_key] = self.env["stock.picking"]
                    ddts[hash_key] += picking
                    if picking.sale_id not in orders:
                        orders.append(picking.sale_id)
        for hash_key in ddts.keys():
            ddt_model.create(
                ddt_model.preparare_ddt_data(
                    ddts[hash_key],
                    defaults={
                        "transportation_reason_id":
                            self.env.ref("l10n_it_ddt.transportation_reason_VEN").id,
                        "goods_description_id":
                            self.env.ref("l10n_it_ddt.goods_description_CAR"),
                    }
                )
            )
        return True


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    espresso = fields.Boolean(
        string="Prodotto espresso",
        related="product_id.espresso",
    )
