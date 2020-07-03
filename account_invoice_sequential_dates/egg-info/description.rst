This module helps ensuring the sequence of sale invoice numbers because Italian law.
.. $if branch in '10.0'

This modulo was deprecated by Italian OCA Group
when OCA published a module to ensue the chronology of invoice numbers.
The OCA module is account_invoice_constraint_chronology in repository account-financial-tools.

This module acts in different way because Italian law is more restrictive from European rules.
.. $fi

It prevents the validation of sale invoices when:

* invoice date is less than previous invoice number date
* invoice date is greater then next invoice date, when invoice ir re-validated
