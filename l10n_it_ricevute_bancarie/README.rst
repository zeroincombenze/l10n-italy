==============================================================
|icon| Ricevute Bancarie/l10n_it_ricevute_bancarie 10.0.1.3.14
==============================================================

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_ricevute_bancarie/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| Module to manage Ricevute Bancarie


|

|it| Modulo per gestire i pagamenti tramite ricevuta bancaria e presentazione distinta in banca.

Si può configurare un conto bancario di presentazione di tipo SBF (Salvo Buon Fine) o DI (Dopo Incasso).
Con la distinta DI nessuna operazione contabile è gestita dal programma.
Si può solo generare il file CBI da inviare in banca.
Con la distinta SBF sono gestite tutte le operazioni contabili come esposto in questo documento.

Le operazioni contabili sono configurabili.



Features | Caratteristiche
--------------------------

+-------------------------------------------+---------+----------------------+
| Feature / Funzione                        | Status  | Notes / Note         |
+-------------------------------------------+---------+----------------------+
| Emissione distinte RiBa                   | |check| |                      |
+-------------------------------------------+---------+----------------------+
| Download file CBI per la banca            | |check| |                      |
+-------------------------------------------+---------+----------------------+
| Registrazioni contabili                   | |check| | Se tipo distinta SBF |
+-------------------------------------------+---------+----------------------+
| Ripristino distinta allo stato precedente | |check| |                      |
+-------------------------------------------+---------+----------------------+
| Gestione insoluti                         | |check| |                      |
+-------------------------------------------+---------+----------------------+
| Ripristino scadenza insoluto o pagata     | |check| |                      |
+-------------------------------------------+---------+----------------------+
| Stampa distinta                           | |check| |                      |
+-------------------------------------------+---------+----------------------+



|

Usage | Utilizzo
----------------

L'utilizzo delle Ri.Ba. utilizza i seguenti menù:

|menu| Contabilità > Pagamenti > Ri.Ba Configurazione

|menu| Contabilità > Management > Termini di pagamento

|menu| Contabilità > Ri.Ba > Distinte

|menu| Contabilità > Ri.Ba > Emetti Ri.Ba

|menu| Contabilità > Ri.Ba > Fatture insolute


Configurazione
~~~~~~~~~~~~~~

Nella configurazione delle Ri.Ba. è possibile specificare il tipo di distinta:

* DI (Dopo Incasso): nessuna registrazione è effettuata automaticamente
* SBF (Salvo Buon Fine): sono emesse le registrazioni come descritte qui sotto

Per attivare la gestione Ri.Ba. è necessario impostare il tipo 'Ri.Ba.' nei termini di pagamento.


Gestione distinta
~~~~~~~~~~~~~~~~~

Ai fini di una corretta comprensione si ipotizza la gestiona da una fattura da 100€ + IVA.
Si ricorda che a scrittura contabile è della fattura è la seguente:

+-----------+------------------------------------------+---------+---------+-----------+
| Riga      | Descrizione                              | D       | A       | Note      |
+-----------+------------------------------------------+---------+---------+-----------+
| 1         | Emessa fattura                           |         |         |           |
+-----------+------------------------------------------+---------+---------+-----------+
| 1.1       | Crediti v/clienti                        | 122     |         |           |
+-----------+------------------------------------------+---------+---------+-----------+
| 1.2       | Ricavi                                   |         | 100     |           |
+-----------+------------------------------------------+---------+---------+-----------+
| 1.3       | IVA                                      |         | 22      |           |
+-----------+------------------------------------------+---------+---------+-----------+



Per iniziare il flusso, usare il menù `Contabilità > Ri.Ba > Emetti Ri.Ba`, selezionare le scadenze da inserire in distinta
e dal bottone `Azione` selezionare `Emetti Ri.Ba`. Scegliere un conto bancario configurato.

Scaricare il file CBI da presentare in banca: dal bottone `Azione` selezionare `Esporta Ri.Ba`.

