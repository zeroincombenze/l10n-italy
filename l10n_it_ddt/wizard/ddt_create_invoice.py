# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#

from odoo import fields, models, api, _


class DdtCreateInvoice(models.TransientModel):
    _name = "ddt.create.invoice"

    def _get_ddt_ids(self):
        return self.env['stock.picking.package.preparation'].browse(
            self.env.context['active_ids'])

    @api.model
    def _default_journal(self):
        return self.env['account.journal'].search([('type', '=', 'sale')],
                                                  order='id', limit=1)
    journal_id = fields.Many2one('account.journal', string='Journal',
                                 default=_default_journal,
                                 domain=[('type', '=', 'sale')])
    date_invoice = fields.Date(string='Invoice Date')
    ddt_ids = fields.Many2many(
        'stock.picking.package.preparation', default=_get_ddt_ids)

    @api.multi
    def create_invoice(self):
        self = self.with_context(
            invoice_date=self.date_invoice,
        )
        if self.ddt_ids:
            invoice_ids = self.ddt_ids.action_invoice_create()
            # ----- Show new invoices
            if invoice_ids:
                ir_model_data = self.env['ir.model.data']
                form_res = ir_model_data.get_object_reference(
                    'account', 'invoice_form')
                form_id = form_res and form_res[1] or False
                tree_res = ir_model_data.get_object_reference(
                    'account', 'invoice_tree')
                tree_id = tree_res and tree_res[1] or False
                return {
                    'name': _('Invoices from DDT'),
                    'view_type': 'form',
                    'view_mode': 'form,tree',
                    'res_model': 'account.invoice',
                    'domain': [('id', 'in', invoice_ids)],
                    # 'res_id': ddt.id,
                    'view_id': False,
                    'views': [(tree_id, 'tree'), (form_id, 'form')],
                    'type': 'ir.actions.act_window',
                }
