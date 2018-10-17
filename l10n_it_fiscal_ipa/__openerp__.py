# -*- coding: utf-8 -*-
#
# Copyright 2014    - KTec S.r.l. <http://www.ktec.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    "name": "IPA Code (IndicePA)",
    "version": "7.0.1.0.1",
    "category": "Localisation/Italy",
    "author": "KTec S.r.l,"
              " Odoo Community Association (OCA),"
              " Odoo Italia Associazione",
    "website": "http://www.ktec.it",
    "description": """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License

IPA Code (IndicePA)
===================

This module adds IPA (IndicePA) field to partner
http://www.indicepa.gov.it


Credits
=======

Contributors
------------

* Luigi Di Naro <luigi.dinaro@ktec.it>
* Alex Comba <alex.comba@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
""",
    "license": "AGPL-3",
    "depends": ['base'],
    "data": [
        'view/partner_view.xml',
    ],
    "qweb": [],
    "demo": [],
    "test": [],
    "active": False,
    'installable': True
}