Quando la banca conferma l'accettazione della distinta, dal menù `Contabilità > Ri.Ba > Emetti Ri.Ba`
selezionare la distinta ed impostare lo stato di `Accettata` tramite l'apposito bottone.
Se la distinta è di tipo SBF viene generata la seguente scrittura contabile (una registrazionne per ogni scadenza in distinta):

+--------+------------------------------+------+------+-----------------------------------+
| Riga   | Descrizione                  | D    | A    | Note                              |
+--------+------------------------------+------+------+-----------------------------------+
| 2      | Emissione RiBA               |      |      |                                   |
+--------+------------------------------+------+------+-----------------------------------+
| 2.1    | Crediti v/clienti            |      | 122  | Riconciliata con 1.1              |
+--------+------------------------------+------+------+-----------------------------------+
| 2.2    | Effetti SBF                  | 122  |      |                                   |
+--------+------------------------------+------+------+-----------------------------------+



Quando la banca accredita la distinta, impostare lo stato `Accreditata` tramite l'apposito bottone.
Se la distinta è di tipo SBF si può generare la seguente scrittura contabile:

+----------+-------------------------------------------------+--------+--------+----------+
| Riga     | Descrizione                                     | D      | A      | Note     |
+----------+-------------------------------------------------+--------+--------+----------+
| 3        | Accredito distinta RiBA                         |        |        |          |
+----------+-------------------------------------------------+--------+--------+----------+
| 3.1      | Banca c/effetti                                 |        | 122    |          |
+----------+-------------------------------------------------+--------+--------+----------+
| 3.2      | Banca c/c                                       | 120    |        |          |
+----------+-------------------------------------------------+--------+--------+----------+
| 3.3      | Spese bancarie                                  | 2      |        |          |
+----------+-------------------------------------------------+--------+--------+----------+



Quando la ricevuta è effettivamente pagata dal cliente è possibile dichiararlo nella relativa riga della distinta.
Se la distinta è di tipo SBF viene generata la sequente scrittura contabile:

+--------+--------------------------------+------+------+----------------------------------+
| Riga   | Descrizione                    | D    | A    | Note                             |
+--------+--------------------------------+------+------+----------------------------------+
| 4      | Pagamento effettivo            |      |      |                                  |
+--------+--------------------------------+------+------+----------------------------------+
| 4.1    | Effetti SBF                    |      | 122  | Riconciliata con 2.2             |
+--------+--------------------------------+------+------+----------------------------------+
| 4.2    | Banca c/effetti                | 122  |      | Riconciliata con 3.1             |
+--------+--------------------------------+------+------+----------------------------------+




Note finali
~~~~~~~~~~~

Per ogni stato della distinta è possibile sia avanzare allo stato successivo che ripristinare lo stato precedente.
Le relative registrazioni contabili saranno inserite o rimosse in modo da mantenere il sistema sempre nel corretto stato contabile.

Si può dichiarare ogni singola scadenza come pagata o insoluta. Anche per le singole scadenze è possibili ripristinare lo stato precedente.



Getting started | Primi passi
=============================

|Try Me|


Prerequisites | Prerequisiti
----------------------------

* python 2.7+ (best 2.7.5+)
* postgresql 9.2+ (best 9.5)



Installation | Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instructions are just an  | Istruzioni di esempio valide solo per    |
| example; use on Linux CentOS 7+ | distribuzioni Linux CentOS 7+,           |
| Ubuntu 14+ and Debian 8+        | Ubuntu 14+ e Debian 8+                   |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__ |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| $HOME/10.0 |
+----------------------------------------------------------------------------+

::

    cd $HOME
    # *** Tools installation & activation ***
    # Case 1: you have not installed zeroincombenze tools
    git clone https://github.com/zeroincombenze/tools.git
    cd $HOME/tools
    ./install_tools.sh -pT
    source $HOME/devel/activate_tools
    # Case 2: you have already installed zeroincombenze tools
    cd $HOME/tools
    ./install_tools.sh -UT
    source $HOME/devel/activate_tools
    # *** End of tools installation or upgrade ***
    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r l10n-italy -b 10.0 -G zero -p $HOME/10.0
    # Upgrade virtual environment
    vem amend $HOME/10.0/venv_odoo

