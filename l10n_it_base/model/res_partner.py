# -*- coding: utf-8 -*-
#
# Copyright 2017-2018, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2010-2018, Associazione Odoo Italia <https://odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _build_where_city(self, level=None):
        level = level or 0
        where = []
        if self.country_id:
            where.append(('country_id', '=', self.country_id.id))
        if self.zip:
            zip = '%s%s' % (self.zip[0: len(self.zip) - level],
                            '%' * level)
            where.append(('zip', '=ilike', zip))
        return where

    def _build_where_stateid(self, state_id):
        where = []
        if self.country_id:
            where.append(('country_id', '=', self.country_id.id))
        where.append(('id', '=', state_id))
        return where

    def _onchange_addrflds(self):
        where = self._build_where_city()
        if where:
            city_ids = self.env['res.city'].search(where)
            if not city_ids:
                where = self._build_where_city(level=1)
                city_ids = self.env['res.city'].search(where)
            if not city_ids:
                where = self._build_where_city(level=2)
                city_ids = self.env['res.city'].search(where)
            if city_ids:
                city = self.env['res.city'].browse(city_ids[0].id)
                self.city = city.name
                where = self._build_where_stateid(city.state_id.id)
                stateid_ids = self.env['res.country.state'].search(where)
                if stateid_ids:
                    self.state_id = stateid_ids[0]

    @api.onchange('country_id')
    def onchange_country(self):
        return self._onchange_addrflds()

    @api.onchange('zip')
    def onchange_zip(self):
        return self._onchange_addrflds()

    @api.onchange('state_id')
    def onchange_state_id(self):
        return self._onchange_addrflds()
