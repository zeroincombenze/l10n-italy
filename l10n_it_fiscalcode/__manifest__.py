# Copyright 2014 Associazione Odoo Italia (<http://www.odoo-italia.org>)
# Copyright 2016 Andrea Gallina (Apulia Software)
# Copyright 2018 Matteo Bilotta (Link IT s.r.l.)
# Copyright 2018 Lorenzo Battistini (https://github.com/eLBati)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Italian Localization - Fiscal Code",
    "version": "12.0.1.1.5",
    "category": "Localisation/Italy",
    "summary": "Italian Localization - Fiscal Code",
    "author": ("Link IT s.r.l.,Apulia Software,Odoo Italia Network"
               ",Odoo Community Association (OCA),SHS-AV s.r.l."),
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Production/Stable",
    "license": "AGPL-3",
    "depends": ["base_vat"],
    "external_dependencies": {'python': ['codicefiscale']},
    "data": [
        "security/ir.model.access.csv",
        "data/res.city.it.code.csv",
        "views/fiscalcode_view.xml",
        "views/report_invoice_document.xml",
        "wizard/compute_fc_view.xml",
        "views/company_view.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
