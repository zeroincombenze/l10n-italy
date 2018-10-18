[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/l10n-italy/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![icon](static/src/img/icon.png)](https://travis-ci.org/zeroincombenze)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

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
per essere spedicta al sistema di interscambio SDI
http://www.fatturapa.gov.it/export/fatturazione/it/sdi.htm

:warning: Leggere attentamente le informazioni di compatibilità e installazione
tecnica disponibili nel modulo l10n_it_fatturapa.


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

[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

* Configurazione > Configurazione > Contabilità > Fattura PA :point_right: Impostare i vari parametri
* Contabilità > Configurazione > Sezionali > Sezionali :point_right: Impostare sezionale fattura elettronica
* Contabilità > Configurazione > Imposte > Imposte :point_right: Impostare natura codici IVA
* Contabilità > Configurazione > Management > Termini di pagamento :point_right: Collegare i terminii di pagamento con i relativi termini fiscali
* Contabilità > Clienti > Clienti :point_right: Impostare IPA, EORI (se necessario), nazione, partita IVA, codice fiscale


Usage
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
* Alex Comba <alex.comba@agilebg.com>
* Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>


### Funders

Questo modulo è stato sviluppato con il contributo di

* Agile BG <https://www.agilebg.com/>
* Innoviu <https://www.innoviu.com/>
* SHS-AV s.r.l. <https://www.zeroincombenze.it/>
* Odoo Community Association (OCA) <https://odoo-community.org/>
* Odoo Italia Associazione <https://odoo-italia.org/>


### Maintainer

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
