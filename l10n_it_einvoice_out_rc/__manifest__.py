# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "ITA - Fattura elettronica - Emissione e-fattura con reverse charge",
    "version": "10.0.1.0.4",
    "category": "Localization/Italy",
    "summary": "Integrazione l10n_it_fatturapa_out e l10n_it_reverse_charge",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "l10n_it_einvoice_out",
        "l10n_it_einvoice_in",
        "l10n_it_reverse_charge",
    ],
    "data": ['views/rc_type_views.xml'],
    "installable": True,
}
