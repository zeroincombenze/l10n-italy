# -*- coding: utf-8 -*-
#
# Copyright 2017-2018, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2010-2018, Associazione Odoo Italia <https://odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Italian Localisation - Base',
    'version': '10.0.0.2.15',
    'category': 'Generic Modules/Accounting',
    'author': 'Odoo Community Association (OCA), Pexego,',
    'website': 'https://www.odoo-community.org',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/city_view.xml',
        'data/res.city.xml',
    ],
    'installable': True,
    'maintainer': 'Antonio Maria Vigliotti',
}
