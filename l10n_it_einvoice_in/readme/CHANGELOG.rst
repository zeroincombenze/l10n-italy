10.0.1.3.47 (2024-06-14)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash with <AdministrativeReference></AdministrativeReference>
* [QUA] Test coverage 63% (1337: 498+839) [0 TestPoints] - quality rating 38 (target 100)


10.0.1.3.46 (2024-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Again weird error linking self-invoice
* [FIX] Avoid company data update from self-invoice / Non cambia dati aziendali da auto-fattura
* [FIX] Cannot import e-invoice with wrong vat / Ignora PI se errata in e-fattura
* [QUA] Test coverage 63% (1337: 498+839) [0 TestPoints] - quality rating 38 (target 100)

10.0.1.3.45 (2024-05-05)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Weird error linking self-invoice
* [IMP] Avoid company data update from self-invoice
* [QUA] Test coverage 63% (1330: 495+835) [0 TestPoints] - quality rating 38 (target 100)

10.0.1.3.44 (2024-02-06)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] E-Lines detail: name changed

10.0.1.3.43 (2024-01-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash with <RiferimentoTesto></RiferimentoTesto> / Crash in alcuni casi
* [FIX] Search state/district by country code from vat / Ricerca provincia con nazione da PI
* [QUA] Test coverage 63% (1326: 493+833) [0 TestPoints] - quality rating 38 (target 100)

10.0.1.3.42 (2023-10-23)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash with <DatiOrdineAcquisto></DatiOrdineAcquisto> / Crash in alcuni casi
* [QUA] Test coverage 63% (1326: 493+833) [0 TestPoints] - quality rating 38 (target 100)

10.0.1.3.41 (2023-04-11)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash in some strange email
* [FIX] Crash when xml tag with extra property

10.0.1.3.40 (2023-04-11)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Import e-invoice from RSM / Importazione file XML da San Marino
* [FIX] Crash when two emails

10.0.1.3.39 (2023-04-04)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Check for double email / Controllo doppia mail
* [IMP] New search method to avoid new partner when receiving self-invoice / Controlli per evitare duplicazione fornitore auto-fattura

10.0.1.3.38 (2023-03-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Import RC invoice w/o tax rate / Import fatture RC senza aliquota IVA

10.0.1.3.37 (2023-02-16)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Now module does not depend on l10n_it_ddt / Ora il modulo non richiede l'installazione del DdT

10.0.1.3.36 (2022-12-27)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import e-invoice with carrier / Errore importazione fatture con spedizioniere


10.0.1.3.35 (2022-11-14)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import e-invoice with round amount / Errore importazione fatture con arrotondamenti

10.0.1.3.34 (2022-11-07)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import e-invoice with WH / Errore importazione fatture con RA

10.0.1.3.33 (2022-08-22)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Link to opened invoice too

10.0.1.3.32 (2022-06-20)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Tax nature renamed
* [FIX] Error _amount_withholding_tax

10.0.1.3.31 (2022-06-14)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] DdT number = space
* [FIX] New check on partner / Controlli su fornitore

10.0.1.3.30 (2022-04-30)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] New foreign invoices w/o province / Fatture da estero senza provincia

10.0.1.3.29 (2022-03-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Detect RC by rc flag / Riconoscimento RC tramite flag rc

10.0.1.3.28 (2022-01-26)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Link existent invoice / Collegamento a fattura esistente

10.0.1.3.27 (2022-01-05)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Recognize withholding tax with wrong rate / Riconosce RA anche con base errata
* [IMP] Accept invoice with wrong currency / Registra fattura con Divisa errata
* [FIX] Import even if rea_code on no contact record / Importa anche se codice REA in recodr non contatto

10.0.1.3.26 (2021-04-07)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Strange error in fiscal code

10.0.1.3.25 (2021-01-25)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Received date / Data di ricezione fattura

10.0.1.3.24 (2021-01-12)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Disabled xml validation / Validazione file xml disabilitata

10.0.1.3.23 (2021-01-05)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Accept old nature code / Accetta codici natura 2020

10.0.1.3.22 (2020-12-20)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Avoid invoice address duplicate / Evita duplicazione indirizzi di fatturazione impport ft. fornitori


10.0.1.3.21 (2020-11-24)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Wrong address number / Ignora numero civico non valido


10.0.1.3.20 (2020-09-09)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Invalid carrier VAT / Ignora PIVA corriere non valida


10.0.1.3.19 (2020-07-29)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] No import if company IBAN in xml / Non importa fattura se IBAN azienda in file XML


10.0.1.3.18 (2020-07-28)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Duplicare rea_code when invoice address / Codice rea duplicato se uso indirizzo fatturazione


10.0.1.3.17 (2020-07-07)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import error level 2 / Errore importazione livello 2


10.0.1.3.16 (2020-06-16)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] No import self-invoice / Non importa autofatture


10.0.1.3.15 (2020-05-22)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if supplier invoice w/o due_adate / Errore importazione se xml senza date scadenza


10.0.1.3.15 (2020-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash import rated invoice if supplier w/o account / Errore importazione per aliquote e fornitore senza conto


10.0.1.3.13 (2020-04-06)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if wrong invoice date (i.e. 2020-04-06Z) / Errore se data formattata erroneamente


10.0.1.3.13 (2020-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if invoice address / Errore durante importazione con indirizzo di fatturazione

10.0.1.3.12 (2020-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Partner data / Dati fornitore non modificati. Se diversi creato indirizzo fatturazione
* [FIX] Crash in some cases / Errore durante importazione in alcuni casi
* [IMP] More incisive message / Messagi più precisi


10.0.1.3.11 (2020-02-17)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor change / Modifiche interne


10.0.1.3.10 (2020-02-04)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] XML Preview / Anteprima file XML


10.0.1.3.9 (2019-12-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] synchro2 error / Errore sunchro2


10.0.1.3.9 (2019-12-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import e-invoice with RF19 / Errore in importazione fattura da forfettario
* [FIX] Conflict with connector_vg7 module / Conflitto con modulo connector_vg7


10.0.1.3.8 (2019-10-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Link to existent invoice set header data / Il collegamento ad una fattura esistente imposta i dati di testata
* [FIX] Unicode error in delivery address / Errore unicode in indirizzo di consegan
* [IMP] Some supplier invoices have natura N6 without vax rate / Fattura fornitori con natura N6 e senza aliquota IVA


10.0.1.3.7 (2019-06-25)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Without province, cannot import e-invoice


10.0.1.3.6 (2019-06-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Some supplier invoices with empty tags fail schema validation / Alcune fatture fornitori con tag vuoti non erano validate dallo schema
* [FIX] Invoice supplier with existent REA code crashes / Fatture fornitori con codice REA esistente mandavano in crash il sistema
* [IMP] New search algorithm finds similar names / Nuovo algoritmo di ricerca che trova nomi simili
