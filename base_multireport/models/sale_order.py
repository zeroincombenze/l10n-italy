# -*- coding: utf-8 -*-
#
# Copyright 2016-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp import fields, models, api


class SaleOrder(models.Model):
    _inherit = ["sale.order"]


    # Override print_quotation method in sale module
    @api.multi
    def print_quotation(self):
        self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        reportname = self.env['report'].select_reportname(self)
        return self.env['report'].get_action(
             self, reportname)
