# -*- coding: utf-8 -*-
# Copyright 2017, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2017, Associazione Odoo Italia <https://odoo-italia.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import orm
from openerp.tools.translate import _


class AccountJournal(orm.Model):
    _inherit = 'account.journal'

    def get_purchase_journal(self, cr, uid, company_id, context=None):
        journal_ids = self.search(
            cr, uid,
            [
                ('type', '=', 'purchase'),
                ('company_id', '=', company_id),
                ('code', '=', 'EXJ')
            ],
            context=context)
        if not journal_ids:
            raise orm.except_orm(
                _('Error!'),
                _('No purchase journal found for company_id: %d!'
                  ) % company_id
            )
        return journal_ids[0]
