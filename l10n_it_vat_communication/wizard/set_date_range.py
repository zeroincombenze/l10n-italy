# -*- coding: utf-8 -*-
#    Copyright 2018 Associazione Odoo Italia
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class SetDateRange(models.TransientModel):
    _name = 'set.date.range.commitment'

    date_range_id = fields.Many2one('date.range', string="Date range")
    from_date = fields.Date('From date', required=True)
    to_date = fields.Date('To date', required=True)
    state = fields.Selection([('init', 'init'), ('done', 'done')],
                             string='Status', readonly=True, default='init')

    @api.multi
    def set_date_range(self):
        self.ensure_one()
        wizard = self
        if not wizard.from_date or not wizard.from_date:
            raise UserError(_('No date range found!\n'
                              'Please insert date values!'))
        self.state = 'done'
        return {
            'name': _('Set Date Range'),
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': False,
            'res_model': 'set.date.range.commitment',
            'domain': [],
            'context': dict(self._context, active_ids=self.ids),
            'type': 'ir.actions.act_window',
            'target': 'new',
            'res_id': self.id,
        }
