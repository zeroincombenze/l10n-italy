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

    # pdf_model = fields.Many2one(
    #     'multireport.model',
    #     'Quote/Order Report',
    #     help="Select Report to use when printing the Sales Order or Quote"
    # )

    # Override print_quotation method in sale module
    @api.multi
    def print_quotation(self):
        # import pdb
        # pdb.set_trace()
        # paper_format_model = self.env['report.paperformat']
        # paper_format = paper_format_model.browse(
        #     self.env.ref('base_multireport.paperformat_sale_order'))
        # return super(SaleOrder, self).print_quotation()
        self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        reportname = self.env['report'].select_reportname(self)
        return self.env['report'].get_action(
             self, reportname)
