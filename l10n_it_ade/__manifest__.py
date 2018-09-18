# -*- coding: utf-8 -*-
#
# Copyright 2018 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2018 - Associazione Odoo Italia <http://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by l10n_it_account of OCA
#
{
    "name": "Base xml Agenzia delle Entrate",
    "version": "10.0.0.1.9",
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
        'views/account_tax_view.xml',
        'views/tax_nature_view.xml',
        ],
    'installable': True,
    "external_dependencies": {
        "python": ["pyxb"],
    }
}
