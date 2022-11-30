# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def _compute_ddt_ids(self):
        for so in self:
            ddt_ids = []
            for picking in so.picking_ids:
                for ddt in picking.ddt_ids:
                    ddt_ids.append(ddt.id)
            so.ddt_ids = ddt_ids

    def _default_ddt_type(self):
        # TODO: FIX in separate module
        # signature = BeautifulSoup(self.env.user.signature).get_text()
        signature = self.env.user.signature
        if signature:
            a = signature.find(">")
            b = signature.find("<", a)
            signature = signature[a + 1 : b]
            res = self.env["stock.ddt.type"].search(
                [("name", "ilike", signature)], limit=1
            )
            if res:
                return res.id
        ids = self.env["stock.ddt.type"].search([], limit=1)
        if not ids:
            return False
        return ids[0].id

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
    partner_carrier_id = fields.Many2one(
        "res.partner",
        string="Carrier",
        oldname="ddt_carrier_id",
    )
    parcels = fields.Integer("Parcels")
    weight = fields.Float(string="Weight")
    gross_weight = fields.Float(string="Gross Weight")
    volume = fields.Float("Volume")
    ddt_ids = fields.Many2many(
        "stock.picking.package.preparation",
        string="Related DdTs",
        compute="_compute_ddt_ids",
    )
    # create_ddt = fields.Boolean('Automatically create the DDT')
    ddt_invoicing_group = fields.Selection(
        [
            ("nothing", "One DDT - One Invoice"),
            ("billing_partner", "Billing Partner"),
            ("shipping_partner", "Shipping Partners"),
            ("sale_order", "By Sale Order"),
            ("code_group", "Code group"),
        ],
        "DDT invoicing group",
        default="billing_partner",
    )
    ddt_type_id = fields.Many2one(
        "stock.ddt.type", string="DdT Type", default=_default_ddt_type
    )
    ddt_invoice_exclude = fields.Boolean(
        string="DDT do not invoice services",
        help="If flagged services from this SO will not be automatically "
        "invoiced from DDT. This parameter can be set on partners and "
        "automatically applied to Sale Orders.",
    )
    delivery_data_set = fields.Boolean(string="Delivery Data is Set")

    @api.model
    def get_delivery_value(self, fieldname):
        if not self[fieldname]:
            ddt_model = self.env["stock.picking.package.preparation"]
            dc_fieldname = ddt_model.fieldname_of_model("delivery.carrier", fieldname)
            dt_fieldname = ddt_model.fieldname_of_model("stock.ddt.type", fieldname)
            rp_fieldname = ddt_model.fieldname_of_model("res.partner", fieldname)
            if self.carrier_id and dc_fieldname and self.carrier_id[dc_fieldname]:
                self[fieldname] = self.carrier_id[dc_fieldname]
            elif self.ddt_type_id and dt_fieldname and self.ddt_type_id[dt_fieldname]:
                self[fieldname] = self.ddt_type_id[dt_fieldname]
            elif self.partner_id and rp_fieldname and self.partner_id[rp_fieldname]:
                self[fieldname] = self.partner_id[rp_fieldname]

    @api.multi
    @api.onchange("partner_id")
    def onchange_partner_id(self):
        result = super(SaleOrder, self).onchange_partner_id()
        for fieldname in (
            "carrier_id",
            "ddt_type_id",
            "goods_description_id",
            "carriage_condition_id",
            "transportation_reason_id",
            "transportation_method_id",
            "partner_carrier_id",
            "ddt_invoicing_group",
            "ddt_invoice_exclude",
        ):
            self.get_delivery_value(fieldname)
        self.delivery_data_set = True
        return result

    @api.multi
    @api.onchange("ddt_type_id")
    def onchange_ddt_type(self):
        if (
            not self.ddt_type_id.company_id
            or self.ddt_type_id.company_id == self.company_id
        ):
            for fieldname in (
                "carrier_id",
                "ddt_type_id",
                "goods_description_id",
                "carriage_condition_id",
                "transportation_reason_id",
                "transportation_method_id",
                "partner_carrier_id",
                "ddt_invoicing_group",
                "ddt_invoice_exclude",
            ):
                self.get_delivery_value(fieldname)
            self.delivery_data_set = True

    @api.multi
    @api.onchange("carrier_id")
    def onchange_carrier_id(self):
        if self.carrier_id:
            for fieldname in (
                "carrier_id",
                "ddt_type_id",
                "goods_description_id",
                "carriage_condition_id",
                "transportation_reason_id",
                "transportation_method_id",
                "partner_carrier_id",
                "ddt_invoicing_group",
                "ddt_invoice_exclude",
            ):
                self.get_delivery_value(fieldname)
            self.delivery_data_set = True

    @api.multi
    def _prepare_invoice(self):
        vals = super(SaleOrder, self)._prepare_invoice()
        vals.update(
            {
                "carriage_condition_id": self.carriage_condition_id.id,
                "goods_description_id": self.goods_description_id.id,
                "transportation_reason_id": self.transportation_reason_id.id,
                "transportation_method_id": self.transportation_method_id.id,
                "partner_carrier_id": self.partner_carrier_id.id,
                "parcels": self.parcels,
                "weight": self.weight,
                "gross_weight": self.gross_weight,
                "volume": self.volume,
            }
        )
        return vals

    @api.multi
    def action_create_ddt(self):
        ddt_model = self.env["stock.picking.package.preparation"]
        pickings = self.env["stock.picking"]
        orders = []
        for order in self:
            for picking in order.picking_ids:
                if (
                    picking.state in ("draft",
                                      "waiting",
                                      "partially_available",
                                      "confirmed",
                                      "assigned",
                                      "done")
                    and len(picking.mapped("ddt_ids")) == 0
                ):
                    pickings += picking
                if picking.sale_id not in orders:
                    orders.append(picking.sale_id)
        if not pickings:
            raise UserError(_("There are not picking to create a DdT"))
        if any([x for x in orders if x.state != 'sale']):
            raise UserError("There are some unconfirmed sale orders!")
        ddt = ddt_model.create(
            ddt_model.preparare_ddt_data(pickings=pickings)
        )
        for order in orders:
            if order.invoice_status == "no":
                order.invoice_status = "to invoice"
        return [ddt.id]

    @api.multi
    def action_cancel(self):
        for order in self:
            for ddt in order.ddt_ids:
                if ddt.state == "draft":
                    ddt.unlink()
                else:
                    raise UserError(_("Document has ddt %s linked" % ddt.ddt_number))
        return super(SaleOrder, self).action_cancel()

    @api.multi
    def action_view_ddt(self):
        mod_obj = self.env["ir.model.data"]
        act_obj = self.env["ir.actions.act_window"]

        result = mod_obj.get_object_reference(
            "stock_picking_package_preparation",
            "action_stock_picking_package_preparation",
        )
        ddt_id = result and result[1] or False
        result = act_obj.browse(ddt_id).read()[0]

        ddt_ids = []
        for so in self:
            ddt_ids += [ddt.id for ddt in so.ddt_ids]

        if len(ddt_ids) > 1:
            result["domain"] = "[('id','in',[" + ",".join(map(str, ddt_ids)) + "])]"
        else:
            res = mod_obj.get_object_reference(
                "stock_picking_package_preparation",
                "stock_picking_package_preparation_form",
            )
            result["views"] = [(res and res[1] or False, "form")]
            result["res_id"] = ddt_ids and ddt_ids[0] or False
        return result

    def get_delivery_values(self, vals):
        """If write is called from external partner (i.e. e-commerce)
        delivery data will be empty even if ddt_type and/or carrier_id are set
        In ordinary edit by end-user, delivery_data_set is True"""
        if self.id and self.delivery_data_set:
            vals["delivery_data_set"] = True
        if not vals.get("delivery_data_set"):
            for fieldname in (
                "carrier_id",
                "ddt_type_id",
                "goods_description_id",
                "carriage_condition_id",
                "transportation_reason_id",
                "transportation_method_id",
                "partner_carrier_id",
                "ddt_invoicing_group",
                "ddt_invoice_exclude",
            ):
                vals = self.env["stock.picking.package.preparation"].get_delivery_value(
                    vals,
                    self if self.id else None,
                    fieldname,
                    target="sale.order",
                )
            vals["delivery_data_set"] = True
        return vals

    @api.multi
    def write(self, vals):
        vals = self.get_delivery_values(vals)
        return super(SaleOrder, self).write(vals)

    @api.model
    def create(self, vals):
        vals = self.get_delivery_values(vals)
        return super(SaleOrder, self).create(vals)


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    weight = fields.Float(string="Line Weight")

    @api.multi
    @api.onchange("product_id", "product_uom_qty")
    def _compute_weight(self):
        if self.product_id:
            self.weight = self.product_id.weight * self.product_uom_qty
        # return super(SaleOrderLine, self)._compute_weight()

    @api.model
    def create(self, vals):
        if vals.get("product_id"):
            order = self.env["sale.order"].browse(vals["order_id"])
            if not order.carrier_id:
                product = self.env["product.product"].browse(vals["product_id"])
                if product.is_delivery:
                    carrier = self.env['delivery.carrier'].search(
                        [('product_id', '=', vals["product_id"])])
                    if carrier:
                        order.carrier_id = carrier.id
        return super(SaleOrderLine, self).create(vals)
