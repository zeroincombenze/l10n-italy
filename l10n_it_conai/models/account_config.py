# -*- coding: utf-8 -*-
#
# Copyright 2021 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
#
from odoo import api, fields, models


class AccountConfigSettings(models.TransientModel):

    _inherit = "account.config.settings"

    conai_product_id = fields.Many2one(
        related="company_id.conai_product_id",
        help="Conai product",
        domain=[("type", "=", "service")],
    )

    @api.model
    def default_get(self, fields):
        res = super(AccountConfigSettings, self).default_get(fields)
        if res:
            res["conai_product_id"] = self.env.user.company_id.conai_product_id.id
        return res


class ResCompany(models.Model):

    _inherit = "res.company"

    conai_product_id = fields.Many2one("product.product")
