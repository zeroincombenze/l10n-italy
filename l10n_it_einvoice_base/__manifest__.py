#
# Copyright 2014    - Davide Corio <davide.corio@abstract.it>
# Copyright 2015-16 - Lorenzo Battistini - Agile Business Group
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Italian Localization - FatturaPA',
    'version': '11.0.2.0.1',
    'category': 'Localization/Italy',
    'summary': 'Electronic invoices',
    'author': 'Odoo Italia Associazione,'
              'Odoo Community Association (OCA)',
    'website': 'http://www.odoo-italia.org',
    'license': 'LGPL-3',
    "depends": [
        'account',
        'l10n_it_fiscalcode',
        'document',
        'l10n_it_fiscal_ipa',
        'l10n_it_rea',
        'base_iban',
        'l10n_it_ade',
        # 'l10n_it_esigibilita_iva',
        # 'l10n_it_fiscal_payment_term',
        # 'l10n_it_split_payment',
        # 'l10n_it_fiscal_document_type',
        # 'partner_firstname',
    ],
    "data": [
        'data/fatturapa_data.xml',
        'data/welfare.fund.type.csv',
        'views/account_view.xml',
        # 'views/company_view.xml',
        'views/partner_view.xml',
        'security/ir.model.access.csv',
    ],
    "demo": [
        'demo/account_tax.xml',
        'demo/res_partner.xml',
    ],
    'installable': False,
    'external_dependencies': {
        'python': [
            'pyxb',  # pyxb 1.2.4
        ],
    }
}
