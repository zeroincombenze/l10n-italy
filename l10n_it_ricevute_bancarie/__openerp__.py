# -*- coding: utf-8 -*-
#
#
#    Copyright (C) 2012 Andrea Cometa.
#    Email: info@andreacometa.it
#    Web site: http://www.andreacometa.it
#    Copyright (C) 2012 Agile Business Group sagl (<http://www.agilebg.com>)
#    Copyright (C) 2012 Domsense srl (<http://www.domsense.com>)
#    Copyright (C) 2012 Associazione OpenERP Italia
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
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    'name': 'Ricevute Bancarie',
    'version': '1.3',
    'category': 'Accounting & Finance',
    'author': 'Odoo Community Association (OCA), Agile Business Group sagl, Apulia Software, SHS-AV s.r.l.',
    'website': 'https://odoo-community.org/',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'account_voucher',
        'l10n_it_fiscalcode',
        'account_due_list',
        'base_iban',
    ],
    'data': [
        'partner/partner_view.xml',
        'configurazione_view.xml',
        'riba_sequence.xml',
        'wizard/wizard_accreditation.xml',
        'wizard/wizard_unsolved.xml',
        'riba_view.xml',
        'account/account_view.xml',
        'wizard/wizard_emissione_riba.xml',
        'wizard/riba_file_export.xml',
        'riba_workflow.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
        'test/riba_invoice.yml',
        'test/issue_riba.yml',
        'test/unsolved_riba.yml',
    ],
    'installable': True,
    'active': False,
    'demo_xml': ['demo/riba_demo.xml'],
    'description': r'''
Overview / Panoramica
=====================

|en| Ricevute Bancarie
----------------------

Module to manage Ricevute Bancarie


|

|it| Ricevute Bancarie
----------------------

Per utilizzare il meccanismo delle Ri.Ba. è necessario configurare un termine
di pagamento di tipo 'Ri.Ba.'.

Per emettere una distinta bisogna andare su Ri.Ba. -> emetti Ri.Ba. e
selezionare i pagamenti per i quali emettere la distinta.
Se per il cliente è stato abilitato il raggruppo, i pagamenti dello stesso
cliente e con la stessa data di scadenza andranno a costituire un solo elemento
della distinta.

I possibili stati della distinta sono: bozza, accettata, accreditata, pagata,
insoluta, annullata.

Ad ogni passaggio di stato sarà possibile generare le relative registrazioni
contabili, le quali verranno riepilogate nel tab 'contabilità'.
Questo tab è presente sia sulla distinta che sulle sue righe.

*Esempio*

* Emissione fattura di 100€ verso cliente1.
* Metodo di pagamento: riba salvo buon fine.

`Fattura`

+------+-------------------+-----+-----+------+
| Riga | Descrizione       | D   | A   | Note |
+------+-------------------+-----+-----+------+
| 1    | Emessa fattura    |     |     |      |
+------+-------------------+-----+-----+------+
| 1.1  | Crediti v/clienti | 122 |     |      |
+------+-------------------+-----+-----+------+
| 1.2  | Ricavi            |     | 100 |      |
+------+-------------------+-----+-----+------+
| 1.3  | IVA               |     | 22  |      |
+------+-------------------+-----+-----+------+



`Emissione RiBA`

+------+-------------------+-----+-----+----------------------+
| Riga | Descrizione       | D   | A   | Note                 |
+------+-------------------+-----+-----+----------------------+
| 2    | Emissione RiBA    |     |     |                      |
+------+-------------------+-----+-----+----------------------+
| 2.1  | Crediti v/clienti |     | 122 | Riconciliata con 1.1 |
+------+-------------------+-----+-----+----------------------+
| 2.2  | Effetti SBF       | 122 |     |                      |
+------+-------------------+-----+-----+----------------------+




`Accredito distinta RiBA`

+------+-------------------------+-----+-----+------+
| Riga | Descrizione             | D   | A   | Note |
+------+-------------------------+-----+-----+------+
| 3    | Accredito distinta RiBA |     |     |      |
+------+-------------------------+-----+-----+------+
| 3.1  | Banca c/effetti         |     | 122 |      |
+------+-------------------------+-----+-----+------+
| 3.2  | Banca c/c               | 120 |     |      |
+------+-------------------------+-----+-----+------+
| 3.3  | Spese bancarie          | 2   |     |      |
+------+-------------------------+-----+-----+------+




`Pagamento effettivo RiBA`

+------+---------------------+-----+-----+----------------------+
| Riga | Descrizione         | D   | A   | Note                 |
+------+---------------------+-----+-----+----------------------+
| 4    | Pagamento effettivo |     |     |                      |
+------+---------------------+-----+-----+----------------------+
| 4.1  | Effetti SBF         |     | 122 | Riconciliata con 2.2 |
+------+---------------------+-----+-----+----------------------+
| 4.2  | Banca c/effetti     | 122 |     | Riconciliata con 3.1 |
+------+---------------------+-----+-----+----------------------+




|

Usage / Utilizo
---------------

Nella configurazione delle Ri.Ba. è possibile specificare se si tratti di
'salvo buon fine' o 'al dopo incasso', che hanno un flusso completamente diverso.

 - Al dopo incasso: nessuna registrazione verrà effettuata automaticamente e le fatture risulteranno pagate solo al momento dell'effettivo incasso.
 - Salvo buon fine: le registrazioni generate seguiranno la struttura descritta in questo documento

E' possibile specificare diverse configurazioni (dal menù
configurazioni -> varie -> Ri.Ba.). Per ognuna, in caso di 'salvo buon fine',
è necessario specificare almeno il sezionale ed il conto da
utilizzare al momento dell'accettazione della distinta da parte della banca.
Tale conto deve essere di tipo 'crediti' (ad esempio "Ri.Ba. all'incasso",
eventualmente da creare).

La configurazione relativa alla fase di accredito, verrà usata nel momento in
cui la banca accredita l'importo della distinta.
E' possibile utilizzare un sezionale creato appositamente, ad esempio "accredito RiBa",
ed un conto chiamato ad esempio "banche c/RIBA all'incasso", che non deve essere di tipo 'banca'.

La configurazione relativa all'insoluto verrà utilizzata in caso di mancato pagamento da parte del cliente.
Il conto può chiamarsi ad esempio "crediti insoluti".

Nel caso si vogliano gestire anche le spese per ogni scadenza con ricevuta bancaria,
si deve configurare un prodotto di tipo servizio e legarlo in
Configurazione -> Contabilità -> Ri.Ba. Configurazione spese d'incasso -> Servizio spese d'incasso.

|
|

Support / Supporto
------------------


|Zeroincombenze| This module is maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


|
|

Credits / Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


|

Authors / Autori
----------------

* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `Apulia Software <https://www.apuliasoftware.it>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Collaboratori
----------------------------

* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Andrea Cometa <a.cometa@apuliasoftware.it>
* Andrea Gallina <a.gallina@apuliasoftware.it>
* Davide Corio <info@davidecorio.com>
* Giacomo Grasso <giacomo.grasso@agilebg.com>
* Gabriele Baldessari <gabriele.baldessari@gmail.com>
* Alex Comba <alex.comba@agilebg.com>
* Antonio M. Vigliotti <info@shs-av.com> 

|

----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://wiki.zeroincombenze.org/en/Odoo>`__ è progettata per le esigenze del mercato italiano.

|

This module is part of l10n-italy project.

Last Update / Ultimo aggiornamento: 2019-12-08

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0
    :alt: Codecov
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/7.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/7.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg
    :target: https://erp7.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov| image:: https://codecov.io/gh/OCA/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/7.0
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
''',
}
