# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
from odoo import api, fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    carriage_condition_id = fields.Many2one(
        'stock.picking.carriage_condition', string='Carriage Condition')
    goods_description_id = fields.Many2one(
        'stock.picking.goods_description',
        string='Description of Goods')
    transportation_reason_id = fields.Many2one(
        'stock.picking.transportation_reason',
        string='Reason for Transportation')
    transportation_method_id = fields.Many2one(
        'stock.picking.transportation_method',
        string='Method of Transportation')
    carrier_id = fields.Many2one(
        'res.partner', string='Carrier')
    parcels = fields.Integer('Parcels')
    weight = fields.Float(string="Weight")
    gross_weight = fields.Float(string="Gross Weight")
    volume = fields.Float('Volume')
    ddt_ids = fields.One2many(
        'stock.picking.package.preparation', 'invoice_id',
        string='DDT', copy=False)

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        res = super(AccountInvoice, self)._onchange_partner_id()
        if self.partner_id:
            self.carriage_condition_id = (
                self.partner_id.carriage_condition_id.id)
            self.goods_description_id = self.partner_id.goods_description_id.id
            self.transportation_reason_id = (
                self.partner_id.transportation_reason_id.id)
            self.transportation_method_id = (
                self.partner_id.transportation_method_id.id)
        return res


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    ddt_id = fields.Many2one(
        'stock.picking.package.preparation', string='Ddt',
        related='ddt_line_id.package_preparation_id',
        store=True, copy=False)
    ddt_line_id = fields.Many2one(
        'stock.picking.package.preparation.line', string='Ddt line',
        copy=False)
    ddt_sequence = fields.Integer(
        string='Ddt sequence', related='ddt_line_id.sequence',
        store=True, copy=False)
    weight = fields.Float(string="Line Weight")

    @api.multi
    @api.onchange('product_id', 'quantity')
    def _compute_weight(self):
        if self.product_id:
            self.weight = self.product_id.weight * self.quantity

    @api.multi
    def unlink(self):
        ddt_line_model = self.env['stock.picking.package.preparation.line']
        for line_inv in self:
            ddt_lines = ddt_line_model.search(
                [('invoice_line_id', '=', line_inv.id)])
            for ddt in ddt_lines:
                ddt.package_preparation_id.write({'invoice_id': False})
        super(AccountInvoiceLine, self).unlink()
