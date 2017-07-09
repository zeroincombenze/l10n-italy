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
        for obj_inv in self.browse(cr, uid, ids, context=context):
            inv_type = obj_inv.type
            if inv_type == 'in_invoice' or inv_type == 'in_refund':
                date_invoice = obj_inv.registration_date
                return self._invoice_validate(cr, uid, obj_inv, date_invoice,
                                                 context=context)
            elif inv_type == 'out_invoice' or inv_type == 'out_refund':
                date_invoice = obj_inv.date_invoice
                return self._invoice_validate(cr, uid, obj_inv, date_invoice,
                                                  context=context)
        return True

    def _invoice_validate(self, cr, uid, obj_inv, date_invoice, context=None):
        if date_invoice:
            where = [('type', '=', obj_inv.type),
                     ('journal_id', '=', obj_inv.journal_id.id),
                     ('date_invoice', '>', date_invoice),
                     ]
            number = obj_inv.number if obj_inv.number else \
                obj_inv.internal_number
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

