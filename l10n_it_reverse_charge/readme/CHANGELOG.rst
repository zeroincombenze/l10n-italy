10.0.1.11 (2025-01-15)
~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Genera autofattura da fattura TD01 con RC locale
* [QUA] Test coverage 79% (378: 80+298) [36 TestPoints] - quality rating 53 (target 100)

10.0.1.10 (2025-12-16)
~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Valida anche autofatture importate ma non precedentemente generate (commercialista)
* [QUA] Test coverage 79% (378: 80+298) [36 TestPoints] - quality rating 53 (target 100)

10.0.1.9 (2025-11-13)
~~~~~~~~~~~~~~~~~~~~~

* [IMP] Data for RC self-invoice on fiscal position / Dati auto-fattura in posizione fiscale
* [QUA] Test coverage 79% (378: 80+298) [36 TestPoints] - quality rating 53 (target 100)

10.0.1.8 (2024-06-28)
~~~~~~~~~~~~~~~~~~~~~

* [IMP] Function get_receivable_line_ids moved to l10n_it_account
* [QUA] Test coverage 64% (404: 146+258) [26 TestPoints] - quality rating 49 (target 100)

10.0.1.7 (2024-06-09)
~~~~~~~~~~~~~~~~~~~~~

* [FIX] Tax with RC requires RC fiscal position / Controllo codici IVA con RC e posizione fiscale
* [IMP] Show net to pay (see l10n_it_account) / Visualizza netto a pagare (vedere l10n_it_account)
* [IMP] RC Amount stored in invoice record / Importo IVA RC in fattura
* [IMP] Sale invoice / Gestione fatture di vendita con RC e netto a pagare
* [IMP] Regression tests
* [QUA] Test coverage 64% (410: 147+263) [26 TestPoints] - quality rating 49 (target 100)

10.0.1.6 (2023-02-20)
~~~~~~~~~~~~~~~~~~~~~

* [IMP] The invoice date of self invoice is the same of the date of purchase invoice / Data auto-fattura come data contabile fattura di acquisto

10.0.1.5 (2023-02-13)
~~~~~~~~~~~~~~~~~~~~~

* [IMP] The date may be different from invoice date for self invoice / Data fattura e contabile diverse per le auto-fatture

10.0.1.4 (2022-06-20)
~~~~~~~~~~~~~~~~~~~~~

* [IMP] Tax nature renamed

10.0.1.3 (2022-03-08)
~~~~~~~~~~~~~~~~~~~~~

* [IMP] Flag RC in account.tax / Flag RC in tasse
