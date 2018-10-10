# -*- coding: utf-8 -*-
#
# Copyright 2010-2011, Odoo Italian Community
# Copyright 2011-2017, Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2014, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import orm
from openerp.osv import fields


FLDS_LIST1 = ['country_id', 'zip', 'city']
FLD_STATE = 'state_id'
FLD_PROVINCE = 'province_id'
FLD_REGION = 'region_id'
ACCEPT_MAX_RES = 16


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

    def copydict(self, where):
        w = []
        for y in where:
            w.append(y)
        return w

    def _set_flds_list(self):
        """Create fields list based on actual models"""
        if hasattr(self, 'fld_res') and \
                hasattr(self, 'fld_all') and \
                hasattr(self, 'alt_name'):
            flds_res = self.flds_res
            flds_all = self.flds_all
            alt_name = self.alt_name
        else:
            # Warning: due to python binding DO NOT change follow code!
            flds_res = []
            flds_all = []
            alt_name = {}
            for f in FLDS_LIST1:
                flds_res.append(f)
            tbl_f = self._fld_in_model('res.city', 'state_id')
            if tbl_f:
                for f in FLDS_LIST1 + [FLD_STATE] + [FLD_PROVINCE]:
                    flds_all.append(f)
                flds_res.append(FLD_STATE)
            else:
                for f in FLDS_LIST1 + [FLD_PROVINCE] + [FLD_STATE]:
                    flds_all.append(f)
                flds_res.append(FLD_PROVINCE)
            flds_all.append(FLD_REGION)
            for f in flds_all:
                if f == 'city':
                    alt_name[f] = 'name'
                elif f[-3:] == '_id':
                    alt_name[f] = f[0: -3]
                else:
                    alt_name[f] = f
            self.flds_res = flds_res
            self.flds_all = flds_all
            self.alt_name = alt_name

    def _clear_field(self, f, fix):
        fix[f] = True
        if hasattr(self, f):
            delattr(self, f)
        return fix

    def _fld_in_model(self, model, f):
        """Check if field is in model"""
        r = False
        model_obj = self.pool.get(model)
        if f in model_obj._columns:
            r = f
        elif hasattr(self, 'alt_name') and f in self.alt_name and \
                self.alt_name[f] in model_obj._columns:
            r = self.alt_name[f]
        return r

    def _set_field(self, fix, f, value):
        if value:
            setattr(self, f, value)

    def _read_field(self, cr, uid, dst, value):
        if dst == 'country_id':
            model = 'res.country'
            dst_obj = self.pool.get(model)
        else:                                               # pragma: no cover
            return False
        if value:
            w = self._bulk_where(model)
            w.append(('code', '=', value))
            res_ids = dst_obj.search(cr,
                                     uid,
                                     w)
            if len(res_ids) == 1:
                return res_ids[0]
        return False

    def _inherit_field(self, cr, uid, dst, src, fix):
        """Due to compatibility old version of l10n_it_base,
        province and state_id have same meaning;
        check if province xor state_id is set and then inherit empty field
        """
        if src == 'province_id':
            src_model = 'res.province'
        elif src == 'state_id':
            src_model = 'res.country.state'
        else:                                               # pragma: no cover
            return False
        src_obj = self.pool.get(src_model)
        if dst == 'province_id':
            dst_model = 'res.province'
        elif dst == 'state_id':
            dst_model = 'res.country.state'
        elif dst == 'region_id':
            dst_model = 'res.region'
        else:                                               # pragma: no cover
            return False
        dst_obj = self.pool.get(dst_model)
        if hasattr(self, src) and (not hasattr(self, dst) or fix[dst]):
            rec = src_obj.browse(cr,
                                 uid,
                                 getattr(self, src))
            if dst == 'region_id':
                if rec.region:
                    res_ids = rec.region.id
                    return res_ids
            else:
                w = self._bulk_where(dst_model)
                w.append(('code', '=', rec.code))
                res_ids = dst_obj.search(cr,
                                         uid,
                                         w)
                if len(res_ids) == 1:
                    return res_ids[0]
        return False

    def _init_local_vars(self, cr, uid, name, value, context):
        do_fill = context.get('DoFill', False)
        fix = {}
        if value != getattr(self, name, False):
            is_updated = True
        else:
            is_updated = False
        for f in self.flds_all:
            fix[f] = False
            if do_fill or f != name:
                if f in context and context[f]:
                    if getattr(self, f, False) != context[f]:
                        is_updated = True
                    setattr(self, f, context[f])
                elif hasattr(self, f) and \
                        f not in context and f != 'country_id':
                    delattr(self, f)
        if not do_fill and name[-3:] == '_id' or \
                (isinstance(value, basestring) and value.find('.') >= 0):
            fix[name] = True
        if value != getattr(self, name, False):
            if value:
                res = False
                if not do_fill:
                    for i, f in enumerate(self.flds_all):
                        if f == name:
                            if name != 'city' or \
                                    (isinstance(value, basestring) and
                                     value.find('.') < 0):
                                res = True
                        elif res:
                            fix[f] = True
                setattr(self, name, value)
            else:
                fix = self._clear_field(f, fix)
        # Special field:country_id
        # This module is for Italy so country is supposed to be Italy
        if not hasattr(self, 'country_id') and hasattr(self, 'city'):
            f = 'country_id'
            id = self._read_field(cr, uid, f, 'IT')
            self._set_field(fix, f, id)
        return fix, is_updated, do_fill

    def _store_lazy_city(self, cr, uid, name):
        """Store a lazy name to engage search of similar cities
        (it works just for Italy)"""
        wrd = getattr(self, 'city').split(' ')
        if len(wrd) > 2:
            pfx = self.pool.get(
                'res.country.state').browse(cr,
                                            uid,
                                            self.state_id).name[0:5]
            where_valid = False
            tofind = '%'
            discard = False
            for i in range(len(wrd)):
                if discard:
                    discard = False
                elif wrd[i].find(pfx) >= 0:
                    where_valid = True
                elif wrd[i].endswith("ano") or \
                        wrd[i].endswith("asco") or \
                        wrd[i].endswith("ese") or \
                        wrd[i].endswith("ino") or \
                        wrd[i].endswith("ota") or \
                        wrd[i].endswith("oto") or \
                        wrd[i].startswith("d'"):
                    where_valid = True
                elif wrd[i].startswith("di"):
                    where_valid = True
                    discard = True
                else:
                    tofind = tofind + wrd[i] + '%'
            if where_valid:
                setattr(self, 'x_city', tofind)
            elif hasattr(self, 'x_city'):
                delattr(self, 'x_city')

    def _bulk_where(self, model):
        where = []
        f = 'country_id'
        tbl_f = self._fld_in_model(model, f)
        if hasattr(self, 'country_id') and \
                getattr(self, 'country_id') and \
                tbl_f:
            where.append(('country_id', '=', getattr(self, 'country_id')))
        return where

    def _build_where(self, name, fix):
        # prepare city 'where condition'
        where = []
        where_valid = False
        for f in self.flds_res:
            tbl_f = self._fld_in_model('res.city', f)
            if hasattr(self, f) and tbl_f:
                if f[-3:] == '_id':
                    where.append((tbl_f, '=', getattr(self, f)))
                    if f != 'country_id':
                        where_valid = True
                elif f == 'city' and f != name and hasattr(self, 'x_city'):
                    where_valid = True
                    tofind = getattr(self, 'x_city')
                    where.append((tbl_f, '=ilike', tofind))
                    fix[f] = True
                elif isinstance(f, basestring):
                    where_valid = True
                    tofind = getattr(self, f).replace('.', '%')
                    if tofind.find('%') < 0:
                        where.append((tbl_f, '=', tofind))
                        if f == name:
                            fix[f] = False
                    else:
                        where.append((tbl_f, '=ilike', tofind))
                        fix[f] = True
        return where, where_valid

    def _search_level2(self, cr, uid, name, value, where):
        """No record found, Look up in a wider domain"""
        best_res = {}
        best_where = {}
        for ix, f in enumerate(self.flds_res):
            # python does not assign dictionary but it binds
            # >>>w=where does not save <where>
            w = self.copydict(where)
            tbl_f = self._fld_in_model('res.city', f)
            for i, x in enumerate(w):
                if x[0] == tbl_f:
                    if x[0] == 'zip':
                        y = int(len(getattr(self, 'zip')) / 2) + 1
                        tofind = getattr(self, 'zip')[0:y] + '%'
                        tofind = tofind.replace('%%', '%')
                        y = (x[0], x[1], tofind)
                        w[i] = y
                        c_ids = self.pool['res.city'].search(cr, uid, w)
                        best_where[ix + 100] = w
                        best_res[ix + 100] = len(c_ids)
                    elif x[0] == 'name':
                        if name != 'city' and hasattr(self, 'x_city'):
                            tofind = getattr(self, 'x_city')
                        else:
                            tofind = getattr(self,
                                             'city').replace('.',
                                                             '%')
                            tofind = tofind.replace(' ',
                                                    '%') + '%'
                            tofind = tofind.replace('%%', '%')
                        y = (x[0], '=ilike', tofind)
                        w[i] = y
                        c_ids = self.pool['res.city'].search(cr, uid, w)
                        best_where[ix + 100] = w
                        best_res[ix + 100] = len(c_ids)
                        w = self.copydict(where)
                        tofind = '%' + tofind
                        y = (x[0], 'ilike', tofind)
                        w[i] = y
                        c_ids = self.pool['res.city'].search(cr, uid, w)
                        best_where[ix + 200] = w
                        best_res[ix + 200] = len(c_ids)
                    if len(where) > 1 and x[0] != name:
                        del w[i]
                        c_ids = self.pool['res.city'].search(cr, uid, w)
                        best_where[ix] = w
                        best_res[ix] = len(c_ids)
                    break
        city_ids = []
        best_result = -1
        for ix, x in best_res.iteritems():
            if x and (best_result < 0 or
                      x < best_res[best_result] or
                      (x == best_res[best_result] and ix < best_result)):
                best_result = ix
        if best_result >= 0 and best_res[best_result] < ACCEPT_MAX_RES:
            where = best_where[best_result]
            city_ids = self.pool['res.city'].search(cr, uid, where)
        return city_ids

    def _search_level3(self, cr, uid, name, value, where):
        """No record found, Look up in a wider domain"""
        city_ids = []
        where = self._bulk_where('res.city')
        if name == 'zip':
            where.append((name, '=', value))
            city_ids = self.pool['res.city'].search(cr, uid, where)
        elif name == 'city':
            tofind = False
            if getattr(self, 'zip', False):
                tofind = self.zip[0:3] + '%'
                where.append(('zip', '=ilike', tofind))
            where.append(('name', '=ilike', value.replace('.', '%')))
            city_ids = self.pool['res.city'].search(cr, uid, where)
            if len(city_ids) == 0:
                where = self._bulk_where('res.city')
                if tofind:
                    where.append(('zip', '=ilike', tofind))
                where.append(('name', 'ilike', value.replace('.', '%') + '%'))
                city_ids = self.pool['res.city'].search(cr, uid, where)
        return city_ids

    def _search_level4(self, cr, uid, name, value, where):
        """No record found, Look up if multizone zip city"""
        city_ids = []
        where = self._bulk_where('res.city')
        if name == 'zip':
            tofind = value[0:4] + '%'
            where.append((name, '=like', tofind))
            city_ids = self.pool['res.city'].search(cr, uid, where)
            if not len(city_ids):
                where = self._bulk_where('res.city')
                tofind = value[0:3] + '%'
                where.append((name, '=like', tofind))
                city_ids = self.pool['res.city'].search(cr, uid, where)
            if len(city_ids) != 1:
                city_ids = []
            else:
                city = self.pool['res.city'].browse(cr, uid, city_ids[0])
                if not city.zip or city.zip.find('%') < 0:
                    city_ids = []
        return city_ids

    def _do_search(self, cr, uid):
        f = 'country_id'
        tbl_f = self._fld_in_model('res.city', f)
        do_search = False
        if tbl_f:
            do_search = True
        elif hasattr(self, f):
            if self.pool.get(
                'res.country').browse(cr,
                                      uid,
                                      self.country_id).code == 'IT':
                do_search = True
        return do_search

    def fill_geoloc(self, cr, uid, ids, name, value, context=None):
        """Set values of geolocalization from country, zip, city and
        other fields.
        Context:
        DoFill => fill field `name` too"""
        context = context or {}
        self._set_flds_list()
        fix, is_updated, do_fill = self._init_local_vars(cr, uid,
                                                         name,
                                                         value,
                                                         context)
        # prepare city 'where condition'
        where, where_valid = self._build_where(name, fix)
        do_search = self._do_search(cr, uid)
        if do_fill:
            res = {}
        else:
            res = {name: value}
        if do_fill or (do_search and is_updated and where_valid):
            city_ids = self.pool['res.city'].search(cr, uid, where)
            if not len(city_ids):
                city_ids = self._search_level2(cr, uid, name, value, where)
            if not len(city_ids) and do_search:
                city_ids = self._search_level3(cr, uid, name, value, where)
            if not len(city_ids) and do_search:
                city_ids = self._search_level4(cr, uid, name, value, where)
            if len(city_ids) and len(city_ids) < ACCEPT_MAX_RES:
                city = self.pool['res.city'].browse(cr, uid, city_ids[0])
                for f in self.flds_all:
                    res_f = self._fld_in_model('res.partner', f)
                    tbl_f = self._fld_in_model('res.city', f)
                    if tbl_f and hasattr(city, tbl_f):
                        if f[-3:] == '_id':
                            if not hasattr(self, f) or \
                                    fix[f] or len(city_ids) == 1:
                                res[res_f] = getattr(city, tbl_f).id
                                if f == 'state_id':
                                    fix = self._clear_field('province_id',
                                                            fix)
                                elif f == 'province_id':
                                    fix = self._clear_field('state_id',
                                                            fix)
                        else:
                            x = getattr(city, tbl_f)
                            if (x and x.find('%') >= 0) and f == 'zip':
                                x = x.replace('%', '0')
                            if (((f == 'city'
                                    and isinstance(value, basestring)
                                    and value.find('.') >= 0)
                                    or f != name) and
                                    (not hasattr(self, f) or
                                     (fix[f] and len(city_ids) == 1))):
                                res[res_f] = x
                    elif f == 'country_id' and res_f and hasattr(self, f):
                        res[res_f] = getattr(self, f)
                    if res_f in res:
                        setattr(self, f, res[res_f])
                f = 'country_id'
                tbl_f = self._fld_in_model('res.city', f)
                if not tbl_f and fix[f] and f not in res:
                    res[f] = getattr(self, f)
                if hasattr(self, 'city') and hasattr(self, 'state_id'):
                    self._store_lazy_city(cr, uid, name)
        for f in ('province_id', 'state_id', 'region_id'):
            f1 = 'province_id' if f != 'province_id' else 'state_id'
            tbl_f = self._fld_in_model('res.city', f)
            if not tbl_f:
                id = self._inherit_field(cr, uid, f, f1, fix)
                self._set_field(fix, f, id)
                res_f = self._fld_in_model('res.partner', f)
                if fix[f] and res_f not in res and hasattr(self, f):
                    res[res_f] = getattr(self, f)
        if 'value' not in res:
            res = {'value': res}
        if context.get('DoWrite', False):
            for f in self.flds_all:
                fix = self._clear_field(f, fix)
        return res


