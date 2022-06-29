# Copyright 2021-22 LibrERP enterprise network <https://www.librerp.it>
# Copyright 2021-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2021-22 Didotech s.r.l. <https://www.didotech.com>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).
from odoo import models, fields, api
import odoo.addons.decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    amount_net_pay = fields.Float(string='Net to pay',
                                  store=True,
                                  digits=dp.get_precision('Account'),
                                  readonly=True,
                                  compute='_compute_net_pay')

    @api.depends('amount_total')
    def _compute_net_pay(self):
        for inv in self:
            amount_sp = inv.amount_sp if hasattr(inv, "amount_sp") else 0.0
            withholding_tax_amount = inv.withholding_tax_amount if hasattr(
                inv, "withholding_tax_amount") else 0.0
            if not inv.amount_net_pay:
                inv.amount_net_pay = (
                    inv.amount_total + amount_sp - withholding_tax_amount
                )
