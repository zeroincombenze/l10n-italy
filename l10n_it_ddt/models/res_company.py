# -*- coding: utf-8 -*-
#
# Copyright 2016-24 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    keep_pick_state_from_ddt = fields.Boolean(
        "Keep DdT state on picking",
        help="Select multi-report style",
    )
    delivery_price_policy = fields.Selection(
        [
            ("order", "From Sale Order"),
            ("delivery", "From Delivery Note"),
        ],
        string="Delivery Cost Policy",
        defauly="order",
        help="How to evaluate delivery cost on invoice",
    )


class AccountConfigSettings(models.TransientModel):
    _inherit = "account.config.settings"

    keep_pick_state_from_ddt = fields.Boolean(
        related='company_id.keep_pick_state_from_ddt'
    )
    delivery_price_policy = fields.Selection(related='company_id.delivery_price_policy')
