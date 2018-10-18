# -*- coding: utf-8 -*-
#
# Copyright 2010-2011, Odoo Italian Community
# Copyright 2011-2017, Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2014, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Italian Localisation - Base',
    'version': '7.0.0.2.14',
    'category': 'Localisation/Italy',
    'description': """(en)

Italian Localization - Base version
-----------------------------------

 Funcionalities:

- Italian cities
- Titles
- Provinces (districts) and Regions


(it)

Localizzazione italiana - Versione base
---------------------------------------

Funzionalità

- Comuni italiani (aggiornati al 2014)
- Titoli
- Province
- Automatistmi su res.partner.address
""",
    'author': "Odoo Italian Community,Odoo Community Association (OCA),"
              "SHS-AV s.r.l.",
    'maintainer': 'Antonio Maria Vigliotti',
    'website': 'https://odoo-italia.org/',
    'license': 'AGPL-3',
    "depends": ['base'],
    "data": [
        'security/ir.model.access.csv',
        'views/partner_view.xml',
        'views/company_view.xml',
        'views/city_view.xml',
        'views/province_view.xml',
        'data/res.region.csv',
        'data/res.province.csv',
        'data/res.country.state.csv',
        'data/res.city.csv',
        'data/res.partner.title.csv',
    ],
    "test": ['test/res_partner.yml'],
    "installable": True
}
