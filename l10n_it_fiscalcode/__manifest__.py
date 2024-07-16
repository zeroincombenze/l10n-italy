# -*- coding: utf-8 -*-
#    Copyright (C) 2014-2018 Associazione Odoo Italia (<http://www.odoo-italia.org>)
#    Copyright (C) 2016      Andrea Gallina (Apulia Software)
#    Copyright (C) 2018      Antonio Vigliotti <https://www.zeroincombenze.it>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
{
    "name": "Italian Localisation - Fiscal Code",
    "version": "10.0.1.0.5",
    "category": "Localisation/Italy",
    "summary": "Italian Localisation - Fiscal Code",
    "author": ("Odoo Italia Network,Odoo Community Association (OCA)"
               ",Agile Business Group sagl,Abstract,Apulia Software s.r.l."
               ",SHS-AV s.r.l."),
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Production/Stable",
    "license": "AGPL-3",
    "depends": ["base_vat"],
    "external_dependencies": {'python': ['codicefiscale']},
    "data": [
        "views/fiscalcode_view.xml",
        "wizard/compute_fc_view.xml",
        "data/res.city.it.code.csv",
        "security/ir.model.access.csv",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
