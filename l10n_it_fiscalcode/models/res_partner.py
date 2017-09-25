# -*- coding: utf-8 -*-
#
#
#    Copyright (C) 2010-2012 Associazione Odoo Italia
#    (<http://www.odoo-italia.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
from osv import fields, orm
import logging


_logger = logging.getLogger(__name__)
try:
    import codicefiscale
except ImportError as err:
    _logger.debug(err)


class res_partner(orm.Model):
    _inherit = 'res.partner'

    def check_fiscalcode(self, cr, uid, ids, context=None):

        for partner in self.browse(cr, uid, ids):
            if not partner.fiscalcode:
                return True
            elif len(partner.fiscalcode) != 16 and partner.individual:
                return False
            else:
                return True

    def _split_last_first_name(self, cr, uid, partner=None,
                               name=None, splitmode=None):
        if partner:
            if not partner.individual and partner.is_company:
                return '', ''
            f = partner.name.split(' ')
            if not splitmode:
                if hasattr(partner, 'splitmode'):
                    splitmode = partner.splitmode
                else:
                    splitmode = self._default_splitmode(cr, uid)
        else:
            if not name:
                return '', ''
            if not splitmode:
                splitmode = self._default_splitmode(cr, uid)
            f = name.split(' ')
        if len(f) == 1:
            if splitmode[0] == 'F':
                return '', f[0]
            elif splitmode[0] == 'L':
                return f[0], ''
        elif len(f) == 2:
            if splitmode[0] == 'F':
                return f[1], f[0]
            elif splitmode[0] == 'L':
                return f[0], f[1]
        elif len(f) == 3:
            if splitmode in ('LFM', 'LF', 'L2FM'):
                return f[2], '%s %s' % (f[0], f[1])
            elif splitmode in ('FML', 'FL', 'FML2'):
                return '%s %s' % (f[0], f[1]), f[2]
            elif splitmode == 'L2F':
                return '%s %s' % (f[0], f[1]), f[2]
            elif splitmode == 'FL2':
                return '%s %s' % (f[1], f[2]), f[0]
        else:
            if splitmode[0] == 'F':
                return '%s %s' % (f[2], f[3]), '%s %s' % (f[0], f[1])
            elif splitmode[0] == 'L':
                return '%s %s' % (f[0], f[1]), '%s %s' % (f[2], f[3])
        return '', ''

    def _split_last_name(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for partner in self.browse(cr, uid, ids, context=context):
            lastname, firstname = self._split_last_first_name(
                cr, uid, partner=partner)
            res[partner.id] = lastname
        return res

    def _split_first_name(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for partner in self.browse(cr, uid, ids, context=context):
            lastname, firstname = self._split_last_first_name(
                cr, uid, partner=partner)
            res[partner.id] = firstname
        return res

    def _set_last_first_name(self, cr, uid, partner_id, name, value, arg,
                             context=None):
        return True

    _columns = {
        'fiscalcode': fields.char(
            'Fiscal Code', size=16, help="Italian Fiscal Code"),
        'individual': fields.boolean(
            'Individual',
            help="If checked the C.F. is referred to a Individual Person"),
        'firstname': fields.function(
            _split_first_name,
            string="First Name",
            type="char",
            store=True,
            select=True,
            readonly=True,
            fnct_inv=_set_last_first_name),
        'lastname':  fields.function(
            _split_last_name,
            string="Last Name",
            type="char",
            store=True,
            select=True,
            readonly=True,
            fnct_inv=_set_last_first_name),
    }
    # 'splitmode': fields.selection([('LF', 'Last/First'),
    #                            ('FL', 'First/Last'),
    #                            ('LFM', 'Last/First Middle'),
    #                            ('L2F', 'Last last/First'),
    #                            ('L2FM', 'Last last/First Middle'),
    #                            ('FML', 'First middle/Last'),
    #                            ('FL2', 'First/Last last'),
    #                            ('FML2', 'First Middle/Last last')],
    #                           "First Last format"),

    _defaults = {
        'individual': False,
        # 'splitmode': 'LF',
    }
    # _constraints = [(
    #     check_fiscalcode,
    #     "The fiscal code doesn't seem to be correct.", ["fiscalcode"])]
    # _sql_constraints = [
    #     ('fiscalcode_uniq', 'unique (fiscalcode, company_id)',
    #      'The fiscal code must be unique per company !'),
    # ]

    def onchange_fiscalcode(self, cr, uid, ids, fiscalcode, context=None):
        name = 'fiscalcode'
        if fiscalcode:
            if len(fiscalcode) == 11:
                res_partner_pool = self.pool.get('res.partner')
                chk = res_partner_pool.simple_vat_check(
                    cr, uid, 'it', fiscalcode)
                if not chk:
                    return {'value': {name: False},
                            'warning': {
                        'title': 'Invalid fiscalcode!',
                        'message': 'Invalid vat number'}
                    }
                individual = False
            elif len(fiscalcode) != 16:
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid len!',
                    'message': 'Fiscal code len must be 11 or 16'}
                }
            else:
                fiscalcode = fiscalcode.upper()
                chk = codicefiscale.control_code(fiscalcode[0:15])
                if chk != fiscalcode[15]:
                    value = fiscalcode[0:15] + chk
                    return {'value': {name: value},
                            'warning': {
                                'title': 'Invalid fiscalcode!',
                                'message': 'Fiscal code could be %s' % (value)}
                            }
                individual = True
            return {'value': {name: fiscalcode,
                              'individual': individual}}
        return {'value': {'individual': False}}

    def onchange_name(self, cr, uid, ids, name, splitmode, context=None):
        lastname, firstname = self._split_last_first_name(
            cr, uid, name=name, splitmode=splitmode)
        res = {'value': {'firstname': firstname,
                         'lastname': lastname}}
        return res

    def onchange_splitmode(self, cr, uid, ids, splitmode, name,
                           context=None):
        lastname, firstname = self._split_last_first_name(
            cr, uid, name=name, splitmode=splitmode)
        res = {'value': {'firstname': firstname,
                         'lastname': lastname}}
        return res

    def _default_splitmode(self, cr, uid, partner=None, context=None):
        return 'LF'
