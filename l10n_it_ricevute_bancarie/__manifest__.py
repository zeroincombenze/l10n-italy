# -*- coding: utf-8 -*-
# Copyright (C) 2012 Andrea Cometa.
# Email: info@andreacometa.it
# Web site: http://www.andreacometa.it
# Copyright (C) 2012 Associazione OpenERP Italia
# (<http://www.odoo-italia.org>).
# Copyright (C) 2012-2017 Lorenzo Battistini - Agile Business Group
# Copyright 2018-22 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Ricevute Bancarie",
    "version": "10.0.1.3.10",
    "category": "Accounting & Finance",
    "author": "Odoo Community Association (OCA)",
    "category": "Accounting & Finance",
    "website": "https://odoo-community.org/",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_accountant",
        "l10n_it_fiscalcode",
        "account_due_list",
        "base_iban",
        "l10n_it_abicab",
    ],
    "data": [
        "views/partner_view.xml",
        "views/configuration_view.xml",
        "data/riba_sequence.xml",
        "wizard/wizard_accreditation.xml",
        "wizard/wizard_unsolved.xml",
        "views/riba_view.xml",
        "views/account_view.xml",
        "wizard/wizard_riba_issue.xml",
        "wizard/wizard_riba_file_export.xml",
        "views/account_config_view.xml",
        "data/riba_workflow.xml",
        "views/distinta_report.xml",
        "views/report.xml",
        "security/ir.model.access.csv",
    ],
    "demo": ["demo/riba_demo.xml"],
    "installable": True,
}