class res_partner(orm.Model):
    _inherit = 'res.partner'

    _columns = {
        'province': fields.many2one('res.province', string='Province'),
        'region': fields.many2one('res.region', string='Region'),
        'province_code': fields.related(
            'province', 'code', type='char',
            size=2, string='Province code'),
    }

    def on_change_country(self, cr, uid, ids,
                          country_id, zip, city, state_id, context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.fill_geoloc(cr, uid, ids, 'country_id', country_id,
                                      context=context)

    def on_change_zip(self, cr, uid, ids,
                      country_id, zip, city, state_id, context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.fill_geoloc(cr, uid, ids, 'zip', zip,
                                      context=context)

    def on_change_state(self, cr, uid, ids,
                        country_id, zip, city, state_id, context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.fill_geoloc(cr, uid, ids, 'state_id', state_id,
                                      context=context)

    def on_change_city(self, cr, uid, ids,
                       country_id, zip, city, state_id, context=None):
        context = self.new_ctx(country_id, zip, city, state_id,
                               context=context)
        config_obj = self.pool.get('res.config.settings')
        return config_obj.fill_geoloc(cr, uid, ids, 'city', city,
                                      context=context)

    def new_ctx(self,
                country_id, zip, city, state_id, context=None):
        context = context or {}
        if country_id:
            if isinstance(country_id, (int, long)):
                context['country_id'] = country_id
            else:
                context['country_id'] = country_id.id
        if zip:
            context['zip'] = zip
        if city:
            context['city'] = city
        if state_id:
            if isinstance(state_id, (int, long)):
                context['state_id'] = state_id
            else:
                context['state_id'] = state_id.id
        return context

    def _set_vals_city_data(self, cr, uid, vals):
        context = self.new_ctx(vals.get('country_id', None),
                               vals.get('zip', None),
                               vals.get('city', None),
                               vals.get('state_id', None),
                               context={'DoWrite': True})
        config_obj = self.pool.get('res.config.settings')
        for f in ('city', 'zip'):
            if f in vals:
                res = config_obj.fill_geoloc(cr, uid, [],
                                             f, vals[f],
                                             context=context)
                if 'value' in res:
                    res = res['value']
                    for f in ('country_id', 'zip', 'city',
                              'province_id', 'state_id', 'region_id',
                              'province', 'region'):
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

    def _fill_fields(self, cr, uid, id):
        partner = self.browse(cr, uid, id)
        context = self.new_ctx(partner.country_id,
                               partner.zip,
                               partner.city,
                               partner.state_id,
                               context={'DoFill': True})
        config_obj = self.pool.get('res.config.settings')
        res = config_obj.fill_geoloc(cr, uid, [],
                                     'city', False,
                                     context=context)
        vals = res['value']
        return super(res_partner, self).write(cr, uid, [id], vals, context)

    # Function compatible with old l10n_it_base
    def create(self, cr, uid, vals, context=None):
        # In order to debug old version records
        if vals.get('name', False) != 'John Doe' or \
                vals.get('city', False) != 'Torino':
            vals = self._set_vals_city_data(cr, uid, vals)
        return super(res_partner, self).create(cr, uid, vals, context)

    # Function compatible with old l10n_it_base
    def write(self, cr, uid, ids, vals, context=None):
        vals = self._set_vals_city_data(cr, uid, vals)
        return super(res_partner, self).write(cr, uid, ids, vals, context)

    def fill_fields(self, cr, uid, ids, context=None):
        """Write record filling address empty fields
        May be called by button"""
        if isinstance(ids, list):
            for id in ids:
                return self._fill_fields(cr, uid, id)
        else:
            return self._fill_fields(cr, uid, ids)

    def button_complete_addr(self, cr, uid, ids, context=None):
        self.fill_fields(cr, uid, ids, context)
