# -*- coding: utf-8 -*-

from openerp.osv import orm
# from openerp.exceptions import Warning as UserError


class WizardSetInvoiceCommyype(orm.TransientModel):
    _name = "wizard.set.invoice.commtype"

    def set_einvoice_commtype(self, cr, uid, ids, context=None):
        context = context or {}
        # invoices = self.env[self.env.context['active_model']].browse(
        #     self.env.context['active_ids'])
        return self.pool['account.invoice'].set_einvoice_commtype(
            cr, uid, context.get('active_ids', []))

