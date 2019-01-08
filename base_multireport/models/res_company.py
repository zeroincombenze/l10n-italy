# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    # custom_header = fields.Boolean('Custom Header')
    # cf_in_header = fields.Boolean(
    #     'Fiscalcode in Header',
    #     help='Print customer fiscalcode, after header vatnumber, if set')
    report_model_style = fields.Many2one(
        'multireport.style', 'Multi-report style',
        help="Select multi-report style",
        )


class ReportConfigSettings(models.TransientModel):
    _inherit = ["base.config.settings"]

    # custom_header = fields.Boolean(
    #     related='company_id.custom_header',
    #     string='Custom Header',
    #     help='Disable report standard header')
    # cf_in_header = fields.Boolean(
    #     related='company_id.cf_in_header',
    #     string='Fiscalcode in Header',
    #     help='Print customer fiscalcode, after header vatnumber, if set')
    report_model_style = fields.Many2one(
        related='company_id.report_model_style',
        string="Multi-report style",
        help='Select multi-report style'
        )


    # @api.onchange('company_id')
    # def onchange_company_id(self):
    #     # res = super(BaseConfigSettings, self).onchange_company_id()
    #     if self.company_id:
    #         company = self.company_id
    #         self.report_model_style = (
    #             company.report_model_style or False
    #             )
    #     else:
    #         self.report_model_style = False
    #     return True