{
    'name': 'Send E-Invoice to SdI',
    'summary': 'Send E-Invoice to customer thought SdI',
    'version': '10.0.1.0.0',
    'category': 'Localization/Italy',
    'author': 'SHS-AV s.r.l.,Odoo Italia Associazione',
    'website': 'http://www.odoo-italia.org',
    'license': 'LGPL-3',
    "depends": [
        'l10n_it_einvoice_base',
        'l10n_it_split_payment',
        'l10n_it_einvoice_in',
        'l10n_it_einvoice_out',
    ],
    "data": [
        'views/account.xml',
        'views/attachment_view.xml'
    ],
    'installable': True,
    'external_dependencies': {
        'python': [
            # 'pycryptodome',
            'Crypto.Cipher',
            'pkcs7',
            'os0',
        ],
    }
}
