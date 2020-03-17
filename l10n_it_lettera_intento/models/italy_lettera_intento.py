# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from datetime import datetime
from odoo import models, fields, api


class ItalyLetteraIntento(models.Model):
    _name = 'italy.lettera.intento'

    @api.depends('plafond')
    def _used_plafond(self):
        for lett in self:
            if lett.partner_id and lett.company_id:
                partner_id = lett.partner_id.id
                company_id = lett.company_id.id
                query = '''SELECT SUM(credit) - SUM(debit)
                FROM account_move_line
                WHERE
                partner_id = %(partner_id)d AND
                company_id = %(company_id)d AND
                journal_id in (SELECT id FROM account_journal WHERE
                               type='sale' AND company_id=%(company_id)d) AND
                account_id in (SELECT id FROM account_account WHERE
                               internal_type='receivable') AND
                date >= '%(date)s'
                ''' % {
                    'company_id': company_id,
                    'partner_id': partner_id,
                    'date': lett.customer_date,
                }
                self.env.cr.execute(query)
                amount = -self.env.cr.fetchall()[0][0]
                lett.plafond_used = amount
                lett.plafond_avaiable = lett.plafond - amount

    name = fields.Char('Name', copy=False)
    date = fields.Date(string='Date')
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner')
    customer_ref = fields.Char('Customer Ref.')
    customer_date = fields.Date(string='Customer Date')
    currency_id = fields.Many2one(
        'res.currency', string='Currency',
        required=True,
        default=lambda self: self.env.user.company_id.currency_id)
    plafond = fields.Monetary(string='Plafond')
    plafond_used = fields.Monetary(string='Used Plafond',
                                   compute=_used_plafond)
    plafond_avaiable = fields.Monetary(string='Avaiable Plafond',
                                       compute=_used_plafond)

    @api.model
    def fiscal_pos_values(self, partner, partner_vals, lett):
        vals = {}
        for nm in ('customer_date', 'date'):
            vals[nm] = ''
            if partner_vals.get(nm):
                vals[nm] = datetime.strptime(partner_vals[nm],
                                             '%Y-%m-%d').strftime('%d-%m-%Y')
            elif lett:
                vals[nm] = datetime.strptime(lett[nm],
                                             '%Y-%m-%d').strftime('%d-%m-%Y')
        for nm in ('customer_ref', 'name'):
            vals[nm] = ''
            if partner_vals.get(nm):
                vals[nm] = partner_vals[nm]
            elif lett:
                vals[nm] = lett[nm]
        return {
            'name': 'Lettera intento %s' % partner.name,
            'company_id': partner.company_id.id,
            'note': 'Operazione senza IVA Vs. lettera d\'intento '
                    'n. %s del %s, ns. prot %s del %s' % (
                vals['customer_ref'],
                vals['customer_date'],
                vals['name'],
                vals['date']),
        }

    @api.model
    def create_fiscal_pos(self, partner, partner_vals):
        vals = self.fiscal_pos_values(partner, partner_vals, False)
        return self.env['account.fiscal.position'].create(vals)

    @api.model
    def write_fiscal_pos(self, fiscalpos, partner, partner_vals, lett):
        vals = self.fiscal_pos_values(partner, partner_vals, lett)
        return fiscalpos.write(vals)

    @api.model
    def set_fiscalpos_customer(self, vals, lett):
        partner = False
        if vals.get('partner_id'):
            partner = self.env['res.partner'].browse(int(vals['partner_id']))
        elif lett:
            partner = lett.partner_id
        if partner:
            fiscalpos = partner.property_account_position_id
            if not fiscalpos:
                fiscalpos = self.create_fiscal_pos(partner, vals)
                partner.write({
                    'property_account_position_id': fiscalpos.id}
                )
            else:
                self.write_fiscal_pos(
                    fiscalpos, partner, vals, lett)

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = self.env['ir.sequence'].with_context(
                force_company=vals['company_id']).next_by_code(
                'italy.lettera.intento')
        self.set_fiscalpos_customer(vals, False)
        return super(ItalyLetteraIntento, self).create(vals)

    @api.multi
    def write(self, vals):
        self.set_fiscalpos_customer(vals, self)
        return super(ItalyLetteraIntento, self).write(vals)
