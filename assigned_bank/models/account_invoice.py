# -*- coding: utf-8 -*-
#
# Copyright 2019-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self.partner_bank_id = False
        if (self.partner_id.commercial_partner_id and
                self.partner_id.commercial_partner_id.assigned_bank):
            self.partner_bank_id = self.\
                partner_id.commercial_partner_id.assigned_bank.id
        return super(AccountInvoice, self)._onchange_partner_id()

