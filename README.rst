================================
|Zeroincombenze| l10n-italy 10.0
================================

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
* Documenti con Reverse Charge

Avaiable Addons / Moduli disponibili
------------------------------------

+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| Name / Nome                          | Version    | OCA Ver.   | Description / Descrizione                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_central_journal              | |no_check| | |halt|     | Account Central Journal                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_entry_date           | 10.0.0.2.0 | |halt|     | Set Account Invoice Entry Dates easy visible                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_entry_dates          | |halt|     | |no_check| | Registration, vat/balance application dates                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_partner_carrier      | 10.0.0.1.0 | |no_check| | Add the Partner Carrier field on account invoice                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_report_ddt_group     | |halt|     | 10.0.0.3.2 | Account invoice report grouped by DDT                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_sequential_dates     | |no_check| | |halt|     | Check invoice date consistency                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_period                       | 10.0.0.1.0 | |no_check| | Account Period                                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_vat_period_end_statement     | 10.0.1.5.4 | 10.0.1.5.1 | Versamento Iva periodica (mensile o trimestrale)                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| base_multireport                     | 10.0.0.2.2 | |no_check| | Manage document multiple reports                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_CEE_balance_generic          | |halt|     | |halt|     | Italy - 4th EU Directive - Consolidation Chart of Accounts                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_abicab                       | 10.0.1.0.0 | |same|     | Base Bank ABI/CAB codes                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account                      | 10.0.1.2.1 | 10.0.1.2.5 | Base account for Italian Localizzation                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp                | |no_check| | 10.0.1.0.1 | Tax stamp automatic management                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp_ddt            | |no_check| | 10.0.1.0.0 | Modulo ponte tra imposta di bollo e DDT                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp_sale           | |no_check| | 10.0.1.0.1 | Modulo ponte tra imposta di bollo e vendite                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_tax_kind             | |no_check| | 10.0.2.0.0 | Italian Localisation - Natura delle aliquote IVA                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ade                          | 10.0.0.3.9 | |no_check| | Codes & Definitions from IRS                                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ateco                        | |halt|     | |same|     | Ateco codes                                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_base                         | 10.0.0.2.1 | |no_check| | Managing Italian addresses                                                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_base_crm                     | |halt|     | |halt|     | Italian Localisation - CRM                                                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_base_location_geonames_impor | 10.0.1.0.0 | |same|     | Import base_location entries (provinces) from Geonames                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_bill_of_entry                | |halt|     | |halt|     | Italian Localisation - Bill of Entry                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_causali_pagamento            | 10.0.2.0.0 | |same|     | Aggiunge la tabella delle causali di pagamento da usare ad esempio nelle ritenut |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_central_journal              | 10.0.0.0.7 | 10.0.1.0.3 | Print fiscal account journal                                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_codici_carica                | |no_check| | 10.0.1.0.0 | Aggiunge la tabella dei codici carica da usare nei dichiarativi fiscali italiani |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_conai                        | 10.0.0.1.1 | |no_check| | CONAI data and amount evalutation                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi                | 10.0.1.1.0 | 10.0.1.2.4 | Italian Localization - Corrispettivi                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi_sale           | |no_check| | 10.0.1.0.3 | Modulo per integrare i corrispettivi in odoo con gli ordini di vendita.          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ddt                          | 10.0.1.8.2 | 10.0.1.9.0 | Delivery Document Type                                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_dichiarazione_intento        | |no_check| | 10.0.1.0.2 | Gestione dichiarazioni di intento                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_base                | 10.0.2.1.2 | |no_check| | Infrastructure for Italian Electronic Invoice + FatturaPA                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_export_zip          | 10.0.1.0.0 | |no_check| | Esportazione di file XML di fatture elettroniche in uno ZIP da esportare.        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_import              | |halt|     | |no_check| | Import fatture elettroniche clienti                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_import_zip          | 10.0.1.0.6 | |no_check| | Importazione di file XML di fatture elettroniche da uno ZIP                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_in                  | 10.0.1.3.4 | |no_check| | E-invoice receive                                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_out                 | 10.0.1.0.2 | |no_check| | E-Invoice emission                                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_out_ddt             | 10.0.1.0.3 | |no_check| | Modulo ponte tra emissione fatture elettroniche e DDT                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_out_li              | 10.0.1.0.2 | |no_check| | Dichiarazioni d'intento in fattura elettronica                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_out_rc              | 10.0.1.0.4 | |no_check| | Integrazione l10n_it_fatturapa_out e l10n_it_reverse_charge                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_send2sdi            | 10.0.1.0.4 | |no_check| | Send E-Invoice to customer through SdI                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_stamp               | 10.0.1.0.5 | |no_check| | Tax stamp automatic management                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_esigibilita_iva              | |no_check| | 10.0.1.0.0 | Esigibilità IVA                                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa                    | |no_check| | 10.0.3.0.0 | Fatture elettroniche                                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_export_zip         | |no_check| | 10.0.1.0.0 | Permette di esportare in uno ZIP diversi file XML di fatture elettroniche        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in                 | |no_check| | 10.0.3.1.0 | Ricezione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in_purchase        | |no_check| | 10.0.1.0.0 | Modulo ponte tra ricezione fatture elettroniche e acquisti                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in_rc              | |no_check| | 10.0.2.1.0 | Modulo di collegamento tra e-fattura in acquisto e reverse charge                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out                | |no_check| | 10.0.2.0.0 | Emissione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_ddt            | |no_check| | 10.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e DDT                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_di             | |no_check| | 10.0.1.0.0 | Dichiarazioni d'intento in fatturapa                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_rc             | |no_check| | 10.0.1.1.0 | Integrazione l10n_it_fatturapa_out e l10n_it_reverse_charge                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_stamp          | |no_check| | 10.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e imposta di bollo               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_triple_discoun | |no_check| | 10.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e sconto triplo                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_wt             | |no_check| | 10.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e ritenute.                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_pec                | |no_check| | 10.0.1.9.1 | Invio fatture elettroniche tramite PEC                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal                       | 10.0.0.2.1 | |no_check| | Italy - Fiscal localization by zeroincombenze(R)                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_document_type         | |no_check| | 10.0.2.0.0 | Italian Localization - Tipi di documento fiscale per dichiarativi                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_ipa                   | 10.0.1.1.2 | |no_check| | IPA Code and Destination Code in Partner Record                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_payment_term          | 10.0.1.0.1 | 10.0.2.0.0 | Electronic & Fiscal invoices payment                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode                   | 10.0.1.0.4 | 10.0.1.3.0 | Italian Localisation - Fiscal Code                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode_invoice           | 10.0.1.0.0 | |same|     | Italian Fiscal Code in invoice PDF                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_intrastat                    | |no_check| | 10.0.1.0.3 | Riclassificazione merci e servizi per dichiarazioni Intrastat                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_intrastat_statement          | |no_check| | 10.0.1.1.4 | Dichiarazione Intrastat per l'Agenzia delle Dogane                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_invoices_data_communication  | |no_check| | 10.0.1.1.3 | Comunicazione dati fatture (c.d. "nuovo spesometro" o "esterometro")             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_invoices_data_communication_ | |no_check| | 10.0.1.0.0 | Integrazione fatturazione elettronica e Comunicazione dati fatture (c.d. "nuovo  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ipa                          | |no_check| | 10.0.2.0.0 | IPA Code (IndicePA)                                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_lettera_intento              | 10.0.0.1.8 | |no_check| | Lettere di intento                                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_location_nuts                | |no_check| | 10.0.1.0.1 | NUTS specific options for Italy                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_partially_deductible_vat     | |halt|     | |halt|     | Italy - Partially Deductible VAT                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pec                          | 10.0.1.0.0 | |same|     | Aggiunge il campo email PEC al partner                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pos_fatturapa                | |no_check| | 10.0.1.0.0 | Gestione dati fattura elettronica del cliente all'interno dell'interfaccia del P |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pos_fiscalcode               | |no_check| | 10.0.1.0.0 | Gestione codice fiscale del cliente all'interno dell'interfaccia del POS         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_prima_nota_cassa             | |halt|     | |halt|     | Italian Localisation - Prima Nota Cassa                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_rea                          | 10.0.1.1.2 | 10.0.1.1.3 | Gestisce i campi del Repertorio Economico Amministrativo                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_reverse_charge               | 10.0.1.7   | 10.0.1.3.0 | Manage Reverse Charge Tax for Italy                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_riba_commission              | |halt|     | |same|     | Ricevute bancarie & commissioni                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ricevute_bancarie            | 10.0.1.3.1 | 10.0.1.3.0 | Ricevute Bancarie                                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_sdi_channel                  | |no_check| | 10.0.1.2.0 | Aggiunge il canale di invio/ricezione dei file XML attraverso lo SdI             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_split_payment                | 10.0.1.1.2 | 10.0.1.1.0 | Italian Split Payment Management                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_communication            | 10.0.0.2.4 | |no_check| | Comunicazione periodica IVA                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries               | 10.0.1.3.2 | 10.0.1.3.1 | ITA - Registri IVA                                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries_cash_basis    | |halt|     | 10.0.1.0.1 | Italian Localization - VAT Registries - Cash Basis                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries_split_payment | |no_check| | 10.0.1.0.0 | Bridge module to make VAT registries work with Split Payment                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_statement_communication  | 10.0.1.5.4 | |no_check| | Comunicazione liquidazione IVA ed esportazione file xml conforme alle specifiche |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_fatturapa     | |no_check| | 10.0.1.0.2 | Add fatturapa fields and checks in frontend user's details                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_fiscalcode    | |no_check| | 10.0.1.0.0 | Add fiscal code to details of frontend user                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_sale_corrispettivi   | |halt|     | 10.0.1.1.1 | Italian localization - Website Sale Corrispettivi                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_sale_fatturapa       | |no_check| | 10.0.1.0.0 | Aggiunge i campi necessari alla fatturazione elettronica nel form del checkout   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_sale_fiscalcode      | 10.0.1.0.1 | 10.0.1.0.2 | Website Sale FiscalCode                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax              | 10.0.1.2.8 | 10.0.2.0.1 | Italian Withholding Tax                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_causali      | |no_check| | 10.0.1.0.0 | Causali pagamento per ritenute d'acconto                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_payment      | 10.0.1.1.0 | 10.0.2.0.0 | Italian Withholding Tax Payment                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_payment_orde | |no_check| | 10.0.1.0.0 | Modulo ponte tra ritenuta d'acconto e ordine di pagamento                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| multibase_plus                       | 10.0.0.1.5 | |no_check| | Enhanced Odoo Features                                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+



