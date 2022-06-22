# -*- coding: utf-8 -*-
# Copyright 2019-22 Antonio M. Vigliotti - SHS-Av srl

from odoo import api, fields, models


class AccountTax(models.Model):
    _inherit = "account.tax"

    @api.onchange("kind_id")
    def _onchange_nature(self):
        rc = False
        if self.kind_id and (
            self.kind_id.code.startswith("N6")
            or (self.kind_id.code.startswith("N3") and self.kind_id.code != "N3.5")
        ):
            rc = True
        self.rc = rc

    rc = fields.Boolean("RC")
