# -*- coding: utf-8 -*-

from openerp.osv import orm, api


class WizardSetInvoiceType(orm.TransientModel):
    _name = "wizard.set.invoice.type"

    @api.multi
    def set_einvoice_type(self):
        self.ensure_one()
        invoices = self.env[self.env.context['active_model']].browse(
            self.env.context['active_ids'])
        return invoices.set_einvoice_type()

