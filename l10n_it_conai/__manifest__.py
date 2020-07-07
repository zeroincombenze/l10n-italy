# -*- coding: utf-8 -*-
#
# Copyright 2019-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'CONAI Management',
    'summary': 'Dati CONAI in fattura e calcolo importi',
    'version': '10.0.0.1.5',
    'category': 'Localization/Italy',
    'author': 'SHS-AV s.r.l.',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'l10n_it_ddt',
        'stock_picking_package_preparation',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/conai_product_category.xml',
        'data/conai_partner_category.xml',
        'views/product_category_view.xml',
        'views/partner_category_view.xml',
        'views/picking_view.xml',
        'views/account_invoice_view.xml',
        'views/product_view.xml',
        'views/partner_view.xml',
        'report/conai_statement.xml'
    ],
    'installable': True,
    'maintainer': 'Zeroincombenze (R)',
    'development_status': 'Beta',
}
