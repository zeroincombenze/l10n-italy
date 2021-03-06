# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#


from odoo import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

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
    ddt_invoicing_group = fields.Selection(
        [('nothing', 'One DDT - One Invoice'),
         ('billing_partner', 'Billing Partner'),
         ('shipping_partner', 'Shipping Partner'),
         ('sale_order', 'By Sale Order'),
         ('code_group', 'Code group')], 'DDT invoicing group',
        default='billing_partner')
    ddt_code_group = fields.Char(string='Code group')
    ddt_show_price = fields.Boolean(
        string='DDT show prices', default=False, help="Show prices and \
        discounts in ddt report")
    ddt_invoice_exclude = fields.Boolean(
        string='Do not invoice services from DDT',
        help="If flagged services will not be automatically "
             "invoiced from DDT. If set on the partner, this parameter will"
             "be automatically applied to Sale Orders.")
