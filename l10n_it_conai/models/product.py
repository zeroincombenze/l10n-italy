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


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    conai_category_id = fields.Many2one(
        'italy.conai.product.category', string='CONAI Category')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    conai_category_id = fields.Many2one(
        'italy.conai.product.category', string='CONAI Category')
