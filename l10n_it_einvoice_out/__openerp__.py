# -*- coding: utf-8 -*-
# Copyright (C) 2014 Davide Corio
# Copyright 2015-2016 Lorenzo Battistini - Agile Business Group
{
    'name': 'EInvoice + FatturaPA Emission',
    'summary': 'Electronic invoices emission',
    'version': '7.0.2.0.1',
    'category': 'Localization/Italy',
    'author': 'Davide Corio, Agile Business Group, Innoviu, Odoo Community Association (OCA)',
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": [
        'l10n_it_einvoice_base',
        'l10n_it_split_payment',
        ],
    "data": [
        'wizard/wizard_export_fatturapa_view.xml',
        'views/attachment_view.xml',
        'views/account_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'external_dependencies': {
        'python': ['unidecode'],
    },
    'description': '''|en|

EInvoice + FatturaPA
=====================

This module allows you to generate the fatturaPA XML file version 1.2
which will be sent to the SdI (Exchange System by Italian Tax Authority)

http://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm

|warning| Read carefully note of module l10n_it_einvoice_base before install this module

|halt| Do not install this module: it is in development status; official release will be avaiable on 2018-10-22


|it|

Fattura Elettronica + FatturaPA
================================

Questo modulo permette di generare il file xml della fatturaPA versione 1.2
da trasmettere al sistema di interscambio SdI.

|warning| Lo schema di definizione dei file xml, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml dell'Agenzia delle Entrate; come conseguenza nasce un conflitto tra
moduli diversi che riferiscono allo schema dell'Agenzia delle Entrate,
segnalato dall'errore:

|exclamation| **name CryptoBinary used for multiple values in typeBinding**

Tutti i moduli della localizzazione italiana che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate **devono** dichiare il modulo
`l10n_it_ade <../l10n_it_ade>`__ come dipendenza.

Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'ultimo autore: Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>.

|halt| Non installare questo modulo: è in fase di svilupp; il rilascio è previsto per lunedì 22-10-2018

Features / Funzioni
--------------------

+-------------------------+----------+----------------------------------------------+
| Feature / Funzione      |  Status  | Notes / Note                                 |
+-------------------------+----------+----------------------------------------------+
| Emissione FatturaPA     | |check|  | Genera file .xml versione 1.2                |
+-------------------------+----------+----------------------------------------------+
| Emissione Fattura B2B   | |check|  | Genera file .xml versione 1.2                |
+-------------------------+----------+----------------------------------------------+
| Dati azienda da fattura | |check|  | Versione OCA utilizza dati azienda da utente |
+-------------------------+----------+----------------------------------------------+


OCA Differences / Differenze da OCA
------------------------------------

+--------------------------------------+---------------------+-------------------------+--------------------------------+
| Description / Descrizione            | Odoo Italia         | OCA                     | Notes / Note                   |
+--------------------------------------+---------------------+-------------------------+--------------------------------+
| Company / Azienda                    | By User / Da Utente | By Invoice / Da Fattura | Different layout               |
+--------------------------------------+---------------------+-------------------------+--------------------------------+




|en|

Usage / Uso
============

|menu| Configurazione > Configurazione > Contabilità > Fattura PA |do_right| Impostare i vari parametri
|menu| Contabilità > Configurazione > Sezionali > Sezionali |do_right| Impostare sezionale fattura elettronica
|menu| Contabilità > Configurazione > Imposte > Imposte |do_right| Impostare natura codici IVA
|menu| Contabilità > Configurazione > Management > Termini di pagamento |do_right| Collegare i terminii di pagamento con i relativi termini fiscali
|menu| Contabilità > Clienti > Clienti |do_right| Impostare IPA, EORI (se necessario), nazione, partita IVA, codice fiscale



Credits / Riconoscimenti
=========================

Authors / Autori
-----------------


* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Contributi
--------------------------


* Davide Corio <davide.corio@abstract.it>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

Maintainers / Manutezione
--------------------------

|Odoo Italia Associazione|

This module is maintained by the Odoo Italia Associazione.

To contribute to this module, please visit https://odoo-italia.org/.


|

Last Update / Ultimo aggiornamento: 2018-10-21

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0
    :alt: Codecov
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg
    :target: https://github.com/OCA/l10n-italy/tree/7.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/7.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/7.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg
    :target: https://erp7.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov Status| image:: badge-oca-codecov
    :target: oca-codecov-URL
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md

''',
}
