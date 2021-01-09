# -*- coding: utf-8 -*-
#
# Copyright 2019-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import fields, models, api
import odoo.addons.decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    conai_exemption_id = fields.Many2one(
        'italy.conai.partner.category', string='CONAI Exemption')
    amount_goods_service = fields.Monetary(
        string='Goods & Service Amount',
        currency_field='company_currency_id',
        store=True, readonly=True)
    amount_conai = fields.Monetary(string='CONAI Amount',
                                   currency_field='company_currency_id',
                                   store=True, readonly=True)

    @api.multi
    def action_move_create(self):
        inv_line_model = self.env['account.invoice.line']
        for invoice in self:
            if invoice.type in ('in_invoice', 'in_refund'):
                continue
            conai_struct = {}
            if (invoice.conai_exemption_id and
                    invoice.conai_exemption_id.conai_percent):
                percent = invoice.conai_exemption_id.conai_percent
                p_name = invoice.conai_exemption_id.name
                ii = p_name.lower().find('vs')
                if ii >= 0:
                    p_name = p_name[ii:]
                p_name = 'Esenzione %s%% %s' % (percent, p_name)
            else:
                percent = 0.0
                p_name = ''
            supplemental_line_ids = []
            for line in invoice.invoice_line_ids:
                if line.name.startswith('Contributo ambientale'):
                    supplemental_line_ids.append(line.id)
                    continue
                if not line.conai_category_id:
                    continue
                conai_category = line.conai_category_id
                weight_conv, uom = conai_category.evaluate_weight_conv()
                if conai_category not in conai_struct:
                    conai = {}
                    conai['name'] = conai_category.name
                    conai['weight'] = 0.0
                    conai['um'] = uom
                    conai['price'] = conai_category.get_price()
                    conai['amount'] = 0.0
                    conai['account_id'] = conai_category.account_id.id
                    if not conai['account_id']:
                        conai[ 'account_id'] = line.account_id.id
                    conai['tax'] = line.invoice_line_tax_ids
                    conai_struct[conai_category] = conai
                if not line.weight and line.product_id:
                    line.weight = (
                            (line.product_id.weight or
                             line.product_id.product_tmpl_id.weight) *
                            line.quantity)
                conai_amount = conai_category.evaluate_conai_amount(
                    line.weight)
                conai_struct[conai_category]['amount'] = conai_amount
                line.write({'conai_amount': conai_amount,
                            'weight': line.weight})
                conai_struct[conai_category]['weight'] += line.weight
            invoice.amount_conai = 0.0
            for nr, conai_category in enumerate(conai_struct):
                if p_name:
                    conai_name = 'Contributo ambientale %s (%s %s)\n%s' % (
                        conai_struct[conai_category]['name'],
                        conai_struct[conai_category]['weight'],
                        conai_struct[conai_category]['um'].name,
                        p_name)
                else:
                    conai_name = 'Contributo ambientale %s (%s %s)' % (
                        conai_struct[conai_category]['name'],
                        conai_struct[conai_category]['weight'],
                        conai_struct[conai_category]['um'].name)
                line_vals = {
                    'name': conai_name,
                    'invoice_id': invoice.id,
                    'uom_id': conai_struct[conai_category]['um'].id,
                    'quantity': conai_category.get_qty(
                        conai_struct[conai_category]['weight'],
                        percent=percent),
                    'price_unit': conai_struct[conai_category]['price'],
                    'account_id': conai_struct[conai_category]['account_id'],
                    'invoice_line_tax_ids': [
                        (6, 0,
                         [x.id for x in conai_struct[conai_category]['tax']])],
                    'sequence': 99999,
                }
                if nr < len(supplemental_line_ids):
                    inv_line_model.browse(
                        supplemental_line_ids[nr]).write(line_vals)
                    inv_line = inv_line_model.browse(
                        supplemental_line_ids[nr])
                else:
                    inv_line = inv_line_model.create(line_vals)
                invoice.amount_conai += inv_line.price_subtotal
            nr = len(conai_struct)
            while nr < len(supplemental_line_ids):
                inv_line_model.browse(
                    supplemental_line_ids[nr]).unlink()
                nr += 1
            invoice.amount_goods_service = (
                    invoice.amount_untaxed - invoice.amount_conai)
            if len(conai_struct):
                invoice.compute_taxes()
        return super(AccountInvoice, self).action_move_create()


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    date_invoice = fields.Date(
        string='Date',
        related='invoice_id.date_invoice', store=True, readonly=True)
    conai_category_id = fields.Many2one(
        'italy.conai.product.category', string='CONAI Category')
    conai_amount = fields.Float(
        string='CONAI Amount',
        digits=dp.get_precision('Product Price'))
    conai_exemption_id = fields.Many2one(
        string='CONAI Exemption',
        related='invoice_id.conai_exemption_id', store=True, readonly=True)

    @api.multi
    @api.onchange('product_id')
    def _set_conai_category(self):
        if self.product_id:
            if self.product_id.conai_category_id:
                self.conai_category_id = self.product_id.conai_category_id.id
            elif self.product_id.product_tmpl_id.conai_category_id:
                self.conai_category_id = \
                    self.product_id.product_tmpl_id.conai_category_id.id
            self.evaluate_conai_amount()

    @api.multi
    @api.onchange('quantity')
    def _set_conai_amount(self):
        self.evaluate_conai_amount()

    @api.model
    def evaluate_conai_amount(self):
        if not self.weight and self.product_id and self.quantity:
            self.weight = (
                    (self.product_id.weight or
                     self.product_id.product_tmpl_id.weight) *
                    self.quantity)
        if self.weight and self.conai_category_id:
            self.conai_amount = self.conai_category_id.evaluate_conai_amount(
                self.weight)

    @api.model
    def create(self, vals):
        if 'conai_category_id' not in vals and 'product_id' in vals:
            weight = vals.get('weight', 0.0)
            conai_category_id = False
            product = self.env['product.product'].browse(vals['product_id'])
            if product.conai_category_id:
                conai_category_id = product.conai_category_id.id
                if not weight:
                    weight = product.weight
            else:
                if (product.product_tmpl_id and
                        product.product_tmpl_id.conai_category_id):
                    conai_category_id = \
                        product.product_tmpl_id.conai_category_id.id
                    if not weight:
                        weight = product.weight
            if conai_category_id:
                vals['conai_category_id'] = conai_category_id
            if weight:
                vals['weight'] = weight
        return super(AccountInvoiceLine, self).create(vals)
