#
# Copyright 2015    Davide Corio <davide.corio@abstract.it>
# Copyright 2015-16  Lorenzo Battistini - Agile Business Group
# Copyright 2016    Alessio Gerace - Agile Business Group
# Copyright 2017-18 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Split Payment',
    'version': '11.0.1.0.2',
    'category': 'Localization/Italy',
    'summary': 'Split Payment',
    'author': 'Abstract, Agile Business Group, '
              'Odoo Community Association (OCA)',
    'website': 'http://www.abstract.it',
    'license': 'AGPL-3',
    'depends': ['account'],
    'data': [
        'views/account_view.xml',
        'views/config_view.xml',
    ],
    'installable': True,
}
