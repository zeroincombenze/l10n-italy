[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/l10n-italy/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)



[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

[![icon](static/src/img/icon.png)](https://travis-ci.org/zeroincombenze)
========================================================================


FatturaPA
=========

This module allows you to generate the fatturaPA XML file version 1.2
http://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm
to be sent to the Exchange System
http://www.fatturapa.gov.it/export/fatturazione/it/sdi.htm


[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

FatturaPA
=========

Questo modulo permette di generare il file xml della fatturaPA versione 1.2
http://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm
per essere spdicta al sistema di interscambio SDI
http://www.fatturapa.gov.it/export/fatturazione/it/sdi.htm

:warning: Lo schema di definizione dei file xml dell'Agenzia delle Entrate, pubblicato
come urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml di gestione fiscale; come conseguenza nasce un conflitto tra moduli diversi
ma con lo stesso schema di riferimento dell'Agenzia delle Entrate con l'errore:

*name CryptoBinary used for multiple values in typeBinding* :heavy_exclamation_mark:

Tutti i moduli che generano file xml per l'Agenzia delle Entrate di OCA *devono*
essere sostituiti con i moduli di Odoo Italia Associazione per funzionare
correttamente.
Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'autore.

Certificati

Ente/Certificato | Data inizio | Da fine | Note
--- | --- | --- | ---
[FatturaPA](http://www.fatturapa.gov.it/export/fatturazione/it/fattura_PA.htm) | 22-09-2017 | 31-12-2017 | [![fatturapa](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/icons/fatturapa.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md)



Installation
------------



:warning: Since version [7-8].0.4.0.0 of this module, definition schemas are
moved into module l10n_it_ade. Please, read l10n_it_ade documentation for furthermore
informations.

:warning: A partire dalla versione [7-8].0.4.0.0 di questo modulo, gli schemi
di definizione sono stati spostati nel modulo l10n_it_ade. Per ulteriori
informazioni, leggete i documenti relativi al modulo l10n_it_ade.

This module requires PyXB 1.2.4 http://pyxb.sourceforge.net/


Configuration
-------------



* Edit the FatturaPA fields of the partners (in partner form) who will receive (send) the electronic invoices. IPA code is mandatory, EORI code is not.
* Configure payment terms filling the fatturaPA fields related to payment terms and payment methods.
* Configure taxes about 'Non taxable nature', 'Law reference' and 'VAT payability'
* Configure FatturaPA data in Accounting Configuration. Note that a sequence 'fatturaPA' is already loaded by the module and selectable.


Usage
-----

-----

-----

-----

-----

-----

-----

-----

-----

Known issues / Roadmap
----------------------



:no_entry: Questo modulo sostituisce i moduli l10n_it_fatturapa di OCA versioni [7-11].0.2.0.0.


Bug Tracker
-----------


Credits
-------







### Contributors



* Davide Corio
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Roberto Onnis <roberto.onnis@innoviu.com>
* Alessio Gerace
* Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>


### Funders
### Maintainer





Questo modulo è stato sviluppato con il contributo di

* SHS-AV s.r.l. <https://www.zeroincombenze.it/>



[![Odoo Italia Associazione](https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png)](https://odoo-italia.org)

Odoo Italia is a nonprofit organization whose develops Italian Localization for
Odoo.

To contribute to this module, please visit <https://odoo-italia.org/>.


[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be deployed on local server too.

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
