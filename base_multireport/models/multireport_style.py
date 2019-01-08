# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class MultireportStyle(models.Model):
    _name = "multireport.style"
    _description = "Multi Report Document Style"

    name = fields.Char(
        'Name of model',
        required=True,
        help="Give a unique name for this report style")
    origin = fields.Selection(
        [('odoo', 'Original Odoo Model'),
         ('odoo_based', 'Odoo based Model'),
         ('vg7', 'VG7 Model')],
        'Report origin/indentity',
        required=True,
        help="Original report",
        default='odoo')
