# -*- coding: utf-8 -*-
#
# Copyright 2012, Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2012, Domsense srl (<http://www.domsense.com>)
# Copyright 2017, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2012-2017, Associazione Odoo Italia <https://odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Italian Localisation - Withholding tax',
    'version': '7.0.0.2.1',
    'category': 'Localisation/Italy',
    'author': 'Odoo Community Association (OCA), ISA s.r.l., Agile Business Group sagl, SHS-AV s.r.l.',
    'website': 'https://odoo-community.org/',
    'license': 'AGPL-3',
    'depends': [
        'l10n_it_ade',
        'account_voucher_cash_basis',
        'account_invoice_entry_date',
    ],
    'data': [
        'views/account_view.xml',
        'views/account_invoice_view.xml',
    ],
    'demo': ['demo/account_demo.xml'],
    'test': ['test/purchase_payment.yml'],
    'installable': True,
    'description': r'''
Overview / Panoramica
=====================

|en| Purchase Invoices with Withholding Tax

|

|it| Ritenute d'acconto sulle fatture fornitore

Configurare i campi associati all'azienda:
 - Termine di pagamento della ritenuta d'acconto
 - Conto di debito per le ritenute da versare
 - Sezionale che conterrà le registrazioni legate alla ritenuta

L'importo della ritenuta d'acconto non è calcolato ma inserito manualmente.

|

Features / Caratteristiche
--------------------------

+----------------------------------------------+---------+-----------------------------------------+
| Feature / Funzione                           | Status  | Notes / Note                            |
+----------------------------------------------+---------+-----------------------------------------+
| Registrazione avvisi di parcella             | |check| | No in registri IVA                      |
+----------------------------------------------+---------+-----------------------------------------+
| Trasformazione avvisi di parcella in fattura | |check| | Con un tasto                            |
+----------------------------------------------+---------+-----------------------------------------+
| Registrazione importo ritenuta d'acconto     | |check| | Importo manuale                         |
+----------------------------------------------+---------+-----------------------------------------+
| Registrazione scadenza RA al pagamento       | |check| | Su conto RA con dettaglio per fornitore |
+----------------------------------------------+---------+-----------------------------------------+


|

Usage / Utilizo
---------------

* |menu| Contabilità > Varie > Termini di pagamento :point_right: Inserire termine di pagamento RA (al 15 del mese)
* |menu| Contabilità > Sezionali > Sezionali :point_right: Inserire sezionale avvisi di parcella
* |menu| Contabilità > Sezionali > Sezionali :point_right: Inserire sezionale avvisi ritenute d'acconto (se diverso da varie)
* |menu| Contabilità > Conti > Conti :point_right: Conto RA da pagare, tipo debito
* |menu| Configurazione > Configurazione > Contabilità :point_right: Impostare termini di pagamento ritenute
* |menu| Configurazione > Configurazione > Contabilità :point_right: Impostare termini conto ritenute
* |menu| Configurazione > Configurazione > Contabilità :point_right: Impostare sezionale ritenute
* |menu| Contabilità > Fornitori > Fatture Fornitori > Quando presente RA marcare il flag ed inserire importo

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

* `ISA s.r.l. <http://www.isa.it>`__
* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Collaboratori
----------------------------

* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Paolo Chiara <p.chiara@isa.it>
* Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>

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

Last Update / Ultimo aggiornamento: 2019-12-08

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
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0
    :alt: Codecov
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/7.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/7.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg
    :target: https://erp7.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov| image:: https://codecov.io/gh/OCA/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/7.0
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
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
