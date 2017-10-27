# -*- coding: utf-8 -*-
# Copyright 2012, Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2012, Domsense srl (<http://www.domsense.com>)
# Copyright 2017, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2012-2017, Associazione Odoo Italia <https://odoo-italia.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm
from openerp.tools.translate import _


class AccountConfigSettings(orm.TransientModel):
    _inherit = 'account.config.settings'
    _columns = {
        'withholding_payment_term_id': fields.related(
            'company_id', 'withholding_payment_term_id',
            type='many2one',
            relation="account.payment.term",
            string="Withholding tax Payment Term"),
        'withholding_account_id': fields.related(
            'company_id', 'withholding_account_id',
            type='many2one',
            relation="account.account",
            string="Withholding account",
            help='Payable account used for amount due to tax authority',
            domain=[('type', '=', 'payable')]),
        'withholding_journal_id': fields.related(
            'company_id', 'withholding_journal_id',
            type='many2one',
            relation="account.journal",
            string="Withholding journal",
            help='Journal used for registration of witholding amounts to be '
                 'paid'),
        # 'authority_partner_id': fields.related(
        #     'company_id', 'authority_partner_id',
        #     type='many2one',
        #     relation="res.partner",
        #     string="Tax Authority Partner"),
    }

    def onchange_company_id(self, cr, uid, ids, company_id, context=None):
        res = super(AccountConfigSettings, self).onchange_company_id(
            cr, uid, ids, company_id, context=context)
        if company_id:
            company = self.pool.get('res.company').browse(
                cr, uid, company_id, context=context)
            res['value'].update({
                'withholding_payment_term_id': (
                    company.withholding_payment_term_id and
                    company.withholding_payment_term_id.id or False),
                'withholding_account_id': (
                    company.withholding_account_id and
                    company.withholding_account_id.id or False),
                'withholding_journal_id': (
                    company.withholding_journal_id and
                    company.withholding_journal_id.id or False),
                # 'authority_partner_id': (
                #     company.authority_partner_id and
                #     company.authority_partner_id.id or False),
            })
        else:
            res['value'].update({
                'withholding_payment_term_id': False,
                'withholding_account_id': False,
                'withholding_journal_id': False,
                # 'authority_partner_id': False,
            })
        return res


