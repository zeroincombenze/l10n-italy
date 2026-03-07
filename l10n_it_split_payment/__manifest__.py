# Copyright 2015  Davide Corio <davide.corio@abstract.it>
# Copyright 2015-2018  Lorenzo Battistini - Agile Business Group
# Copyright 2016  Alessio Gerace - Agile Business Group
# Copyright 2018  Ruben Tonetto (Associazione PNLUG - Gruppo Odoo)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Split Payment",
    "version": "12.0.1.0.1_12",
    "category": "Localization/Italy",
    "summary": "Split Payment",
    "author": ("Abstract,Agile Business Group,Odoo Community Association (OCA)"
               ",SHS-AV s.r.l."),
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "depends": [
        "account",
        "l10n_it_account_zma",
        "account_payment_method",
        "account_duedates",
        "account_move_line_type",
    ],
    "data": [
        "views/account_view.xml",
        "views/config_view.xml",
    ],
    "maintainer": "powERP enterprise network",
    "installable": True,
    "pre_init_hook": "pre_init_hook",
}
