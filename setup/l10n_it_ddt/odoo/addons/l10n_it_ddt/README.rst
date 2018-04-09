[![Build Status](https://travis-ci.org/zeroincombenze/addons.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/addons)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/addons/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/addons?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/addons/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/addons/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/addons/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)


































[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Italian Localization - DDT: Documento di trasporto
==================================================

This modules extends stock_picking_package_preparation module adding DDT data

Installation
------------





Configuration
-------------





Usage
-----







=====

English

You can automatically create a DDT From a Sale Order, setting
'Automatically create the DDT' field that will automatically create the DDT on
Sale Order confirmation.

You can also directly create a DDT using
warehouse -> operations -> package preparations
menu and add existings delivery orders to it, in the 'transfers' tab.

You can add lines to an existing DDT using the 'details' tab.
Lines can be descriptive or linked to a product. If linked to a product,
the stock movement will also be created.

When you work with delivery orders, you can create a DDT selecting 1 or more
pickings and running wizard 'DDT from pickings'.

Also, you can select 1 or more pickings and run 'add pickings to DDT' to add
the selected delivery orders to an existing DDT

If the state of the delivery orders allows it, you can deliver them from the
DDT directly, clicking 'put in pack' and 'package done'.

Otherwise, you can process delivery orders separately, then go to the DDT and
click on 'set done'.

Finally you can create your invoice directly from the DDT using the 
'Create Invoice' button that creates a new Invoice with the ddt lines as 
invoice lines

Italian

E' possibile creare automaticamente un DDT da un ordine di vendita, impostando
il campo 'crea automaticamente il DDT' che creerà il DDT alla conferma
dell'ordine.

E' anche possibile creare un DDT direttamente, usando
magazzino -> operazioni -> preparazione pacchi
e aggiungendo degli ordini di consegna esistenti al DDT, nel tab
'trasferimenti'.

E' possibile aggiungere righe ad un DDT esistente usando il tab 'dettagli'.
Le righe possono essere descrittive o collegate a prodotti. Le righe collegate
ad un prodotto creeranno anche i movimenti di magazzino.

Se si lavora con gli ordini di consegna, è possibile creare un DDT selezionando
1 o più ordini di consegna ed eseguendo il wizard 'DDT da picking'.

Inoltre, è possibile selezionare 1 o più ordini di consegna ed eseguire
'aggiungi i picking al DDT' per aggiungere gli ordini selezionati ad un DDT
esistente.

Se lo stato degli ordini di consegna lo permette, è possibile consegnarli tutti
direttamente dal DDT, cliccando sui bottoni 'metti nel pacco' e
'pacco completato'.

Altrimenti, è possibile processare gli ordini di consegna separamente, poi
andare sul DDT e cliccare su 'imposta completato'.

Infine, è possibile creare la fattura direttamente dal DDT usando il bottone
'crea fattura' il quale crea una nuova fattura usando le righe del DDT.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/122/10.0

Known issues / Roadmap
----------------------





Bug Tracker
-----------





Credits
-------











### Contributors






* Davide Corio <davide.corio@abstract.it>
* Nicola Malcontenti <nicola.malcontenti@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
* Andrea Gallina <a.gallina@apuliasoftware.it>
* Alex Comba <alex.comba@agilebg.com>
* Alessandro Camilli <alessandrocamilli@openforce.it>

### Funders

### Maintainer










.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

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
