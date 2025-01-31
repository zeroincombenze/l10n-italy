# -*- coding: utf-8 -*-
#
# Copyright 2016-22 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import api, models


class SaleOrder(models.Model):
    _inherit = ["sale.order"]

    # Override print_quotation method in sale module
    @api.multi
    def print_quotation(self):
        action = super(SaleOrder, self).print_quotation()
        reportname = self.env["report"].select_reportname(self)
        if reportname:
            action["reportname"] = reportname
        return action
