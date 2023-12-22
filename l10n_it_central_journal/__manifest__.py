# -*- coding: utf-8 -*-
# Author: Gianmarco Conte - Dinamiche Aziendali Srl
# Copyright 2017
# Dinamiche Aziendali Srl <www.dinamicheaziendali.it>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "ITA - Account central journal",
    "version": "10.0.0.0.7",
    "category": "Localization/Italy",
    "summary": "Print fiscal account journal",
    "author": "Dinamiche Aziendali,Odoo Community Association (OCA),SHS-AV s.r.l.",
    "website": "https://github.com/OCA/l10n-italy/10.0/l10n_it_central_journal",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "depends": [
        "account",
        "l10n_it_account",
        "date_range",
    ],
    "data": [
        "security/ir.model.access.csv",
        "report/reports.xml",
        "wizard/print_giornale.xml",
        "views/report_account_central_journal.xml",
        "views/date_range_view.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
