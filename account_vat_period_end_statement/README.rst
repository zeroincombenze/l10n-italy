|Build Status| |license agpl| |Coverage Status| |codecov| |OCA project| |Tech Doc| |Help| |try it|

|br|

========================
Period End VAT Statement
========================

This module evaluates VAT to pay (or on credit) and generates the electronic
VAT closeout statement as VAT Authority http://www.agenziaentrate.gov.it/wps/content/nsilib/nsi/documentazione/normativa+e+prassi/provvedimenti/2017/marzo+2017+provvedimenti/provvedimento+27+marzo+2017+liquidazioni+periodiche+iva

By default, amounts of debit and credit taxes are automatically loaded
from tax codes of selected periods.

Previous debit or credit is loaded from previous VAT statement, according
to its payments status.

`How to use <https://www.zeroincombenze.it/liquidazione-iva-elettronica-ip17>`__

|it|

==========================
Liquidazione IVA periodica
==========================

Questo modulo calcola l'IVA da pagare (o a credito) sia per i contribuenti
mensili che trimestrali e permette di generare il file della comunicazione
elettronica come da normativa del 2017 dell'Agenzia delle Entrate
http://www.agenziaentrate.gov.it/wps/content/nsilib/nsi/documentazione/normativa+e+prassi/provvedimenti/2017/marzo+2017+provvedimenti/provvedimento+27+marzo+2017+liquidazioni+periodiche+iva

La liquidazione è calcolata sommando i totali di periodo dei conti
imposte.

L'utente può aggiungere l'eventuale credito/debito del periodo precedente e
calcolare gli interessi; può anche registrare l'utilizzo del credito in
compensazione.

`Istruzioni di utilizzo <https://www.zeroincombenze.it/liquidazione-iva-elettronica-ip17>`__


**Funzionalità & Certificati**

+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------+
| Logo                  | Ente/Certificato                                                                                                                                                                        | Data inizio   | Da fine      | Note                                   |
+=======================+=========================================================================================================================================================================================+===============+==============+========================================+
| |xml\_schema|         | `ISO + Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__   | 01-06-2017    | 31-12-2017   | Validazione contro schema xml          |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------+
| |DesktopTelematico|   | `Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__         | 01-06-2017    | 31-12-2017   | Controllo tramite Desktop telematico   |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------+

----------------

|br|

|en| Installation
=================

These instruction are just an example to remember what you have to do:

::

    pip install PyXB==1.2.4
    git clone https://github.com/zeroincombenze/l10n-italy
    cp -R l10n-italy/account_vat_period_end_statement ODOO_DIR/l10n-italy/
    sudo service odoo-server restart -i account_vat_period_end_statement -d MYDB

From UI: go to Setup > Module > Install

----------------

|br|

|it| Configuration/Configurazione
=================================



----------------

|br|

|it| Usage/Utilizzo
===================

For furthermore information, please visit
http://wiki.zeroincombenze.org/it/Odoo/7.0/man/FI

----------------

|br|

|it| Known issues / Roadmap
---------------------------

|warning| Questo modulo rimpiazza il modulo OCA. Leggete attentamente il
paragrafo relativo alle funzionalità e differenze.

|warning| Questo modulo richiede `l10n\_it\_base <l10n_it_base/>`__ 
aggiornato rispetto alla repository OCA.

|warning| Questo modulo richiede `l10n\_it\_fiscalcode <l10n_it_fiscalcode/>`__ 
aggiornato rispetto alla repository OCA.

|warning| Questo modulo richiede `l10n\_it\_ade <l10n_it_ade/>`__ che non esiste
nella repository OCA e contiene le stesse definizioni del modulo OCA
*l10n_it_fiscal_document_type* che è quidni incompatbile.
----------------

|br|

|en| Bug Tracker
================

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home

----------------

|br|

|en| Credits
============

Contributors
------------

*  Lorenzo Battistini lorenzo.battistini@agilebg.com
*  Marco Marchiori marcomarkiori@gmail.com
*  Sergio Corato sergiocorato@gmail.com
*  Andrei Levin andrei.levin@didotech.com
*  Antonio M. Vigliotti antoniomaria.vigliotti@gmail.com

Funders
-------

This module has been financially supported by

* `Agile BG <https://www.agilebg.com/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__
*  `Didotech srl <http://www.didotech.com>`__

Maintainer
----------

|Odoo Italia Associazione|

Odoo Italia is a nonprofit organization whose develops Italian
Localization for Odoo.

To contribute to this module, please visit https://odoo-italia.org/.

--------------

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

|chat with us|

.. |icon| image:: /l10n_it_split_payment/static/description/icon.png
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0
   :target: https://travis-ci.org/zeroincombenze/l10n-italy
.. |license agpl| image:: https://img.shields.io/badge/License-AGPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0
   :alt: License: AGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0
   :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0
.. |codecov| raw:: html

    <a href="https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0"><img src="https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg"/></a>

.. |OCA project| raw:: html

    <a href="https://github.com/OCA/l10n-italy/tree/10.0"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg"/></a>

.. |Tech Doc| raw:: html

    <a href="http://wiki.zeroincombenze.org/en/Odoo/10.0/dev"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg"/></a>

.. |Help| raw:: html

    <a href="http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg"/></a>

.. |try it| raw:: html

    <a href="http://erp10.zeroincombenze.it"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg"/></a>

.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
.. |chat with us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
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
