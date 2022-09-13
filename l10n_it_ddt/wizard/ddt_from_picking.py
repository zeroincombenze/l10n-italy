# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class DdTFromPickings(models.TransientModel):
    _name = "ddt.from.pickings"

    def _get_picking_ids(self):
        return self.env["stock.picking"].browse(self.env.context["active_ids"])

    picking_ids = fields.Many2many("stock.picking", default=_get_picking_ids)

    @api.multi
    def create_ddt(self):
        ddt_model = self.env["stock.picking.package.preparation"]
        ddt = ddt_model.create(ddt_model.preparare_ddt_data(pickings=self.picking_ids))
        # ----- Show new ddt
        ir_model_data = self.env["ir.model.data"]
        form_res = ir_model_data.get_object_reference(
            "stock_picking_package_preparation",
            "stock_picking_package_preparation_form",
        )
        form_id = form_res and form_res[1] or False
        tree_res = ir_model_data.get_object_reference(
            "stock_picking_package_preparation",
            "stock_picking_package_preparation_tree",
        )
        tree_id = tree_res and tree_res[1] or False
        return {
            "name": "DdT",
            "view_type": "form",
            "view_mode": "form,tree",
            "res_model": "stock.picking.package.preparation",
            "res_id": ddt.id,
            "view_id": False,
            "views": [(form_id, "form"), (tree_id, "tree")],
            "type": "ir.actions.act_window",
        }


class StockPicking(models.Model):
    _inherit = "stock.picking"

    ddt_type = fields.Many2one(
        "stock.ddt.type", related="picking_type_id.default_location_src_id.type_ddt_id"
    )
