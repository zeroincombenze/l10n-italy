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
    'name': 'Lettere di intento',
    'summary': 'Lettere di intento',
    'version': '10.0.0.1.3',
    'category': 'Generic Modules/Accounting',
    'author': 'SHS-AV s.r.l.',
    'website': 'https://www.zeroincombenze.it/',
    'depends': ['base', 'l10n_it_einvoice_stamp'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/italy_lettera_intento_view.xml',
        'views/account_fiscal_position_view.xml',
        'views/config_view.xml',
        'views/account_invoice_view.xml',
    ],
    'installable': True,
}
