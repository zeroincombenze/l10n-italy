#
# Copyright 2015    Davide Corio <davide.corio@abstract.it>
# Copyright 2015    Lorenzo Battistini - Agile Business Group
# Copyright 2016    Alessio Gerace - Agile Business Group
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'
    sp_account_id = fields.Many2one(
        'account.account',
        string='Split Payment Write-off Account',
        help='Account used to write off the VAT amount')
    sp_tax_id = fields.Many2one(
        'account.tax',
        string='Split Payment Write-off tax',
        help='Account used to write off the VAT amount')


class AccountConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sp_account_id = fields.Many2one(
        related='company_id.sp_account_id',
        string='Split Payment Write-off account',
        help='Account used to write off the VAT amount')
    sp_tax_id = fields.Many2one(
        related='company_id.sp_tax_id',
        string='Split Payment Write-off tax',
        help='Account used to write off the VAT amount')
