# -*- coding: utf-8 -*-
#    Copyright (C) 2011-12 Domsense s.r.l. <http://www.domsense.com>.
#    Copyright (C) 2012-15 Agile Business Group sagl <http://www.agilebg.com>
#    Copyright (C) 2013-15 LinkIt Spa <http://http://www.linkgroup.it>
#    Copyright (C) 2013-17 Associazione Odoo Italia
#                          <http://www.odoo-italia.org>
#    Copyright (C) 2017    Didotech srl <http://www.didotech.com>
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.tests.common import TransactionCase
from openerp import netsvc
# import pdb


class TestTax(TransactionCase):
    def env7(self, model):
        return self.registry(model)

    def setUp(self):
        super(TestTax, self).setUp()
        self.tax_model = self.env7('account.tax')
        self.tax_code_model = self.env7('account.tax.code')
        self.account_model = self.env7('account.account')
        self.term_model = self.env7('account.payment.term')
        self.term_line_model = self.env7('account.payment.term.line')
        self.invoice_model = self.env7('account.invoice')
        self.invoice_line_model = self.env7('account.invoice.line')
        self.period_model = self.env7('account.period')
        self.current_period = self.period_model.find(self.cr, self.uid, )
        self.vat_statement_model = self.env7(
            'account.vat.period.end.statement')

        # ----- Set invoice date to recent date in the system
        # ----- This solves problems with account_invoice_sequential_dates
        ids = self.invoice_model.search(self.cr, self.uid, [(
            'date_invoice', '!=', False)], order='date_invoice desc', limit=1)
        self.recent_date = self.invoice_model.browse(self.cr, self.uid, ids[
            0]).date_invoice

        self.account_tax_code_22 = self.tax_code_model.create(
            self.cr, self.uid, {'name': '22%', 'vat_statement_type':
                                'debit', 'vat_statement_account_id': self.ref(
                                    'account.ova'), })
        self.account_tax_code_22_imp = self.tax_code_model.create(
            self.cr, self.uid, {'name': '22% IMP', })
        self.account_tax_code_22_credit = self.tax_code_model.create(
            self.cr, self.uid, {'name': '22% credit', 'vat_statement_type':
                                'credit', 'vat_statement_account_id': self.ref(
                                    'account.iva'), })
        self.account_tax_code_22_imp_credit = self.tax_code_model.create(
            self.cr, self.uid, {'name': '22% IMP credit', })

        self.account_tax_22 = self.tax_model.create(self.cr, self.uid, {
            'name': '22%', 'amount': 0.22, 'tax_code_id':
                self.account_tax_code_22, 'base_code_id':
                    self.account_tax_code_22_imp, })
        self.account_tax_22_credit = self.tax_model.create(self.cr, self.uid, {
            'name': '22% credit', 'amount': 0.22, 'tax_code_id':
                self.account_tax_code_22_credit, 'base_code_id':
                    self.account_tax_code_22_imp_credit, })

        self.vat_authority = self.account_model.create(self.cr, self.uid, {
            'code': 'VAT AUTH', 'name': 'VAT Authority', 'parent_id':
                self.ref('account.cli'), 'type': 'payable', 'reconcile':
                    True, 'user_type': self.ref(
                        'account.data_account_type_payable'), })

        self.account_payment_term = self.term_model.create(self.cr, self.uid, {
            'name': '16 Days End of Month', 'note': '16 Days End of Month', })
        self.term_line_model.create(self.cr, self.uid,
                                    {'value': 'balance',
                                     'days': 16,
                                     'days2': -1,
                                     'payment_id': self.account_payment_term})

    def test_vat_statement(self):
        wf_service = netsvc.LocalService('workflow')
        out_invoice = self.invoice_model.create(self.cr, self.uid, {
            'date_invoice': self.recent_date, 'account_id': self.ref(
                'account.a_recv'), 'journal_id': self.ref(
                    'account.sales_journal'), 'partner_id': self.ref(
                        'base.res_partner_3'), 'type': 'out_invoice', })
        self.invoice_line_model.create(
            self.cr,
            self.uid,
            {'invoice_id': out_invoice,
             'account_id': self.ref('account.a_sale'),
             'name': 'service',
             'price_unit': 100,
             'quantity': 1,
             'invoice_line_tax_id': [(6, 0, [self.account_tax_22])], })
        # out_invoice.signal_workflow('invoice_open')
        wf_service.trg_validate(self.uid, 'account.invoice', out_invoice,
                                'invoice_open', self.cr)

        in_invoice = self.invoice_model.create(self.cr, self.uid, {
            'date_invoice': self.recent_date, 'account_id': self.ref(
                'account.a_pay'), 'journal_id': self.ref(
                    'account.expenses_journal'), 'partner_id': self.ref(
                        'base.res_partner_4'), 'type': 'in_invoice', })
        self.invoice_line_model.create(
            self.cr,
            self.uid,
            {'invoice_id': in_invoice,
             'account_id': self.ref('account.a_expense'),
             'name': 'service',
             'price_unit': 50,
             'quantity': 1,
             'invoice_line_tax_id': [(6, 0, [self.account_tax_22_credit])], })
        # in_invoice.signal_workflow('invoice_open')
        wf_service.trg_validate(self.uid, 'account.invoice', in_invoice,
                                'invoice_open', self.cr)

        self.vat_statement_id = self.vat_statement_model.create(
            self.cr, self.uid,
            {'journal_id': self.ref('account.miscellaneous_journal'),
             'authority_vat_account_id': self.vat_authority,
             'payment_term_id': self.account_payment_term, })
        self.vat_statement = self.vat_statement_model.browse(
            self.cr, self.uid, self.vat_statement_id)
        # self.vat_statement.compute_amounts()
        self.vat_statement_model.compute_amounts(self.cr, self.uid,
                                                 [self.vat_statement_id])
        # self.assertEqual(self.vat_statement.authority_vat_amount, 11)
        # self.assertEqual(self.vat_statement.deductible_vat_amount, 11)
        # self.assertEqual(self.vat_statement.payable_vat_amount, 22)
        # self.assertEqual(self.vat_statement.residual, 0)
        # self.assertEqual(
        #     len(self.vat_statement.debit_vat_account_line_ids), 1)
        # self.assertEqual(
        #     len(self.vat_statement.credit_vat_account_line_ids), 1)
        # # self.vat_statement.signal_workflow('create_move')
        # wf_service.trg_validate(self.uid, 'account.invoice', vat_statement,
        #                             'create_move', self.cr)
        # self.assertEqual(self.vat_statement.state, 'confirmed')
        # self.assertTrue(self.vat_statement.move_id)
        # TODO payment
