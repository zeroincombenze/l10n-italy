# -*- coding: utf-8 -*-
#
# Copyright 2014 Davide Corio <davide.corio@abstract.it>
# Copyright 2015-16 Lorenzo Battistini - Agile Business Group
# Copyright 2018 Gianmarco Conte - Dinamiche Aziendali srl
# Copyright 2018-21 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Italian Localization - Fiscal payment term',
    'version': '8.0.1.0.0',
    'category': 'Localization/Italy',
    'summary': 'Electronic invoices payment',
    'author': 'Odoo Italia Associazione,'
              'Odoo Community Association (OCA)',
    'website': 'https://odoo-community.org',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'l10n_it_ade',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/fatturapa_data.xml',
        'views/account_view.xml',
        'views/payment_term_view.xml',
        'views/payment_method_view.xml',
    ],
    'installable': True,
    'pre_init_hook': 'pre_init_hook',
}
