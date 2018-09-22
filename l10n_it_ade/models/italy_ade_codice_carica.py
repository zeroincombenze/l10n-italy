# -*- coding: utf-8 -*-
#
# Copyright 2018 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2018 - Associazione Odoo Italia <http://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by l10n_it_codice_carica OCA
#
from openerp.osv import fields, orm


class AdECodiceCarica(orm.Model):
    _name = 'italy.ade.codice.carica'
    _description = 'Codice Carica'

    _columns = {
        'code': fields.char(string='Code', size=2,
                            help='Code assigned by Tax Authority'),
        'name': fields.char(string='Name'),
        'help': fields.char(string='Help'),
        'scope': fields.char(string='Scope',
                             help='Reserved to specific scope'),
        'active': fields.boolean(string='Active')
    }
    _default = {
        'active': True
    }
