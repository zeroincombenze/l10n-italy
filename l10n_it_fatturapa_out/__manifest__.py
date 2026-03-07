# Copyright 2014 Davide Corio
# Copyright 2015-2016 Lorenzo Battistini - Agile Business Group
# Copyright 2018 Sergio Zanchetta (Associazione PNLUG - Gruppo Odoo)
# Copyright 2018 Sergio Corato
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "ITA - Fattura elettronica - Emissione",
    "version": "12.0.2.2.5_10",
    "category": "Localization/Italy",
    "summary": "Emissione fatture elettroniche",
    "author": ("Davide Corio,Agile Business Group,Innoviu"
               ",Odoo Community Association (OCA),SHS-AV s.r.l."),
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "l10n_it_account",
        "l10n_it_fatturapa",
        "l10n_it_split_payment",
    ],
    "external_dependencies": {
        "python": [
            "unidecode",
            "pyxb",
        ],
    },
    "data": [
        "wizard/wizard_export_fatturapa_view.xml",
        "wizard/wizard_export_fatturapa_view_regenerate.xml",
        "views/attachment_view.xml",
        "views/account_view.xml",
        "views/partner_view.xml",
        "views/company_view.xml",
        "security/ir.model.access.csv",
        "data/l10n_it_fatturapa_out_data.xml",
        "security/rules.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
