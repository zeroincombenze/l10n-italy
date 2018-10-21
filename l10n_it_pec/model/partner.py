# -*- coding: utf-8 -*-
#
# Copyright 2014    Associazione Odoo Italia
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
#    (<http://www.odoo-italia.org>).
#

from openerp.osv import fields, orm


class ResPartner(orm.Model):
    _inherit = "res.partner"
    _columns = {
        'pec_mail': fields.char(
            'PEC Mail'
        ),
    }
