# -*- encoding: utf-8 -*-
#
#
#    Copyright (C) 2010 OpenERP Italian Community
#    (<http://www.openerp-italia.org>).
#    Copyright (C) 2010 Associazione OpenERP Italia.
#    Copyright (C) 2014 Lorenzo Battistini <lorenzo.battistini@agilebg.com>.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
from openerp.osv import osv
from openerp.osv import fields


class res_city(osv.osv):
    _name = 'res.city'
    _description = 'City'
    _columns = {
        'name': fields.char('City',
                            size=64,
                            help='Official city name.',
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
    }