OCA comparation / Confronto con OCA
-----------------------------------

+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Description / Descrizione            | Odoo Italia      | OCA             | Notes / Note                                                                         |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Coverage                             | |Codecov Status| | |OCA Codecov|   |                                                                                      |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Gestione evoluta anagrafiche         | |check|          | |no_check|      | `l10n_it_base <https://github.com/zeroincombenze/l10n-italy/tree/8.0/l10n_it_base>__ |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Piano dei conti evoluto              | |check|          | |no_check|      |                                                                                      |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Codici IVA completi                  | |check|          | |no_check|      |                                                                                      |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| FatturaPA                            | v1.2.1           | v1.2.1          |                                                                                      |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+
| Validazione Codice Fiscale           | |check|          | |no_check|      |                                                                                      |
+--------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+



Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
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


Installation / Installazione
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


Upgrade / Aggiornamento
-----------------------

::

    deploy_odoo update -r l10n-italy -b 10.0 -G zero -p $HOME/10.0
    vem amend $HOME/10.0/venv_odoo
    # Adjust following statements as per your system
    sudo systemctl restart odoo


Support / Supporto
------------------

|Zeroincombenze| This project is mainly supported by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



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


ChangeLog History / Cronologia modifiche
----------------------------------------

l10n_it_account: 10.0.1.2.12 (2024-06-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Field amount_net_pay displayed on invoice form / Netto a pagare visualizzato in fattura
* [QUA] Test coverage 81% (93: 18+75) [0 TestPoints] - quality rating 49 (target 100)


l10n_it_withholding_tax: 10.0.1.2.8 (2024-06-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Depending on l10n_it_account for amount_net_pay
* [QUA] Test coverage 29% (542: 387+155) [0 TestPoints] - quality rating 18 (target 100)


l10n_it_split_payment: 10.0.1.1.2 (2024-06-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Depending on l10n_it_account for amount_net_pay
* [IMP] Show net to pay (see l10n_it_account) / Visualizza netto a pagare (vedere l10n_it_account)
* [QUA] Test coverage 73% (142: 39+103) [0 TestPoints] - quality rating 44 (target 100)


l10n_it_reverse_charge: 10.0.1.7 (2024-06-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Tax with RC requires RC fiscal position / Controllo codici IVA con RC e posizione fiscale
* [IMP] Show net to pay (see l10n_it_account) / Visualizza netto a pagare (vedere l10n_it_account)
* [IMP] RC Amount stored in invoice record / Importo IVA RC in fattura
* [IMP] Sale invoice / Gestione fatture di vendita con RC e netto a pagare
* [IMP] Regression tests
* [QUA] Test coverage 64% (410: 147+263) [26 TestPoints] - quality rating 49 (target 100)


l10n_it_ricevute_bancarie: 10.0.1.3.16 (2024-06-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Workflow for list with "DI" configuraiton  / Workflow per distinte al dopo-incasso
* [QUA] Test coverage 78% (1145: 254+891) [258 TestPoints] - quality rating 83 (target 100)


l10n_it_ddt: 10.0.1.8.26 (2024-06-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Wrong inheritance for delivery values
* [IMP] Delivery Carrier Notes
* [QUA] Test coverage 67% (1385: 454+931) [266 TestPoints] - quality rating 72 (target 100)


l10n_it_conai: 10.0.0.1.11 (2024-06-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Check for version of l10n_it_ddt to depend on
* [QUA] Test coverage 67% (505: 166+339) [23 TestPoints] - quality rating 48 (target 100)


l10n_it_einvoice_send2sdi: 10.0.1.0.44 (2024-05-14)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Invoice rejected in some cases
* [QUA] Test coverage 15% (814: 688+126) [1 TestPoints] - quality rating 10 (target 100)


l10n_it_einvoice_send2sdi: 10.0.1.0.43 (2024-05-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor improvements
* [QUA] Test coverage 16% (812: 686+126) [1 TestPoints] - quality rating 10 (target 100)


l10n_it_einvoice_in: 10.0.1.3.46 (2024-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Again weird error linking self-invoice
* [FIX] Avoid company data update from self-invoice / Non cambia dati aziendali da auto-fattura
* [FIX] Cannot import e-invoice with wrong vat / Ignora PI se errata in e-fattura
* [QUA] Test coverage 63% (1337: 498+839) [0 TestPoints] - quality rating 38 (target 100)


l10n_it_einvoice_in: 10.0.1.3.45 (2024-05-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Weird error linking self-invoice
* [IMP] Avoid company data update from self-invoice
* [QUA] Test coverage 63% (1330: 495+835) [0 TestPoints] - quality rating 38 (target 100)


l10n_it_einvoice_send2sdi: 10.0.1.0.42 (2024-05-04)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor improvements
* [QUA] Test coverage 16% (812: 686+126) [1 TestPoints] - quality rating 10 (target 100)


l10n_it_einvoice_out_ddt: 10.0.1.0.3 (2024-03-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Invalid name for carier_id, right name is partner_carrier_id
* [QUA] Test coverage 19% (43: 35+8) [0 TestPoints] - quality rating 12 (target 100)


l10n_it_einvoice_base: 10.0.2.1.25 (2024-03-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Field carrier_id conflicts with other modules
* [QUA] Test coverage 61% (515: 202+313) [0 TestPoints] - quality rating 37 (target 100)


l10n_it_lettera_intento: 10.0.0.1.8 (2024-03-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash on creation lettera intento / Crash durante creazione lettera di intento
* [IMP] Domain on partner / Selezione clienti con pos.fiscale assente o con lettera di intento


l10n_it_einvoice_send2sdi: 10.0.1.0.41 (2024-02-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor improvements
* [QUA] Test coverage 16% (812: 686+126) [1 TestPoints] - quality rating 10 (target 100)


l10n_it_einvoice_in: 10.0.1.3.44 (2024-02-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] E-Lines detail: name changed


l10n_it_einvoice_out_rc: 10.0.1.0.5 (2024-02-01)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [QUA] Test coverage 78% (100: 22+78) [20 TestPoints] - quality rating 79 (target 100)



l10n_it_einvoice_out: 10.0.1.0.27 (2024-02-01)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Self e-invoice management - Emissione auto-fatture
* [QUA] Test coverage 64% (762: 276+486) [87 TestPoints] - quality rating 57 (target 100)


l10n_it_einvoice_base: 10.0.2.1.24 (2024-02-01)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Sender on invoice header / Soggetto emittente in testata fattura
* [QUA] Test coverage 61% (515: 202+313) [0 TestPoints] - quality rating 37 (target 100)


l10n_it_ade: 10.0.0.3.9 (2024-01-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Fiscal document TD28 / Documento fiscale TD28
* [IMP] Fiscal document: searching improvements / Migliorie ricerca documento fiscale
* [FIX] TD20 is self invoice


l10n_it_conai: 10.0.0.1.10 (2024-01-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [QUA] Test coverage 67% (505: 166+339) [23 TestPoints] - quality rating 48 (target 100)


l10n_it_einvoice_in: 10.0.1.3.43 (2024-01-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash with <RiferimentoTesto></RiferimentoTesto> / Crash in alcuni casi
* [FIX] Search state/district by country code from vat / Ricerca provincia con nazione da PI
* [QUA] Test coverage 63% (1326: 493+833) [0 TestPoints] - quality rating 38 (target 100)


l10n_it_central_journal: 10.0.0.0.8 (2023-12-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Layout orientation / Orientamento di stampa
* [IMP] Font size 9px / Dimensione fotn 9px
* [QUA] Test coverage 33% (199: 134+65) [0 TestPoints] - quality rating 40 (target 100)


l10n_it_ricevute_bancarie: 10.0.1.3.15 (2023-11-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice payment with "DI" configuraiton / Pagamento fattura anche al Dopo Incasso
* [QUA] Test coverage 78% (1145: 254+891) [258 TestPoints] - quality rating 83 (target 100)


l10n_it_einvoice_send2sdi: 10.0.1.0.40 (2023-11-15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor improvements
* [QUA] Test coverage 16% (812: 686+126) [1 TestPoints] - quality rating 77 (target 100)


l10n_it_ade: 10.0.0.3.8 (2023-11-15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] pyxb 1.2.6
* [IMP] Remove support for pyxb 1.2.4 / Rimosso supporto per pyxb 1.2.4
* [QUA] Test coverage 66% (168: 57+111) [3 TestPoints] - quality rating 74 (target 100)


l10n_it_einvoice_send2sdi: 10.0.1.0.39 (2023-10-25)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Rejected invoce / Stato fattura rifiutata
* [FIX] NO response / Nessuna risposta da SDI
* [QUA] Test coverage 16% (812: 686+126) [1 TestPoints] - quality rating 77 (target 100)


l10n_it_einvoice_in: 10.0.1.3.42 (2023-10-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash with <DatiOrdineAcquisto></DatiOrdineAcquisto> / Crash in alcuni casi
* [QUA] Test coverage 63% (1326: 493+833) [0 TestPoints] - quality rating 38 (target 100)


l10n_it_einvoice_send2sdi: 10.0.1.0.38 (2023-10-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] First very simple unit test
* [QUA] Test coverage 16% (812: 686+126) [1 TestPoints] - quality rating 0/100


l10n_it_central_journal: 10.0.0.0.7 (2023-09-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] 1st line numer / Primo numero di riga


l10n_it_ricevute_bancarie: 10.0.1.3.14 (2023-09-14)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] RiBA account reconciled after payment / Conto effetti attivi riconciliato dopo incasso
* [IMP] Unsolved accounts set automatically / Conti insoluti imposttai automaticamente


l10n_it_einvoice_send2sdi: 10.0.1.0.37 (2023-08-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor improvements


l10n_it_ricevute_bancarie: 10.0.1.3.13 (2023-08-03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Overdue with expenses / Insoluto con spese
* [QUA] Test coverage 66% (1155: 389+766) [113 TestPoint]


l10n_it_einvoice_send2sdi: 10.0.1.0.36 (2023-08-01)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor improvements


l10n_it_central_journal: 10.0.0.0.6 (2023-07-31)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Upgraded layout / Aggiornamento impaginazione
* [FIX] Final print: update result / Stampa ufficiale aggiorna dati su anno fiscale
 


l10n_it_einvoice_send2sdi: 10.0.1.0.35 (2023-07-25)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor improvements
* [QUA] Test coverage 15% (816: 694+122)


l10n_it_einvoice_send2sdi: 10.0.1.0.34 (2023-07-04)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor improvements
* [QUA] Test coverage 15% (816: 694+122) 


base_multireport: 10.0.0.2.28 (2023-06-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice report with due dates from account lines / Date scadenza stampa fattura da righe contabili
* [QUA] Test coverage 39% (650: 395+255) 


l10n_it_ddt: 10.0.1.8.25 (2023-06-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Cancel DdT from order with invoice / Annullo DdT da ordine con fattura
* [IMP] Cancel DdT check for backorder / Annullo DdT controlla se creato ordine saldo
* [QUA] Coverage 67% (1377/453) + 247cp


l10n_it_einvoice_out: 10.0.1.0.26 (2023-06-12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Foreign customer w/o vat but with fiscalcode / Cliente estero senza PI ma con CF
* [QUA] Coverage 60% (731/292) + 39cp


Credits / Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


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


Last Update / Ultimo aggiornamento: 2024-06-10

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
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
