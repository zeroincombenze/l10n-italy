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

from openerp.osv import osv, orm
from openerp.osv import fields
import re
# import pdb #debug
from tndb import tndb

FLDS_LIST = ['country_id', 'zip', 'city', 'state_id',
             'province_id', 'region_id']


class res_config_settings(orm.TransientModel):
    _inherit = 'res.config.settings'
    _columns = {
        'country_id': fields.many2one('res.country'),
        'zip': fields.many2one('res.city'),
        'city': fields.many2one('res.city',
                                domain="[('country_id', '=', country_id)]"),
        'state_id':
            fields.many2one('res.country.state',
                            domain="[('country_id', '=', country_id)]"),
        'province_id': fields.many2one('res.province', string='Province'),
        'region_id': fields.many2one('res.region', string='Region'),
    }

    def fld_in_model(self, model, f, name):
        if f in model._columns:
            return f
        elif name in model._columns:
            return name
        return False

    def set_geoloc(self, cr, uid, ids, name, value, context=None):
        """Set values of geolocalization from country, zip, city
        and other fields."""
        # pdb.set_trace()
        tndb.wstamp(name, value)
        context = {} if context is None else context
        res_obj = self.pool.get('res.partner')
        city_obj = self.pool.get('res.city')
        state_obj = self.pool.get('res.country.state')
        province_obj = self.pool.get('res.province')
        search_in_it = False
        is_updated = False
        flds = FLDS_LIST
        names = {}
        for f in flds:
            if f == 'city':
                names[f] = 'name'
            elif f[-3:] == '_id':
                names[f] = f[0: -3]
            else:
                names[f] = f
        fix = {}
        for f in flds:
            fix[f] = False
            if f != name:
                if not hasattr(self, f) and f in context and context[f]:
                    setattr(self, f, context[f])
                    tndb.wlog(f, '=ctx(', context[f], ')')
                elif hasattr(self, f) and \
                        f not in context and f != 'country_id':
                    delattr(self, f)
                    tndb.wlog('del', f)
        fix[name] = True
        if not hasattr(self, name) or value != getattr(self, name):
            is_updated = True
            tndb.wlog(name, 'is updated')
            if value:
                res = False
                for i, f in enumerate(flds):
                    if f == name and i < 3:
                        res = True
                    elif res:
                        fix[f] = True
                        if hasattr(self, f):
                            delattr(self, f)
                        tndb.wlog('clear ', f)
                if value:
                    setattr(self, name, value)
                    tndb.wlog(name, '=', value)
                else:
                    delattr(self, name)
                    tndb.wlog('del', name)
        # This module is for Italy so country is supposed to be Italy
        if not hasattr(self, 'country_id'):
            country_id = self.pool.get(
                'res.country').search(cr,
                                      uid,
                                      [('code', '=', 'IT')])
            if len(country_id):
                f = 'country_id'
                setattr(self, f, country_id[0])
                tndb.wlog(f, '=', country_id[0])
                fix[f] = True
                tndb.wlog('fix[', f, '] = True')
        # prepare city where
        where = []
        for f in flds:
            tbl_f = self.fld_in_model(city_obj, f, names[f])
            tndb.wlog(tbl_f, '= self.fld_in_model(city_obj,', f,
                      ', names[f]);', names[f])
            tndb.wlog('123>if hasattr(self, ', f, ') and tbl_f:',
                      hasattr(self, f), tbl_f)
            if hasattr(self, f) and tbl_f:
                if f[-3:] == '_id':
                    where.append((tbl_f, '=', getattr(self, f)))
                else:
                    tofind = getattr(self, f).replace('.', '%') + '%'
                    where.append((tbl_f, '=ilike', tofind))
                    if tofind.find('%') < 0:
                        fix[f] = False
                        tndb.wlog('fix[', f, '] = False')
                    else:
                        fix[f] = True
                        tndb.wlog('fix[', f, '] = True')
        if hasattr(self, 'country_id'):
            if self.pool.get(
                    'res.country').browse(cr,
                                          uid,
                                          self.country_id).code == 'IT':
                search_in_it = True
                tndb.wlog('search_in_it =', search_in_it)
        res = True
        f = 'country_id'
        tbl_f = self.fld_in_model(city_obj, f, names[f])
        tndb.wlog(tbl_f, '= self.fld_in_model(city_obj,', f, ', names[f]);',
                  names[f])
        tndb.wlog('150>if (search_in_it or tbl_f) and '
                  'is_updated and len(where):',
                  search_in_it, tbl_f,
                  is_updated, '(', where, ')')
        if (search_in_it or tbl_f) and is_updated and len(where):
            city_ids = city_obj.search(cr, uid, where)
            tndb.wlog('search(city,', where, ')=', city_ids)
            ix = 4
            while not len(city_ids) and ix:
                for i, x in enumerate(where):
                    if x[0] == 'zip':
                        if ix > 1:
                            l = len(getattr(self, 'zip')) + ix - 5
                            tofind = getattr(self, 'zip')[0:l] + '%'
                        else:
                            tofind = '%'
                        y = (x[0], x[1], tofind)
                        where[i] = y
                    elif x[0] == 'name':
                        if ix > 2:
                            tofind = getattr(self, 'city').replace('.', '%')
                        elif ix == 2:
                            l = len(getattr(self, 'city')) - 2
                            if l < 6:
                                l = 6
                            tofind = getattr(self, 'city')[0:l] + '%'
                            tofind = tofind.replace('.', '%')
                        else:
                            l = len(getattr(self, 'city')) - 4
                            if l < 4:
                                l = 4
                            tofind = getattr(self, 'city')[0:l] + '%'
                            tofind = tofind.replace('.', '%')
                        y = (x[0], 'ilike', tofind)
                        where[i] = y
                        if tofind.find('%') < 0:
                            fix[f] = False
                        else:
                            fix[f] = True
                    elif x[0] == 'province_id':
                        if ix < 4:
                            del where[i]
                            break
                    elif x[0] == 'state_id':
                        if ix < 4:
                            del where[i]
                            break
                    elif x[0] == 'region':
                        if ix < 4:
                            del where[i]
                            break
                city_ids = city_obj.search(cr, uid, where)
                tndb.wlog('search(city,', where, ')=', city_ids)
                ix -= 1
            if len(city_ids):
                city = city_obj.browse(cr, uid, city_ids[0])
                r = {}
                for f in flds:
                    res_f = self.fld_in_model(res_obj, f, names[f])
                    tbl_f = self.fld_in_model(city_obj, f, names[f])
                    tndb.wlog(tbl_f, '= self.fld_in_model(city_obj,', f,
                              ', names[f]);', names[f])
                    tndb.wlog('172>if tbl_f and hasattr(city, tbl_f) and',
                              '(not hasattr(self, ', f, ') or',
                              '(fix[f] and len(city_ids) == 1)):',
                              tbl_f,
                              hasattr(city, tbl_f or 'NA'),
                              hasattr(self, f), fix[f],
                              city_ids)
                    if tbl_f and hasattr(city, tbl_f) and \
                            (not hasattr(self, f) or
                             (fix[f] and len(city_ids) == 1)):
                        if f[-3:] == '_id':
                            r[res_f] = getattr(city, tbl_f).id
                        else:
                            r[res_f] = getattr(city, tbl_f)
                        tndb.wlog('r[', res_f, '] = ', r[res_f])
                    if res_f in r:
                        setattr(self, f, r[res_f])
                        tndb.wlog(f, '=', r[res_f])
                f = 'province_id'
                f1 = 'state_id'
                tndb.wlog('201>if', hasattr(self, f1), 'and (not',
                          hasattr(self, f), 'or(', fix[f],
                          'and len(city_ids)==', city_ids, '))')
                if hasattr(self, f1) and \
                        (not hasattr(self, f) or
                         (fix[f] and len(city_ids) == 1)):
                    state = state_obj.browse(cr,
                                             uid,
                                             getattr(self, f1))
                    w = []
                    res_f = self.fld_in_model(res_obj, f, names[f])
                    tbl_f = self.fld_in_model(province_obj,
                                              'country_id',
                                              names['country_id'])
                    tndb.wlog(tbl_f, '= self.fld_in_model(city_obj,', f,
                              ', names[f]);', names[f])
                    if tbl_f:
                        w.append((tbl_f, '=', getattr(self, 'country_id')))
                    w.append(('code', '=', state.code))
                    state_ids = province_obj.search(cr,
                                                    uid,
                                                    w)
                    tndb.wlog('search(province,', w, ')=', state_ids)
                    if len(state_ids) == 1:
                        r[res_f] = state_ids[0]
                        tndb.wlog('r[', res_f, '] = ', state_ids[0])
                        setattr(self, f, r[res_f])
                        tndb.wlog(f, '=', r[res_f])
                f = 'state_id'
                f1 = 'province_id'
                tndb.wlog('228>if', hasattr(self, f1), 'and (not',
                          hasattr(self, f), 'or(', fix[f],
                          'and len(city_ids)==', city_ids, '))')
                if hasattr(self, f1) and \
                        (not hasattr(self, f) or
                         (fix[f] and len(city_ids) == 1)):
                    province = province_obj.browse(cr,
                                                   uid,
                                                   getattr(self, f1))
                    w = []
                    res_f = self.fld_in_model(res_obj, f, names[f])
                    tbl_f = self.fld_in_model(state_obj,
                                              'country_id',
                                              names['country_id'])
                    tndb.wlog(tbl_f, '= self.fld_in_model(city_obj,', f,
                              ', names[f]);', names[f])
                    if tbl_f:
                        w.append((tbl_f, '=', getattr(self, 'country_id')))
                    w.append(('code', '=', province.code))
                    state_ids = state_obj.search(cr,
                                                 uid,
                                                 w)
                    tndb.wlog('search(state,', w, ')=', state_ids)
                    if len(state_ids) == 1:
                        r[res_f] = state_ids[0]
                        tndb.wlog('r[', res_f, '] = ', state_ids[0])
                        setattr(self, f, r[res_f])
                        tndb.wlog(f, '=', r[res_f])
                f = 'country_id'
                if fix[f] and f not in r:
                    r[f] = getattr(self, f)
                res = {'value': r}
                tndb.wlog('fix', fix)
                tndb.wlog('res =', res)
        return res


