# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class ItalyAdeCodiceCarica(orm.Model):
    _name = 'italy.ade.codice.carica'
    _description = 'Codice Carica'

    _sql_constraints = [('code',
                         'unique(code)',
                         'Code already exists!')]

    _columns = {
        'code': fields.char(string='Code', size=2,
                            help='Code assigned by Tax Authority'),
        'name': fields.char(string='Name'),
        'help': fields.text(string='Help'),
        'scope': fields.char(string='Scope',
                             help='Reserved to specific scope'),
        'active': fields.boolean(string='Active')
    }
    _default = {
        'active': True
    }
