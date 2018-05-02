# -*- coding: utf-8 -*-
#
# Copyright 2017-2018, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2010-2018, Associazione Odoo Italia <https://odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp import fields, models


class ResCity(models.Model):
    _name = 'res.city'
    _description = 'City'
    name = fields.Char('City',
                       size=64,
                       help='Use "." (dot) to search with abbreviation',
                       required=True)
    zip = fields.Char('CAP',
                      size=16,
                      help='City\'s ZIP code. (Country dependent).',
                      required=True,
                      index=1)
    province = fields.Char('Province')
    phone_prefix = fields.Char('Telephone Prefix', size=16)
    istat_code = fields.Char('ISTAT code', size=16)
    cadaster_code = fields.Char('Cadaster Code', size=16)
    web_site = fields.Char('Web Site')
