# -*- coding: utf-8 -*-
#
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2009 Zikzakmedia S.L. (http://zikzakmedia.com)
#                       Jordi Esteve <jesteve@zikzakmedia.com>
#    Copyright (c) 2008 ACYSOS S.L. (http://acysos.com)
#                       Pedro Tarrafeta <pedro@acysos.com>
#    Copyright (C) 2011 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>).
#    Copyright (C) 2012 Agile Business Group sagl (<http://www.agilebg.com>)
#    Copyright (C) 2012 Domsense srl (<http://www.domsense.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    'name': 'Fiscal Year Closing',
    'version': '7.0.1.0.1',
    'category': 'Generic Modules/Accounting',
    'author': 'Odoo Community Association (OCA), Pexego,',
    'website': 'https://www.odoo-community.org',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'account',
    ],
    'installable': True,
    'update_xml': [
        'security/ir.model.access.csv',
        'fyc_workflow.xml',
        'wizard/wizard_run.xml',
        'fyc_view.xml',
        'hide_account_wizards.xml',
    ],
    'active': False,
    'description': r'''
Overview / Panoramica
=====================

|en| Fiscal Year Closing Wizard
-------------------------------

Generalization of l10n_es_fiscal_year_closing (http://apps.openerp.com/addon/4506)

Replaces the default OpenERP end of year wizards (from account module)
with a more advanced all-in-one wizard that will let the users:

* Check for unbalanced moves, moves with invalid dates or period or draft moves on the fiscal year to be closed.
* Create the Loss and Profit entry.
* Create the Net Loss and Profit entry.
* Create the Closing entry.
* Create the Opening entry.

It is stateful, saving all the info about the fiscal year closing, so the
user can cancel and undo the operations easily.


|

|it| Chiusure e riaperture contabili
------------------------------------

Completa l'ordinaria apertura di Odoo in conformità alle leggi fiscali italiane.

Permette:

* Verifica sbilanciamento e date delle operazioni contabili
* Registra l'operazione di profitti e perdite
* Registra l'operazione di perdita o utile di esercizio
* Registra le operazioni di chiusura contabile
* Registra le operazioni di riapertura contabile


|

Usage / Utilizo
---------------

|it| Operazioni di chiusura e riapertura

* Registrazione nuovo esercizio
* Controlli
* Stampe fiscali di fine anno
* Apertura provvisoria esercizio (eventuale)
* Cancellazione apertura provvisoria (eventuale)
* Chiusura esercizio
* Apertura esercizio

`Registrazione nuovo esercizio`

| menu | contabilità > Configurazione > periodi > anni fiscali


`Controlli`

Prima di procedere con le operazioni di chiusura e riapertura procedere con i seguenti controlli:

* Determinazione registrazioni stato bozza
* Sezionale apertura
* Sezionale di chiusura profitti e perdite
* Sezionale di chiusura utile o perdita
* Sezionale di chiusura patrimoniale


.. image:: /account_fiscal_year_closing/static/src/img/sezionale_apertura.png
    :alt: sezionale apertura

.. image:: /account_fiscal_year_closing/static/src/img/sezionale_chiusura_pp.png
    :alt: sezionale chiusura


|
|

Support / Supporto
------------------


|Zeroincombenze| This module is maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


|
|

Credits / Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


|

Authors / Autori
----------------

* `Pexego <http://www.pexego.es/>`__
* `Zikzakmedia S.L. <http://zikzakmedia.com>`__
* `ACYSOS S.L. <http://acysos.com>`__
* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `Agile Business Group sagl <http://www.agilebg.com>`__
* `Domsense srl <http://www.domsense.com>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


Contributors / Collaboratori
----------------------------

* Borja López Soilán (Pexego) - borja@kami.es
* Lorenzo Battistini - lorenzo.battistini@agilebg.com
* Jordi Esteve <jesteve@zikzakmedia.com>
* Pedro Tarrafeta <pedro@acysos.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>


|

----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://wiki.zeroincombenze.org/en/Odoo>`__ è progettata per le esigenze del mercato italiano.

|

This module is part of l10n-italy project.

Last Update / Ultimo aggiornamento: 2019-05-15

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/7.0
    :alt: Codecov
.. |OCA project| image:: /account_fiscal_year_closing/static/src/img/Unknown badge-OCA
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
.. |OCA Codecov Status| image:: https://codecov.io/gh/OCA/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/7.0
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
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
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
''',
}
