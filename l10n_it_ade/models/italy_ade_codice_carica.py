# -*- coding: utf-8 -*-
# Copyright 2018 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                  Associazione Odoo Italia <http://www.odoo-italia.org>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by l10n_it_codice_carica OCA
#
from odoo import _, api, fields, models


class ItalyAdeCodiceCarica(models.Model):
    _name = 'italy.ade.codice.carica'
    _description = 'Codice Carica'

    _sql_constraints = [('code',
                         'unique(code)',
                         'Code already exists!')]

    code = fields.Char(string='Code', size=2,
                       help='Code assigned by Tax Authority')
    name = fields.Char(string='Name')
    help = fields.Char(string='Help')
    scope = fields.Char(string='Scope',
                        help='Reserved to specific scope')
    active = fields.Boolean(string='Active',
                            default=True)
