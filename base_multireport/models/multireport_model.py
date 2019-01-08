# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class MultireportModel(models.Model):
    _name = "multireport.model"
    _description = "Multi Report Document Model"

    name = fields.Char(
        'Name of model',
        required=True,
        help="Give a unique name for this report model")
    template_id = fields.Many2one(
        'multireport.template',
        'Report Template',
        required=True)
