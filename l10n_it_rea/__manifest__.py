#
# Copyright 2014    Associazione Odoo Italia (<https://www.odoo-italia.org>)
# Copyright 2015    Alessio Gerace <alessio.gerace@agilebg.com>
# Copyright 2016    Andrea Gallina (Apulia Software)
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'REA Register',
    'version': '11.0.1.0.1',
    'category': 'Localisation/Italy',
    'summary': 'Manage fields for  Economic Administrative catalogue',
    'author': 'Agile Business Group, Odoo Italia Network,'
              'Odoo Community Association (OCA)',
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": [
        'account'
    ],
    "data": [
        'views/partner_view.xml',
    ],
    'installable': True,
}
