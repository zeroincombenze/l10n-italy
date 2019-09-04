
========================================
|icon| base_rule_multireport 10.0.0.2.13
========================================


**Manage document multiple reports**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/base_multireport/static/description/icon.png

|Maturity| |Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en|  Manage document multiple reports
--------------------------------------

Install this module if you wish to wish customize your report printing.

The module is built on follow concepts:

* Module customize order, invoice and delivery documents
* Module does not disable standard Odoo modules: you can use them whenever you want
* You can use this module as base of your custom report module
* Configuration parameters are organized as a hierarchical tree



|

|it| Gestisci modelli di stampa multipli
----------------------------------------

Installate questo modulo se volete personalizzare i modelli di stampa.

Il modulo è costruito sui seguenti concetti:

* Personalizza ordini, fatture e documenti di trasporto
* Il modulo non disabilita i modelli standard di Odoo, che potete utilizzare in qualsiasi momento
* Potete usare questo modulo come base per un vostro modulo di personalizzazione stampe
* I parametri di configurazione sono organizzati tramite albero gerarchico


|

Features / Caratteristiche
--------------------------

+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Feature / Funzione                                                            | Notes / Note                                                                                              |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Print original Odoo reports / Stampa modelli originali di Odoo                | Style configuration = Odoo/Configurazione a livello di stile = Odoo                                       |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Header line-up: logo and slogan / Intestazione solo logo e slogan             |                                                                                                           |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Header line-up: logo and company data / Intestazione solo logo e dati azienda | Company data shifted up / Dati aziende spostati in alto                                                   |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Header with only wide logo / Intestazione solo logo largo                     | Logo with company data / Logo con i dati dell'azienda                                                     |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Header without data / No intestazione                                         | Use preprinted paper / Utilizzo su carta intestata                                                        |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Optiona separation line / Linea di separazione opzionale                      |                                                                                                           |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Address mode / Modo stampa indirizzo                                          | Print 2 addresses or only the specific one / Stampa doppio indirizzo o solo specifico                     |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Print product code / Stampa codice prodotto                                   |                                                                                                           |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Print descriprion without code / Stampa descrizione senza codice              | Extract code from description / Estrapola il codice dalla descrizione                                     |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Configurable documents / Documenti configurabili:                             | Sale order, Delivery document, Invoice, Purchase order / Ordine cliente, DdT, Fattura, Ordine a fornitore |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Watermark / Filigrana                                                         | High quality report / Stampa di alta qualità                                                              |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Ending page / Pagina finale                                                   | Ending page with commercial info / Pagina finale con informazioni commerciali                             |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+


|

Usage / Utilizzo
----------------

This module gives a lot of pretty features to print nice reports.

Inside every report it is possible check for some characteristics and/or add some values.
The value of every parameter is evaluate in fallback way.
The fallback path is:
1. Valid value (not null and not space) in report (model ir_action_report_xml)
2. Valid value (not null and not space) in template of report (model multireport.template), if declared
3. Valid value (not null and not space) in specific document style (model multireport.style)
4. Value in default document style (model multireport.style)
5. For some parameters, for historical reason, value may be load from other sources (i.e. custom footer)

In report the fallback function is report.get_report_attrib(PARAM,o,doc_opts), where param is parme to get value.

Report may load specific value if declare field as follow:
* If field name beginning with `doc_opts`, value is from the specific report which is printing.
* If Field name beginning with `doc_style`, value is from the style of the company.

Warning! If report get value directly from report or style, can get a None value and result may be unexpected.

Look at follow table for details:

+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| Name                       | Description                                 | Notes / Example                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| address_mode               | Which addresses are printed                 |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| bottom_text                | Text to print at the bottom of the document |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| code                       | Product code                                |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| code_mode                  | Print code in document body                 | <t t-set="code_mode" t-value="report.get_report_attrib('code_mode',o,doc_opts)"/>               |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| company                    | Company of current document                 | Set by external layout                                                                          |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| company_partner            | Company partner of current document         | Set by external layout                                                                          |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| ddt_ref_text               | Text at every change of delivery document   |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| def_company                | Default company                             | Set by Odoo report module                                                                       |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| description_mode           | Print code in document body                 | <t t-set="description_mode" t-value="report.get_report_attrib('description_mode',o,doc_opts)"/> |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| doc                        | Current document which is printing          | Set by module. External layout set 'o' to compatibility with Odoo reports                       |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| doc_model                  | Document model                              | It is the same of use doc_opts.model                                                            |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| doc_opts                   | Document parametes                          |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| doc_opts.model             | Document model                              | Same as doc_model                                                                               |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| doc_opts.paperformat_id    | ID to paperformat                           |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| doc_opts.report_name       | Report Name                                 |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| doc_style                  | Style parameteres                           |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| doc_style.name             | Name of Style                               |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| doc_style.origin           | `Report Identity` (see below)               |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| footer_mode                | How to print footer                         |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| header_mode                | How to print header                         |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| l                          | Current invoice line when printing          | Alias used in invoice print                                                                     |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| logo style                 | Html logo style                             | Default is “max-height: 45px;”                                                                  |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| o                          | Current invoice which is printing           | Alias used in invoice print set by external layout                                              |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| order_ref_text             | Text at every change of order reference     |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| payment_term_position      | Payment data position                       |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| pdf_watermark              | Default watermark for this report           |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| pdf_watermark_expression   | Default watermark for this report           |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| report                     | Document report class                       |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| report.get_report_attrib   | Get specific fallback value                 | <div t-if="report.get_report_attrib('header_mode',o,doc_opts)"> .. </div>.                      |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| style                      | Current `Report Identity` (see below)       |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| pdf_ending_page            | Default Ending Page for this report         |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+
| pdf_ending_page_expression | Default Ending Page for this report         |                                                                                                 |
+----------------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------+



