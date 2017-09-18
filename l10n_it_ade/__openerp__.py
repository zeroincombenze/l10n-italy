# -*- coding: utf-8 -*-
# Copyright 2017 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                  Associazione Odoo Italia <http://www.odoo-italia.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    "name": "Base xml Agenzia delle Entrate",
    "version": "7.0.0.1.0",
    "category": "Localization/Italy",
    "summary": "Codice con le definizioni dei file xml Agenzia delle Entrate",
    "author": "SHS-AV s.r.l.,"
              " Odoo Italia Associazione",
    "maintainer": "Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "description": """(en)

Italian Localization - Definition for xml files
===============================================

This module ha no any specific function for End-user. It is base for modules
generate xml file like FatturaPA o VAT settlement.

This module requires PyXB 1.2.4
http://pyxb.sourceforge.net/


(it)

Localizzazione italiana - Definizioni per file xml
==================================================

Questo modulo non ha funzioni specifice per l'utente finale. Serve come base
per i moduli che generano file xml in formato stabilito dall'Agenzia delle
Entrate, come FatturaPA o Liquidazione IVA elettronica.
""",
    "license": "AGPL-3",
    "depends": [],
    "data": [],
    "installable": True,
    "external_dependencies": {
        "python": ["pyxb"],
    }
}
