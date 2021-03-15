# -*- coding: utf-8 -*-
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import api, models
# from odoo.tools.translate import _
# from odoo.exceptions import UserError


class WizardDefaultInvoiceRegistrationdate(models.TransientModel):
    _name = "wizard.default.invoice.registrationdate"
    _description = "Refresh registration date"

    @api.multi
    def action_set_registration_date(self):
        self.ensure_one()
        invoices = self.env[self.env.context['active_model']].browse(
            self.env.context['active_ids'])
        invoices.action_set_registration_date()

        return True
