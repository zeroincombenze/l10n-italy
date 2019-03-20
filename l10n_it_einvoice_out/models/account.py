# -*- coding: utf-8 -*-
#
# Copyright 2014    - Davide Corio <davide.corio@lsweb.it>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#

from openerp import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    fatturapa_attachment_out_id = fields.Many2one(
        'fatturapa.attachment.out', 'E-Fattura Export File',
        readonly=True)

    # @api.one
    # def copy(self, defaults=None):
    def copy(self, cr, uid, ids, defaults=None, context=None):
        defaults = defaults or {}
        defaults.update({'fatturapa_attachment_out_id': False})
        return super(AccountInvoice, self).copy(cr, uid, ids, defaults, context)
