# -*- coding: utf-8 -*-
#
# Copyright 2012, Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2012, Domsense srl (<http://www.domsense.com>)
# Copyright 2017, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2012-2017, Associazione Odoo Italia <https://odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': "Italian Localisation - Withholding tax",
    'version': '7.0.0.2.1',
    'category': 'Localisation/Italy',
    'description': """
Ritenute d'acconto sulle fatture fornitore
==========================================

Configurare i campi associati all'azienda:
 - Termine di pagamento della ritenuta d'acconto
 - Conto di debito per le ritenute da versare
 - Sezionale che conterrà le registrazioni legate alla ritenuta

L'importo della ritenuta d'acconto non è calcolato ma inserito manualmente.
""",
    'author': "Odoo Italia Associazione, Odoo Community Association (OCA)",
    'website': 'http://www.odoo-italia.org',
    'license': 'AGPL-3',
    "depends": ['l10n_it_ade',
                'account_voucher_cash_basis',
                'account_invoice_entry_date'],
    "data": [
        'views/account_view.xml',
        'views/account_invoice_view.xml', ],
    "demo": [
        'demo/account_demo.xml',
    ],
    'test': [
        'test/purchase_payment.yml',
    ],
    "installable": True
}
