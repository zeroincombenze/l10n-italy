==============================================================
|icon| ITA - Account central journal/Libro giornale 10.0.0.0.7
==============================================================

**Print fiscal account journal**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_central_journal/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| This module prints the italian fiscal journal.

Italian law requires some specific data on journal layout: this module
respect these rules.

This module, sometime, is called account_central_journal.


|it| ::

    Cosa è:

Questo modulo permette di stampare il libro giornale secondo le regole legali e
fiscali italiane.
Questo modulo differisce dall'analogo modulo OCA per alcune caratteristiche.
Si prega di leggere attentamente le caratteristiche riportate in basso.



::

    Destinatari:

Tutti i soggetti passivi IVA

::

    Normativa e prassi:

* `Articolo 39 del  DPR n. 633/72 - Tenuta e conservazione documenti <https://def.finanze.it/DocTribFrontend/decodeurn?urn=urn:doctrib::DPR:1972-10-26;633_art39>`__
* `Articolo 22 del  DPR n. 600/72 - Tenuta e conservazione documenti <https://def.finanze.it/DocTribFrontend/decodeurn?urn=urn:doctrib::DPR:1973-09-29;600_art22>`__



Features | Caratteristiche
--------------------------

+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Description | Descrizione                                     | Z0incombenze(R)                 | OCA       | Note(s)                                      |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Number sequence | Numerazione progressiva                     | ✅                              | ✅        | Art. 2219 del CC                             |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Separation between moves | Riga separazione tra registrazioni | ✅                              | ❌        |                                              |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Print layout | Impaginazione                                  | Min larghezza colonne           |           | Miglioramenti layout                         |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Print layout | Impaginazione                                  | Importi a zero non stampati     | ❌        |                                              |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Journal search | Ricerca sezionali                            | Per azienda                     |           | Gestione multi-company                       |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Targert move | Finalità registrazioni                         | Solo contabilizzato             | All       | In stampa ufficiale è un controllo bloccante |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Date search | Ricerca per data                                |                                 |           | Procedimento modificato                      |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Print order | Ordine di stampa                                | date/name/id                    | date/name |                                              |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Final print | Stampa ufficiale                                | Aggiorna pagina su anno fiscale | ❌        |                                              |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+
| Paper orientation | Orientamento carta                        | Orizzontale o verticale         | Fixed     |                                              |
+---------------------------------------------------------------+---------------------------------+-----------+----------------------------------------------+



Configuration | Configurazione
------------------------------

☰ Accounting > Configuration > Accounting > Date Ranges

Create a date range of type "Fiscal Year" or set "Fiscal Year" value to
a date range to print.
This record gather the fiscal progressive values.



Usage | Utilizzo
----------------

☰ Accounting > Reports > Central Journal

Set value to print.

* Date Range: choice fiscal year date range to print
* Journal: journal list to print; default: all journals are printed
* Layout - Orientation: choice Portrit or Landscape (default) orientation
* Layout - Target Move: which entries with specific state to print (default posted)
* Layout - Last Printed Page: page number printed in previous journal (fiscal requirement)
* Layout - Start Row: 1st row number, next to previous journal last line (fiscal requirement)
* Layout - Year for footer: fiscal year to print in journal footer (fiscal requirement)

To print, click on button [Print] or [Final print].
Final Print cannot be repeated and set layout values on data range



Getting started | Primi passi
=============================

|Try Me|


Prerequisites | Prerequisiti
----------------------------

* python 2.7+ (best 2.7.5+)
* postgresql 9.2+ (best 9.5)

::

    cd $HOME
    # Follow statements activate deployment, installation and upgrade tools
    cd $HOME
    [[ ! -d ./tools ]] && git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -pUT
    source $HOME/devel/activate_tools



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

    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r l10n-italy -b 10.0 -G zero -p $HOME/10.0
    # Upgrade virtual environment
    vem amend $HOME/10.0/venv_odoo



Upgrade | Aggiornamento
-----------------------

::

    deploy_odoo update -r l10n-italy -b 10.0 -G zero -p $HOME/10.0
    vem amend $HOME/10.0/venv_odoo
    # Adjust following statements as per your system
    sudo systemctl restart odoo



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

10.0.0.0.8 (2023-12-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Layout orientation / Orientamento di stampa
* [IMP] Font size 9px / Dimensione fotn 9px
* [QUA] Test coverage 33% (199: 134+65) [0 TestPoints] - quality rating 40 (target 100)

10.0.0.0.7 (2023-09-28)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] 1st line numer / Primo numero di riga

10.0.0.0.6 (2023-07-31)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Upgraded layout / Aggiornamento impaginazione
* [FIX] Final print: update result / Stampa ufficiale aggiorna dati su anno fiscale
 



Credits | Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* `Dinamiche Aziendali <https://www.dinamicheaziendali.it>`__
* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Contributi da
----------------------------

* `Gianmarco Conte <gconte@dinamicheaziendali.it>`__
* `Lara Baggio <lbaggio@linkgroup.it>`__
* `Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>`__



Maintainer | Manutenzione
-------------------------

* `Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>`__



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

Last Update / Ultimo aggiornamento: 2023-12-23

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-black.png
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
