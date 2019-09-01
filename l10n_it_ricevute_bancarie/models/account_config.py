# -*- coding: utf-8 -*-
#
# Copyright 2012    - Andrea Cometa <http://www.andreacometa.it>
# Copyright 2012    - Associazione Odoo Italia <https://www.odoo-italia.org>
# Copyright 2012-17 - Lorenzo Battistini <https://www.agilebg.com>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from openerp import api, fields, models


class AccountConfigSettings(models.TransientModel):

    _inherit = 'account.config.settings'

    due_cost_service_id = fields.Many2one(
        related='company_id.due_cost_service_id',
        help='Default Service for RiBa Due Cost (collection fees) on invoice',
        domain=[('type', '=', 'service')])

    @api.model
    def default_get(self, fields):
        res = super(AccountConfigSettings, self).default_get(fields)
        if res:
            res[
                'due_cost_service_id'
            ] = self.env.user.company_id.due_cost_service_id.id
        return res


class ResCompany(models.Model):

    _inherit = 'res.company'

    due_cost_service_id = fields.Many2one('product.product')
