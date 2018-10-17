# -*- coding: utf-8 -*-
#
# Copyright 2010-2013, Odoo Italian Community
# Copyright 2014-2018, Associazione Odoo Italia <https://odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Italian Localisation - Base',
    'version': '8.0.0.2.14',
    'category': 'Localisation/Italy',
    'author': "Odoo Italian Community,Odoo Community Association (OCA),"
              "SHS-AV s.r.l.",
    'maintainer': 'Antonio Maria Vigliotti',
    'website': 'https://odoo-italia.org/',
    'license': 'AGPL-3',
    "depends": ['base'],
    "data": [
        'security/ir.model.access.csv',
        'views/res_config_view.xml',
        'views/res_partner_view.xml',
        'views/city_view.xml',
        'data/res.country.state.csv',
        'data/res.city.csv',
    ],
    # "test": ['test/res_partner.yml'],
    'installable': True
}
