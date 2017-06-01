# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2010-2011 Associazione Odoo Italia
#    (<http://www.odoo-italia.org>).
#    All Rights Reserved
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
##############################################################################
{
    'name': 'Italian Localisation - HR',
    'version': '0.2',
    'category': 'Localisation/Italy',
    'description': """Odoo Italian Localization - HR version

Functionalities:

- Fiscal Code for employee

""",
    'author': 'Odoo Italian Community',
    'website': 'http://www.odoo-italia.org',
    'license': 'AGPL-3',
    "depends": ['hr'],
    "init_xml": [
    ],
    "update_xml": [
        'employee_view.xml',
    ],
    "demo_xml": [],
    "active": False,
    "installable": True
}
