# -*- coding: utf-8 -*-
#
# Copyright 2017-2018 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2017-2018 - Associazione Odoo Italia <http://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by l10n_it_account of OCA
#
{
    "name": "Base xml Agenzia delle Entrate",
    "version": "7.0.0.1.9",
    "category": "Localization/Italy",
    "summary": "Codice con le definizioni dei file xml Agenzia delle Entrate",
    "author": "SHS-AV s.r.l.,"
              " Odoo Italia Associazione",
    "maintainer": "Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "description": """(en)
Tax Authority Definitions
=========================

This module has no any specific function for End-user.
It contains various tax data for Italian account.
Inside there are xml schema files used by FatturaPA, eInvoice and VAT settlement.

This module requires PyXB 1.2.4
http://pyxb.sourceforge.net/


(it)

Definizioni Agenzia delle Entrate
=================================

Questo modulo non ha funzioni specifiche per l'utente finale.
Contiene dati e definizioni per la fiscalità italiana.
All'interno sono presenti gli schemi xml nei formati stabiliti dall'Agenzia
delle Entrate usati da FatturaPA, fattura elettronica, Liquidazione IVA
elettronica e Comunicazione IVA.

Attenzione! Questo modulo è incompatibile con i seguenti moduli OCA:
l10n_it_fatturapa versioni [7-11].0.2.0.0

Dallo schema di definizione dei file xml dell'Agenzia delle Entrate, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche dipendono tutti i file
xml da inviare all'AdE; se moduli diversi richiamano lo stesso schema
dell'Agenzia delle Entrate nasce un conflitto che genera l'errore:

*name CryptoBinary used for multiple values in typeBinding*

Tutti i moduli che generano file xml destinati all'Agenzia delle Entrate *devono*
dipendere da questo modulo. Questo è il motivo del conflitto con i moduli OCA.
Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'autore.


Schemi
------

Il modulo rende disponibili i seguenti schemi:

* Liquidazione IVA elettronica versione 1.0
* Comunicazione clienti e fornitori (spesometro 2018) versione 2.1
* FatturaPA versione 1.2
""",
    "license": "AGPL-3",
    "depends": [
        'account',
        ],
    "data": [
        'security/ir.model.access.csv',
        'data/italy.ade.tax.nature.csv',
        'data/italy.ade.codice.carica.xml',
        'views/ir_ui_menu.xml',
        'views/account_tax_view.xml',
        'views/account_journal.xml',
        'views/codice_carica_view.xml',
        'views/tax_nature_view.xml',
        ],
    'installable': True,
    "external_dependencies": {
        "python": ["pyxb"],
    }
}
