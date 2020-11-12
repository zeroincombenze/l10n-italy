
========================================
|icon| Agenzia delle Entrate 10.0.0.1.14
========================================


**Codice e definizioni come da Agenzia delle Entrate**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_ade/static/description/icon.png

|Maturity| |Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en| Tax Authority Definitions
==============================

This module has no specific function for End-user.

It defines the structures by Italian IRS (Tax Authority) to manage
all fiscal communications.
Inside there are xml schema files used by FatturaPA, EInvoice and VAT settlement.

This module requires `PyXB 1.2.4 <http://pyxb.sourceforge.net/>`__ or `PyXB 1.2.5 <http://pyxb.sourceforge.net/>`__

This code partially inherits some parts from l10n_it_account of OCA.

|

|it| Definizioni Agenzia delle Entrate
======================================

Questo modulo non ha funzioni specifiche per l'utente finale.
Contiene dati e definizioni come stabilito dall'Agenzia delle Entrate
All'interno sono presenti gli schemi xml usati da FatturaPA,
Fattura Elettronica B2B, Liquidazione IVA elettronica e Comunicazione IVA.

|info| Questo modulo è incompatibile con alcuni moduli OCA.

Tutti i moduli che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate devono dichiare il modulo
`l10n_it_ade <https://github.com/zeroincombenze/l10n-italy/tree/10.0/l10n_it_ade>`__ come dipendenza.

Questo modulo eredita alcune parti di codice del modulo l10n_it_account di OCA.


|

Features / Caratteristiche
--------------------------

Features / Funzioni
-------------------

+------------------------------------------------------+----------+----------------------------------------------+
| Feature / Funzione                                   |  Status  | Notes / Note                                 |
+------------------------------------------------------+----------+----------------------------------------------+
| Fiscal Invoice Type / Tipo fattura fiscale           | |check|  | Codifica tipo di fattura come da AdE         |
+------------------------------------------------------+----------+----------------------------------------------+
| Codice Carica                                        | |check|  | Codifica codice carica come da AdE           |
+------------------------------------------------------+----------+----------------------------------------------+
| Tax Nature / Natura fiscale dell'IVA                 | |check|  | Codifica natura fiscale dell'IVA come da AdE |
+------------------------------------------------------+----------+----------------------------------------------+


|
|

Certifications / Certificazioni
-------------------------------

Certifications / Certificazioni
-------------------------------

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| Logo                 | Ente/Certificato                                                                                                                                                                                                  | Data inizio   | Da fine      | Note                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |xml\_schema|        | `ISO + Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__                             | 01-06-2017    | 31-12-2020   | Validazione contro schema xml                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |FatturaPA|          | `FatturaPA <https://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Comunicazioni/Fatture+e+corrispettivi/Fatture+e+corrispettivi+ST/ST+invio+di+fatturazione+elettronica/?page=schedecomunicazioni/>`__  | 01-06-2017    | 31-12-2020   | Controllo tramite sito Agenzia delle Entrate |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+


|

Usage / Utilizzo
----------------

Usage / Uso
===========

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Natura dell'IVA

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Tipi Fattura

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Codice Carica


|

OCA comparation / Confronto con OCA
-----------------------------------

