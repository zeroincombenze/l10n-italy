# -*- coding: utf-8 -*-
# Copyright 2019-22 Antonio M. Vigliotti - SHS-Av srl

from odoo import models, fields, api


class AccountTax(models.Model):
    _inherit = 'account.tax'

    @api.onchange('nature_id')
    def _onchange_nature(self):
        rc = False
        if self.nature_id and self.rc:
            rc = True
        self.rc = rc

    # end _compute_rc
    rc = fields.Boolean("RC")
