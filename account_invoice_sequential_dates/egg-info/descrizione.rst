Sequenza numero fattura

Questo modulo controlla la sequenza delle date della fattura per onorare la
legge fiscale italiana.
.. $if branch in '10.0'

Il modulo è stato abbandoanto dal gruppo Italiano di OCA quando OCA ha publicato un modulo analogo
Tcon il nome account_invoice_constraint_chronology nella repository account-financial-tools.

Questo modulo agisce in modo diverso a causa della legislazione italiana più restrittiva delle regole europee.
.. $fi

Il modulo previene la validazione se:

* La data fattura è antecedente la precednte fattura
* La data fattura è posteriore rispetto alla successiva fattura, se rivalidata
