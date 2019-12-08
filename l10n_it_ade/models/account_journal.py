# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class AccountJournal(orm.Model):
    _inherit = "account.journal"

    _columns = {
        'rev_charge': fields.boolean(
            'Reverse Charge Journal',
            help="Check if reverse charge EU invoices journal"),
        'anom_sale_receipts': fields.boolean(
            'Anonimous sale receipts journal',
            help="Check if this is the Anonimous Sale Receipts Journal"),
        'proforma': fields.boolean(
            'Proforma journal',
            help="Check if this is a Proforma Journal"),
        'einvoice': fields.boolean(
            'E-Invoice journal',
            help="Check if this is a E-Invoice Journal"),
    }

    _defaults = {
        'rev_charge': False,
        'anom_sale_receipts': False,
        'proforma': False,
        'einvoice': False,
    }

    # @api.onchange('rev_charge', 'anom_sale_receipts', 'proforma', 'einvoice')
    def onchange_check_subtype(self, cr, uid, ids, name,
                               jtype, rev_charge, anom_sale_receipts, proforma,
                               einvoice, context=None):
        res = {'value': {}}
        for p in ('rev_charge', 'anom_sale_receipts', 'proforma', 'einvoice'):
            if p != name:
                res['value'][p] = False
        if ((name =='rev_charge' and rev_charge) or
                (name == 'anom_sale_receipts' and anom_sale_receipts)):
            if jtype != 'sale':
                res = {'value': {name: False},
                        'warning': {
                    'title': 'Invalid setting!',
                    'message': 'Journal type must be sale'}
                }
        elif ((name == 'proforma' and proforma) or
              (name == 'einvoice' and einvoice)):
            if jtype not in ('purchase', 'sale'):
                res = {'value': {name: False},
                        'warning': {
                    'title': 'Invalid setting!',
                    'message': 'Journal type must be sale or purchase'}
                }
        return res
