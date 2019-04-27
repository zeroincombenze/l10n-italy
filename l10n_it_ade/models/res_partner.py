# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    def wep_fiscalcode(self, fc):
        if fc:
            return fc.replace(
                ' ', '').replace('.', '').replace('-', '').upper()
        return fc

    def wep_vat(self, vat):
        if vat and vat[0:2].upper() == 'IT':
            return self.wep_fiscalcode(vat)
        return vat

    def split_vat_n_country(self, vat):
        '''Split iso code & vat number from odoo vat.
        If vat starts with IT8 or IT9 return empty vat number
        because it is actually an fiscal code'''
        if vat:
            vat = self.wep_vat(vat)
            if vat[0:3] != 'IT9' and vat[0:3] != 'IT8':
                country_code = vat[0:2]
                vat_number = vat[2:]
            else:
                country_code = ''
                vat_number = ''
        else:
            country_code = ''
            vat_number = ''
        return country_code, vat_number
