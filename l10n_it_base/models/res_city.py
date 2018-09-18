# -*- coding: utf-8 -*-
#
# Copyright 2010-2011, Odoo Italian Community
# Copyright 2011-2017, Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2014, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, osv


class ResCity(osv.osv):
    _name = 'res.city'
    _description = 'City'

    _columns = {
        'country_id': fields.many2one('res.country',
                                      'Country',
                                      help='Country encoded by ISO-3166.'),
        'name': fields.char('City',
                            size=64,
                            help='Use "." (dot) to search with abbreviation',
                            required=True),
        'province_id': fields.many2one('res.province', 'Province'),
        'zip': fields.char('CAP',
                           size=16,
                           help='City\'s ZIP code. (Country dependent).'),
        'phone_prefix': fields.char('Telephone Prefix', size=16),
        'istat_code': fields.char('ISTAT code', size=16),
        'cadaster_code': fields.char('Cadaster Code', size=16),
        'web_site': fields.char('Web Site', size=64),
        'region': fields.related(
            'province_id', 'region', type='many2one', relation='res.region',
            string='Region', readonly=True),
        'state_id': fields.many2one(
            'res.country.state',
            'District',
            help='Upper administration (Province, District or Federal State).',
            domain="[('country_id', '=', country_id)]"),
        'nuts': fields.integer('NUTS', size=1),
    }
