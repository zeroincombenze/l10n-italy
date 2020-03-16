# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import fields, models


class AccountTax(models.Model):
    _inherit = 'account.tax'

    nature_id = fields.Many2one(
        'italy.ade.tax.nature',
        string='Nature',
        help='Nature of tax code: may be taxable, out of scope, etc ...')
    non_taxable_nature = fields.Selection([
        ('N1', 'escluse ex art. 15'),
        ('N2', 'non soggette'),
        ('N3', 'non imponibili'),
        ('N4', 'esenti'),
        ('N5', 'regime del margine/IVA non esposta'),
        ('N6', 'inversione contabile (acq. in reverse charge)'),
        ('N7', 'IVA assolta in altro stato UE'),
        ('FC', 'FC applicazione IVA'),
    ], string="Non taxable nature (*DEPRECATED*)")
    payability = fields.Selection([
        ('I', 'Immediate payability'),
        ('D', 'Deferred payability'),
        ('S', 'Split payment'),
    ], string="VAT payability",
        default='I')
    law_reference = fields.Char(
        'Law reference', size=128)
