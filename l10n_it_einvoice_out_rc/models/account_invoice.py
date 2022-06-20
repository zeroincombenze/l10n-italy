# -*- coding: utf-8 -*-

from odoo import api, models, _
# from odoo.exceptions import UserError


class Invoice(models.Model):
    _inherit = "account.invoice"
