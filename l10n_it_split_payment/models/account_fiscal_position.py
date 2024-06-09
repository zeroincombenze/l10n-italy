# -*- coding: utf-8 -*-
# Copyright 2015    Davide Corio <davide.corio@abstract.it>
# Copyright 2015-16 Lorenzo Battistini - Agile Business Group
# Copyright 2016    Alessio Gerace - Agile Business Group
# Copyright 2018-22 Antonio M. Vigliotti - SHS-AV s.r.l.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountFiscalPosition(models.Model):
    _inherit = "account.fiscal.position"

    split_payment = fields.Boolean("Split Payment")