class AccountVoucher(orm.Model):
    _inherit = "account.voucher"

    _columns = {
        'withholding_move_ids': fields.many2many(
            'account.move', 'voucher_withholding_move_rel', 'voucher_id',
            'move_id', 'Withholding Tax Entries', readonly=True),
    }

    def reconcile_withholding_move(
        self, cr, uid, invoice, wh_move, context=None
    ):
        line_pool = self.pool.get('account.move.line')
        rec_ids = []
        for inv_move_line in invoice.move_id.line_id:
            if (
                inv_move_line.account_id.type == 'payable' and
                not inv_move_line.reconcile_id
            ):
                rec_ids.append(inv_move_line.id)
        for wh_line in wh_move.line_id:
            if (
                wh_line.account_id.type == 'payable' and
                invoice.company_id.withholding_account_id and
                invoice.company_id.withholding_account_id.id !=
                wh_line.account_id.id and
                not wh_line.reconcile_id
            ):
                rec_ids.append(wh_line.id)
        return line_pool.reconcile_partial(
            cr, uid, rec_ids, type='auto', context=context)

    def action_move_line_create(self, cr, uid, ids, context=None):
        res = super(AccountVoucher, self).action_move_line_create(
            cr, uid, ids, context)
        inv_pool = self.pool.get('account.invoice')
        move_pool = self.pool.get('account.move')
        curr_pool = self.pool.get('res.currency')
        term_pool = self.pool.get('account.payment.term')
        priod_obj = self.pool.get('account.period')
        for voucher in self.browse(cr, uid, ids, context):
            amounts_by_invoice = super(
                AccountVoucher, self).allocated_amounts_grouped_by_invoice(
                    cr, uid, voucher, context)
            for inv_id in amounts_by_invoice:
                invoice = inv_pool.browse(cr, uid, inv_id, context)
                if invoice.withholding_amount:
                    # only for supplier payments
                    if voucher.type != 'payment':
                        raise orm.except_orm(
                            _('Error'),
                            _('Can\'t handle withholding tax with voucher of '
                              'type other than payment'))
                    if not invoice.company_id.withholding_account_id:
                        raise orm.except_orm(
                            _('Error'),
                            _('The company does not have an associated '
                              'Withholding account'))
                    if not invoice.company_id.withholding_payment_term_id:
                        raise orm.except_orm(
                            _('Error'),
                            _('The company does not have an associated '
                              'Withholding Payment Term'))
                    if not invoice.company_id.withholding_journal_id:
                        raise orm.except_orm(
                            _('Error'),
                            _('The company does not have an associated '
                              'Withholding journal'))
                    # if not invoice.company_id.authority_partner_id:
                    #     raise orm.except_orm(
                    #         _('Error'),
                    #         _('The company does not have an associated Tax '
                    #           'Authority partner'))
                    # compute the new amount proportionally to paid amount
                    new_line_amount = curr_pool.round(
                        cr, uid, voucher.company_id.currency_id,
                        ((
                            amounts_by_invoice[invoice.id]['allocated'] +
                            amounts_by_invoice[invoice.id]['write-off']
                        ) / invoice.net_pay) * invoice.withholding_amount)

                    # compute the due date
                    due_list = term_pool.compute(
                        cr, uid,
                        invoice.company_id.withholding_payment_term_id.id,
                        new_line_amount,
                        date_ref=voucher.date or invoice.date_invoice,
                        context=context)
                    if len(due_list) > 1:
                        raise orm.except_orm(
                            _('Error'),
                            _('The payment term %s has too many due dates')
                            % invoice.company_id.withholding_payment_term_id.
                            name)
                    if len(due_list) == 0:
                        raise orm.except_orm(
                            _('Error'),
                            _('The payment term %s does not have due dates')
                            % invoice.company_id.withholding_payment_term_id.
                            name)

                    period_ids = priod_obj.find(
                        cr, uid, dt=voucher.date, context=context)
                    new_move = {
                        'journal_id': (
                            invoice.company_id.
                            withholding_journal_id.id),
                        'period_id': period_ids and period_ids[0] or False,
                        'date': voucher.date,
                        'line_id': [
                            (0, 0, {
                                'name': invoice.number,
                                'account_id': invoice.account_id.id,
                                'partner_id': invoice.partner_id.id,
                                'debit': new_line_amount,
                                'credit': 0.0,
                            }),
                            (0, 0, {
                                'name': _(
                                    'Payable withholding - ') + invoice.number,
                                'account_id': (
                                    invoice.company_id.
                                    withholding_account_id.id),
                                'partner_id': invoice.partner_id.id,
                                # 'partner_id': (
                                #     invoice.company_id.
                                #     authority_partner_id.id),
                                'debit': 0.0,
                                'credit': new_line_amount,
                                'date_maturity': due_list[0][0],
                            }),
                        ]
                    }
                    move_id = self.pool.get('account.move').create(
                        cr, uid, new_move, context=context)
                    self.reconcile_withholding_move(
                        cr, uid, invoice, move_pool.browse(
                            cr, uid, move_id, context), context)
                    voucher.write({'withholding_move_ids': [(4, move_id)]})
        return res

    def cancel_voucher(self, cr, uid, ids, context=None):
        res = super(AccountVoucher, self).cancel_voucher(
            cr, uid, ids, context)
        move_pool = self.pool.get('account.move')
        for voucher in self.browse(cr, uid, ids, context=context):
            for move in voucher.withholding_move_ids:
                move_pool.button_cancel(cr, uid, [move.id])
                move_pool.unlink(cr, uid, [move.id])
        return res
