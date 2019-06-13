Ricevute Bancarie
-----------------

Per utilizzare il meccanismo delle Ri.Ba. è necessario configurare un termine
di pagamento di tipo 'Ri.Ba.'.

Per emettere una distinta bisogna andare su Ri.Ba. -> emetti Ri.Ba. e
selezionare i pagamenti per i quali emettere la distinta.
Se per il cliente è stato abilitato il raggruppo, i pagamenti dello stesso
cliente e con la stessa data di scadenza andranno a costituire un solo elemento
della distinta.

I possibili stati della distinta sono: bozza, accettata, accreditata, pagata,
insoluta, annullata.

Ad ogni passaggio di stato sarà possibile generare le relative registrazioni
contabili, le quali verranno riepilogate nel tab 'contabilità'.
Questo tab è presente sia sulla distinta che sulle sue righe.

*Esempio*

* Emissione fattura di 100€ verso cliente1.
* Metodo di pagamento: riba salvo buon fine.

`Fattura`

.. $include example-invoice.rst

`Emissione RiBA`

.. $include example-riba.rst


`Accredito distinta RiBA`

.. $include example-paylist.rst


`Pagamento effettivo RiBA`

.. $include example-payment.rst
