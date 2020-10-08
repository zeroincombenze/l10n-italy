# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#

from odoo import fields, models, api, _


class DdtLineCreateInvoice(models.TransientModel):
    _name = "ddt.line.new.inv"

    def _get_line_ids(self):
        return self.env['stock.picking.package.preparation.line'].browse(
            self.env.context['active_ids'])

    def _get_partner_id(self):
        partner_id = False
        if self.env.context.get('active_ids'):
            for line in self._get_line_ids():
                if not partner_id:
                    partner_id = line.partner_id.id
                if line.partner_id.id != partner_id:
                    partner_id = False
                    break
        return partner_id

    line_ids = fields.Many2many(
        'stock.picking.package.preparation.line', default=_get_line_ids)
    invoice_id = fields.Many2one('account.invoice')
    partner_id = fields.Many2one('res.partner', default=_get_partner_id)

    @api.multi
    def create_invoice(self):
        if self.line_ids:
            invoice_ids = self.line_ids.action_line_invoice_create()
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

    def add_to_invoice(self):
        if self.line_ids and self.invoice_id:
            for line in self.line_ids:
                line.invoice_line_create(
                    self.invoice_id.id, line.product_uom_qty)
                self.invoice_id.invoice_line_ids = [
                    (4, line[0].invoice_line_id.id)]
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
                # 'domain': [('id', 'in', invoice_ids)],
                'res_id': self.invoice_id.id,
                'view_id': False,
                'views': [(tree_id, 'tree'), (form_id, 'form')],
                'type': 'ir.actions.act_window',
            }
