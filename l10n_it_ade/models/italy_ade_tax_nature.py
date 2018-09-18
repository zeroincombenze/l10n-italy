# -*- coding: utf-8 -*-
#
# Copyright 2018 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2018 - Associazione Odoo Italia <http://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class ItalyAdeTaxNature(orm.Model):
    _name = 'italy.ade.tax.nature'
    _description = 'Tax Italian NAture'

    _sql_constraints = [('code', 
                         'unique(code)',
                         'Code already exists!')]

    _columns = {
        'code': fields.char(string='Code',
                       size=2),
        'name': fields.char(string='Name')
    }
