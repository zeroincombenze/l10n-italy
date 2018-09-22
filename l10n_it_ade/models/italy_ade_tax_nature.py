# -*- coding: utf-8 -*-
#
# Copyright 2018 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2018 - Associazione Odoo Italia <http://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by l10n_it_codice_carica OCA
#
from odoo import _, api, fields, models


class ItalyAdeTaxNature(models.Model):
    _name = 'italy.ade.tax.nature'
    _description = 'Tax Italian Nature'

    _sql_constraints = [('code',
                         'unique(code)',
                         'Code already exists!')]

    code = fields.Char(string='Code',
                       size=2)
    name = fields.Char(string='Name')
