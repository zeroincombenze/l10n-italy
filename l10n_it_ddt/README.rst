
=====================
|icon| DDT 10.0.1.8.9
=====================


**Delivery Document to Transfer**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_ddt/static/description/icon.png

|Maturity| |Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en| This module print the Italian deliver document AKA DdT

You can automatically create a DDT From a Sale Order, setting
'Automatically create the DDT' field that will automatically create the DDT on
Sale Order confirmation.

You can also directly create a DDT using
Inventory -> Operations -> DDT
menu and add existings delivery orders to it, in the 'transfers' tab.

You can add lines to an existing DDT using the 'Details' tab.
Lines can be descriptive or linked to a product. If linked to a product,
the stock movement will also be created.

When you work with delivery orders, you can create a DDT selecting 1 or more
pickings and launching the action 'DDT from pickings'.

Also, you can select 1 or more pickings and run 'add pickings to DDT' to add
the selected delivery orders to an existing DDT

If the state of the delivery orders allows it, you can deliver them from the
DDT directly, clicking 'put in pack' and 'package done'.

Otherwise, you can process delivery orders separately, then go to the DDT and
click on 'set done'.

Finally you can create your invoice directly from the DDT using the 
'Create Invoice' button that creates a new Invoice with the ddt lines as 
invoice lines


|

|it| Stampa documento di trasporto, conosciuto anche come DdT

È possibile creare automaticamente un DDT da un ordine di vendita, impostando
il campo 'crea automaticamente il DDT' che creerà il DDT alla conferma
dell'ordine.

È anche possibile creare un DDT direttamente, usando
Inventario -> Operazioni -> DDT
e aggiungendo degli ordini di consegna esistenti al DDT, nel tab
'trasferimenti'.

È possibile aggiungere righe ad un DDT esistente usando il tab 'Dettaglio'.
Le righe possono essere descrittive o collegate a prodotti. Le righe collegate
ad un prodotto creeranno anche i movimenti di magazzino.

Se si lavora con gli ordini di consegna, è possibile creare un DDT selezionando
1 o più ordini di consegna ed eseguendo l'azione 'DDT da Picking'.

Inoltre, è possibile selezionare 1 o più ordini di consegna ed eseguire
'aggiungi Picking al DDT' per aggiungere gli ordini selezionati ad un DDT
esistente.

Se lo stato degli ordini di consegna lo permette, è possibile consegnarli tutti
direttamente dal DDT, cliccando sui bottoni 'metti nel pacco' e
'pacco completato'.

Altrimenti, è possibile processare gli ordini di consegna separatamente, poi
andare sul DDT e cliccare su 'imposta completato'.

Infine, è possibile creare la fattura direttamente dal DDT usando il bottone
'crea fattura' il quale crea una nuova fattura usando le righe del DDT.

E' possibile fatturare i DDT che hanno una 'Causale trasporto' impostata come 'da fatturare'


|

OCA comparation / Confronto con OCA
-----------------------------------


+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+
| Description / Descrizione                                       | Zeroincombenze    | OCA            | Notes / Note                   |
+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+
| Coverage / Copertura test                                       |  |Codecov Status| | |OCA Codecov|  |                                |
+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+


|
|

Getting started / Come iniziare
===============================

|Try Me|


|

Installation / Installazione
----------------------------


+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instructions are just an  | Istruzioni di esempio valide solo per    |
| example; use on Linux CentOS 7+ | distribuzioni Linux CentOS 7+,           |
| Ubuntu 14+ and Debian 8+        | Ubuntu 14+ e Debian 8+                   |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__    |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| $HOME/10.0                                                                 |
+----------------------------------------------------------------------------+

::

    cd $HOME
    # *** Tools installation & activation ***
    # Case 1: you have not installed zeroincombenze tools
    git clone https://github.com/zeroincombenze/tools.git
    cd $HOME/tools
    ./install_tools.sh -p
    source $HOME/devel/activate_tools
    # Case 2: you have already installed zeroincombenze tools
    cd $HOME/tools
    ./install_tools.sh -U
    source $HOME/devel/activate_tools
    # *** End of tools installation or upgrade ***
    # Odoo repository installation; OCB repository must be installed
    odoo_install_repository l10n-italy -b 10.0 -O zero -o $HOME/10.0
    vem create $HOME/10.0/venv_odoo -O 10.0 -a "*" -DI -o $HOME/10.0

From UI: go to:

* |menu| Setting > Activate Developer mode 
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **l10n_it_ddt** > Install


|

Upgrade / Aggiornamento
-----------------------


::

    cd $HOME
    # *** Tools installation & activation ***
    # Case 1: you have not installed zeroincombenze tools
    git clone https://github.com/zeroincombenze/tools.git
    cd $HOME/tools
    ./install_tools.sh -p
    source $HOME/devel/activate_tools
    # Case 2: you have already installed zeroincombenze tools
    cd $HOME/tools
    ./install_tools.sh -U
    source $HOME/devel/activate_tools
    # *** End of tools installation or upgrade ***
    # Odoo repository upgrade
    odoo_install_repository l10n-italy -b 10.0 -o $HOME/10.0 -U
    vem amend $HOME/10.0/venv_odoo -o $HOME/10.0
    # Adjust following statements as per your system
    sudo systemctl restart odoo

