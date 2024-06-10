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



