# -*- coding: utf-8 -*-
#    Copyright (C) 2010-17 Associazione Odoo Italia
#                          <http://www.odoo-italia.org>
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2010: odoo-italia] First version
# [2017: SHS-AV, odoo-italia] Totally rewritten
#
{
    'name': 'Check invoice date consistency',
    'version': '7.0.0.1.4',
    'category': 'Tools',
    'description': """(en)
This module check for sequential invoice date because Italian law.

Like OCA module, out_invoice dates are checked.

Also in_invoice registration date are checked (this function is not [yet]
implemented in OCA module).


(it)
Questo modulo controlla la sequenza delle date della fattura per onorare la
legge fiscale italiana.

Come il modulo OCA è controllata la sequenza delle date della fatture di
vendita.

Inoltre è verificata la sequenza della date di registrazione delle fatture
di acquisto (queste funzione non è [ancora] implementata nel modulo OCA).

Il controllo è effettuato sull'anno fiscale e permette la registrazione
contestuale di fatture su 2 anni fiscali diversi durante il periodo di
accavallamento degli esercizi.
""",
    'author': "Zeroincombenze®, "
              "Odoo Italian Community, Odoo Community Association (OCA)",
    'website': 'http://www.odoo-italia.org',
    'license': 'AGPL-3',
    "depends": [
        'account',
        'account_invoice_entry_date',
        'l10n_it_ade'],
    'test': ['test/invoice_sequential.yml', ],
    "active": False,
    "installable": False
}
