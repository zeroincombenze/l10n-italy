# -*- coding: utf-8 -*-
#
#
#    Copyright (C) 2010 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    'name': 'Italian Localisation - Sale',
    'version': '7.0.0.2.1',
    'category': 'Localisation/Italy',
    'description': """OpenERP Italian Localization - Sale version

Functionalities:

- Documento di trasporto

(Da Odoo 8.0 è rimpiazzato con il modulo l10n_it_ddt)
""",
    'author': "OpenERP Italian Community,Odoo Community Association (OCA)",
    'website': 'http://www.openerp-italia.org',
    'license': 'AGPL-3',
    "depends": ['stock', 'sale', 'account', 'delivery'],
    "data": [
        'security/ir.model.access.csv',
        'wizard/assign_ddt.xml',
        'views/carriage_condition_view.xml',
        'views/transportation_reason_view.xml',
        'views/goods_description_view.xml',
        'views/invoice_view.xml',
        'views/partner_view.xml',
        'views/sale_view.xml',
        'views/picking_view.xml',
        'data/transportation_reason_data.xml',
        'data/goods_description_data.xml',
        'data/carriage_condition_data.xml',
        'data/sequence.xml',
    ],
    "demo": [],
    "active": False,
    "installable": True
}
