# -*- coding: utf-8 -*-
# Copyright (C) 2014 Davide Corio
# Copyright 2015-2016 Lorenzo Battistini - Agile Business Group

{
    'name': 'Italian Localization - FatturaPA - Emission',
    'version': '7.0.0.2.1',
    'category': 'Localization/Italy',
    'summary': 'Electronic invoices emission',
    'author': 'Davide Corio, Agile Business Group, Innoviu, '
              'Odoo Community Association (OCA)',
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License


Italian Localization - FatturaPA - Emission
===========================================

This module allows you to generate the fatturaPA XML file version 1.2
http://www.fatturapa.gov.it/export/fatturazione/en/normativa/f-2.htm
to be sent to the Exchange System
http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm


Configuration
=============

See l10n_it_fatturapa


Usage
=====

 * Fill invoice data you need to export. For instance, in
   'related documents' TAB, or in 'related documents' section
   within invoice line.

 * Select N invoices and run 'Export FatturaPA' wizard

Credits
=======

Contributors
------------

* Davide Corio <davide.corio@abstract.it>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Roberto Onnis <roberto.onnis@innoviu.com>
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
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": [
        'l10n_it_fatturapa',
        'l10n_it_split_payment',
        ],
    "data": [
        'wizard/wizard_export_fatturapa_view.xml',
        'views/attachment_view.xml',
        'views/account_view.xml',
        'security/ir.model.access.csv',
    ],
    "installable": True,
    'external_dependencies': {
        'python': ['unidecode'],
    }
}
