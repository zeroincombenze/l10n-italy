# -*- coding: utf-8 -*-
# Copyright 2017 Davide Corio
# Copyright 2017 Alex Comba - Agile Business Group
# Copyright 2017 Lorenzo Battistini - Agile Business Group
# Copyright 2017 Marco Calcagni - Dinamiche Aziendali srl
# Copyright 2019-24 Antonio M. Vigliotti - SHS-Av srl
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Reverse Charge Tax",
    "version": "10.0.1.8",
    "category": "Localization/Italy",
    "summary": "Manage Reverse Charge Tax for Italy",
    "author": "Odoo Italia Network,Odoo Community Association (OCA),SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "account_accountant",
        "account_cancel",
        "l10n_it_ade",
        "l10n_it_account",
    ],
    "version_depends": ["l10n_it_account>=10.0.1.2.13"],
    "data": [
        "security/ir.model.access.csv",
        "data/rc_type.xml",
        "security/ir.model.access.csv",
        "views/account_invoice_view.xml",
        "views/account_fiscal_position_view.xml",
        "views/account_rc_type_view.xml",
        "views/account_tax_view.xml",
        "security/reverse_charge_security.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
    "pre_init_hook": "check_4_depending",
}
