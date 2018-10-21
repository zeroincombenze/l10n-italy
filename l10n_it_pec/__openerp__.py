# -*- coding: utf-8 -*-
#
# Copyright 2014    Associazione Odoo Italia
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
#    (<http://www.odoo-italia.org>).
#
{
    'name': 'Pec Mail',
    'version': '0.1',
    'category': 'Localisation/Italy',
    'author': 'Odoo Italian Community,Odoo Community Association (OCA)',
    'website': 'http://www.odoo-italia.org',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': ['views/partner_view.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'description': '''|en|

PEC Mail
=========

Add PEC Mail field in partner profile


|it|

Casella posta PEC
==================

Permette di inserire l'indirizzo di Posta Elettronica Certificata in anagrafica
cliente e fornitore.

|en|

Credits / Riconoscimenti
=========================

Authors / Autori
-----------------

* `Abstract <https://www.abstract.it>`__
* `Apulia Software <https://www.apuliasoftware.it>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Contributi
--------------------------

* Franco Tampieri <franco.tampieri@abstract.it>
* Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

Maintainers / Manutezione
--------------------------

|Odoo Italia Associazione|

This module is maintained by the Odoo Italia Associazione.

To contribute to this module, please visit https://odoo-italia.org/.


|

Last Update / Ultimo aggiornamento: 2018-10-21

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
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg
    :target: https://github.com/OCA/l10n-italy/tree/7.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/7.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/7.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg
    :target: https://erp7.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov Status| image:: badge-oca-codecov
    :target: oca-codecov-URL
    :alt: Codecov
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
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md

''',
}
