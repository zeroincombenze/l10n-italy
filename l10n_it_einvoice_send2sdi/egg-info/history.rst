10.0.1.0.33 (2023-04-20)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] new state mappingple

10.0.1.0.29 (2022-08-31)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import e-invoice with multiple attachments
* [FIX] Check for existent attachment (avoid raise)

10.0.1.0.28 (2022-08-22)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] TD17/18/19 recognition

10.0.1.0.27 (2022-07-28)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Module migration

10.0.1.0.26 (2022-06-24)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Module migration

10.0.1.0.25 (2022-06-15)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Old "recipient error" to ready / Stato ready di vecchie fatture

10.0.1.0.22 (2022-06-09)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Now import invoices for all companies / Ora importa le fatture per tutte le aziende

10.0.1.0.21 (2022-02-02)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Sometime "ready" state / Errato stato "ready" in alcuni casi

10.0.1.0.20 (2022-01-17)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoices counters / Contatori fatture
* [IMP] Lock send if negative counter / Blocco invio se contatore negativo

10.0.1.0.19 (2022-01-05)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Limit read to max 59 days / Limite lettura a 59 giorni

10.0.1.0.18 (2021-03-22)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Manage "'Il documento è in fase di invio"

10.0.1.0.17 (2021-03-16)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Send invoice already sent if previous error / Reinvia fattura inviata con errore
* [REF] Messages history / Cronologie invio

10.0.1.0.16 (2021-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Set e_invoice_received_date / Imposta data arrivo SDI

10.0.1.0.15 (2021-03-05)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Set e_invoice_received_date / Imposta data arrivo SDI


10.0.1.0.14 (2021-01-21)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Log http error / Log error http
* [IMP] Fatture consegnate in area riservata sono marcate consegnate

10.0.1.0.13 (2021-01-12)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Get supplier invoice range by parameter / Intervallo fatture fornitori da parametro


10.0.1.0.12 (2020-12-20)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Detailed error messages / Messaggi di errore dettagliata


10.0.1.0.9 (2020-03-31)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash in some error cases / Crash in alcuni casi di rifiuto fattura


10.0.1.0.8 (2020-03-06)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Best display error message / Miglioramento messaggi di errore


10.0.1.0.7 (2020-01-17)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Use custom value of channel / Uso valori personalizzati del canale


10.0.1.0.6 (2019-11-11)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Check for channel URL / Verifica URL del canale
* [IMP] Check for response of errored sent invoices (15 days) / Verifica invio fatture con errore (15 gg)


10.0.1.0.5 (2019-07-10)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Avoid crash if not client_key of channel / No crash se client_key del canale assente
* [IMP] Set error if not response over 5 days / Imposta stato di errore dopo 5 giorni senza risposta


10.0.1.0.4 (2019-06-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Recoginze state "Notifica di esito: documento accettato"
* [IMP] New button "Set to delivered" when recipient_error


10.0.1.0.3 (2019-06-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Checks for valid channel / Test validazione canale
