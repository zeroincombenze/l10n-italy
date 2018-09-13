# -*- coding: utf-8 -*-
# Copyright 2018 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                  Associazione Odoo Italia <http://www.odoo-italia.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#

from odoo import models, fields


class AccountTax(models.Model):
    _inherit = 'account.tax'

    non_taxable_nature = fields.Selection([
        ('N1', 'escluse ex art. 15'),
        ('N2', 'non soggette'),
        ('N3', 'non imponibili'),
        ('N4', 'esenti'),
        ('N5', 'regime del margine/IVA non esposta'),
        ('N6', 'inversione contabile (acq. in reverse charge)'),
        ('N7', 'IVA assolta in altro stato UE'),
        ('FC', 'FC applicazione IVA'),
        ], string="Non taxable nature")
    payability = fields.Selection([
        ('I', 'Immediate payability'),
        ('D', 'Deferred payability'),
        ('S', 'Split payment'),
        ], string="VAT payability",
        default='I')
    law_reference = fields.Char(
        'Law reference', size=128)
