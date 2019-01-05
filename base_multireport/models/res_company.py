# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    custom_header = fields.Boolean('Custom Header')
    cf_in_header = fields.Boolean(
        'Fiscalcode in Header',
        help='Print customer fiscalcode, after header vatnumber, if set')


class BaseConfigSettings(models.TransientModel):
    _inherit = 'base.config.settings'

    custom_header = fields.Boolean(
        related='company_id.custom_header',
        string='Custom Header',
        help='Disable report standard header')
    cf_in_header = fields.Boolean(
        related='company_id.cf_in_header',
        string='Fiscalcode in Header',
        help='Print customer fiscalcode, after header vatnumber, if set')
