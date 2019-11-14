
===================================
|icon| Fiscal Year Closing 10.0.1.0
===================================


.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/account_fiscal_year_closing/static/description/icon.png

|Maturity| |Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


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

Usage / Utilizzo
----------------

|it| Operazioni di chiusura e riapertura

* Registrazione nuovo esercizio
* Controlli
* Stampe fiscali di fine anno
* Apertura provvisoria esercizio (eventuale)
* Cancellazione apertura provvisoria (eventuale)
* Chiusura esercizio
* Apertura esercizio

`Registrazione nuovo esercizio`

|menu| contabilità > Configurazione > periodi > anni fiscali


`Controlli`

Prima di procedere con le operazioni di chiusura e riapertura procedere con i seguenti controlli:

* Determinazione registrazioni stato bozza
* Sezionale apertura
* Sezionale di chiusura profitti e perdite
* Sezionale di chiusura utile o perdita
* Sezionale di chiusura patrimoniale


.. image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/account_fiscal_year_closing/static/description/sezionale_apertura.png
    :alt: sezionale apertura

.. image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/account_fiscal_year_closing/static/description/sezionale_chiusura_pp.png
    :alt: sezionale chiusura

stamp

|
|

Getting started / Come iniziare
===============================

|Try Me|


|

Installation / Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__         |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| /opt/odoo/10.0/l10n-italy/                                                 |
+----------------------------------------------------------------------------+

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    source /opt/odoo/dev/activate_tools
    odoo_install_repository l10n-italy -b 10.0 -O zero
    sudo manage_odoo requirements -b 10.0 -vsy -o /opt/odoo/10.0

From UI: go to:

* |menu| Setting > Activate Developer mode 
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **account_fiscal_year_closing** > Install

|

Upgrade / Aggiornamento
-----------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| When you want upgrade and you   | Per aggiornare, se avete installato con  |
| installed using above           | le istruzioni di cui sopra:              |
| statements:                     |                                          |
+---------------------------------+------------------------------------------+

::

    odoo_install_repository l10n-italy -b 10.0 -O zero -U
    # Adjust following statements as per your system
    sudo systemctl restart odoo

From UI: go to:

* |menu| Setting > Activate Developer mode
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **account_fiscal_year_closing** > Update

|

Support / Supporto
------------------


|Zeroincombenze| This module is maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


|
|

Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------


|en| If you have a proposal to change this module, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare questo modulo, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.

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


|chat_with_us|


|

This module is part of l10n-italy project.

Last Update / Ultimo aggiornamento: 2019-11-14

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0
    :alt: Codecov
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/10.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/10.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov| image:: https://codecov.io/gh/OCA/l10n-italy/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/10.0
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