From UI: go to:

* |menu| Setting > Activate Developer mode
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **l10n_it_ricevute_bancarie** > Install



Upgrade | Aggiornamento
-----------------------

::

    cd $HOME
    # *** Tools installation & activation ***
    # Case 1: you have not installed zeroincombenze tools
    git clone https://github.com/zeroincombenze/tools.git
    cd $HOME/tools
    ./install_tools.sh -pT
    source $HOME/devel/activate_tools
    # Case 2: you have already installed zeroincombenze tools
    cd $HOME/tools
    ./install_tools.sh -UT
    source $HOME/devel/activate_tools
    # *** End of tools installation or upgrade ***
    # Odoo repository upgrade
    deploy_odoo update -r l10n-italy -b 10.0 -G zero -p $HOME/10.0
    vem amend $HOME/10.0/venv_odoo
    # Adjust following statements as per your system
    sudo systemctl restart odoo

From UI: go to:

* |menu| Setting > Activate Developer mode
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **l10n_it_ricevute_bancarie** > Update



Support | Supporto
------------------

|Zeroincombenze| This module is supported by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved | Ci mettiamo in gioco
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



ChangeLog History | Cronologia modifiche
----------------------------------------

10.0.1.3.14 (2023-09-14)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] RiBA account reconciled after payment / Conto effetti attivi riconciliato dopo incasso
* [IMP] Unsolved accounts set automatically / Conti insoluti imposttai automaticamente
* [QUA] Test coverage 78% (1141: 252+889) [258 TestPoints] - quality rating 46/100

10.0.1.3.13 (2023-08-03)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Overdue with expenses / Insoluto con spese
* [QUA] Test coverage 66% (1155: 389+766) [113 TestPoint]

10.0.1.3.12 (2023-05-24)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Two supplemental accreditation accounts / Due conti aggiuntivi in accredito
* [FIX] Confirm payment / Conferma pagamento

10.0.1.3.11 (2023-04-17)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Confirm invoice + refund / Errore accettazione fattura + NC

10.0.1.3.10 (2022-12-30)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Riba flag updatable / Scadenza Riba modificabile
* [REF] Process refactoring

10.0.1.3.9 (2022-07-20)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Riba flag read-only / Scadenza Riba non modificabile

10.0.1.3.8 (2022-06-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [TNL] Translation
* [IMP] Riba flag updatable / Scadenza Riba modificabile

10.0.1.3.7 (2022-05-03)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Unsoved with 2 or more invoices / Insoluto di 2 o più fatture

10.0.1.3.6 (2022-01-28)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Button [Cancel] in list / Bottone [Annulla] in distinta
* [IMP] Button [Back2Draft] in list / Bottone [Riporta in bozza] in distinta



Credits | Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* Odoo Community Association (OCA) <https://odoo-community.org>
* Agile Business Group sagl <https://www.agilebg.com>
* Apulia Software s.r.l. <https://www.apuliasoftware.it>
* SHS-AV s.r.l. <https://www.zeroincombenze.it>



Contributors | Contributi da
----------------------------

* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Andrea Cometa <a.cometa@apuliasoftware.it>
* Andrea Gallina <a.gallina@apuliasoftware.it>
* Davide Corio <info@davidecorio.com>
* Giacomo Grasso <giacomo.grasso@agilebg.com>
* Gabriele Baldessari <gabriele.baldessari@gmail.com>
* Alex Comba <alex.comba@agilebg.com>
* Antonio M. Vigliotti <info@shs-av.com>



Maintainer | Manutenzione
-------------------------

Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>



----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://www.zeroincombenze.it/>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://www.zeroincombenze.it/>`__ è progettata per le esigenze del mercato italiano.


|
|

This module is part of l10n-italy project.

Last Update / Ultimo aggiornamento: 2023-11-09

.. |Maturity| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0
    :target: https://travis-ci.com/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
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
   :target: https://t.me/Assitenza_clienti_powERP
