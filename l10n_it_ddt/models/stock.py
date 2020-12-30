# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#


from odoo import models, api


class StockPicking(models.Model):
    _inherit = 'stock.move'

    @api.multi
    def action_cancel(self):
        for move in self:
            if move.procurement_id:
                move.procurement_id.cancel()
            for quant in move.quant_ids:
                quant.quants_move(
                    quant, move, move.location_id,
                    location_from=move.location_dest_id,
                    lot_id=move.lot_ids and move.lot_ids[0] or False)
            move.write({'state': 'cancel', 'date': False})
            if move.picking_id:
                move.picking_id.action_revert_done()
        return True
