# -*- coding: utf-8 -*-
#
#
#    Copyright (C) 2010-2012 Associazione Odoo Italia
#    (<http://www.openerp-italia.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    'name': 'Italian Localisation - Fiscal Code',
    'version': '7.0.0.2.1',
    'category': 'Localisation/Italy',
    'description': """(en)
This module extends the functionality of partner to fit italian laws and mores
and to allow you to computation Fiscal code computation for partner


(it)
Modulo che gestisce il codice fiscale. Permette di calcolare il codice fiscale e
verifica la validità del codice fiscale inserito, se soggetto italiano.

Fornisce anche la separazione del cognome/nome per la gestione della comunicazione IVA.
""",
    'author': "Odoo Italian Community,Odoo Community Association (OCA)",
    'website': 'http://www.openerp-italia.org',
    'license': 'AGPL-3',
    "depends": ['base', 'base_vat', 'l10n_it_base'],
    'external_dependencies': {
        'python': ['codicefiscale'],
    },
    "init_xml": [
        'views/fiscalcode_view.xml',
        'wizard/compute_fc_view.xml'
    ],
    "update_xml": [],
    "demo_xml": [],
    'test': [
        'test/fiscalcode.yml',
    ],
    'post_init_hook': 'set_default_splitmode',
    "installable": True
}
