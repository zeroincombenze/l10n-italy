# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class MultireportTemplate(models.Model):
    _name = "multireport.template"
    _description = "Multi Report Template"

    name = fields.Char(
        'Name of report template',
        required=True,
        help="Give a unique name for this report template")
    header_id = fields.Many2one(
        'ir.ui.view', 'Related header',
        required=True,
        domain=[('type', '=', 'qweb'),
                ('inherit_id', '=', False),
                ('name', 'like', 'header')],
        help="Name of header associated to this template")
    footer_id = fields.Many2one(
        'ir.ui.view', 'Related footer',
        required=True,
        domain=[('type', '=', 'qweb'),
                ('inherit_id', '=', False),
                ('name', 'like', 'footer')],
        help="Name of footer associated to this template")
