# -*- coding: utf-8 -*-
# Copyright 2019-22 Antonio M. Vigliotti - SHS-Av srl

from odoo import models, fields, api


class AccountTax(models.Model):
    _inherit = 'account.tax'

    @api.onchange('nature_id')
    def _onchange_nature(self):
        rc = False
        if (self.nature_id and
                (self.nature_id.code.startswith('N6') or (
                     self.nature_id.code.startswith('N3') and
                     self.nature_id.code != 'N3.5'))):
            rc = True
        self.rc = rc

    rc = fields.Boolean("RC")
