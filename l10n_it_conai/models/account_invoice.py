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
    def invoice_validate(self):
        self.ensure_one()
        conai_struct = {}
        if self.conai_exemption_id:
            p_rate = self.conai_exemption_id.conai_percent
        elif self.partner_id.conai_exemption_id:
            p_rate = self.partner_id.conai_exemption_id.conai_percent
        else:
            p_rate = 0
        p_rate = (100 - p_rate) / 100.0
        weight_conv = 1000
        supplemental_line_ids = []
        for line in self.invoice_line_ids:
            if line.name.startswith('Contributo ambientale'):
                supplemental_line_ids.append(line.id)
                continue
            conai_category_id = False
            if line.conai_category_id:
                conai_category_id = line.conai_category_id
            elif line.product_id:
                if line.product_id.conai_category_id:
                    conai_category_id = line.product_id.conai_category_id
                elif line.product_id.product_tmpl_id:
                    conai_category_id = \
                        line.product_id.product_tmpl_id.conai_category_id
            if conai_category_id and conai_category_id not in conai_struct:
                conai_struct[conai_category_id] = {}
                conai_struct[conai_category_id]['qty'] = 0.0
                if conai_category_id.conai_uom_id == self.env.ref(
                        'product.product_uom_ton'):
                    conai_struct[conai_category_id]['price'] = \
                        conai_category_id.conai_price_unit / weight_conv
                    conai_struct[conai_category_id]['um'] = 'Kg'
                else:
                    conai_struct[conai_category_id][
                        'price'] = conai_category_id.conai_price_unit
                    conai_struct[conai_category_id]['um'] = \
                        conai_category_id.conai_uom_id.name
                conai_struct[conai_category_id]['amount'] = 0.0
                conai_struct[conai_category_id][
                    'account_id'] = conai_category_id.account_id.id
                if not conai_struct[conai_category_id]['account_id']:
                    conai_struct[conai_category_id][
                        'account_id'] = line.account_id.id
                conai_struct[conai_category_id][
                    'tax'] = line.invoice_line_tax_ids
            if conai_category_id:
                if not line.weight and line.product_id:
                    line.weight = line.product_id.weight
                conai_struct[conai_category_id][
                    'name'] = conai_category_id.name
                conai_amount = (line.weight * line.quantity *  p_rate *
                                conai_struct[conai_category_id]['price'])
                conai_struct[conai_category_id][
                    'amount'] = conai_amount
                if conai_amount != line.conai_amount:
                    line.write({'conai_amount': conai_amount,
                                'weight': line.weight})
                conai_struct[conai_category_id]['qty'] += (
                        line.weight * line.quantity)
        self.amount_conai = 0.0
        for nr, line in enumerate(conai_struct):
            line_vals = {
                'name': 'Contributo ambientale %s (%s)' % (conai_struct[
                    line]['name'], conai_struct[line]['um']),
                'invoice_id': self.id,
                'quantity': conai_struct[line]['qty'],
                'price_unit': conai_struct[line]['price'] * p_rate,
                'account_id': conai_struct[line]['account_id'],
                'invoice_line_tax_ids': [(
                    6, 0, [x.id for x in conai_struct[line]['tax']])],
            }
            if nr < len(supplemental_line_ids):
                self.env['account.invoice.line'].browse(
                    supplemental_line_ids[nr]).write(line_vals)
            else:
                self.env['account.invoice.line'].create(line_vals)
            self.amount_conai += conai_struct[
                line]['price'] * p_rate * conai_struct[line]['qty']
        self.amount_goods_service = self.amount_untaxed - self.amount_conai
        return super(AccountInvoice, self).invoice_validate()


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
