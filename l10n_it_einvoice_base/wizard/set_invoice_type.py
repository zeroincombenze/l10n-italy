# -*- coding: utf-8 -*-

from odoo import models, api


class WizardSetInvoiceType(models.TransientModel):
    _name = "wizard.set.invoice.type"

    @api.multi
    def set_einvoice_type(self):
        self.ensure_one()
        invoices = self.env[self.env.context['active_model']].browse(
            self.env.context['active_ids'])
        return invoices.set_einvoice_type()
