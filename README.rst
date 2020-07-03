
================================
|Zeroincombenze| l10n-italy 12.0
================================
|Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en| Italian Localization

|it| Localizzazione Italiana

La localizzazione italiana comprende moduli per la gestione delle principali
incombenze fiscali che le imprese italiane devono gestire.

Sono coperte le aree:

* Stampa registri IVA
* Stampa libro giornale
* Registrazione fatture fornitori con RA
* FatturaPA
* Fattura Elettronica B2B
* Gestione DdT
* Data di registrazione fatture fornitori
* Gestione Ricevute Bancarie
* Split payment

Avaiable Addons / Moduli disponibili
------------------------------------

+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| Name / Nome                          | Version    | OCA Ver.   | Description / Descrizione                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_report_ddt_group     | 12.0.1.0.2 | 12.0.1.0.3 | Raggruppa le righe fattura per DDT che le ha generate, mostrando eventualmente i |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_sequential_dates     | 12.0.1.0.4 | |no_check| | Check invoice date consistency                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_vat_period_end_statement     | 12.0.1.5.3 | 12.0.1.5.2 | Versamento Iva periodica (mensile o trimestrale)                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| fiscal_epos_print                    | 12.0.1.1.6 | |same|     | ePOS-Print XML Fiscal Printer Driver - Stampanti Epson compatibili: FP81II, FP90 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| fiscal_epos_print_fiscalcode         | 12.0.1.0.1 | |same|     | Consente di includere il codice fiscale negli scontrini                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_abicab                       | 12.0.1.1.1 | |same|     | Base Bank ABI/CAB codes                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account                      | 12.0.1.4.2 | |same|     | Modulo base usato come dipendenza di altri moduli contabili                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_balance_report       | 12.0.1.0.1 | |same|     | Rendicontazione .pdf e .xls per stato patrimoniale e conto economico a sezioni c |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp                | 12.0.1.1.2 | |same|     | Gestione automatica dell'imposta di bollo                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp_ddt            | 12.0.1.0.0 | 12.0.1.0.1 | Modulo ponte tra imposta di bollo e DDT                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp_sale           | 12.0.1.0.0 | 12.0.1.0.1 | Modulo ponte tra imposta di bollo e vendite                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_tax_kind             | 12.0.1.0.0 | 12.0.1.0.1 | Italian Localisation - Natura delle aliquote IVA                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ade                          | |halt|     | |no_check| | Codice con le definizioni dei file xml Agenzia delle Entrate                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ateco                        | 12.0.1.0.1 | |same|     | ITA - Codici Ateco                                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_causali_pagamento            | 12.0.1.0.0 | 12.0.1.0.1 | Aggiunge la tabella delle causali di pagamento da usare ad esempio nelle ritenut |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_central_journal              | 12.0.1.1.2 | |same|     | ITA - Libro giornale                                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_codici_carica                | 12.0.1.0.0 | 12.0.1.0.1 | Aggiunge la tabella dei codici carica da usare nelle dichiarazioni fiscali itali |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi                | 12.0.1.1.6 | |same|     | Italian Localization - Ricevute                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi_fatturapa_out  | 12.0.1.0.0 | 12.0.1.0.1 | Modulo per integrare ricevute e fatturazione elettronica                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi_sale           | 12.0.1.0.3 | |same|     | Modulo per integrare le ricevute in Odoo con gli ordini di vendita.              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ddt                          | 12.0.1.6.1 | |same|     | Documento di Trasporto                                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_dichiarazione_intento        | 12.0.0.1.1 | |same|     | Gestione dichiarazioni di intento                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_esigibilita_iva              | 12.0.1.0.0 | 12.0.1.0.1 | Italian Localization - Esigibilita' IVA                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa                    | 12.0.1.12. | |same|     | Fatture elettroniche                                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_export_zip         | 12.0.1.0.0 | 12.0.1.0.1 | Permette di esportare in uno ZIP diversi file XML di fatture elettroniche        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in                 | 12.0.1.17. | |same|     | Ricezione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in_purchase        | 12.0.1.0.0 | 12.0.1.0.1 | Modulo ponte tra ricezione fatture elettroniche e acquisti                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in_rc              | 12.0.1.1.2 | 12.0.1.1.3 | Modulo ponte tra e-fattura in acquisto e inversione contabile                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out                | 12.0.1.8.2 | |same|     | Emissione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_ddt            | 12.0.1.1.1 | 12.0.1.1.2 | Modulo ponte tra emissione fatture elettroniche e DDT                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_stamp          | 12.0.1.0.3 | 12.0.1.0.4 | Modulo ponte tra emissione fatture elettroniche e imposta di bollo               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_triple_discoun | 12.0.1.0.3 | |same|     | Modulo ponte tra emissione fatture elettroniche e sconto triplo                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_wt             | 12.0.1.1.2 | |same|     | Modulo ponte tra emissione fatture elettroniche e ritenute.                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_pec                | 12.0.1.6.0 | |same|     | Invio fatture elettroniche tramite PEC                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_document_type         | 12.0.1.2.0 | 12.0.1.2.1 | Italian Localization - Tipi di documento fiscale per dichiarativi                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_payment_term          | 12.0.1.1.0 | 12.0.1.1.1 | Condizioni di pagamento delle fatture elettroniche                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode                   | 12.0.1.1.3 | |same|     | Italian Localization - Fiscal Code                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode_crm               | 12.0.1.0.1 | 12.0.1.0.2 | Aggiunge il campo codice fiscale ai contatti/opportunità                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_intrastat                    | 12.0.1.1.2 | |same|     | Riclassificazione merci e servizi per dichiarazioni Intrastat                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_intrastat_statement          | 12.0.1.1.3 | |same|     | Dichiarazione Intrastat per l'Agenzia delle Dogane                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_invoices_data_communication  | 12.0.1.2.1 | |same|     | Comunicazione dati fatture (c.d. "nuovo spesometro" o "esterometro")             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_invoices_data_communication_ | 12.0.1.0.1 | |same|     | Integrazione fatturazione elettronica e comunicazione dati fatture (c.d. "nuovo  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ipa                          | 12.0.1.0.0 | 12.0.1.0.1 | IPA Code (IndicePA)                                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_location_nuts                | 12.0.1.0.1 | 12.0.1.0.2 | Opzioni NUTS specifiche per l'Italia                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pec                          | 12.0.1.0.1 | |same|     | Aggiunge il campo email PEC al partner                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pos_fatturapa                | 12.0.1.0.0 | 12.0.1.0.1 | Gestione dati fattura elettronica del cliente all'interno dell'interfaccia del P |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pos_fiscalcode               | 12.0.1.0.0 | 12.0.1.0.1 | Gestione codice fiscale del cliente all'interno dell'interfaccia del POS         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_rea                          | 12.0.1.0.2 | 12.0.1.0.3 | Gestisce i campi del Repertorio Economico Amministrativo                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_reverse_charge               | 12.0.1.2.3 | |same|     | Inversione contabile                                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ricevute_bancarie            | 12.0.1.3.1 | |same|     | Ricevute bancarie                                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_sdi_channel                  | 12.0.1.3.2 | |same|     | Aggiunge il canale di invio/ricezione dei file XML attraverso lo SdI             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_split_payment                | 12.0.1.0.0 | 12.0.1.0.1 | Split Payment                                                                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries               | 12.0.1.2.2 | |same|     | ITA - Registri IVA                                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries_cash_basis    | |halt|     | |no_check| | Italian Localization - VAT Registries - Cash Basis                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries_split_payment | 12.0.1.0.2 | |same|     | Modulo di congiunzione tra registri IVA e scissione dei pagamenti                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_statement_communication  | 12.0.1.5.3 | |same|     | Comunicazione liquidazione IVA ed esportazione file xmlconforme alle specifiche  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_statement_split_payment  | 12.0.1.0.0 | 12.0.1.0.1 | Migliora la liquidazione dell'IVA tenendo in considerazione la scissione dei pag |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_fatturapa     | 12.0.1.2.0 | 12.0.1.2.1 | Add fatturapa fields and checks in frontend user's details                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_fatturapa_sal | 12.0.1.1.0 | 12.0.1.1.1 | Controlli per la fattura elettronica nel portale vendite                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_fiscalcode    | 12.0.1.0.1 | 12.0.1.0.2 | Add fiscal code to details of frontend user                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_ipa           | 12.0.1.1.0 | 12.0.1.1.1 | Aggiunge l'indice PA (IPA) tra i dettagli dell'utente nel portale.               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_sale_corrispettivi   | 12.0.1.0.0 | 12.0.1.0.1 | Aggiunge la ricevuta come opzione per l'utente e-commerce                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_sale_fatturapa       | 12.0.1.0.2 | 12.0.1.0.3 | Aggiunge i campi necessari alla fatturazione elettronica nel form del checkout   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_sale_fiscalcode      | 12.0.1.1.2 | |same|     | Website Sale FiscalCode                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax              | 12.0.1.2.0 | |same|     | Italian Withholding Tax                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_causali      | 12.0.1.1.1 | |same|     | Causali pagamento per ritenute d'acconto                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_payment      | 12.0.1.0.1 | |same|     | Gestisce le ritenute sulle fatture e sui pagamenti                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+



