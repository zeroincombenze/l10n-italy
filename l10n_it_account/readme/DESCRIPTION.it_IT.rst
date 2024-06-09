Modulo tecnico che fornisce alcune strutture utilizzabili da altri moduli
come *l10n_it_vat_registries* e *account_vat_period_end_statement*

I moduli esterni possono usare il campo ``amount_net_pay`` che contiene l'importo
della fattura da pagare. In alcuni casi fiscali, l'importo della fattira da
pagare differisce dal totale fattura; i casi più comuni sono:

* reverse charge
* split-payment
* ritenute d'acconto

Il campi ``amount_net_pay`` è visibile solo se diverso dal totale fattura.
Il modulo può essere usato sia per i documenti passivi che attivi.