From UI: go to:

* |menu| Setting > Activate Developer mode
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **l10n_it_ddt** > Update

|

Support / Supporto
------------------


|Zeroincombenze| This module is maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


|
|

Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------


|en| If you have a proposal to change this module, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare questo modulo, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.

ChangeLog History / Cronologia modifiche
----------------------------------------

10.0.1.8.9 (2021-01-04)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice TD24 / Tipo documento fiscale TD24

10.0.1.8.8 (2020-12-27)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Create DdT check for picking state / Controllo stato picking in creazione DdT

10.0.1.8.7 (2020-12-07)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Date done updatable / Data spedizione modificabile
* [IMP} Total amount in tree view / Totale importo DdT in vista albero


10.0.1.8.6 (2020-07-20)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Add DdT lines to invoice / Aggiunta righe DdT a fattura esistente


10.0.1.8.2 (2020-02-19)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Change version id / Cambio identificativo versione
* [IMP] Invoicing by order / Fatturazione divisa per ordini


10.0.1.5.14 (2020-01-21)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Qty zero becomes 1 in Invoice / Q.tà zero diventa 1 in fattura


10.0.1.5.13 (2019-12-11)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Line weight / Peso in riga


10.0.1.5.12 (2019-11-20)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Total amount of stock.package.preparation / Totale del DdT


10.0.1.5.11 (2019-11-11)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Sometime it crashes when cancel sale order / A volte sistema andava in crash in annullo ordine


10.0.1.5.10 (2019-10-18)
~~~~~~~~~~~~~~~~~~~~~~~~

* [REF] Delivery condition inheritance / Determinazione dei valori di consegna
* [FIX] Weights are evaluated from pickig or order / I pesi del DdT sono calcolati dal prelivo o dall'ordine
* [IMP] Parcels is the sum of picking or order parcels / I colli sono la somma dei colli del prelievo o dell'ordine
* [IMP] Volume is the sum of picking or order volume / Il volume è la somma dei volumi del prelievo o dell'ordine
* [FIX] Show price is inherit from customer / Il flag mostra prezzi è ereditato del cliente


10.0.1.5.9 (2019-10-15)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Default delivery data by xmlrpc tough / Imposta dati predefiniti di traporto anche da xmlrpc


10.0.1.5.8 (2019-09-23)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Total amount in line / Importo totale di riga
* [FIX] Order cancel unlink DdTs too / Annullo ordine elimina anche i DdT
* [FIX] Order confirm with DdT set 'to invoice' / Conferma ordine, se crea DdT, imposta ordine da fatturare
* [FIX] Unlink DdT recover sequence number / L'eliminazione di un DdT recupera il numero, se ultimo DdT


10.0.1.5.7 (2019-09-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Shipping condition by carrier / Informazioni di spedizione da metodo di consegna


10.0.1.5.6 (2019-09-03)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Sale invoice ref / Riferimento al numero di ordine


10.0.1.5.5 (2019-08-26)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice from delivery documents base on flag / La creazione righe da ordine non in DdT è opzionale


10.0.1.5.4 (2019-06-24)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Print UoM in lines / Stampa UM in dettagli
* [IMP] DdT type visible in picking / Tipo DdT visbile nella consegna
* [IMP] DdT type in sale order / Tipo DdT in ordine di vendita


10.0.1.5.3 (2019-05-20)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice from delivery documents add service lines from sale order / La creazione della fattura da ordine aggiunge le righe di servizi che non sono in DdT


10.0.1.5.2
~~~~~~~~~~

* [IMP] Ref. fields not copied / Campi con riferimenti con copiati in duplica DdT
* [IMP] DdT name based on DdT number or partner name / Nome DdT (per ricerche) basato su numero o nome cliente
* [IMP] Report header / Cessionario e Destinatario in modello di stampa


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

* `Abstract <https://www.abstract.it>`__
* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `Apulia Software <https://www.apuliasoftware.it>`__
* `Open Force <https://www.openforce.it/>`__
* `Dinamiche Aziendali <http://www.dinamicheaziendali.it>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


Contributors / Collaboratori
----------------------------

* Davide Corio <davide.corio@abstract.it>
* Nicola Malcontenti <nicola.malcontenti@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
* Andrea Gallina <a.gallina@apuliasoftware.it>
* Alex Comba <alex.comba@agilebg.com>
* Alessandro Camilli <alessandrocamilli@openforce.it>
* Gianmarco Conte <gconte@dinamicheaziendali.it>
* Antonio M. Vigliotti <info@shs-av.com>


Maintainer / Manutenzione
-------------------------




|

----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://wiki.zeroincombenze.org/en/Odoo>`__ è progettata per le esigenze del mercato italiano.


|chat_with_us|


|

This module is part of l10n-italy project.

Last Update / Ultimo aggiornamento: 2021-01-04

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0
    :alt: Codecov
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/10.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/10.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov| image:: https://codecov.io/gh/OCA/l10n-italy/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/10.0
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
   :target: https://t.me/axitec_helpdesk

