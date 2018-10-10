# -*- coding: utf-8 -*-
# Copyright 2014 Associazione Odoo Italia <http://www.odoo-italia.org>
# Copyright 2015 Alessio Gerace <alessio.gerace@agilebg.com>
{
    'name': 'REA Register',
    'version': '7.0.0.1.1',
    'category': 'Localisation/Italy',
    'summary': 'Manage fields for  Economic Administrative catalogue',
    'author': 'Agile Business Group, Odoo Community Association (OCA)',
    'website': 'https://odoo-italia.org',
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License

REA Registration
=======================

The module implement fields of REA data in partner
http://www.registroimprese.it/il-registro-imprese-e-altre-banche-dati#page=registro-imprese

Usage
=====

The module adds fields in page Accounting of partner form, where you can
add data of registry of businesses


Credits
=======

Contributors
------------

* Alessio Gerace <alessio.gerace@agilebg.com>

Maintainer
----------

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
""",
    'license': 'AGPL-3',
    "depends": [
        'account'
    ],
    "data": [
        'views/partner_view.xml',
    ],
    "installable": True
}
