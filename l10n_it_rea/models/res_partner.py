# -*- coding: utf-8 -*-
# Copyright 2014 Associazione Odoo Italia (<http://www.odoo-italia.org>)
# Copyright 2015 Alessio Gerace <alessio.gerace@agilebg.com>

from openerp.osv import fields, orm


class resPartner(orm.Model):
    _inherit = 'res.partner'

    _columns = {
        'rea_office': fields.many2one(
            'res.country.state', string='Office Province'),
        'rea_code': fields.char('REA Code', size=20),
        'rea_capital': fields.float('Capital'),
        'rea_member_type': fields.selection(
            [
                ('SU', 'Unique Member'),
                ('SM', 'Multiple Members'),
            ], 'Member Type'
        ),
        'rea_liquidation_state': fields.selection(
            [
                ('LS', 'In liquidation'),
                ('LN', 'Not in liquidation'),
            ], 'Liquidation State'
        ),
    }

    _sql_constraints = [
        ('rea_code_uniq', 'unique (rea_code, company_id)',
         'The rea code code must be unique per company !'),
    ]