`Report Identity`

Report Identity is used to select standard Odoo reports or customized reports.
If value is 'Odoo' all customization is disabled and original Odoo reports are printed.
It is only an attribute of company style.

|

`Header mode`

This parameter, named `header_mode` set how the header is printed.
May be one of 'standard', 'logo', 'only_logo', 'line-up', 'line-up2', 'line-up3', 'line-up4', 'no_header'

* standard: standard Odoo header is printed
* logo: only the wide logo is printed which must contain company informations; separation line after logo
* only_logo: only the wide logo is printed which must contain company informations; no separation line is printed
* line-up:  logo and slogan, separation line but no company data
* line-up2:  logo and slogan but no separation line neither company data
* line-up3:  logo and company data and separation line; no slogan
* line-up3:  logo and company data; no separation line neither slogan
* no_header: no header is printed; used on pre-printed paper

|

`Footer mode`

This parameter, name `footer_mode` set how the footer is printed.
May be one of 'standard', 'auto', 'custom', 'no_footer'

        help='Which content is printed in document footer\n'
             'If "standard", footer is printed as "auto" or "custom"\n'
             'based on company.custom_footer field (Odoo standaed behavior)\n'
             'If "auto", footer is printed with automatic data\n'
             'If "custom", footer is printed from user data written\n',


* standard: standard Odoo footer is printed; may be as 'auto' or as 'custom' based on company.custom_footer field
* auto: footer is printed with comapny data
* custom: user data is printed in footer (like Odoo custom footer)
* no_footer: no footer is printed; anyway pages are printed

|

`Address mode`

This parameter, named `address_mode` set how the partner address is printed.
May be on of 'standard', 'only_one'.

* standard: standard Odoo behavior; id shipping and invoice addresses are different, both of them are printed
* only_on: just the specific address is printed; specific is shipping address on delivery document, invoice addres on invoice document

|

`Payment Term Position`
 
This parameter, named `payment_term_position` set where the payment datas (payment term, due date and payment term notes) are printed.
May be one of 'odoo', 'auto', 'header', 'footer', 'none'

* odoo: standard Odoo behavior; payment term on header, payment term notes on footer
* auto: when due payment is whole in one date, all datas are printed on header otherwise on footer
* header: all the payment datas are printed on header
* footer: all the payment data are printed on footer
* none: no any payment data is printed


|

`Print code`

This parameter, name `code_mode` manage the printing of product code in document lines.
May be one of: 'print', 'no_print'

* noprint: standard Odoo behavior
* print: print a column with code in body of documents

|

`Print description`

This parameter, name `description_mode` manage the printing of description in document lines.
May be one of: 'as_is', 'line1', 'nocode', 'nocode1'

* as_is: that is the default value; it means description is printed as is, without manipulations
* line1: only the 1st line of description is printed
* nocode: product code (text between [brackets]) is removed
* nocode1: same of line1 + nocode

|

`Order reference text`

This parameter, named `order_ref_text` contains the text to print before every line of document body when order changes.
May be used following macroes:

%(client_order_ref)s => Customer reference of order
%(order_name)s => Sale order number
%(date_order)s => Sale order date

i.e. "Order #: %(order_name)s - Your ref: %(client_order_ref)s"'

|

`DdT reference text`

This parameter, named `ddt_ref_text` contains the text to print before every line of document body when delivery document changes.
May be used following macroes:

%(ddt_number)s => Delivery document number
%(date_ddt)s => Delivery document date
%(date_done)s => Delivery date

'i.e. "Ddt #: %(ddt_number)s of %(date_ddt)s"'

|

In xml report it is also possible test the existence of a field. The should be as follow:

`
<div t-if="'some_field' in docs[0]">FOUND SOME FIELD</div>
<div t-if="'some_field' not in docs[0]">NOT FOUND SOME FIELD</div>
`


|

OCA comparation / Confronto con OCA
-----------------------------------

This module is exclusive of Zeroincombenze® and is not avaiable on OCA repository.

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

10.0.0.2.13 (2019-09-04)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Due payments + IBAN / Scadenze + IBAN


10.0.0.2.12 (2019-09-03)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Line-up header / Intestazione con allineamento logo + dati


10.0.0.2.11 (2019-09-02)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Address mode / MOdalità stampa indirizzo


10.0.0.2.10 (2019-08-26)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Fallback parameters / Parametri a cascata


10.0.0.2.9 (2019-08-07)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Description with NL / Stampa descrizione con NL


10.0.0.2.8 (2019-07-05)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Print Bank account base on payment type / Stampa banca d'appoggio in base al tipo di pagamento
* [IMP] Payment datas on header or on footer / Dati di pagamento in intestazione o nel piede
* [IMP] Print due dates and due amounts / STampa data e importo scadenze


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

Last Update / Ultimo aggiornamento: 2019-09-04

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
