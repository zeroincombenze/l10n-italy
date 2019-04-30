# -*- coding: utf-8 -*-
{
    'name': 'Italy - Fiscal localization by zeroincombenze(R)',
    'version': '10.0.0.2.0',
    'category': 'Localization/Account Charts',
    'author': 'SHS-AV s.r.l.',
    'website': 'http://www.zeroincombenze.it',
    'license': 'AGPL-3',
    'depends': [
        'base_vat',
        'base_iban',
    ],
    'data': [
        'data/l10n_it_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.tax.template.csv',
        'data/account.fiscal.position.template.csv',
        'data/account.chart.template.csv',
        'data/account_chart_template_data.yml',
    ],
    'installable': True,
    'maintainer': 'Antonio Maria Vigliotti',
}
