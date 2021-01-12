
================================
|Zeroincombenze| l10n-italy 10.0
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
* Documenti con Reverse Charge

Avaiable Addons / Moduli disponibili
------------------------------------

+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| Name / Nome                          | Version    | OCA Ver.   | Description / Descrizione                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_central_journal              | |no_check| | |halt|     | Account Central Journal                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_check_total          | 10.0.1.0.0 | |no_check| |  Check if the verification total is equal to the bill's total                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_entry_date           | 10.0.0.1.1 | |halt|     | Account Invoice Entry Dates                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_entry_dates          | 10.0.1.0.4 | |no_check| | Registration, vat/balance application dates                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_report_ddt_group     | 10.0.0.3.1 | |same|     | Account invoice report grouped by DDT                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_invoice_sequential_dates     | |no_check| | |halt|     | Check invoice date consistency                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_period                       | 10.0.1.0   | |no_check| | Account Period                                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_vat_period_end_statement     | 10.0.1.5.1 | |same|     | Versamento Iva periodica (mensile o trimestrale)                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| assigned_bank                        | 10.0.0.1.1 | |no_check| | Assign internal bank to customers or supplier                                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| base_multireport                     | 10.0.0.2.2 | |no_check| | Manage document multiple reports                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_eu_trial_balance                | |halt|     | |no_check| | 2013/34/EU - Trial Balance + Financial Statements                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_CEE_balance_generic          | |halt|     | |halt|     | Italy - 4th EU Directive - Consolidation Chart of Accounts                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_abicab                       | 10.0.1.0.0 | |same|     | Base Bank ABI/CAB codes                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account                      | 10.0.1.2.5 | 10.0.1.2.4 | Italian Localization - Account                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp                | |no_check| | 10.0.1.0.1 | Tax stamp automatic management                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp_ddt            | |no_check| | 10.0.1.0.0 | Modulo ponte tra imposta di bollo e DDT                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_stamp_sale           | |no_check| | 10.0.1.0.1 | Modulo ponte tra imposta di bollo e vendite                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_account_tax_kind             | |no_check| | 10.0.2.0.0 | Italian Localisation - Natura delle aliquote IVA                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ade                          | 10.0.0.3.1 | |no_check| | Codice e definizioni come da Agenzia delle Entrate                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ateco                        | |halt|     | |same|     | Ateco codes                                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_base                         | 10.0.0.2.1 | |no_check| | Italian Localisation - Base                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_base_crm                     | |halt|     | |halt|     | Italian Localisation - CRM                                                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_base_location_geonames_impor | 10.0.1.0.0 | |same|     | Import base_location entries (provinces) from Geonames                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_bill_of_entry                | |halt|     | |halt|     | Italian Localisation - Bill of Entry                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_causali_pagamento            | 10.0.1.0.0 | 10.0.2.0.0 | Aggiunge la tabella delle causali di pagamento da usare ad esempio nelle ritenut |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_central_journal              | 10.0.0.0.3 | 10.0.1.0.2 | Italian Localization - Account central journal                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_codici_carica                | |no_check| | 10.0.1.0.0 | Aggiunge la tabella dei codici carica da usare nei dichiarativi fiscali italiani |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_conai                        | 10.0.0.1.6 | |no_check| | Dati CONAI in fattura e calcolo importi                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi                | 10.0.1.1.0 | 10.0.1.2.4 | Italian Localization - Corrispettivi                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_corrispettivi_sale           | |no_check| | 10.0.1.0.3 | Modulo per integrare i corrispettivi in odoo con gli ordini di vendita.          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ddt                          | 10.0.1.8.1 | 10.0.1.9.0 | Delivery Document to Transfer                                                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_dichiarazione_intento        | |no_check| | 10.0.1.0.0 | Gestione dichiarazioni di intento                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_base                | 10.0.2.1.1 | |no_check| | Infrastructure for Italian Electronic Invoice + FatturaPA                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_export_zip          | 10.0.1.0.0 | |no_check| | Esportazione di file XML di fatture elettroniche in uno ZIP da esportare.        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_import_zip          | 10.0.1.0.4 | |no_check| | Importazione di file XML di fatture elettroniche da uno ZIP                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_in                  | 10.0.1.3.2 | |no_check| | Ricezione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_out                 | 10.0.1.0.1 | |no_check| | Electronic invoices emission                                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_out_ddt             | 10.0.1.0.2 | |no_check| | Modulo ponte tra emissione fatture elettroniche e DDT                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_send2sdi            | 10.0.1.0.1 | |no_check| | Send E-Invoice to customer by SdI                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_einvoice_stamp               | 10.0.1.0.5 | |no_check| | Tax stamp automatic management                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_esigibilita_iva              | |no_check| | 10.0.1.0.0 | Esigibilità IVA                                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa                    | |no_check| | 10.0.3.0.0 | Fatture elettroniche                                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_export_zip         | |no_check| | 10.0.1.0.0 | Permette di esportare in uno ZIP diversi file XML di fatture elettroniche        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in                 | |no_check| | 10.0.3.0.0 | Ricezione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in_purchase        | |no_check| | 10.0.1.0.0 | Modulo ponte tra ricezione fatture elettroniche e acquisti                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_in_rc              | |no_check| | 10.0.2.0.0 | Modulo di collegamento tra e-fattura in acquisto e reverse charge                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out                | |no_check| | 10.0.2.0.0 | Emissione fatture elettroniche                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_ddt            | |no_check| | 10.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e DDT                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_stamp          | |no_check| | 10.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e imposta di bollo               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_triple_discoun | |no_check| | 10.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e sconto triplo                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_out_wt             | |no_check| | 10.0.2.0.0 | Modulo ponte tra emissione fatture elettroniche e ritenute.                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fatturapa_pec                | |no_check| | 10.0.1.9.0 | Invio fatture elettroniche tramite PEC                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal                       | 10.0.0.2.0 | |no_check| | Italy - Fiscal localization by zeroincombenze(R)                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_document_type         | |no_check| | 10.0.2.0.0 | Italian Localization - Tipi di documento fiscale per dichiarativi                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_ipa                   | 10.0.1.1.1 | |no_check| | IPA Code and Destination Code in Partner Record                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscal_payment_term          | 10.0.1.0.0 | 10.0.2.0.0 | Electronic & Fiscal invoices payment                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode                   | 10.0.1.0.3 | 10.0.1.3.0 | Italian Localisation - Fiscal Code                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_fiscalcode_invoice           | 10.0.1.0.0 | |same|     | Italian Fiscal Code in invoice PDF                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_intrastat                    | |no_check| | 10.0.1.0.2 | Riclassificazione merci e servizi per dichiarazioni Intrastat                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_intrastat_statement          | |no_check| | 10.0.1.0.2 | Dichiarazione Intrastat per l'Agenzia delle Dogane                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_invoices_data_communication  | |no_check| | 10.0.1.1.2 | Comunicazione dati fatture (c.d. "nuovo spesometro" o "esterometro")             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_invoices_data_communication_ | |no_check| | 10.0.1.0.0 | Integrazione fatturazione elettronica e Comunicazione dati fatture (c.d. "nuovo  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ipa                          | |no_check| | 10.0.2.0.0 | IPA Code (IndicePA)                                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_lettera_intento              | 10.0.0.1.3 | |no_check| | Lettere di intento                                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_location_nuts                | |no_check| | 10.0.1.0.1 | NUTS specific options for Italy                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_partially_deductible_vat     | |halt|     | |halt|     | Italy - Partially Deductible VAT                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pec                          | 10.0.1.0.0 | |same|     | Pec Mail                                                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pos_fatturapa                | |no_check| | 10.0.1.0.0 | Gestione dati fattura elettronica del cliente all'interno dell'interfaccia del P |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_pos_fiscalcode               | |no_check| | 10.0.1.0.0 | Gestione codice fiscale del cliente all'interno dell'interfaccia del POS         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_prima_nota_cassa             | |halt|     | |halt|     | Italian Localisation - Prima Nota Cassa                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_rea                          | 10.0.1.1.2 | |same|     | Gestisce i campi del Repertorio Economico Amministrativo                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_reverse_charge               | 10.0.1.2.3 | 10.0.1.2.2 | Reverse Charge for Italy                                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_riba_commission              | |halt|     | |same|     | Ricevute bancarie & commissioni                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_ricevute_bancarie            | 10.0.1.3.6 | 10.0.1.3.0 | Ricevute Bancarie                                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_sdi_channel                  | |no_check| | 10.0.1.2.0 | Aggiunge il canale di invio/ricezione dei file XML attraverso lo SdI             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_split_payment                | 10.0.1.0.4 | 10.0.1.1.0 | Split Payment                                                                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_communication            | 10.0.0.2.0 | |no_check| | Comunicazione periodica IVA                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_vat_registries               | 10.0.1.3.0 | 10.0.1.3.1 | Italian Localization - VAT Registries                                            |
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
| l10n_it_withholding_tax              | 10.0.1.2.6 | 10.0.2.0.0 | Italian Withholding Tax                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_causali      | |no_check| | 10.0.1.0.0 | Causali pagamento per ritenute d'acconto                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_payment      | 10.0.1.1.0 | 10.0.2.0.0 | Italian Withholding Tax Payment                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| l10n_it_withholding_tax_payment_orde | |no_check| | 10.0.1.0.0 | Modulo ponte tra ritenuta d'acconto e ordine di pagamento                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| multibase_plus                       | 10.0.0.1.4 | |no_check| | Enhanced Odoo Features                                                           |
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
| $HOME/10.0                                                                 |
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
    odoo_install_repository l10n-italy -b 10.0 -O zero -o $HOME/10.0
    vem create $HOME/10.0/venv_odoo -O 10.0 -a "*" -DI -o $HOME/10.0



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
    odoo_install_repository l10n-italy -b 10.0 -o $HOME/10.0 -U
    vem amend $HOME/10.0/venv_odoo -o $HOME/10.0
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


Last Update / Ultimo aggiornamento: 2021-01-12

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
   :target: https://t.me/axitec_helpdesk

