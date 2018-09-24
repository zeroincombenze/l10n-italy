# -*- coding: utf-8 -*-
# Copyright 2018 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                  Associazione Odoo Italia <http://www.odoo-italia.org>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by l10n_it_account of OCA
#
{
    "name": "Base xml Agenzia delle Entrate",
    "version": "11.0.0.1.10",
    "category": "Localization/Italy",
    "summary": "Codice con le definizioni dei file xml Agenzia delle Entrate",
    "author": "SHS-AV s.r.l.,"
              " Odoo Italia Associazione",
    "maintainer": "Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "license": "LGPL-3",
    "depends": [
        'account',
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/italy.ade.tax.nature.csv',
        'data/italy.ade.codice.carica.xml',
        'views/ir_ui_menu.xml',
        'views/account_tax_view.xml',
        # 'views/account_journal.xml',
        'views/codice_carica_view.xml',
        'views/tax_nature_view.xml',
    ],
    'installable': True,
    "external_dependencies": {
        "python": ["pyxb"],
    }
}