OCA comparation / Confronto con OCA
-----------------------------------

+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Description / Descrizione            | Odoo Italia      | OCA             | Notes / Note                                                                         |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Coverage                             | |Codecov Status| | |OCA Codecov|   |                                                                                      |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Piano dei conti evoluto              | |check|          | |no_check|      |                                                                                      |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Codici IVA completi                  | |check|          | |no_check|      |                                                                                      |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| FatturaPA                            | v1.2.1           | v1.2.1          |                                                                                      |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+



Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
----------------------------


* python 3.7+
* postgresql 9.5+ (experimental 10.0+)
* unicodecsv
* codicefiscale
* unidecode==0.04.17
* PyXB==1.2.6
* asn1crypto==0.24.0


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
| /home/odoo/12.0/l10n-italy/                                                |
+----------------------------------------------------------------------------+

::

    cd $HOME
    # Tools installation & activation: skip if you have installed this tool
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    source /opt/odoo/dev/activate_tools
    # Odoo installation
    odoo_install_repository l10n-italy -b 12.0 -O zero
    vem create /opt/odoo/VENV-12.0 -O 12.0 -DI



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
    odoo_install_repository l10n-italy -b 12.0 -O zero -U
    vem amend /opt/odoo/VENV-12.0 -O 12.0 -DI
    # Adjust following statements as per your system
    sudo systemctl restart odoo


Support / Supporto
------------------


|Zeroincombenze| This project is mainly maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------


|en| If you have a proposal to change on oh these modules, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare uno dei moduli, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.

Credits / Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


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


Last Update / Ultimo aggiornamento: 2020-07-02

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=12.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=12.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=12.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/12.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/12.0
    :alt: Codecov
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-12.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/12.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-12.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/12.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-12.svg
    :target: https://erp12.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov| image:: https://codecov.io/gh/OCA/l10n-italy/branch/12.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/12.0
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

