# -*- coding: utf-8 -*-
from odoo import models, fields


class Picking(models.Model):
    _inherit = "stock.picking"

    move_line_ids = fields.One2many('stock.move.line', 'picking_id', 'Operations')
    move_ids_without_package = fields.One2many(
        'stock.move.line',
        'picking_id',
        'Operations without package',
        domain=['|',
                ('package_ids', '=', False),
                ('picking_type_entire_packs', '=', False)]
    )
