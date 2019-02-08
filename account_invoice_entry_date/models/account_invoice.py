# -*- coding: utf-8 -*-
#
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 ISA srl (<http://www.isa.it>).
#    Copyright (C) 2013 Associazione OpenERP Italia
#    http://www.openerp-italia.org>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import time
from odoo import fields
from odoo import models
from odoo.tools.translate import _


class account_invoice(models.Model):

    _inherit = 'account.invoice'
    registration_date = fields.Date(
        'Registration Date',
        states={
            'paid': [('readonly', True)],
            'open': [('readonly', True)],
            'close': [('readonly', True)]
        }, index=True, help="Keep empty to use the current date")

    def action_move_create(self):

        super(account_invoice, self).action_move_create()

        for inv in self.browse(self._ids):

            date_invoice = inv.date_invoice

            reg_date = inv.registration_date
            if not inv.registration_date:
                if not inv.date_invoice:
                    reg_date = time.strftime('%Y-%m-%d')
                else:
                    reg_date = inv.date_invoice

            if date_invoice and reg_date:
                if (date_invoice > reg_date):
                    raise models.except_orm(
                        _('Error date !'),
                        _('The invoice date cannot be later than the date of '
                          'registration!'))

            # periodo
            date_start = (
                inv.registration_date or inv.date_invoice or time.strftime(
                    '%Y-%m-%d'))
            date_stop = (
                inv.registration_date or inv.date_invoice or time.strftime(
                    '%Y-%m-%d'))

            # period_ids = self.env['account.period'].search(
            #     self._cr, self._uid, [
            #         ('date_start', '<=', date_start),
            #         ('date_stop', '>=', date_stop),
            #         ('company_id', '=', inv.company_id.id)
            #     ])
            # if period_ids:
            #     period_id = period_ids[0]

            self.write({'registration_date': reg_date})

            mov_date = reg_date or inv.date_invoice or time.strftime(
                '%Y-%m-%d')

            self.env['account.move'].write({'state': 'draft'})

            sql = "update account_move_line set date='" + mov_date + \
                "' where move_id = " + str(inv.move_id.id)

            self._cr.execute(sql)

            self.env['account.move'].write({'date': mov_date})

            self.env['account.move'].write({'state': 'posted'})

        # self._log_event(self._ids)
        return True
