
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
| account_invoice_check_total          | 12.0.10.0. | |no_check| |  Check if the verification total is equal to the bill's total                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_entry_date           | 12.0.10.0. | |no_check| | Account Invoice Entry Dates                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_entry_dates          | 12.0.10.0. | |no_check| | Registration, vat/balance application dates                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_report_ddt_group     | 12.0.10.0. | 12.0.1.0.5 | Account invoice report grouped by DDT                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_period                       | 12.0.1.0   | |no_check| | Account Period                                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_vat_period_end_statement     | 12.0.10.0. | 12.0.1.8.0 | Versamento Iva periodica (mensile o trimestrale)                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| assets_management                    | |no_check| | 12.0.1.0.0 | Gestione Cespiti                                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| assigned_bank                        | 12.0.10.0. | |no_check| | Assign internal bank to customers or supplier                                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| base_multireport                     | 12.0.10.0. | |no_check| | Manage document multiple reports                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| currency_rate_update_boi             | |no_check| | 12.0.1.0.0 | Update exchange rates using www.bancaditalia.it                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| fiscal_epos_print                    | |no_check| | 12.0.1.3.5 | ePOS-Print XML Fiscal Printer Driver - Stampanti Epson compatibili: FP81II, FP90 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| fiscal_epos_print_fiscalcode         | |no_check| | 12.0.1.1.0 | Consente di includere il codice fiscale negli scontrini                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| fiscal_epos_print_meal_voucher       | |no_check| | 12.0.1.1.0 | Consente di controllare e comunicare al registratore telematico le informazioni  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_CEE_balance_generic          | |halt|     | |no_check| | Italy - 4th EU Directive - Consolidation Chart of Accounts                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_abicab                       | 12.0.10.0. | 12.0.1.1.1 | Base Bank ABI/CAB codes                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_accompanying_invoice         | |no_check| | 12.0.1.0.0 | Stampa della fattura accompagnatoria                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account                      | 12.0.10.0. | 12.0.1.4.5 | Italian Localization - Account                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_balance_report       | |no_check| | 12.0.1.0.3 | Rendicontazione .pdf e .xls per stato patrimoniale e conto economico a sezioni c |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp                | |no_check| | 12.0.1.4.0 | Gestione automatica dell'imposta di bollo                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp_ddt            | |no_check| | 12.0.1.0.1 | Modulo ponte tra imposta di bollo e DDT                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp_sale           | |no_check| | 12.0.1.0.1 | Modulo ponte tra imposta di bollo e vendite                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_tax_kind             | |no_check| | 12.0.2.1.0 | Italian Localisation - Natura delle aliquote IVA                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ade                          | 12.0.10.0. | |no_check| | Codice e definizioni come da Agenzia delle Entrate                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ateco                        | |halt|     | 12.0.1.0.1 | Ateco codes                                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_base                         | 12.0.10.0. | |no_check| | Managing Italian addresses                                                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_base_crm                     | |halt|     | |no_check| | Italian Localisation - CRM                                                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_base_location_geonames_impor | 12.0.10.0. | |no_check| | Import base_location entries (provinces) from Geonames                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_bill_of_entry                | |halt|     | |no_check| | Italian Localisation - Bill of Entry                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_causali_pagamento            | 12.0.10.0. | 12.0.2.0.0 | Aggiunge la tabella delle causali di pagamento da usare ad esempio nelle ritenut |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_central_journal              | 12.0.10.0. | 12.0.1.1.4 | Italian Localization - Account central journal                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_codici_carica                | |no_check| | 12.0.1.0.2 | Aggiunge la tabella dei codici carica da usare nelle dichiarazioni fiscali itali |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_conai                        | 12.0.10.0. | |no_check| | Dati CONAI in fattura e calcolo importi                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi                | 12.0.10.0. | 12.0.1.1.8 | Italian Localization - Corrispettivi                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi_fatturapa_out  | |no_check| | 12.0.1.0.1 | Modulo per integrare ricevute e fatturazione elettronica                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi_sale           | |no_check| | 12.0.1.0.3 | Modulo per integrare le ricevute in Odoo con gli ordini di vendita.              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ddt                          | 12.0.10.0. | 12.0.1.9.4 | Delivery Document to Transfer                                                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_delivery_note                | |no_check| | 12.0.1.0.5 | Crea, gestisce e fattura i DDT partendo dalle consegne                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_delivery_note_base           | |no_check| | 12.0.1.0.0 | Crea e gestisce tabelle principali per gestire i DDT                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_delivery_note_batch          | |no_check| | 12.0.1.0.0 | Crea i DDT partendo da gruppi di prelievi                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_delivery_note_order_link     | |no_check| | 12.0.1.0.0 | Crea collegamento tra i DDT e ordine di vendita                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_dichiarazione_intento        | |no_check| | 12.0.0.1.1 | Gestione dichiarazioni di intento                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_base                | 12.0.10.0. | |no_check| | Infrastructure for Italian Electronic Invoice + FatturaPA                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_export_zip          | 12.0.10.0. | |no_check| | Esportazione di file XML di fatture elettroniche in uno ZIP da esportare.        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_import              | 12.0.10.0. | |no_check| | Import fatture elettroniche clienti                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_import_zip          | 12.0.10.0. | |no_check| | Importazione di file XML di fatture elettroniche da uno ZIP                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_in                  | 12.0.10.0. | |no_check| | Ricezione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_out                 | 12.0.10.0. | |no_check| | E-Invoice emission                                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_out_ddt             | 12.0.10.0. | |no_check| | Modulo ponte tra emissione fatture elettroniche e DDT                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_out_li              | 12.0.10.0. | |no_check| | Dichiarazioni d'intento in fattura elettronica                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_send2sdi            | 12.0.10.0. | |no_check| | Send E-Invoice to customer by SdI                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_stamp               | 12.0.10.0. | |no_check| | Tax stamp automatic management                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_esigibilita_iva              | |no_check| | 12.0.2.0.0 | Italian Localization - Esigibilita' IVA                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa                    | |no_check| | 12.0.2.3.0 | Fatture elettroniche                                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_export_zip         | |no_check| | 12.0.1.0.1 | Permette di esportare in uno ZIP diversi file XML di fatture elettroniche        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in                 | |no_check| | 12.0.2.8.0 | Ricezione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in_purchase        | |no_check| | 12.0.1.0.2 | Modulo ponte tra ricezione fatture elettroniche e acquisti                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in_rc              | |no_check| | 12.0.1.1.4 | Modulo ponte tra e-fattura in acquisto e inversione contabile                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out                | |no_check| | 12.0.2.3.1 | Emissione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_ddt            | |no_check| | 12.0.1.4.0 | Modulo ponte tra emissione fatture elettroniche e DDT                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_di             | |no_check| | 12.0.1.0.0 | Dichiarazioni d'intento in fatturapa                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_rc             | |no_check| | 12.0.1.0.4 | Integrazione l10n_it_fatturapa_out e l10n_it_reverse_charge                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_stamp          | |no_check| | 12.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e imposta di bollo               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_triple_discoun | |no_check| | 12.0.2.0.1 | Modulo ponte tra emissione fatture elettroniche e sconto triplo                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_wt             | |no_check| | 12.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e ritenute.                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_pec                | |no_check| | 12.0.1.9.2 | Invio fatture elettroniche tramite PEC                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_sale               | |no_check| | 12.0.1.1.2 | Aggiunge alcuni dati per la fatturazione elettronica nell'ordine di vendita      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal                       | 12.0.10.0. | |no_check| | Italy - Fiscal localization by zeroincombenze(R)                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_document_type         | |no_check| | 12.0.2.1.1 | Italian Localization - Tipi di documento fiscale per dichiarativi                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_ipa                   | 12.0.10.0. | |no_check| | IPA Code and Destination Code in Partner Record                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_payment_term          | 12.0.10.0. | 12.0.2.0.0 | Electronic & Fiscal invoices payment                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode                   | 12.0.10.0. | 12.0.1.1.4 | Italian Localisation - Fiscal Code                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode_crm               | |no_check| | 12.0.1.0.2 | Aggiunge il campo codice fiscale ai contatti/opportunità                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode_invoice           | 12.0.10.0. | |no_check| | Italian Fiscal Code in invoice PDF                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode_sale              | |no_check| | 12.0.1.0.0 | Mostra il codice fiscale del cliente nella stampa del preventivo                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_intrastat                    | |no_check| | 12.0.1.2.2 | Riclassificazione merci e servizi per dichiarazioni Intrastat                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_intrastat_statement          | |no_check| | 12.0.1.2.4 | Dichiarazione Intrastat per l'Agenzia delle Dogane                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_invoices_data_communication  | |no_check| | 12.0.1.3.2 | Comunicazione dati fatture (c.d. "nuovo spesometro" o "esterometro")             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_invoices_data_communication_ | |no_check| | 12.0.1.0.2 | Integrazione fatturazione elettronica e comunicazione dati fatture (c.d. "nuovo  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ipa                          | |no_check| | 12.0.1.0.2 | ITA - Codice IPA                                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_lettera_intento              | 12.0.10.0. | |no_check| | Lettere di intento                                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_location_nuts                | |no_check| | 12.0.1.0.2 | Opzioni NUTS specifiche per l'Italia                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_mis_reports_pl_bs            | |no_check| | 12.0.1.0.1 | Modelli "MIS Builder" per il conto economico e lo stato patrimoniale             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_partially_deductible_vat     | |halt|     | |no_check| | Italy - Partially Deductible VAT                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pec                          | 12.0.10.0. | 12.0.1.0.1 | Pec Mail                                                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pos_fatturapa                | |no_check| | 12.0.1.0.2 | Gestione dati fattura elettronica del cliente all'interno dell'interfaccia del P |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pos_fiscalcode               | |no_check| | 12.0.1.0.1 | Gestione codice fiscale del cliente all'interno dell'interfaccia del POS         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_prima_nota_cassa             | |halt|     | |no_check| | Italian Localisation - Prima Nota Cassa                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_rea                          | 12.0.10.0. | 12.0.1.0.4 | Gestisce i campi del Repertorio Economico Amministrativo                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_reverse_charge               | 12.0.10.0. | 12.0.1.2.7 | Reverse Charge for Italy                                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_riba_commission              | |halt|     | |no_check| | Ricevute bancarie & commissioni                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ricevute_bancarie            | 12.0.10.0. | 12.0.1.8.0 | Ricevute Bancarie                                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_sdi_channel                  | |no_check| | 12.0.1.3.4 | Aggiunge il canale di invio/ricezione dei file XML attraverso lo SdI             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_split_payment                | 12.0.10.0. | 12.0.1.0.1 | Split Payment                                                                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_communication            | 12.0.10.0. | |no_check| | Comunicazione periodica IVA                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries               | 12.0.10.0. | 12.0.1.2.5 | Italian Localization - VAT Registries                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries_cash_basis    | |halt|     | |no_check| | Italian Localization - VAT Registries - Cash Basis                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries_split_payment | |no_check| | 12.0.1.0.2 | Modulo di congiunzione tra registri IVA e scissione dei pagamenti                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_statement_communication  | 12.0.10.0. | 12.0.1.6.1 | Comunicazione liquidazione IVA ed esportazione file xml conforme alle specifiche |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_statement_split_payment  | |no_check| | 12.0.1.0.2 | Migliora la liquidazione dell'IVA tenendo in considerazione la scissione dei pag |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_corrispettivi | |no_check| | 12.0.1.0.0 | Aggiunge ricevuta o fattura come opzione nel profilo dell'utente portale         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_fatturapa     | |no_check| | 12.0.1.3.0 | Add fatturapa fields and checks in frontend user's details                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_fatturapa_sal | |no_check| | 12.0.1.1.1 | Controlli per la fattura elettronica nel portale vendite                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_fiscalcode    | |no_check| | 12.0.1.0.2 | Add fiscal code to details of frontend user                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_portal_ipa           | |no_check| | 12.0.1.1.1 | Aggiunge l'indice PA (IPA) tra i dettagli dell'utente nel portale.               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_sale_corrispettivi   | |halt|     | 12.0.1.0.1 | Italian localization - Website Sale Corrispettivi                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_sale_fatturapa       | |no_check| | 12.0.1.0.3 | Aggiunge i campi necessari alla fatturazione elettronica nel form del checkout   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_website_sale_fiscalcode      | 12.0.10.0. | 12.0.1.1.3 | Website Sale FiscalCode                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax              | 12.0.10.0. | 12.0.2.1.4 | Italian Withholding Tax                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_causali      | |no_check| | 12.0.2.0.0 | Causali pagamento per ritenute d'acconto                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_payment      | 12.0.10.0. | 12.0.1.0.1 | Italian Withholding Tax Payment                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| multibase_plus                       | 12.0.10.0. | |no_check| | Enhanced Odoo Features                                                           |
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
* postgresql 9.6+ (experimental 10.0+)
* codicefiscale
* unidecode
* pyxb==1.2.5
* pycryptodome
* pkcs7
* PyPDF2


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
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__    |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| $HOME/12.0                                                                 |
+----------------------------------------------------------------------------+

