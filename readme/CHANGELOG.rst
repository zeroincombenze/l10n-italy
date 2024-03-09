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

[IMP] Invoice payment with "DI" configuraiton / Pagamento fattura anche al Dopo Incasso


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
* [QUA] Test coverage 78% (1141: 252+889) [258 TestPoints] - quality rating 46/100


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


l10n_it_ddt: 10.0.1.8.24 (2023-05-31)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] DdT from 'done' order / Emissione DdT da ordini bloccati
* [IMP] Check for dependecies version / Controllo versione dipendenze


l10n_it_ricevute_bancarie: 10.0.1.3.12 (2023-05-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Two supplemental accreditation accounts / Due conti aggiuntivi in accredito
* [FIX] Confirm payment / Conferma pagamento


base_multireport: 10.0.0.2.27 (2023-05-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Layout review / Controllo formattazione stampa


l10n_it_ddt: 10.0.1.8.23 (2023-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Wrong line weight evaluation / Errato calcolo peso riga


l10n_it_conai: 10.0.0.1.9 (2023-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Wrong CONAI quantity / Errata quantità CONAI
* [IMP] Coverage test 63% (504, 188, +20)


base_multireport: 10.0.0.2.26 (2023-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Logo: some time is not printed / IL logo a volte non è stampato


l10n_it_ddt: 10.0.1.8.22 (2023-05-03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Report wrong carrier value / Errato valore vettore in stampa


base_multireport: 10.0.0.2.25 (2023-05-03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Report wrong carrier value / Errato valore vettore in stampa


l10n_it_conai: 10.0.0.1.8 (2023-04-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] CONAI summary line upgradable / Righe riepilogo CONAI modificabili da operatore


l10n_it_einvoice_send2sdi: 10.0.1.0.33 (2023-04-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] new state mapping


l10n_it_ricevute_bancarie: 10.0.1.3.11 (2023-04-17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Confirm invoice + refund / Errore accettazione fattura + NC


l10n_it_ddt: 10.0.1.8.21 (2023-04-17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Delivery price from DN or Sale Order / Calcolo trasporto da DdT o Ordine
* [FIX] Crash with module sale order revision
* [IMP] New test coverage 67% (1373/449/+247)


l10n_it_fiscalcode: 10.0.1.0.4 (2023-04-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Check FC/individual of child record / Controllo CF/PF su record figli


l10n_it_einvoice_in: 10.0.1.3.40 (2023-04-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Import e-invoice from RSM / Importazione file XML da San Marino
* [FIX] Crash when two emails


l10n_it_einvoice_in: 10.0.1.3.39 (2023-04-04)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Check for double email / Controllo doppia mail
* [IMP] New search method to avoid new partner when receiving self-invoice / Controlli per evitare duplicazione fornitore auto-fattura


l10n_it_einvoice_out: 10.0.1.0.25 (2023-03-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] First regression tests: coverage 60% (733/296)


l10n_it_einvoice_in: 10.0.1.3.38 (2023-03-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Import RC invoice w/o tax rate / Import fatture RC senza aliquota IVA


l10n_it_einvoice_base: 10.0.2.1.23 (2023-03-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Fiscal document type for refund / TD04 per note credito


l10n_it_einvoice_out_rc: 10.0.1.0.4 (2023-03-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] AttributeError: 'DatiPagamentoType' object has no attribute 'ImportoPagamento'


l10n_it_einvoice_out_rc: 10.0.1.0.3 (2023-03-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Self-invoice TD17-19 with "IT" vat / Codice IVA italiano modificato eper autofatture TD17-19




