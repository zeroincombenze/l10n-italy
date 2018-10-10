# -*- coding: utf-8 -*-
#
# Copyright 2014    Davide Corio <davide.corio@lsweb.it>
# Copyright 2015    Agile Business Group <http://www.agilebg.com>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Italian Localization - FatturaPA',
    'version': '9.0.2.1.0',
    'category': 'Localization/Italy',
    'summary': 'Electronic invoices',
    'author': 'Odoo Italia Associazione,'
              'Odoo Community Association (OCA)',
    'website': 'http://www.odoo-italia.org',
    'license': 'LGPL-3',
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
        # 'views/account_tax_view.xml',
        'security/ir.model.access.csv',
    ],
    "demo": ['demo/account_invoice_fatturapa.xml'],
    'installable': False,
    'external_dependencies': {
        'python': ['pyxb'],
    }
}
