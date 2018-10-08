#
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
# Code partially inherited by l10n_it_codice_carica OCA
#
from odoo import fields, models


class ItalyAdeTaxNature(models.Model):
    _name = 'italy.ade.tax.nature'
    _description = 'Tax Italian Nature'

    _sql_constraints = [('code',
                         'unique(code)',
                         'Code already exists!')]

    code = fields.Char(string='Code',
                       size=2)
    name = fields.Char(string='Name')
    help = fields.Char(string='Help')
    active = fields.Boolean(string='Active',
                            default=True)
