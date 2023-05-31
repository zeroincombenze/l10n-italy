# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
from odoo import api, fields, models, _
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

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
    carrier_id = fields.Many2one(
        "delivery.carrier",
        string="Delivery Method",
        help="Fill this field if you plan to invoice the shipping based on picking.",
    )
    delivery_price = fields.Float(
        string='Estimated Delivery Price', compute='_compute_delivery_price', store=True
    )
    # partner_carrier_id = fields.Many2one(
    #     "res.partner",
    #     string="Carrier",
    #     oldname="carrier_id",
    # )
    parcels = fields.Integer("Parcels")
    weight = fields.Float(string="Weight", digits=dp.get_precision("Stock Weight"))
    gross_weight = fields.Float(
        string="Gross Weight", digits=dp.get_precision("Stock Weight")
    )
    volume = fields.Float("Volume")
    ddt_ids = fields.One2many(
        "stock.picking.package.preparation", "invoice_id", string="DDT", copy=False
    )

    @api.onchange("partner_id", "company_id")
    def _onchange_partner_id(self):
        res = super(AccountInvoice, self)._onchange_partner_id()
        if self.partner_id:
            self.carriage_condition_id = self.partner_id.carriage_condition_id.id
            self.goods_description_id = self.partner_id.goods_description_id.id
            self.transportation_reason_id = self.partner_id.transportation_reason_id.id
            self.transportation_method_id = self.partner_id.transportation_method_id.id
        return res

    @api.depends('carrier_id', 'invoice_line_ids')
    def _compute_delivery_price(self):
        for inv in self:
            if inv.state != 'draft' or not inv.invoice_line_ids:
                continue
            if inv.company_id.delivery_price_policy == "delivery":
                delivery_price = 0.0
                for line in inv.invoice_line_ids:
                    if line.is_delivery:
                        delivery_price += line.price_subtotal
                inv.delivery_price = delivery_price

    @api.multi
    def _delivery_unset(self):
        self.env['account.invoice.line'].search(
            [('invoice_id', 'in', self.ids), ('is_delivery', '=', True)]
        ).unlink()

    @api.multi
    def delivery_set(self):
        # Remove delivery products from the account invoice
        self._delivery_unset()

        for inv in self:
            if inv.state not in ('draft', 'sent'):
                raise UserError(
                    _('The invoice state have to be draft to add delivery lines.')
                )
            if inv.company_id.delivery_price_policy == "delivery":
                carriers = {}
                delivery_price = 0.0
                for line in inv.invoice_line_ids:
                    if line.ddt_line_id:
                        ddt = line.ddt_line_id.package_preparation_id
                        if ddt not in carriers:
                            carriers[ddt] = {}
                            if ddt.carrier_id:
                                carriers[ddt]["carrier"] = ddt.carrier_id
                            elif (
                                line.sale_line_id
                                and line.sale_line_id.order_id
                                and line.sale_line_id.order_id.carrier_id
                            ):
                                carriers[ddt][
                                    "carrier"
                                ] = line.sale_line_id.order_id.carrier_id
                            carriers[ddt]["delivery_price"] = ddt.delivery_price
                            delivery_price += ddt.delivery_price
                for ddt in carriers.keys():
                    inv._create_delivery_line(
                        carriers[ddt]["carrier"], carriers[ddt]["delivery_price"]
                    )
                inv.delivery_price = delivery_price
        return True

    def _create_delivery_line(self, carrier, price_unit):
        AccountInvoiceLine = self.env['account.invoice.line']
        if self.partner_id:
            carrier = carrier.with_context(lang=self.partner_id.lang)

        taxes = carrier.product_id.taxes_id.filtered(
            lambda t: t.company_id.id == self.company_id.id
        )
        taxes_ids = taxes.ids
        if self.partner_id and self.fiscal_position_id:
            taxes_ids = self.fiscal_position_id.map_tax(
                taxes, carrier.product_id, self.partner_id
            ).ids

        account_id = AccountInvoiceLine.get_invoice_line_account(
            'out_invoice', carrier.product_id, self.fiscal_position_id, self.company_id
        )

        carrier_with_partner_lang = carrier.with_context(lang=self.partner_id.lang)
        if carrier_with_partner_lang.product_id.description_sale:
            inv_description = '%s: %s' % (
                carrier_with_partner_lang.name,
                carrier_with_partner_lang.product_id.description_sale,
            )
        else:
            inv_description = carrier_with_partner_lang.name
        values = {
            'account_id': account_id.id,
            'invoice_id': self.id,
            'name': inv_description,
            'quantity': 1,
            'uom_id': carrier.product_id.uom_id.id,
            'product_id': carrier.product_id.id,
            'price_unit': price_unit,
            'invoice_line_tax_ids': [(6, 0, taxes_ids)],
            'is_delivery': True,
        }
        if self.invoice_line_ids:
            values['sequence'] = self.invoice_line_ids[-1].sequence + 1
        invl = AccountInvoiceLine.sudo().create(values)
        return invl


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    ddt_id = fields.Many2one(
        "stock.picking.package.preparation",
        string="Ddt",
        related="ddt_line_id.package_preparation_id",
        store=True,
        copy=False,
    )
    ddt_line_id = fields.Many2one(
        "stock.picking.package.preparation.line", string="Ddt line", copy=False
    )
    ddt_sequence = fields.Integer(
        string="Ddt sequence", related="ddt_line_id.sequence", store=True, copy=False
    )
    weight = fields.Float(string="Line Weight", digits=dp.get_precision("Stock Weight"))
    sale_line_id = fields.Many2one(
        "sale.order.line", string="Sale order line", store=True, readonly=True
    )
    # TODO: Remove
    sale_line_ids = fields.Many2many(
        "sale.order.line", string="Sale order lines", store=True, readonly=True
    )
    is_delivery = fields.Boolean(string="Is a Delivery", default=False)

    @api.onchange("product_id", "quantity")
    def _compute_weight(self):
        if self.product_id:
            prod_weight = (self.product_id.weight
                           or self.product_id.product_tmpl_id.weight)
            if not self.weight or self.weight <= (prod_weight * 1.05):
                self.weight = prod_weight * self.quantity

    @api.multi
    def unlink(self):
        ddt_line_model = self.env["stock.picking.package.preparation.line"]
        for line_inv in self:
            ddt_lines = ddt_line_model.search([("invoice_line_id", "=", line_inv.id)])
            for ddt in ddt_lines:
                ddt.package_preparation_id.write({"invoice_id": False})
        super(AccountInvoiceLine, self).unlink()
