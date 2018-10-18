#
# Copyright 2014    - KTec S.r.l. <http://www.ktec.it>
# Copyright 2014-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'IPA Code (IndicePA)',
    'version': '7.0.1.1.0',
    'category': 'Localisation/Italy',
    'author': 'KTec S.r.l, Odoo Community Association (OCA), Odoo Italia Associazione',
    'website': 'http://www.ktec.it',
    'summary': 'IPA Code and Destination Code in Partner Record',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': ['view/partner_view.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'description': '''|en|

IPA Code
=========

This module adds IPA (IndicePA) code and Recipient Code fields to partner,
used by Italian Electronic Invoice.

http://www.indicepa.gov.it




|it|

Codice IPA (IndicePA)
======================

Questo modulo permette l'inseriento del codice IPA (IndicePA) e del Codice Destinatario
nell'anagrafica cliente.

Questi dati sono indispensabili per la gestione della Fattura Elettronica B2B e
per la FatturaPA.

http://www.indicepa.gov.it



Features / Funzioni
--------------------

+-------------------------------------------------+----------+----------------------------------------------+
| Feature / Funzione                              |  Status  | Notes / Note                                 |
+-------------------------------------------------+----------+----------------------------------------------+
| Parter: IPA Code / Codice IPA                   | |check|  | Per FatturaPA                                |
+-------------------------------------------------+----------+----------------------------------------------+
| Partner: Recipient Code / Codice Destinatario   | |check|  | EInvoice / Per Fattura Elettronica B2B       |
+-------------------------------------------------+----------+----------------------------------------------+



OCA Differences / Differenze da OCA
------------------------------------

+--------------------------------------+-------------+-------------------+--------------------------------+
| Description / Descrizione            | Odoo Italia | OCA               | Notes / Note                   |
+--------------------------------------+-------------+-------------------+--------------------------------+
| Partner view / Vista cliente         | This Module | This Module       | Different layout               |
+--------------------------------------+-------------+-------------------+--------------------------------+
| IPA Code                             | This Module | This Module       |                                |
+--------------------------------------+-------------+-------------------+--------------------------------+
| Recipient Code / Codice Destinatario | This Module | l10n_it_fatturapa | |warning| Different deployment |
+--------------------------------------+-------------+-------------------+--------------------------------+





|en|




Credits
========

Authors
--------


* `KTec S.r.l. <https://www.ktec.it/>`__
* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors
-------------


* Luigi Di Naro <luigi.dinaro@ktec.it>
* Alex Comba <alex.comba@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

Maintainers
------------

|Odoo Italia Associazione|

This module is maintained by the Odoo Italia Associazione.

To contribute to this module, please visit https://odoo-italia.org/.



.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0
    :alt: Codecov
.. |OCA project| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg
    :target: https://github.com/OCA/l10n-italy/tree/7.0
    :alt: OCA
.. |Tech Doc| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg
    :target: http://wiki.zeroincombenze.org/en/Odoo/7.0/dev
    :alt: Technical Documentation
.. |Help| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg
    :target: http://wiki.zeroincombenze.org/it/Odoo/7.0/man
    :alt: Technical Documentation
.. |Try Me| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg
    :target: https://erp7.zeroincombenze.it
    :alt: Try Me
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md
   

''',
}