class res_partner(osv.osv):
    _inherit = 'res.partner'

    def _get_birthday(self, cr, uid, ids, field_names, arg, context=None):
        """ Read string birthday from res.partner """
        res = {}
        for partner in self.browse(cr, uid, ids, context=context):
            if partner.birthdate:
                f = partner.birthdate
                if re.match('[0-9]{4}.[0-9]{2}.[0-9]{2}', f):
                    res[partner.id] = f[0:4] + '-' + f[5:7] + '-' + f[8:10]
                elif re.match('[0-9]{2}.[0-9]{2}.[0-9]{4}', f):
                    res[partner.id] = f[6:10] + '-' + f[3:5] + '-' + f[0:2]
        return res

    def _set_birthday(self, cr, uid, partner_id, name, value, arg,
                      context=None):
        """ Write string birthday to res.partner """
        self.write(cr,
                   uid,
                   [partner_id],
                   {'birthdate': value or False},
                   context=context)
        return True

    _columns = {
        'province': fields.many2one('res.province', string='Province'),
        'region': fields.many2one('res.region', string='Region'),
        'province_code': fields.related(
            'province', 'code', type='char',
            size=2, string='Province code'),
        'birthday': fields.function(_get_birthday,
                                    fnct_inv=_set_birthday,
                                    type='date',
                                    string='Birth date')
    }

    def new_ctx(self,
                country_id, zip, city, state_id, province_id, region_id,
                context=None):
        context = {} if context is None else context
        if country_id:
            context['country_id'] = country_id
        if zip:
            context['zip'] = zip
        if city:
            context['city'] = city
        if state_id:
            context['state_id'] = state_id
        if province_id:
            context['province_id'] = province_id
        if region_id:
            context['region_id'] = region_id
        return context

    def on_change_country(self, cr, uid, ids,
                          country_id, zip, city, state_id, province, region,
                          context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               province, region, context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.set_geoloc(cr, uid, ids, 'country_id', country_id,
                                     context=context)

    def on_change_zip(self, cr, uid, ids,
                      country_id, zip, city, state_id, province, region,
                      context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               province, region, context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.set_geoloc(cr, uid, ids, 'zip', zip,
                                     context=context)

    def on_change_state(self, cr, uid, ids,
                        country_id, zip, city, state_id, province, region,
                        context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               province, region, context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.set_geoloc(cr, uid, ids, 'state_id', state_id,
                                     context=context)

    def on_change_province(self, cr, uid, ids,
                           country_id, zip, city, state_id, province, region,
                           context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               province, region, context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.set_geoloc(cr, uid, ids, 'province_id', province,
                                     context=context)

    def on_change_region(self, cr, uid, ids,
                         country_id, zip, city, state_id, province, region,
                         context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               province, region, context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.set_geoloc(cr, uid, ids, 'region_id', region,
                                     context=context)

    def on_change_city(self, cr, uid, ids,
                       country_id, zip, city, state_id, province, region,
                       context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               province, region, context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.set_geoloc(cr, uid, ids, 'city', city,
                                     context=context)

    def _set_vals_city_data(self, cr, uid, vals):
        context = self.new_ctx(vals.get('country_id', None),
                               vals.get('zip', None),
                               vals.get('city', None),
                               vals.get('state_id', None),
                               vals.get('province', None),
                               vals.get('region', None),
                               context=None)
        config_obj = self.pool.get('res.config.settings')
        for f in ('city', 'zip'):
            if f in vals:
                res = config_obj.set_geoloc(cr, uid, [],
                                            f, vals[f], context=context)
                if not isinstance(res, bool) and 'value' in res:
                    res = res['value']
                    for f in ('country_id', 'zip', 'city',
                              'province_id', 'state_id', 'region_id'):
                        if f == 'province_id':
                            f1 = 'province'
                        elif f == 'region_id':
                            f1 = 'region'
                        else:
                            f1 = f
                        if f1 not in vals and f in res:
                            vals[f1] = res[f]
                    break
        return vals

    # Function compatible with old l10n_it_base
    def create(self, cr, uid, vals, context=None):
        vals = self._set_vals_city_data(cr, uid, vals)
        return super(res_partner, self).create(cr, uid, vals, context)

    # Function compatible with old l10n_it_base
    def write(self, cr, uid, ids, vals, context=None):
        vals = self._set_vals_city_data(cr, uid, vals)
        return super(res_partner, self).write(cr, uid, ids, vals, context)