::

    cd $HOME
    # *** Tools installation & activation ***
    # Case 1: you have not installed zeroincombenze tools
    git clone https://github.com/zeroincombenze/tools.git
    cd $HOME/tools
    ./install_tools.sh -p
    source $HOME/devel/activate_tools
    # Case 2: you have already installed zeroincombenze tools
    cd $HOME/tools
    ./install_tools.sh -U
    source $HOME/devel/activate_tools
    # *** End of tools installation or upgrade ***
    # Odoo repository installation; OCB repository must be installed
    odoo_install_repository l10n-italy -b 12.0 -O zero -o $HOME/12.0
    vem create $HOME/12.0/venv_odoo -O 12.0 -a "*" -DI -o $HOME/12.0



Upgrade / Aggiornamento
-----------------------


::

    cd $HOME
    # *** Tools installation & activation ***
    # Case 1: you have not installed zeroincombenze tools
    git clone https://github.com/zeroincombenze/tools.git
    cd $HOME/tools
    ./install_tools.sh -p
    source $HOME/devel/activate_tools
    # Case 2: you have already installed zeroincombenze tools
    cd $HOME/tools
    ./install_tools.sh -U
    source $HOME/devel/activate_tools
    # *** End of tools installation or upgrade ***
    # Odoo repository upgrade
    odoo_install_repository l10n-italy -b 12.0 -o $HOME/12.0 -U
    vem amend $HOME/12.0/venv_odoo -o $HOME/12.0
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


