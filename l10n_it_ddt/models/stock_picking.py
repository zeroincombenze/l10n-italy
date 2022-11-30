# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#


from odoo import api, fields, models, _
from odoo.exceptions import Warning as UserError


class StockPicking(models.Model):

    _inherit = "stock.picking"

    ddt_ids = fields.Many2many(
        comodel_name="stock.picking.package.preparation",
        relation="stock_picking_pack_prepare_rel",
        column1="stock_picking_id",
        column2="stock_picking_package_preparation_id",
        string="DdT",
        copy=False,
    )
    ddt_type = fields.Many2one(
        "stock.ddt.type", related="picking_type_id.default_location_src_id.type_ddt_id"
    )

    @api.multi
    def write(self, values):
        pack_to_update = None
        if "move_lines" in values:
            pack_to_update = self.env["stock.picking.package.preparation"]
            for picking in self:
                pack_to_update |= picking.ddt_ids
        res = super(StockPicking, self).write(values)
        if pack_to_update:
            pack_to_update._update_line_ids()
        return res

    @api.multi
    def unlink(self):
        pack_to_update = self.env["stock.picking.package.preparation"]
        for picking in self:
            pack_to_update |= picking.ddt_ids
        res = super(StockPicking, self).unlink()
        if pack_to_update:
            pack_to_update._update_line_ids()
        return res

    @api.model
    def create(self, values):
        picking = super(StockPicking, self).create(values)
        if picking.ddt_ids:
            picking.ddt_ids._update_line_ids()
        return picking

    def get_ddt_shipping_partner(self):
        # this is mainly used in dropshipping configuration,
        # where self.partner_id is your supplier, but 'move_lines.partner_id'
        # is your customer
        if not self.picking_type_code == "internal":
            move_partners = self.mapped("move_lines.partner_id")
            if len(move_partners) == 1:
                return move_partners[0]
            else:
                return self.partner_id
        else:
            return self.location_dest_id.partner_id

    @api.multi
    def open_form_current(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": self._name,
            "res_id": self.id,
            "target": "current",
        }

    @api.model
    def check_is_linked_ddt(self):
        if self.ddt_ids:
            raise UserError(
                _("Selected Picking %s is already linked to DDT: %s") % (
                    self.name, self.ddt_ids[0].ddt_number,
                )
            )

    @api.model
    def check_4_delivery_value(self, target_ddt, fieldname, condition_help):
        """Check if current delivery condition is equal to DdT condition.
        See file "ddt_from_self" to furthermo information."""
        ddt_fieldname = target_ddt.fieldname_of_model(
            "stock.picking.package.preparation", fieldname
        )
        sp_fieldname = target_ddt.fieldname_of_model("stock.picking", fieldname)
        so_fieldname = target_ddt.fieldname_of_model("sale.order", fieldname)

        if (
            sp_fieldname and
            ddt_fieldname and
            self[sp_fieldname] and
            target_ddt[ddt_fieldname] and
            self[sp_fieldname] != target_ddt[ddt_fieldname]
        ):
            raise UserError(
                _(
                    "Selected Picking %s has different %s"
                    % (self.name, condition_help)
                )
            )
        elif (
            so_fieldname and
            not sp_fieldname and
            ddt_fieldname and
            self.sale_id and
            self.sale_id[so_fieldname] and
            self.sale_id[so_fieldname] != target_ddt[ddt_fieldname]
        ):
            raise UserError(
                _(
                    "Selected Picking %s has different %s"
                    % (self.name, condition_help)
                )
            )

    @api.multi
    def add_to_ddt(self, target_ddt):
        for picking in self:
            picking.check_is_linked_ddt()

            if (
                picking.state in ("cancel", "done") or
                (picking.state != target_ddt.state and
                 (picking.state not in (
                     "waiting", "partially_available", "confirmed", "assigned") or
                  target_ddt.state != "draft"))
            ):
                raise UserError(
                    _("Selected Picking %s has invalid state %s") % (
                        picking.name, picking.state,
                    )
                )

            if picking.partner_id != target_ddt.partner_shipping_id:
                raise UserError(
                    _("Selected Picking %s has different Partner") % picking.name
                )

            for fieldname, condition_help in (
                ("carriage_condition_id", _("carriage condition")),
                ("transportation_reason_id", _("transportation reason")),
                ("transportation_method_id", _("transportation method")),
                ("partner_carrier_id", _("carrier")),
            ):
                self.check_4_delivery_value(
                    target_ddt, fieldname, condition_help)

            target_ddt.picking_ids = [(4, picking.id)]
