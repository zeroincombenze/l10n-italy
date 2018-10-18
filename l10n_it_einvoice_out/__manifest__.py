#
# Copyright 2014    Davide Corio
# Copyright 2015-16 Lorenzo Battistini - Agile Business Group
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Italian Localization - FatturaPA - Emission',
    'version': '11.0.1.0.0',
    'category': 'Localization/Italy',
    'summary': 'Electronic invoices emission',
    'author': 'Davide Corio, Agile Business Group, Innoviu,'
              'Odoo Community Association (OCA)',
    'website': 'http://www.agilebg.com',
    'license': 'LGPL-3',
    "depends": [
        'l10n_it_einvoice_base',
        'l10n_it_split_payment',
    ],
    "data": [
        'wizard/wizard_export_fatturapa_view.xml',
        'views/attachment_view.xml',
        'views/account_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': False,
    'external_dependencies': {
        'python': ['unidecode'],
    }
}
