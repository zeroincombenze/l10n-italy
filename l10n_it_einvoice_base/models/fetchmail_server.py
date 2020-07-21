# -*- coding: utf-8 -*-
# Copyright 2018 Sergio Corato (https://efatto.it)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp.osv import orm, fields


class FetchmailServer(orm.Model):
    _inherit = "fetchmail.server"

    _columns = {
        'is_fatturapa_pec': fields.boolean("E-invoice PEC server"),
    }

