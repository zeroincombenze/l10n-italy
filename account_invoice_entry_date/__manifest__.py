# -*- encoding: utf-8 -*-
{
    'name': 'Account Invoice entry Date',
    'version': '10.0.0.1.1',
    'category': 'Generic Modules/Accounting',
    'summary': """Account Invoice Entry Dates""",
    'author': "SHS-AV s.r.l.",
    'website':
        'http://www.zeroincombenze.it/servizi-le-imprese/software-gestionale/',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'views/account_invoice_view.xml',
        'wizard/wizard_default_invoice_registrationdate_view.xml'
    ],
    'installable': True
}
