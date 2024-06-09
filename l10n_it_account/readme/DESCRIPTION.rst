Technical module that supplies some structures usable by other modules like
*l10n_it_vat_registries* and *account_vat_period_end_statement*

External module can use the field ``amount_net_pay`` which is the amount to pay
the invoice. In some cases, the total invoice amount and the amount to pay can be
different; the most common cases are:

* reverse charge
* Italian split-payment
* withholding tax

The field ``amount_net_pay`` is visible just if it is different from Total Invoice
Amount.
