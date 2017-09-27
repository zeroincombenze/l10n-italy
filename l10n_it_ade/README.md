[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=7.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=7.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/l10n-italy/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)

[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Base xml Agenzia delle Entrate
==============================

This module has no any specific function for End-user. It is base for modules
generate xml file like FatturaPA o VAT settlement.



[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Localizzazione italiana - Definizioni per file xml
==================================================

Questo modulo non ha funzioni specifice per l'utente finale. Serve come base
per i moduli che generano file xml in formato stabilito dall'Agenzia delle
Entrate, come FatturaPA o Liquidazione IVA elettronica.

Attenzione! Questo modulo è incompatibile con i moduli l10n_it_fatturapa di OCA
versioni [7-11].0.2.0.0
Lo schema di definizione dei file xml dell'Agenzia delle Entrate, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml; come conseguenza nasce un conflitto tra moduli diversi con lo stesso
schema di riferimento dell'Agenzia delle Entrate con l'errore:
*name CryptoBinary used for multiple values in typeBinding*

Tutti i moduli che generano file xml per l'Agenzia delle Entrate *devono*
dipendere da questo modulo.
Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'autore.

Schemi

Il modulo rende disponibili i seguenti schemi:

* Liquidazione IVA elettronica versione 1.0
* Comunicazione clienti e fornitori (spesometro 2017) versione 2.0
* FatturaPA versione 1.2


Per aggiungere nuovi schemi o modificare o aggiornare gli schemi gestiti:

- Aggiungere o modificare gli schemi nella directory ./data
- Eseguire da una macchina CentOS lo script ./pyxbgen.sh -u


Installation
------------








This module requires PyXB 1.2.4
http://pyxb.sourceforge.net/


Configuration
-------------







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








Incompatibile con moduli OCA fatturaPA e liquidazione IVA


Bug Tracker
-----------







Credits
-------








[![Odoo Italia Associazione]]











### Contributors







-   Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
-   Andrei Levin <andrei.levin@didotech.com>


### Funders
### Maintainer















Questo modulo è stato sviluppato con il contributo di SHS-AV s.r.l. <https://www.zeroincombenze.it/>



This module is maintained by Odoo Italia Associazione

Odoo Italia is a nonprofit organization whose develops Italian Localization for
Odoo.

To contribute to this module, please visit <https://odoo-italia.org/>.


[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017, Odoo Italia Associazione replaces OCA members of Italy are developping code under Odoo Proprietary License.
Odoo Italia Associazione distributes code only under AGPL free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 sostituisce gli sviluppatori italiani di OCA che sviluppano
con Odoo Proprietary License a pagamento.

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](http://www.gnu.org/licenses/agpl-3.0.html)

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)

