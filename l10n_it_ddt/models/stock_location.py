# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#

from odoo import fields, models


class StockLocationTypeDdt(models.Model):
    _inherit = 'stock.location'

    type_ddt_id = fields.Many2one('stock.ddt.type', string='Type DDT')
