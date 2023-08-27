L'utilizzo delle Ri.Ba. utilizza i seguenti menù:

|menu| Contabilità > Pagamenti > Ri.Ba Configurazione

|menu| Contabilità > Management > Termini di pagamento

|menu| Contabilità > Ri.Ba > Distinte

|menu| Contabilità > Ri.Ba > Emetti Ri.Ba

|menu| Contabilità > Ri.Ba > Fatture insolute


Configurazione
~~~~~~~~~~~~~~

Nella configurazione delle Ri.Ba. è possibile specificare il tipo di distinta:

* DI (Dopo Incasso): nessuna registrazione è effettuata automaticamente
* SBF (Salvo Buon Fine): sono emesse le registrazioni come descritte qui sotto

Per attivare la gestione Ri.Ba. è necessario impostare il tipo 'Ri.Ba.' nei termini di pagamento.


Gestione distinta
~~~~~~~~~~~~~~~~~

Ai fini di una corretta comprensione si ipotizza la gestiona da una fattura da 100€ + IVA.
Si ricorda che a scrittura contabile è della fattura è la seguente:

.. $include example-invoice.rst

Per iniziare il flusso, usare il menù `Contabilità > Ri.Ba > Emetti Ri.Ba`, selezionare le scadenze da inserire in distinta
e dal bottone `Azione` selezionare `Emetti Ri.Ba`. Scegliere un conto bancario configurato.

Scaricare il file CBI da presentare in banca: dal bottone `Azione` selezionare `Esporta Ri.Ba`.

Quando la banca conferma l'accettazione della distinta, dal menù `Contabilità > Ri.Ba > Emetti Ri.Ba`
selezionare la distinta ed impostare lo stato di `Accettata` tramite l'apposito bottone.
Se la distinta è di tipo SBF viene generata la seguente scrittura contabile (una registrazionne per ogni scadenza in distinta):

.. $include example-riba.rst

Quando la banca accredita la distinta, impostare lo stato `Accreditata` tramite l'apposito bottone.
Se la distinta è di tipo SBF si può generare la seguente scrittura contabile:

.. $include example-paylist.rst

Quando la ricevuta è effettivamente pagata dal cliente è possibile dichiararlo nella relativa riga della distinta.
Se la distinta è di tipo SBF viene generata la sequente scrittura contabile:

.. $include example-payment.rst


Note finali
~~~~~~~~~~~

Per ogni stato della distinta è possibile sia avanzare allo stato successivo che ripristinare lo stato precedente.
Le relative registrazioni contabili saranno inserite o rimosse in modo da mantenere il sistema sempre nel corretto stato contabile.

Si può dichiarare ogni singola scadenza come pagata o insoluta. Anche per le singole scadenze è possibili ripristinare lo stato precedente.
