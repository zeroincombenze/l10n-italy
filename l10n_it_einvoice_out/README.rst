
==============================================================
|icon| Italian Localization - FatturaPA - Emission 10.0.1.0.11
==============================================================


**Electronic invoices emission**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_einvoice_out/static/description/icon.png

|Maturity| |Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en| EInvoice + FatturaPA
-------------------------

This module allows you to generate the fatturaPA XML file version 1.2.1
which will be sent to the SdI (Exchange System by Italian Tax Authority)

http://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm

|warning| Read carefully note of module l10n_it_einvoice_base before install this module


|

|it| Fattura Elettronica + FatturaPA
------------------------------------

Questo modulo permette di generare il file xml della fatturaPA versione 1.2
da trasmettere al sistema di interscambio SdI.

::

    Destinatari:

Il modulo è destinato a tutte le aziende che dal 2019 dovranno emettere fattura elettronica


::

    Normativa:

Le leggi inerenti la fattura elettronica sono numerose. Potete consultare la `normativa fattura elettronica <https://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm>`__

Per maggiori info leggere le informazioni relative al modulo l10n_it_einvoice_base


|

Features / Caratteristiche
--------------------------

+--------------------------------------+----------+----------------------------------------------+
| Feature / Funzione                   |  Status  | Notes / Note                                 |
+--------------------------------------+----------+----------------------------------------------+
| Emissione FatturaPA                  | |check|  | Genera file .xml versione 1.2.1              |
+--------------------------------------+----------+----------------------------------------------+
| Emissione Fattura B2B                | |check|  | Genera file .xml versione 1.2.1              |
+--------------------------------------+----------+----------------------------------------------+
| Emissione Fattura a privato senza PI | |check|  | Genera file .xml versione 1.2.1              |
+--------------------------------------+----------+----------------------------------------------+
| E-fattura a rappresentante fiscale   | |check|  | Genera file .xml versione 1.2.1              |
+--------------------------------------+----------+----------------------------------------------+
| E-fattura a stabile organizzazione   | |check|  | Genera file .xml versione 1.2.1              |
+--------------------------------------+----------+----------------------------------------------+
| Dati azienda da fattura              | |check|  |                                              |
+--------------------------------------+----------+----------------------------------------------+
| Controllo dati durante inserimento   | |check|  |                                              |
+--------------------------------------+----------+----------------------------------------------+


|
|

Certifications / Certificazioni
-------------------------------

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| Logo                 | Ente/Certificato                                                                                                                                                                                                  | Data inizio   | Da fine      | Note                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |xml\_schema|        | `ISO + Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__                             | 01-06-2017    | 31-12-2019   | Validazione contro schema xml                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |FatturaPA|          | `FatturaPA <https://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Comunicazioni/Fatture+e+corrispettivi/Fatture+e+corrispettivi+ST/ST+invio+di+fatturazione+elettronica/?page=schedecomunicazioni/>`__  | 01-06-2017    | 31-12-2019   | Controllo tramite sito Agenzia delle Entrate |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+


|

Usage / Utilizzo
----------------

|menu| Configurazione > Configurazione > Contabilità > Fattura PA |do_right| Impostare i vari parametri

|menu| Contabilità > Configurazione > Sezionali > Sezionali |do_right| Impostare sezionale fattura elettronica

|menu| Contabilità > Configurazione > Imposte > Imposte |do_right| Impostare natura codici IVA

|menu| Contabilità > Configurazione > Management > Termini di pagamento |do_right| Collegare i termini di pagamento con i relativi termini fiscali

|menu| Contabilità > Clienti > Clienti |do_right| Impostare Codice Destinatario o PEC o IPA, nazione, partita IVA, codice fiscale

|menu| Contabilità > Configurazione > Contabilità > Posizioni fiscali |do_right| Collegare posizioni fiscali con regimi fiscali

Per consultazione (non modificare):

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Natura dell'IVA

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Tipi Fattura


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
* |menu| Setting > Apps |right_do| Select **l10n_it_einvoice_out** > Install

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
* |menu| Setting > Apps |right_do| Select **l10n_it_einvoice_out** > Update

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

10.0.1.0.11 (2019-11-07)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] PA with VAT number / Reinserita partita IVA per fatture PA
* [IMP] No fiscal code if equal to TIN (by parameter) / Codice fiscale non inserito se equale alla partita IVA (parametrico)


10.0.1.0.10 (2019-09-27)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Set xml data for Foreign customers w/o vat / Compilato il campo partita IVA per clienti esteri senza P.IVA


10.0.1.0.9 (2019-07-30)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] If customer has flag PA, vat becomes fiscal code / Se cliente con flag PA trasforma la P.IVA in codice fiscale


10.0.1.0.8 (2019)
~~~~~~~~~~~~~~~~~

* [FIX] No vat id customer is PA or no-profit company / Se cliente PA o ente no-profit non è inserita la P.IVA nel file xml


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

* `Davide Corio <info@davidecorio.com>`__
* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `Innoviu srl <http://www.innoviu.com>`__
* `Odoo Italia Network`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


Contributors / Collaboratori
----------------------------

* Davide Corio
* Roberto Onnis <roberto.onnis@innoviu.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Alessio Gerace <alessio.gerace@agilebg.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>


Translations by / Traduzioni a cura di
--------------------------------------

* Sergio Zanchetta <https://github.com/primes2h>
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
