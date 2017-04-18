# -*- encoding: utf-8 -*-
#
#
#    Copyright (C) 2010-2011 OpenERP Italian Community
#    http://www.openerp-italia.org>
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
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    'name': 'Italian Localisation - Base',
    'version': '7.0.0.2.9',
    'category': 'Localisation/Italy',
    'description': """Italian Localization module - Base version

Italian Localization - Base version
-----------------------------------

[en] Funcionalities:

- Italian cities
- Titles
- Provinces (districts) and Regions


Localizzazione italiana - Versione base
---------------------------------------

[en] Funzionalità

- Comuni italiani (aggiornati al 2008)
- Titoli
- Province e regioni
- Automatistmi su res.partner.address
""",
    'author': "Odoo Italian Community,Odoo Community Association (OCA),"
              "SHS-AV s.r.l.",
    'maintainer': 'Antonio Maria Vigliotti',
    'website': 'https://odoo-italia.org/',
    'license': 'AGPL-3',
    "depends": ['base'],
    "init_xml": [
    ],
    "update_xml": ['views/partner_view.xml',
                   'views/company_view.xml',
                   'views/city_view.xml',
                   'views/province_view.xml',
                   'security/ir.model.access.csv',
                   'data/res.region.csv',
                   'data/res.province.csv',
                   'data/res.city.csv',
                   'data/res.partner.title.csv',
                   'data/res.country.state.csv',
                   ],
    "demo_xml": [],
    "test": ['test/res_partner.yml',
             ],
    "active": False,
    "installable": True
}

# http://www.istat.it/strumenti/definizioni/comuni/
# i dati dovrebbero essere sincronizzati con questi
