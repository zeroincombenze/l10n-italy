# -*- coding: utf-8 -*-
#
# Copyright 2019-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import odoo.addons.decimal_precision as dp
from odoo import fields, models, api, exceptions, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    conai_exemption_id = fields.Many2one(
        'italy.conai.partner.category', string='CONAI Category')