History / Cronologia
--------------------

l10n_it_einvoice_out: 10.0.1.0.19 (2022-01-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Check lettere intento / Test su lettere di intento
* [FIX] Rea capital / controllo capitale sociale


l10n_it_ricevute_bancarie: 10.0.1.3.6 (2022-01-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Button [Cancel] in list / Bottone [Annulla] in distinta
* [IMP] Button [Back2Draft] in list / Bottone [Riporta in bozza] in distinta


l10n_it_lettera_intento: 10.0.0.1.4 (2022-01-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Editable Lettera intento id in invoice / Numero lettera intento in fattura modificabile


l10n_it_account: 10.0.1.2.8 (2022-01-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] New function for einvoice



l10n_it_base: 10.0.0.2.16 (2022-01-27)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Foreign country w/o zip code / Stati esteri senza CAP

l10n_it_einvoice_in: 10.0.1.3.28 (2022-01-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Link existent invoice / Collegamento a fattura esistente


l10n_it_einvoice_import_zip: 10.0.1.0.5 (2022-01-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] XML filename with 4 char suffix / File xml con suffisso di 4 caratteri


l10n_it_einvoice_import: 10.0.1.3.28 (2022-01-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Link existent invoice / Collegamento a fattura esistente


l10n_it_einvoice_send2sdi: 10.0.1.0.20 (2022-01-17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoices counters / Contatori fatture
* [IMP] Lock send if negative counter / Blocco invio se contatore negativo


l10n_it_fiscal: 12.0.0.2.8 (2022-01-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Memorandum accounts (wrongly set as costs) are set as liability


l10n_it_fiscal: 12.0.0.2.7 (2022-01-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Tax for RC with wrong account code / Alcuni codici IVA per RC con conti errati


l10n_it_einvoice_send2sdi: 10.0.1.0.19 (2022-01-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Limit read to max 59 days / Limite lettura a 59 giorni


l10n_it_einvoice_in: 10.0.1.3.27 (2022-01-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Recognize withholding tax with wrong rate / Riconosce RA anche con base errata
* [IMP] Accept invoice with wrong currency / Registra fattura con Divisa errata
* [FIX] Import even if rea_code on no contact record / Importa anche se codice REA in recodr non contatto


l10n_it_einvoice_import: 10.0.1.3.27 (2022-01-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Recognize withholding tax with wrong rate / Riconosce RA anche con base errata
* [IMP] Accept invoice with wrong currency / Registra fattura con Divisa errata
* [FIX] Import even if rea_code on no contact record / Importa anche se codice REA in recodr non contatto


l10n_it_fiscal: 12.0.0.2.6 (2022-01-04)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Module name changed (l10n_it_coa -> l10n_it_coa)


l10n_it_einvoice_out: 10.0.1.0.18 (2022-01-03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Avoid old VAT nature code / Controllo anti utilizzo codici natura scaduti


l10n_it_fiscal: 12.0.0.2.5 (2021-12-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Account group no change on module upgrade
* [FIX] Installation error


l10n_it_fiscal: 12.0.0.2.4 (2021-12-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Tax 5%
* [FIX] Wrong tax Dogana
* [IMP] Taxes for all EU countries


assigned_bank: 10.0.0.1.2 (2021-12-04)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Default from company partner / Valore predefinito da soggetto azienda


l10n_it_fiscal: 12.0.0.2.3 (2021-11-27)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Tax for NL
* [IMP] Fiscal position for EU-OSS


l10n_it_fiscal: 12.0.0.2.2 (2021-10-15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Wrong classification for cut-off and prepayments accounts / Errata classificazione ratei e risconti
* [FIX] Wrong classification for SP tax codes / Errata classificazione codice IVA split-payment


l10n_it_central_journal: 10.0.0.0.5 (2021-09-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if final print / Errore in stampa definitiva


l10n_it_fiscal: 12.0.0.2.1 (2021-08-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] POW-486: Account groups / Tabella gruppi


l10n_it_fiscal: 12.0.0.2.0 (2021-08-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] EU-OSS tax accounts / Conti IVA EU-OSS




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


Last Update / Ultimo aggiornamento: 2022-01-31

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=12.0
    :target: https://travis-ci.com/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
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
   :target: https://t.me/Assitenza_clienti_powERP


