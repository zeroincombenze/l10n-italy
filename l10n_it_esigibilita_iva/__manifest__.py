#
# Copyright 2017    Alessandro Camilli - Openforce
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Esigibilità IVA',
    'version': '11.0.1.0.0',
    'category': 'Account',
    'author': "Openforce di Camilli Alessandro, "
              "Odoo Community Association (OCA)",
    'website': 'https://www.odoo-italia.net',
    'license': 'LGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'views/account_view.xml',
    ],
    'installable': True,
}