+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+
| Dato Fattura Elettronica       | Modulo zeroincombenze       | Modello zeroincombenze    | Nome tecnico                 | Modulo OCA                  | Modello OCA               | Note tecnico OCA             | Note                                                                                                     |
+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+
| Schema di definizione xsd      | l10n_it_ade                 |                           |                              | l10n_it_fatturapa           |                           |                              | Il modulo di zeroincombenze serve anche alla liquidazione IVA e comunicazione IVA (ex Spesometro)        |
+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+
| Natura dell'IVA                | l10n_it_ade                 | italy.ade.tax.nature      | nature_id                    | l10n_it_account_tax_kind    | account.tax.kind          | tax_kind_id                  | Estensione della tabella account.tax usata anche da liquidazione IVA e comunicazione IVA (ex Spesometro) |
+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+
| Termini di pagamento           | l10n_it_fiscal_payment_term | fatturapa.payment_term    |                              | l10n_it_fiscal_payment_term | fatturapa.payment_term    |                              | Modelle in comune                                                                                        |
+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+
| Metodi di pagamento            | l10n_it_fiscal_payment_term | fatturapa.payment_method  |                              | l10n_it_fiscal_payment_term | fatturapa.payment_method  |                              | Modello in comune                                                                                        |
+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+
| Codice Destinatario            | l10n_it_fiscal_ipa          | res.partner               | codice_destinatario          | l10n_it_fatturapa           | res.partner               | codice_destinatario          |                                                                                                          |
+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+
| Partner è PA?                  | l10n_it_fiscal_ipa          | res.partner               | is_pa                        | l10n_it_fatturapa           | res.partner               | is_pa                        |                                                                                                          |
+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+
| Soggetto a Fattura elettronica | l10n_it_fiscal_ipa          | res.partner               | electronic_invoice_subjected | l10n_it_fatturapa           | res.partner               | electronic_invoice_subjected | Il comportamento è diverso                                                                               |
+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+
| Regime Fiscale                 | l10n_it_fatturapa           | fatturapa.fiscal_position | fiscal_position              | l10n_it_fatturapa           | fatturapa.fiscal_position |                              |                                                                                                          |
+--------------------------------+-----------------------------+---------------------------+------------------------------+-----------------------------+---------------------------+------------------------------+----------------------------------------------------------------------------------------------------------+


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
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__    |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| /home/odoo/10.0/l10n-italy/                                                |
+----------------------------------------------------------------------------+

::

    cd $HOME
    # Tools installation & activation: skip if you have installed this tool
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    source /opt/odoo/dev/activate_tools
    # Odoo installation
    odoo_install_repository l10n-italy -b 10.0 -O zero
    vem create /opt/odoo/VENV-10.0 -O 10.0 -DI

From UI: go to:

* |menu| Setting > Activate Developer mode 
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **l10n_it_ade** > Install


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

    cd $HOME
    # Tools installation & activation: skip if you have installed this tool
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    source /opt/odoo/dev/activate_tools
    # Odoo upgrade
    odoo_install_repository l10n-italy -b 10.0 -O zero -U
    vem amend /opt/odoo/VENV-10.0 -O 10.0 -DI
    # Adjust following statements as per your system
    sudo systemctl restart odoo

From UI: go to:

* |menu| Setting > Activate Developer mode
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **l10n_it_ade** > Update

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

ChangeLog History / Cronologia modifiche
----------------------------------------

10.0.0.1.14 (2020-11-07)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] New xml schema binding / Nuovi file xml


10.0.0.1.13 (2019-06-13)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Symbols quotes and double quotes / Conversione simboli '«»' e apostrofo


10.0.0.1.13 (2019-06-13)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Dim_text function / field to search for similarity 


< 10.0.0.1.13 (2018)
~~~~~~~~~~~~~~~~~~~~

* [IMP] Use both pyxb 1.2.4 both 1.2.5 (automatic detection)
* [IMP] File xml without characters not accepted by Tax Authority
* [FIX] Link fiscal type refund by refund / Riconoscimento NC fiscale da documento Odoo

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

* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


Contributors / Collaboratori
----------------------------

* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>


Acknowledges / Riconoscimenti
-----------------------------

+-----------------------------------+-------------------------------------------+
| |en|                              | |it|                                      |
+-----------------------------------+-------------------------------------------+
| This software inherits from past  | Questo software eredita da versioni       |
| versions some parts of code. Even | passate alcune parti di codice. Anche     |
| if people did not actively        | se non hanno partecipato attivamente allo |
| participate to development, we    | allo sviluppo, noi siamo grati a tutte le |
| acknowledge them for their prior  | persone che precedentemente vi hanno      |
| contributions.                    | contribuito.                              |
+-----------------------------------+-------------------------------------------+

* Davide Corio <info@davidecorio.com>
* Alex Comba <alex.comba@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>

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

Last Update / Ultimo aggiornamento: 2020-11-11

.. |Maturity| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
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
   :target: https://t.me/axitec_helpdesk

