# -*- coding: utf-8 -*-
# Copyright 2015 Abstract srl (<http://www.abstract.it>)
# Copyright 2015-2017 Agile Business Group (<http://www.agilebg.com>)
# Copyright 2015 Link It Spa (<http://www.linkgroup.it/>)
# Copyright 2018-2024 SHS-AV s.r.l. <https://www.zeroincombenze.it/>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Italian Localization - Account",
    "version": "10.0.1.2.13",
    "category": "Hidden",
    "summary": "Base account for Italian Localizzation",
    "author": ("Odoo Community Association (OCA),Abstract,Agile Business Group sagl"
               ",LinkIt Spa,SHS-AV s.r.l."),
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_fiscal_year",
        "account_tax_balance",
    ],
    "data": [
        "views/account_invoice_view.xml",
        "reports/account_reports_view.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
