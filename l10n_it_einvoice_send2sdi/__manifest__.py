# -*- coding: utf-8 -*-
#
# Copyright 2018-21 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Send E-Invoice to SdI',
    'summary': 'Send E-Invoice to customer by SdI',
    'version': '10.0.1.0.14',
    'category': 'Localization/Italy',
    'author': 'SHS-AV s.r.l.,Odoo Italia Associazione',
    'website': 'http://www.odoo-italia.org',
    'license': 'LGPL-3',
    "depends": [
        'l10n_it_einvoice_base',
        'l10n_it_split_payment',
        'l10n_it_einvoice_in',
        'l10n_it_einvoice_out',
        # 'status_widget',
    ],
    "data": [
        'views/account.xml',
        'views/attachment_view.xml',
        'data/ir_cron.xml'
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
