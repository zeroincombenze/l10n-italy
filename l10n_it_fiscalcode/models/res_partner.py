# -*- coding: utf-8 -*-
#    Copyright (C) 2010-2012 Associazione Odoo Italia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import logging
from openerp.osv import fields, orm

_logger = logging.getLogger(__name__)
try:
    import codicefiscale
except ImportError as err:
    _logger.debug(err)

SPLIT_MODE = [('LF', 'Last/First'),
              ('FL', 'First/Last'),
              ('LFM', 'Last/First Middle'),
              ('FML', 'First middle/Last'),
              ('L2F', 'Last last/First'),
              ('FL2', 'First/Last last'),
              ('L2FM', 'Last last/First Middle'),
              ('FML2', 'First Middle/Last last')]


class ResPartner(orm.Model):
    _inherit = 'res.partner'

    def check_fiscalcode(self, cr, uid, ids, context=None):
        for partner in self.browse(cr, uid, ids):
            if not partner.fiscalcode:
                return True
            elif len(partner.fiscalcode) != 16 and partner.individual:
                return False
            else:
                return True

    def _join_lastname_particle(self, fields):
        """Join most common surname particles"""
        if len(fields) > 1:
            particles = ['de', 'der', 'des', 'di', 'mc', 'van', 'von', 'zu']
            for particle in particles:
                i = [i for i, x in enumerate(fields) if x == particle]
                if i:
                    i = i[0]
                    fields[i + 1] = '%s %s' % (fields[i], fields[i + 1])
                    del fields[i]
                    break
        return fields

    def _split_last_name(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for partner in self.browse(cr, uid, ids, context=context):
            lastname, firstname = self._split_last_first_name(
                cr, uid, partner=partner)
            if lastname:
                res[partner.id] = lastname
        return res

    def _split_first_name(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for partner in self.browse(cr, uid, ids, context=context):
            lastname, firstname = self._split_last_first_name(
                cr, uid, partner=partner)
            if firstname:
                res[partner.id] = firstname
        return res

    def _split_last_first_name(self, cr, uid, partner=None,
                               name=None, splitmode=None):
        if partner:
            if not partner.individual and partner.is_company:
                return '', ''
            name = partner.name
            if not splitmode:
                if hasattr(partner, 'splitmode') and partner.splitmode:
                    splitmode = partner.splitmode
                else:
                    splitmode = self._default_splitmode(cr, uid)
        elif not splitmode:
            splitmode = self._default_splitmode(cr, uid)
        if not isinstance(name, basestring) or \
                not isinstance(splitmode, basestring):
            return '', ''
        f = self._join_lastname_particle(name.split(' '))
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

    def _set_last_first_name(self, cr, uid, partner_id, name, value, arg,
                             context=None):
        return True

    _columns = {
        'fiscalcode': fields.char(
            'Fiscal Code', size=16, help="Italian Fiscal Code"),
        'individual': fields.boolean(
            'Individual',
            help="If checked the C.F. is referred to a Individual Person"),
        'splitmode': fields.selection(SPLIT_MODE,
                                      "First Last format"),
        'firstname': fields.function(
            _split_first_name,
            string="First Name",
            type="char",
            store=True,
            select=True,
            readonly=True,
            fnct_inv=_set_last_first_name),
        'lastname': fields.function(
            _split_last_name,
            string="Last Name",
            type="char",
            store=True,
            select=True,
            readonly=True,
            fnct_inv=_set_last_first_name),
        'split_next': fields.boolean(
            'Θ ⇔ Φ',
            help="Check for change first/last name format"),
    }

    _defaults = {
        'individual': False,
        'splitmode': 'LF',
    }
    _constraints = [(
        check_fiscalcode,
        "The fiscal code doesn't seem to be correct.", ["fiscalcode"])]
    # _sql_constraints = [
    #     ('fiscalcode_uniq', 'unique (fiscalcode, company_id)',
    #      'The fiscal code must be unique per company !'),
    # ]

    def onchange_fiscalcode(self, cr, uid, ids, fiscalcode, country_id,
                            context=None):
        name = 'fiscalcode'
        if fiscalcode:
            country_model = self.pool.get('res.country')
            if country_id and country_model.browse(
                    cr, uid, country_id).code != 'IT':
                return {'value': {name: fiscalcode,
                                  'individual': True}}
            elif len(fiscalcode) == 11:
                res_partner_model = self.pool.get('res.partner')
                chk = res_partner_model.simple_vat_check(
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
                individual = True
                fiscalcode = fiscalcode.upper()
                chk = codicefiscale.control_code(fiscalcode[0:15])
                if chk != fiscalcode[15]:
                    value = fiscalcode[0:15] + chk
                    return {'value': {name: value,
                                      'individual': individual},
                            'warning': {
                                'title': 'Invalid fiscalcode!',
                                'message': 'Fiscal code could be %s' % (value)}
                            }
            return {'value': {name: fiscalcode,
                              'individual': individual}}
        return {'value': {'individual': False}}

    def onchange_name(self, cr, uid, ids, name, splitmode, context=None):
        lastname, firstname = self._split_last_first_name(
            cr, uid, name=name, splitmode=splitmode)
        value = {'splitmode': splitmode,
                 'split_next': False}
        if firstname:
            value['firstname'] = firstname
        if lastname:
            value['lastname'] = lastname
        res = {'value': value}
        return res

    def onchange_splitmode(self, cr, uid, ids, splitmode, name,
                           context=None):
        lastname, firstname = self._split_last_first_name(
            cr, uid, name=name, splitmode=splitmode)
        value = {'splitmode': splitmode,
                 'split_next': False}
        if firstname:
            value['firstname'] = firstname
        if lastname:
            value['lastname'] = lastname
        res = {'value': value}
        return res

    def onchange_split_next(self, cr, uid, ids, splitmode, name, context=None):
        i = [i for i, x in enumerate(SPLIT_MODE) if x[0] == splitmode][0]
        i = (i + 1) % len(SPLIT_MODE)
        splitmode = SPLIT_MODE[i][0]
        return self.onchange_splitmode(cr, uid, ids, splitmode, name, context)

    def _default_splitmode(self, cr, uid, partner=None, context=None):
        return 'LF'
