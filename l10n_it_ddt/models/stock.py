# -*- coding: utf-8 -*-
#
#    License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#


from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.move"

    # @api.multi
    # def action_cancel(self):
    #     for move in self:
    #         if move.state == "done":
    #             # Force cancel of "done" state !?!?!?
    #             if move.procurement_id and move.procurement_id == "done":
    #                 move.procurement_id.write({'state': 'running'})
    #             move.write({'state': 'assigned'})
    #             if move.picking_id and move.picking_id.state == "done":
    #                 move.picking_id.write({'state': 'assigned'})
    #     return super(StockPicking, self).action_cancel()
