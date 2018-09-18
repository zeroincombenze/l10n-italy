# -*- coding: utf-8 -*-
# Copyright 2017, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2017, Associazione Odoo Italia <https://odoo-italia.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import logging
from datetime import datetime

import decimal_precision as dp
from openerp import netsvc
from openerp.osv import fields, orm
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)
PAY_MOVE_STS_2_DRAFT = ['posted', ]
INVOICES_STS_2_DRAFT = ['open', 'paid']
STATES_2_DRAFT = ['open', 'paid', 'posted']


class account_invoice(orm.Model):
    _inherit = "account.invoice"

    def _net_pay(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for invoice in self.browse(cr, uid, ids, context):
            res[invoice.id] = invoice.amount_total - invoice.withholding_amount
        return res

    def _is_proforma(self, cr, uid, ids, fname, args, context=None):
        res = {}
        for inv in self.browse(cr, uid, ids, context=context):
            res[inv.id] = inv.journal_id and inv.journal_id.proforma
        return res

    _columns = {
        'withholding_amount': fields.float(
            'Withholding amount', digits_compute=dp.get_precision('Account'),
            readonly=True, states={'draft': [('readonly', False)]}),
        'has_withholding': fields.boolean(
            'With withholding tax', readonly=True,
            states={'draft': [('readonly', False)]}),
        'net_pay': fields.function(_net_pay, string="Net Pay"),
        'proforma': fields.function(
            _is_proforma,
            string="Proforma",
            type="boolean",
            multi=False,
            store=False,
            select=True,
            readonly=True),
    }

    def invoice_pay_customer(self, cr, uid, ids, context=None):
        res = super(account_invoice, self).invoice_pay_customer(
            cr, uid, ids, context=context)
        inv = self.browse(cr, uid, ids[0], context=context)
        if inv.has_withholding and \
                'context' in res and 'default_amount' in res['context']:
            pay_rate = inv.net_pay / inv.amount_total
            amount = res['context']['default_amount']
            amount = amount * pay_rate
            res['context']['default_amount'] = amount
        return res

    def get_payment_info(self, cr, uid, move_line):
        """Return move (header) and move_line (detail) ids of passed move line
        record and return payment state if needed to become draft
        """
        move_line_id = move_line.id
        move_id = move_line.move_id.id
        move = self.pool['account.move'].browse(cr, uid, move_id)
        mov_state = False
        if move.state in PAY_MOVE_STS_2_DRAFT:
            mov_state = move.state
        return move_id, move_line_id, mov_state

    def upd_invoices_2_post(self, cr, uid, move_dict):
        """Set invoices (header) list/dictionary to posted state.
        See upd_invoices_2_draft to set in draft state before execute this one.
        @ param move_dict: invoices (header) dictionary keyed on state or
                           invoices list to set in posted state
        """
        wf_service = netsvc.LocalService('workflow')
        for i, state in enumerate(INVOICES_STS_2_DRAFT):
            invoice_ids = []
            if isinstance(move_dict, dict):
                invoice_ids = move_dict[state]
            elif isinstance(move_dict, list) and i == 0:
                invoice_ids = move_dict
            if len(invoice_ids):
                for inv_id in invoice_ids:
                    self.button_compute(cr, uid, [inv_id])
                    try:
                        wf_service.trg_validate(uid, 'account.invoice',
                                                inv_id, 'invoice_open', cr)
                    except BaseException:
                        _logger.info(_('Cannot validate invoice %d') % inv_id)

    def upd_invoices_2_draft(self, cr, uid, move_dict):
        """Set invoices (header) list/dictionary to draft state.
        See upd_invoices_2_posted to return in posted state
        @ param move_dict: invoices (header) dictionary keyed on state or
                           invoices list to set in draft state
        """
        passed = []
        for i, state in enumerate(INVOICES_STS_2_DRAFT):
            invoice_ids = []
            if isinstance(move_dict, dict):
                invoice_ids = move_dict[state]
            elif isinstance(move_dict, list) and i == 0:
                invoice_ids = move_dict
            if len(invoice_ids):
                self.action_cancel(cr, uid, invoice_ids)
                # set 'draft' state to zero-amount invoices
                for inv_id in invoice_ids:
                    if self.browse(cr, uid, inv_id).state == 'paid':
                        try:
                            self.write(cr, uid, [inv_id],
                                       {'state': 'draft'})
                            passed.append(inv_id)
                        except BaseException:
                            pass
                invoice_ids = list(set(invoice_ids) - set(passed))
                self.action_cancel_draft(cr, uid, invoice_ids)

    def get_reconcile_from_inv(self, cr, uid, inv_id):
        """Return a list of reconciled move lines of passed (included) invoice
        List may be used to unreconcile all movements, set draft all of them,
        update something and then reconcile again all movements.
        If there no reconcile movements, returned list is empty
        @param inv_id: invoice (header) id
        @return: list of reconciled move lines of passed (included) invoice
        @return: dictionary of posted movements (header) to set to draft state
        """
        reconcile_ids = []
        move_dict = {}
        for state in STATES_2_DRAFT:
            move_dict[state] = []
        move_line_model = self.pool['account.move.line']
        invoice = self.browse(cr, uid, inv_id)
        if invoice.payment_ids:
            partner_id = invoice.partner_id.id
            move_id = invoice.move_id.id
            move_line_ids = move_line_model.search(
                cr, uid, [('move_id', '=', move_id),
                          ('partner_id', '=', partner_id)])
            for move_line_id in move_line_ids:
                account_id = move_line_model.browse(
                    cr, uid, move_line_id).account_id.id
                type = self.pool['account.account'].browse(
                    cr, uid, account_id).type
                if type in ('receivable', 'payable'):
                    reconcile_ids.append(move_line_id)
            for move_line in invoice.payment_ids:
                move_id, move_line_id, move_state = \
                    self.get_payment_info(cr, uid, move_line)
                reconcile_ids.append(move_line_id)
                if move_state:
                    move_dict[state].append(move_id)
        if invoice.state in INVOICES_STS_2_DRAFT:
            move_dict[invoice.state].append(inv_id)
        return reconcile_ids, move_dict

    def refresh_reconcile_from_inv(self, cr, uid, inv_id, reconcile_ids):
        """If invoice state is update to draft and returned to open, linked
        account move is changed. So move_id and all move_line_ids read by
        'get_reconcile_from_inv' and/or 'get_reconcile_list_from_move_line'
        are no more valid, while payments reference are still valid.
        So all invoice reference are update with new reference.
        @ param inv_id: invoice (header) id (CANNOT BE CHANGED BY PRIOR READ)
        @ param reconciles: prior reconciled move lines
        @ return: list of reconciled move lines of passed (included) invoice
        @ return: dictionary of posted movements (header) to set to draft state
        """
        move_line_model = self.pool['account.move.line']
        invoice = self.browse(cr, uid, inv_id)
        partner_id = invoice.partner_id.id
        move_id = invoice.move_id.id or False
        move_line_ids = move_line_model.search(
            cr, uid, [('move_id', '=', move_id),
                      ('partner_id', '=', partner_id)])
        new_reconcile_ids = []
        for move_line_id in move_line_ids:
            account_id = move_line_model.browse(
                cr, uid, move_line_id).account_id.id
            type = self.pool['account.account'].browse(
                cr, uid, account_id).type
            if type in ('receivable', 'payable'):
                new_reconcile_ids.append(move_line_id)
        company_id = invoice.company_id.id
        valid_recs = True
        for move_line_id in reconcile_ids[1:]:
            move_line = move_line_model.browse(
                cr, uid, move_line_id)
            if move_line.partner_id.id != partner_id or \
                    move_line.company_id.id != company_id:
                valid_recs = False
            else:
                new_reconcile_ids.append(move_line_id)
        if not valid_recs:
            new_reconcile_ids = []
        reconcile_dict = {inv_id: new_reconcile_ids}
        return new_reconcile_ids, reconcile_dict

    def unreconcile_invoices(self, cr, uid, reconcile_ids):
        if reconcile_ids:
            try:
                context = {'active_ids': reconcile_ids}
                self.pool['account.unreconcile'].trans_unrec(
                    cr, uid, False, context=context)
            except BaseException:
                _logger.info(_('Cannot unreconcile invoices %s') %
                             str(reconcile_ids))

    def reconcile_invoices(self, cr, uid, reconcile_dict):
        for inv_id in reconcile_dict:
            try:
                context = {'active_ids': reconcile_dict[inv_id]}
                self.pool['account.move.line.reconcile'].\
                    trans_rec_reconcile_partial_reconcile(
                        cr, uid, [inv_id], context=context)
            except BaseException:
                _logger.info(_('Cannot reconcile invoices %s') %
                             str(reconcile_dict[inv_id]))

    def proforma_2_invoice(self, cr, uid, ids, context=None):
        for inv_id in ids:
            invoice = self.browse(cr, uid, inv_id)
            if not invoice.journal_id or not invoice.journal_id.proforma:
                continue
            company_id = self.browse(cr, uid, inv_id).company_id.id
            puchase_journal_id = self.pool[
                'account.journal'].get_purchase_journal(cr,
                                                        uid,
                                                        company_id,
                                                        context=context)
            ids = self.search(
                cr, uid, [('registration_date', '!=', False),
                          ('state', 'in', INVOICES_STS_2_DRAFT),
                          ('journal_id', '=', puchase_journal_id)],
                order='registration_date desc', limit=1)
            if ids:
                last_date = self.browse(cr, uid, ids[0]).registration_date
            else:
                last_date = datetime.now().strftime(DEFAULT_SERVER_DATE_FORMAT)
            reconcile_ids, move_dict = self.get_reconcile_from_inv(
                cr, uid, inv_id)
            self.unreconcile_invoices(cr, uid, reconcile_ids)
            self.upd_invoices_2_draft(cr, uid, move_dict)
            self.write(cr, uid, [inv_id],
                       {'internal_number': '',
                        'journal_id': puchase_journal_id,
                        'registration_date': last_date})
            self.upd_invoices_2_post(cr, uid, move_dict)
            if len(reconcile_ids):
                cur_reconcile_ids, cur_reconcile_dict = \
                    self.refresh_reconcile_from_inv(
                        cr, uid, inv_id, reconcile_ids)
                self.reconcile_invoices(cr, uid, cur_reconcile_dict)
        return True
