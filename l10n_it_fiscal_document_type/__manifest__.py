# Copyright 2017 Alessandro Camilli
# Copyright 2018 Sergio Zanchetta (Associazione PNLUG - Gruppo Odoo)
# Copyright 2018 Lorenzo Battistini (https://github.com/eLBati)
# Copyright 2023 Simone Rubino - TAKOBI
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "ITA - Tipi di documento fiscale per dichiarativi",
    "version": "12.0.2.2.0",
    "category": "Localisation/Italy",
    "summary": "ITA - Tipi di documento fiscale per dichiarativi",
    "author": "LinkIt Spa,Odoo Community Association (OCA),SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "depends": [
        "l10n_it_account",
        "test_mail",
    ],
    "data": [
        "views/fiscal_document_type_view.xml",
        "views/res_partner_view.xml",
        "views/account_invoice_view.xml",
        "views/account_view.xml",
        "data/fiscal.document.type.csv",
        "security/ir.model.access.csv",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
