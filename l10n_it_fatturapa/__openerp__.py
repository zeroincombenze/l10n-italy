# -*- coding: utf-8 -*-
# Copyright (C) 2014 Davide Corio
# Copyright 2015-2016 Lorenzo Battistini - Agile Business Group

{
    'name': 'Italian Localization - FatturaPA',
    'version': '8.0.2.0.1',
    'category': 'Localization/Italy',
    'summary': 'Electronic invoices',
    'author': 'Davide Corio, Agile Business Group, Innoviu, '
              'Odoo Community Association (OCA)',
    'website': 'http://www.odoo-italia.org',
    'license': 'AGPL-3',
    "depends": [
        'l10n_it_ade',
        'account',
        'l10n_it_base',
        'l10n_it_fiscalcode',
        'document',
        'l10n_it_ipa',
        'l10n_it_rea',
        'base_iban',
        ],
    "data": [
        'data/fatturapa_data.xml',
        'data/welfare.fund.type.csv',
        'views/account_view.xml',
        'views/company_view.xml',
        'views/partner_view.xml',
        'views/account_tax_view.xml',
        'security/ir.model.access.csv',
    ],
    "demo": ['demo/account_invoice_fatturapa.xml'],
    "installable": True,
    'external_dependencies': {
        'python': ['pyxb'],
    }
}
