Fattura Elettronica in
----------------------

Questo modulo consente di importare i file XML della fattura elettronica versione 1.2

http://www.fatturapa.gov.it/export/fatturazione/it/normativa/f-2.htm

ricevuti attraverso il Sistema di Interscambio (SdI).

http://www.fatturapa.gov.it/export/fatturazione/it/sdi.htm


::

    Destinatari:

Il modulo è destinato a tutte le aziende che dal 2019 dovranno emettere fattura elettronica


::

    Normativa:

Le leggi inerenti la fattura elettronica sono numerose. Potete consultare la `normativa fattura elettronica <https://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm>`__


|warning| Lo schema di definizione dei file xml, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml dell'Agenzia delle Entrate; come conseguenza nasce un conflitto tra
moduli diversi che riferiscono allo schema dell'Agenzia delle Entrate,
segnalato dall'errore:

|exclamation| **name CryptoBinary used for multiple values in typeBinding**


Tutti i moduli della localizzazione italiana che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate **devono** dichiare il modulo
`l10n_it_ade <../l10n_it_ade>`__ come dipendenza.

Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'ultimo autore: Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>.

|halt| Non utilizzare ancora questo modulo in produzione: alpha release soggetta
ad ulteriori modifiche

er ciascun fornitore è possibile impostare il "Livello dettaglio e-fatture":

 - Livello minimo: la fattura fornitore viene creata senza righe, che dovranno essere create dall'utente in base a quanto indicato nella fattura elettronica
 - Livello massimo: le righe della fattura fornitore verranno generate a partire da tutte quelle presenti nella fattura elettronica

Nella scheda fornitore è inoltre possibile impostare il "Prodotto predefinito per e-fattura": verrà usato, durante la generazione delle fatture fornitore, quando non sono disponibili altri prodotti adeguati. Il conto e l'imposta della riga fattura verranno impostati in base a quelli configurati nel prodotto.

Tutti i codici prodotto usati dai fornitori possono essere impostati nella relativa scheda, in

Magazzino →  Prodotti
