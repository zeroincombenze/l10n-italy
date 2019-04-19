# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
{
    "name": "Comunicazione periodica IVA",
    "version": "10.0.0.1.15",
    'category': 'Generic Modules/Accounting',
    'license': 'LGPL-3',
    "depends": [
        # "account_invoicing",
        "account_cancel",
        "account_period",
        "l10n_it_ade",
        "l10n_it_fiscalcode",
        "account_invoice_entry_date",
        # "account_accountant_cbc",
        # "l10n_it_vat_registries",
    ],
    "author": "SHS-AV s.r.l.",
    'maintainer': 'Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>',
    'website': 'https://odoo-italia.org',
    'data': ['security/ir.model.access.csv',
             'wizard/views/add_period.xml',
             'wizard/views/remove_period.xml',
             'views/account_view.xml',
             'wizard/views/wizard_export_view.xml',
             #'communication_workflow.xml',
             ],
    'external_dependencies': {
        'python': ['pyxb', 'unidecode'],
    },
    'demo': [],
    'installable': True,
}

