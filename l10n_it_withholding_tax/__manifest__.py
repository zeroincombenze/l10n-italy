# -*- coding: utf-8 -*-
# Copyright 2015 Alessandro Camilli (<http://www.openforce.it>)
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).
#
{
    'name': 'Italian Withholding Tax',
    'version': '10.0.1.2.6',
    'category': 'Account',
    'author': 'Odoo Community Association (OCA) and other subjects',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'l10n_it_causali_pagamento',
        'l10n_it_einvoice_base',
    ],
    'data': [
        'views/account.xml',
        'views/withholding_tax.xml',
        'security/ir.model.access.csv',
        'workflow.xml',
        'security/security.xml',
    ],
    'installable': True,
}
