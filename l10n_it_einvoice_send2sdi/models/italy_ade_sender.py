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


class ItalyAdeSender(models.Model):
    _inherit = 'italy.ade.sender'

    max_invoices_ctr = fields.Integer(
        string='Max invoices',
        readonly=True,
        help="Total # of invoices to send or receive")
    used_invoices_ctr = fields.Integer(
        string='Sent/Received invoices',
        readonly=True,
        help="Total # of invoices sent and received")
    avail_invoices_ctr = fields.Integer(
        string='# of invoices available',
        readonly=True,
        help="Total # of invoices you can still send or receive")