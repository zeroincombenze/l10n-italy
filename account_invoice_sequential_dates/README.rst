[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/l10n-italy/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](https://erp8.zeroincombenze.it)



[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

|br|

================================
Account Invoice Sequential Dates
================================

|en| This module check for invoices to avoid wrong date sequence.

|br|

|it| Controllo data fattura sequenziale

Il modulo controlla che la data fattura clienti o la data di registrazione
della fattura fornitore sia sequenziale e conforme alla normativa italiana.

::

    Destinatari:

Tutte le aziende che emettono fatture in Italia.

::

    Normativa:

La normativa di legge è il `DPR 633 art. 23 <http://def.finanze.it/DocTribFrontend/getAttoNormativoDetail.do?ACTION=getArticolo&id={75A4827C-3766-4ECC-9C45-00C8D6CDC552}&codiceOrdinamento=200002300000000&articolo=Articolo%2023>`__


::

    Funzionalità & Differenze da OCA:

Funzione                                          Status   OCA    Note
Fattura cliente                                    |ok|    |ok|   La versione non distingue gli anni fiscali
Fattura fornitore                                  |ok|    |No|   Controllo su data di registrazione

|br|

::

    Note di implementazione:

Il modulo controlla la data fattura cliente o la data di registrazione della
fattura fornitore per il sezionale e l'anno fiscale.
Durente l'accavallamento degli esercizi è possibile registrare sia fatture
nell'anno correnet che nell'esercizio precedente.


|br|

|en| Installation

These instruction are just an example to remember what you have to do:
::

    $ ODOO\_DIR=/opt/odoo/8.0/l10n-italy # here your Odoo dir
    $ BACKUP\_DIR=/opt/odoo/backup # here your backup dir
    # Check for modules
    $ cd /tmp
    $ git clone https://github.com/zeroincombenze/l10n-italy.git l10n-italy
    $ mv $ODOO\_DIR/l10n-italy/account\_invoice\_sequential\_dates/ $BACKUP\_DIR/
    $ mv /tmp/l10n-italy/account\_invoice\_sequential\_dates/ $ODOO\_DIR/


|br|

|it| Configuration/Configurazione

Nessuna configurazione necessaria


|br|

|it| Usage/Utilizzo

Per ulteriori informazioni vedere
`Guida utente Odoo <http://wiki.zeroincombenze.org/it/Odoo/8.0/man/FI/>`__


|br|

|it| Known issues / Roadmap

|warning| Questo modulo rimpiazza il modulo OCA. Leggete attentamente il
paragrafo relativo alle funzionalità e differenze.


|br|

|en| Bug Tracker

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home


|br|

|en| Credits

Installation
------------

Configuration
-------------

Usage
-----

Known issues / Roadmap
----------------------

Bug Tracker
-----------

Credits
-------

### Contributors

* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

### Funders

This module has been financially supported by

* `Apulia Software srl <info@apuliasoftware.it>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

### Maintainer

|Odoo Italia Associazione|

Odoo Italia is a nonprofit organization whose develops Italian
Localization for Odoo.

To contribute to this module, please visit https://odoo-italia.org/.


**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP, formerly TinyERP)

**OCA**, or the `Odoo Community Association <http://odoo-community.org/>`__,
is a nonprofit organization whose mission is to support
the collaborative development of Odoo features and promote its widespread use.

**zeroincombenze®** is a trademark of `SHS-AV s.r.l. <http://www.shs-av.com/>`__
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
`Zeroincombenze® distribution <http://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed for Italian law and markeplace.
Users can download from `Zeroincombenze® distribution <https://github.com/zeroincombenze/OCB>`__
and deploy on local server.


.. |icon| image:: /l10n_it_split_payment/static/description/icon.png
   :target: https://travis-ci.org/zeroincombenze/l10n-italy
   :target: https://www.gnu.org/licenses/agpl-3.0
   :alt: License: AGPL-3
   :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=8.0
.. |codecov| raw:: html

    <a href="https://codecov.io/gh/zeroincombenze/l10n-italy/branch/8.0"><img src="https://codecov.io/gh/zeroincombenze/l10n-italy/branch/8.0/graph/badge.svg"/></a>

.. |OCA project| raw:: html

    <a href="https://github.com/OCA/l10n-italy/tree/8.0"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg"/></a>

.. |Tech Doc| raw:: html

    <a href="http://wiki.zeroincombenze.org/en/Odoo/8.0/dev"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg"/></a>

.. |Help| raw:: html

    <a href="http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg"/></a>


    <a href="http://erp10.zeroincombenze.it"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg"/></a>

.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
.. |ok| raw:: html

   <i class="fa fa-check-square" style="font-size:24px;color:green"></i>
.. |No| raw:: html

   <i class="fa fa-minus-circle" style="font-size:24px;color:red"></i>

.. |menu| raw:: html

   <i class="fa fa-ellipsis-v" style="font-size:18px"></i>

.. |hand right| raw:: html

   <i class="fa fa-hand-o-right" style="font-size:12px"></i>

.. |warning| raw:: html

    <i class="fa fa-warning" style="font-size:24px;color:orange"></i>

.. |br| raw:: html

    <br/>

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017 Odoo Italia Associazione issues modules for Italian localization not developed by OCA
or available only with Odoo Proprietary License.
Odoo Italia Associazione distributes code under [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) or [LGPL](https://www.gnu.org/licenses/lgpl.html) free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 rilascia moduli per la localizzazione italiana non sviluppati da OCA
o disponibili solo con [Odoo Proprietary License](https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html).

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) o [LGPL](https://www.gnu.org/licenses/lgpl.html)

[//]: # (end copyright)



