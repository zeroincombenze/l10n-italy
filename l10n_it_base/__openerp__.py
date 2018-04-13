# -*- coding: utf-8 -*-
#
# Copyright 2017-2018, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2010-2018, Associazione Odoo Italia <https://odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Italian Localisation - Base',
    'version': '10.0.0.1.0',
    'category': 'Localisation/Italy',
    'description': """
Italian Localisation module - Base version
==========================================
""",
    'author': "OpenERP Italian Community,Odoo Community Association (OCA)",
    'website': 'http://www.openerp-italia.org',
    'license': 'AGPL-3',
    "depends": ['base'],
    "data": [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'data/res.city.csv',
        # 'data/res.country.state.csv',
    ],
    'installable': True
}
