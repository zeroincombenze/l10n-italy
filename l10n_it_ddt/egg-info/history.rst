10.0.1.8.7 (2020-12-07)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Date done updatable / Data spedizione modificabile
* [IMP} Total amount in tree view / Totale importo DdT in vista albero


10.0.1.8.6 (2020-07-20)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Add DdT lines to invoice / Aggiunta righe DdT a fattura esistente


10.0.1.8.2 (2020-02-19)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Change version id / Cambio identificativo versione
* [IMP] Invoicing by order / Fatturazione divisa per ordini


10.0.1.5.14 (2020-01-21)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Qty zero becomes 1 in Invoice / Q.tà zero diventa 1 in fattura


10.0.1.5.13 (2019-12-11)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Line weight / Peso in riga


10.0.1.5.12 (2019-11-20)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Total amount of stock.package.preparation / Totale del DdT


10.0.1.5.11 (2019-11-11)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Sometime it crashes when cancel sale order / A volte sistema andava in crash in annullo ordine


10.0.1.5.10 (2019-10-18)
~~~~~~~~~~~~~~~~~~~~~~~~

* [REF] Delivery condition inheritance / Determinazione dei valori di consegna
* [FIX] Weights are evaluated from pickig or order / I pesi del DdT sono calcolati dal prelivo o dall'ordine
* [IMP] Parcels is the sum of picking or order parcels / I colli sono la somma dei colli del prelievo o dell'ordine
* [IMP] Volume is the sum of picking or order volume / Il volume è la somma dei volumi del prelievo o dell'ordine
* [FIX] Show price is inherit from customer / Il flag mostra prezzi è ereditato del cliente


10.0.1.5.9 (2019-10-15)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Default delivery data by xmlrpc tough / Imposta dati predefiniti di traporto anche da xmlrpc


10.0.1.5.8 (2019-09-23)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Total amount in line / Importo totale di riga
* [FIX] Order cancel unlink DdTs too / Annullo ordine elimina anche i DdT
* [FIX] Order confirm with DdT set 'to invoice' / Conferma ordine, se crea DdT, imposta ordine da fatturare
* [FIX] Unlink DdT recover sequence number / L'eliminazione di un DdT recupera il numero, se ultimo DdT


10.0.1.5.7 (2019-09-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Shipping condition by carrier / Informazioni di spedizione da metodo di consegna


10.0.1.5.6 (2019-09-03)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Sale invoice ref / Riferimento al numero di ordine


10.0.1.5.5 (2019-08-26)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice from delivery documents base on flag / La creazione righe da ordine non in DdT è opzionale


10.0.1.5.4 (2019-06-24)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Print UoM in lines / Stampa UM in dettagli
* [IMP] DdT type visible in picking / Tipo DdT visbile nella consegna
* [IMP] DdT type in sale order / Tipo DdT in ordine di vendita


10.0.1.5.3 (2019-05-20)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice from delivery documents add service lines from sale order / La creazione della fattura da ordine aggiunge le righe di servizi che non sono in DdT


10.0.1.5.2
~~~~~~~~~~

* [IMP] Ref. fields not copied / Campi con riferimenti con copiati in duplica DdT
* [IMP] DdT name based on DdT number or partner name / Nome DdT (per ricerche) basato su numero o nome cliente
* [IMP] Report header / Cessionario e Destinatario in modello di stampa
