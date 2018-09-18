# -*- coding: utf-8 -*-
#    Copyright (C) 2010-17 Associazione Odoo Italia
#                          <http://www.odoo-italia.org>
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2010: odoo-italia] First version
# [2017: SHS-AV, odoo-italia] Totally rewritten
from openerp.osv import orm


class account_invoice(orm.Model):
    _inherit = 'account.invoice'

    def _check_4_inv_date(self, cr, uid, ids, context=None):
        res = True
        for obj_inv in self.browse(cr, uid, ids, context=context):
            if obj_inv.journal_id.proforma:
                continue
            inv_type = obj_inv.type
            if inv_type == 'in_invoice' or inv_type == 'in_refund':
                date_invoice = obj_inv.registration_date
                res = self._invoice_validate(cr, uid, obj_inv, date_invoice,
                                             context=context)
            elif inv_type == 'out_invoice' or inv_type == 'out_refund':
                date_invoice = obj_inv.date_invoice
                res = self._invoice_validate(cr, uid, obj_inv, date_invoice,
                                             context=context)
            if not res:
                break
        return res

    def _invoice_validate(self, cr, uid, obj_inv, date_invoice, context=None):
        if date_invoice and obj_inv.state == 'draft':
            where = [('type', '=', obj_inv.type),
                     ('journal_id', '=', obj_inv.journal_id.id),
                     ('date_invoice', '>', date_invoice),
                     ('state', '!=', 'draft'),
                     ('state', '!=', 'cancel'),
                     ]
            if obj_inv.period_id:
                period_pool = self.pool.get('account.period')
                # fy_pool = self.pool.get('account.fiscalyear')
                fiscalyear_id = period_pool.browse(
                    cr, uid, obj_inv.period_id.id).fiscalyear_id.id
                periods = period_pool.search(
                    cr, uid, [('fiscalyear_id', '=', fiscalyear_id)])
                where.append(('period_id', 'in', periods))
            number = obj_inv.internal_number
            if number:
                where.append(('number', '<', number))
            res = self.search(cr, uid, where, context=context)
            if res:
                return False
        return True

    _constraints = [(
        _check_4_inv_date,
        'Cannot create invoice! Post the invoice with a greater date',
        ['date_invoice', 'registration_date'])]

    def copy(self, cr, uid, id, default=None, context=None):
        default = default or {}
        default.update({
            'registration_date': False,
        })
        return super(account_invoice, self).copy(cr, uid, id, default, context)
