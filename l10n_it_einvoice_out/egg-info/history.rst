10.0.1.0.18 (2021-01-03)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Avoid old VAT nature code / Controllo anti utilizzo codici natura scaduti

10.0.1.0.17 (2020-09-10)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Check for flag subject_electronic_invoice / Controllo cliente soggetto a fattura elettronica


10.0.1.0.16 (2020-07-02)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Non XML with multiple invoices / Genera 1 XML per ogni fattura


10.0.1.0.15 (2020-05-05)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Comment lines / Righe di descrizione senza codice IVA ne prezzo


10.0.1.0.14 (2020-02-12)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Invoice address empty / Compila indirizzo di fatturazione vuoto


10.0.1.0.13 (2020-02-04)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] XML Preview / Anteprima file XML


10.0.1.0.12 (2020-02-03)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] PDF Attachment / Inserimento allagetao PDF in e-fattura


10.0.1.0.11 (2019-11-07)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] PA with VAT number / Reinserita partita IVA per fatture PA
* [IMP] No fiscal code if equal to TIN (by parameter) / Codice fiscale non inserito se equale alla partita IVA (parametrico)


10.0.1.0.10 (2019-09-27)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Set xml data for Foreign customers w/o vat / Compilato il campo partita IVA per clienti esteri senza P.IVA


10.0.1.0.9 (2019-07-30)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] If customer has flag PA, vat becomes fiscal code / Se cliente con flag PA trasforma la P.IVA in codice fiscale


10.0.1.0.8 (2019)
~~~~~~~~~~~~~~~~~

* [FIX] No vat id customer is PA or no-profit company / Se cliente PA o ente no-profit non è inserita la P.IVA nel file xml
