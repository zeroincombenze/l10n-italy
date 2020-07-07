# -*- coding: utf-8 -*-
#
# Copyright 2017-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#

from odoo import models, fields, api


class AccountJournal(models.Model):
    _inherit = ['account.journal']

    check_4_sequence = fields.Boolean(
        default=False,
        help='If set, check for cronology of invoice numbers')

    @api.onchange('type')
    def _onchange_type(self):
        if self.type not in ['sale', 'sale_refund',
                             'purchase', 'purchase_refund']:
            self.check_4_sequence = False
