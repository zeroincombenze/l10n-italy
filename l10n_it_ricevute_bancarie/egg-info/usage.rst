Nella configurazione delle Ri.Ba. è possibile specificare se si tratti di
'salvo buon fine' o 'al dopo incasso', che hanno un flusso completamente diverso.

 - Al dopo incasso: nessuna registrazione verrà effettuata automaticamente e le fatture risulteranno pagate solo al momento dell'effettivo incasso.
 - Salvo buon fine: le registrazioni generate seguiranno la struttura descritta in questo documento

E' possibile specificare diverse configurazioni (dal menù
configurazioni -> varie -> Ri.Ba.). Per ognuna, in caso di 'salvo buon fine',
è necessario specificare almeno il sezionale ed il conto da
utilizzare al momento dell'accettazione della distinta da parte della banca.
Tale conto deve essere di tipo 'crediti' (ad esempio "Ri.Ba. all'incasso",
eventualmente da creare).

La configurazione relativa alla fase di accredito, verrà usata nel momento in
cui la banca accredita l'importo della distinta.
E' possibile utilizzare un sezionale creato appositamente, ad esempio "accredito RiBa",
ed un conto chiamato ad esempio "banche c/RIBA all'incasso", che non deve essere di tipo 'banca'.

La configurazione relativa all'insoluto verrà utilizzata in caso di mancato pagamento da parte del cliente.
Il conto può chiamarsi ad esempio "crediti insoluti".

Nel caso si vogliano gestire anche le spese per ogni scadenza con ricevuta bancaria,
si deve configurare un prodotto di tipo servizio e legarlo in
Configurazione -> Contabilità -> Ri.Ba. Configurazione spese d'incasso -> Servizio spese d'incasso.