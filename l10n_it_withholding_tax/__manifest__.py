# -*- coding: utf-8 -*-
# Copyright 2015 Alessandro Camilli (<http://www.openforce.it>)
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).
#
{
    "name": "Italian Withholding Tax",
    "version": "10.0.1.2.8",
    "category": "Account",
    "summary": "Italian Withholding Tax",
    "author": ("Odoo Community Association (OCA) and other subjects,Open Force"
               ",Agile Business Group sagl,SHS-AV s.r.l."),
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "account",
        "l10n_it_account",
        "l10n_it_causali_pagamento",
        "l10n_it_einvoice_base",
    ],
    "version_depends": ["l10n_it_account>=10.0.1.2.12"],
    "data": [
        "views/account.xml",
        "views/withholding_tax.xml",
        "security/ir.model.access.csv",
        "workflow.xml",
        "security/security.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
    "pre_init_hook": "check_4_depending",
}
