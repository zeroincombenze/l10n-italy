# -*- coding: utf-8 -*-
# Copyright (C) 2014 Davide Corio
# Copyright 2015-2016 Lorenzo Battistini - Agile Business Group

{
    'name': 'Italian Localization - FatturaPA - Emission',
    'version': '7.0.2.0.1',
    'category': 'Localization/Italy',
    'summary': 'Electronic invoices emission',
    'author': 'Davide Corio, Agile Business Group, Innoviu, '
              'Odoo Community Association (OCA)',
    'description': """
Italian Localization - FatturaPA - Emission
===========================================

Questo modulo permette di generare il file xml della fatturaPA versione 1.2
da trasmettere al sistema di interscambio SdI.

Attenzione! Lo schema di definizione dei file xml, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml dell'Agenzia delle Entrate; come conseguenza nasce un conflitto tra
moduli diversi che riferiscono allo schema dell'Agenzia delle Entrate,
segnalato dall'errore:

*name CryptoBinary used for multiple values in typeBinding*

Tutti i moduli della localizzazione italiana che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate *devono* dichiare il modulo
l10n_it_ade come dipendenza.

Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'ultimo autore: Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>.
""",
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": [
        'l10n_it_fatturapa',
        'l10n_it_split_payment',
        ],
    "data": [
        'wizard/wizard_export_fatturapa_view.xml',
        'views/attachment_view.xml',
        'views/account_view.xml',
        'security/ir.model.access.csv',
    ],
    "installable": False,
    'external_dependencies': {
        'python': ['unidecode'],
    }
}
