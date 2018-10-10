# -*- coding: utf-8 -*-
#
# Copyright 2014    - Davide Corio <davide.corio@abstract.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class fatturapa_payment_term(orm.Model):
    # _position = ['2.4.1']
    _name = "fatturapa.payment_term"
    _description = 'FatturaPA Payment Term'

    _columns = {
        'name': fields.char('Description', size=128),
        'code': fields.char('Code', size=4),
    }


class fatturapa_payment_method(orm.Model):
    # _position = ['2.4.2.2']
    _name = "fatturapa.payment_method"
    _description = 'FatturaPA Payment Method'

    _columns = {
        'name': fields.char('Description', size=128),
        'code': fields.char('Code', size=4),
    }


#  used in fatturaPa export
class account_payment_term(orm.Model):
    # _position = ['2.4.2.2']
    _inherit = 'account.payment.term'

    _columns = {
        'fatturapa_pt_id': fields.many2one(
            'fatturapa.payment_term', string="FatturaPA Payment Term"),
        'fatturapa_pm_id': fields.many2one(
            'fatturapa.payment_method', string="FatturaPA Payment Method"),
    }
