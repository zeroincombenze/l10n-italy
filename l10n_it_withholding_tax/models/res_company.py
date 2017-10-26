# -*- coding: utf-8 -*-
# Copyright 2012, Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2012, Domsense srl (<http://www.domsense.com>)
# Copyright 2017, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2012-2017, Associazione Odoo Italia <https://odoo-italia.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class ResCompany(orm.Model):
    _inherit = 'res.company'
    _columns = {
        'withholding_payment_term_id': fields.many2one(
            'account.payment.term',
            'Withholding tax Payment Term',
            help="The withholding tax will have to be paid within this term"),
        'withholding_account_id': fields.many2one(
            'account.account', 'Withholding account',
            help='Payable account used for amount due to tax authority',
            domain=[('type', '=', 'payable')]),
        'withholding_journal_id': fields.many2one(
            'account.journal', 'Withholding journal',
            help="Journal used for registration of witholding amounts to be "
                 "paid"),
        # 'authority_partner_id': fields.many2one(
        #     'res.partner', 'Tax Authority Partner'),
    }
