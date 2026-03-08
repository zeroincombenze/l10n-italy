# Copyright 2015 AgileBG SAGL <http://www.agilebg.com>
# Copyright 2015 innoviu Srl <http://www.innoviu.com>
# Copyright 2018 Lorenzo Battistini
# Copyright 2018 Sergio Zanchetta (Associazione PNLUG - Gruppo Odoo)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "ITA - Fattura elettronica - Ricezione",
    "version": "12.0.3.1.10",
    "category": "Localization/Italy",
    "summary": "Ricezione fatture elettroniche",
    "author": ("Agile Business Group,Innoviu,Odoo Community Association (OCA)"
               ",SHS-AV s.r.l."),
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "base_vat_sanitized",
        "l10n_it_fatturapa",
        "l10n_it_withholding_tax_causali",
    ],
    "data": [
        "views/account_view.xml",
        "views/partner_view.xml",
        "wizard/wizard_import_fatturapa_view.xml",
        "wizard/link_to_existing_invoice.xml",
        "views/company_view.xml",
        "security/ir.model.access.csv",
        "security/rules.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
