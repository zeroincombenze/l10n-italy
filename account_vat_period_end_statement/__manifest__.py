# -*- coding: utf-8 -*-
#
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-2012 Domsense s.r.l. (<http://www.domsense.com>).
#    Copyright (C) 2012-17 Agile Business Group (<http://www.agilebg.com>)
#    Copyright (C) 2012-15 LinkIt Spa (<http://http://www.linkgroup.it>)
#    Copyright (C) 2015 Associazione Odoo Italia
#    (<http://www.odoo-italia.org>).
#
{
    "name": "ITA - Liquidazione IVA",
    "summary": "Versamento Iva periodica (mensile o trimestrale) ",
    "version": "10.0.1.5.4",
    "category": "Localization/Italy",
    "license": "AGPL-3",
    "depends": [
        "account_accountant",
        "account_fiscal_year",
        "account_tax_balance",
        "date_range",
        "l10n_it_account",
        "l10n_it_ade",
        "l10n_it_fiscalcode",
        "report",
    ],
    "author": "Agile Business Group, Odoo Community Association (OCA)" ", LinkIt Spa",
    "website": "https://github.com/OCA/l10n-italy",
    "data": [
        "wizard/add_period.xml",
        "wizard/remove_period.xml",
        "security/ir.model.access.csv",
        "security/security.xml",
        "report/reports.xml",
        "views/report_vatperiodendstatement.xml",
        "views/config.xml",
        "views/account_view.xml",
    ],
    "installable": True,
    "development_status": "Beta",
}
