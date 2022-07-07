# -*- coding: utf-8 -*-
#
# Copyright 2022 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
{
    "name": "Prodotti Espresso",
    "version": "10.0.1.0.0",
    "category": "Accounting",
    "summary": "Prodotti espresso",
    "author": "SHS-AV s.r.l. and other partners",
    "website": "",
    "development_status": "Beta",
    "license": "OPL-1",
    "depends": [
        "base",
        "sale",
        "mrp",
        "l10n_it_ddt",
    ],
    "data": [
        "views/product_views.xml",
        "views/action_generate_ddt.xml",
        "wizard/wizard_create_ddt_espresso_view.xml",
    ],
    "installable": False,
}
