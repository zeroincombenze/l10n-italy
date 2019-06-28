
=======================================
|icon| base_rule_multireport 10.0.0.2.7
=======================================


**Manage document multiple reports**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/base_multireport/static/description/icon.png

|Maturity| |Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en|  Manage document multiple reports
--------------------------------------

Install this module if you wish to set rules to select
graphical document model to print, depending by:

* Journal
* Customer (some partner can have the own document model)
* Date (special model at specific time)
* Company
* Partner language
* Fiscal position
* Team

You can build your own customized report and add it to document report list.
You can find an customized invoice report example in this module.


|

|it| Gestisci modelli di stampa multipli
----------------------------------------

Installare questo modulo per stampare modelli multipli di documenti basati su:

* Sezionale (utile per gestire le fatture accompagnatorie)
* Partner (alcuni partner posso avare documenti persolizzati)
* Date (modelli speciali in particolai periodi dell'anno)
* Azienda
* Lingua partner
* Posizione fiscale
* Team

Si può anche costruire un modulo di fattura personalizzata da aggiungere
alla lista dei modelli.


|

Features / Caratteristiche
--------------------------

+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Feature / Funzione                                              | Status                                                                                                    | Notes / Note                                                                                                                                  |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Print original Odoo reports / Stampa modelli originali di Odoo  | |check|                                                                                                   | Style configuration /Configurazione a livello di stile                                                                                        |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Print product code / Stampa codice prodotto                     | |check|                                                                                                   | Configurable by report / Configurabile per ogni singolo report                                                                                |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Prin descriprion without code / Stampa descrizione senza codice | |check|                                                                                                   | Configurable by report / Configurabile per ogni singolo report                                                                                |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Print only logo header / Stampa solo logo in intestazione       | |check|                                                                                                   | Syle configuration: company info must be present in log / Configurabile a livello di stile: le informazioni aziendali vanno inserite nel logo |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| No print header / Non stampare intestazione                     | |check|                                                                                                   | Style configuration /Configurazione a livello di stile                                                                                        |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Configurable documents / Documenti configurabili:               | Sale order, Delivery document, Invoice, Purchase order / Ordine cliente, DdT, Fattura, Ordine a fornitore |                                                                                                                                               |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Watermark / Filigrana                                           | |check|                                                                                                   | High quality report / Stampa di alta qualità                                                                                                  |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Ending page / Pagina finale                                     | |check|                                                                                                   | Ending page with commercial info / Pagina finale con informazioni commerciali                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+


|

Usage / Utilizzo
----------------

This module gives a lot of pretty features to print nice reports.

Inside every report it is possible check for some characteristics and/or add some values.
Field name beginning with `doc_opts` are values from the specific report which is printing.
Field name beginning with `doc_style` are values from the style of the company.
Values in `doc_opts` are more priority than value in `doc_style`.

Look at follow table for details:

+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| Name                                                         | Description                           | Notes / Example                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| company                                                      | Company of current document           | Set by external layout                                                       |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| company_partner                                              | Company partner of current document   | Set by external layout                                                       |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| def_company                                                  | Default company                       | Set by module                                                                |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc                                                          | Current document which is printing    | Set by module. External layout set 'o' to compatibilit with Odoo reports     |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_model                                                    | Document model                        | Deprecated: use doc_opts.model                                               |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_opts                                                     | Document parameters                   |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_opts.code_mode                                           | Print code in document body           | <td t-if="doc_opts.code_mode=='print'"><span t-esc="l.code_2_print()"/></td> |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_opts.description_mode                                    | Print code in document body           | <td><span t-esc="l.description_2_print()"/></td>                             |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_opts.header                                              | Add header to report                  |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_opts.model                                               | Document model                        | Same as doc_model                                                            |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_opts.paperformat_id                                      | ID to paperformat                     |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_opts.report_name                                         | Report Name                           |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style                                                    | Style parameteres                     |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.custom_header                                      | No Header Logo                        | <div t-if="doc_style.custom_header"> .. </div>.                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.description_mode_account_invoice                   | `Print Description` (see below)       |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.description_mode_purchase_order                    | `Print Description` (see below)       |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.description_mode_sale_order                        | `Print Description` (see below)       |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.description_mode_stock_picking_package_preparation | `Print Description` (see below)       |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.header_account_invoice                             | `Header mode` (see below)             |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.header_purchase_order                              | `Header mode` (see below)             |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.header_sale_order                                  | `Header mode` (see below)             |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.header_stock_picking_package_preparation           | `Header mode` (see below)             |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.name                                               | Name of Style                         |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.origin                                             | `Report Identity` (see below)         |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.pdf_ending_page                                    | Ending Page PDF                       |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.pdf_watermark                                      | Default watermark for this style      |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.pdf_watermark_account_invoice                      | Sale Invoice default Watermark PDF    |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.pdf_watermark_purchase_order                       | Purchase Order default Watermark PDF  |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.pdf_watermark_sale_order                           | Sale Order default Watermark PDF      |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| doc_style.pdf_watermark_stock_picking_package_preparation    | Packing List default Watermark PDF    |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| o                                                            | Current invoice which is printing     | Alias used in invoice print set by external layout                           |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+
| style                                                        | Current `Report Identity` (see below) |                                                                              |
+--------------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------+



`Report Identity`

Report Identity is used to select standard Odoo reports or customized reports.
If value is 'Odoo' all customization is disabled and original Odoo reports are printed.
It is an attribute of company style.

`Print description`

This parameter manage the printing of description in document lines.
May be one of: 'as_is', 'line1', 'nocode', 'nocode1'

* as_is: that is the default value; it means description is printed as is, without manipulations
* line1: only the 1st line of description is printed
* nocode: product code (text between [brackets]) is removed
* nocode1: same of line1 + nocode

It is an attribute of specific report which is printing.

`Header mode`

This parameter set how header is printed. May be one of 'standard', 'logo', 'no_header'

* standard: standard Odoo header is printed
* logo: only the logo is printed, without text; logo must contain company informations
* no_header: no header is printed

It is an attribute of company style.

|

In xml report it is also possible test the existence of a field. The should be as follow:

`
<div t-if="'some_field' in docs[0]">FOUND SOME FIELD</div>
<div t-if="'some_field' not in docs[0]">NOT FOUND SOME FIELD</div>
`


|

OCA comparation / Confronto con OCA
-----------------------------------


+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+
| Description / Descrizione                                       | Zeroincombenze    | OCA            | Notes / Note                   |
+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+
| Coverage / Copertura test                                       |  |Codecov Status| | |OCA Codecov|  |                                |
+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+

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
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 10.0 -O zero
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 10.0 -vsy -o /opt/odoo/10.0

From UI: go to:

* |menu| Setting > Activate Developer mode 
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **base_multireport** > Install

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
* |menu| Setting > Apps |right_do| Select **base_multireport** > Update

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

10.0.0.2.7 (2019-06-21)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Error "description_2_print() takes exactly 2 arguments (1 given)"
* [FIX] Does not print fiscalcode on custom invoice


10.0.0.2.6 (2019-05-20)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Print code in document details


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

Last Update / Ultimo aggiornamento: 2019-06-27

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
