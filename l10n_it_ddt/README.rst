==========================
|icon| DDT/DdT 10.0.1.8.26
==========================

**Delivery Document Type**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_ddt/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| This module manages the Italian deliver document AKA DdT.
The DdT is a document container of picking, so every action on the DDT
is appled to all pickings inside DdT.

You can create invoices from DdT rather than invoice from Sale Orders.


|it| Gestione documento di trasporto, conosciuto anche come DdT.
Il DDT è documento contenitore dei prelievi; così ogni azione sul DdT
viene applicata a tutti i prelievi dentro il DdT.

Il modulo permette anche di creare fatture basate su DdT in alternativa alla
fatturazione da ordini.


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_ddt/static/description/description.gif


Configuration | Configurazione
------------------------------

☰ Inventory > DdT Data > Type

☰ Inventory > DdT Data > Carriage Condition

☰ Inventory > DdT Data > Descriptions of goods

☰ Inventory > DdT Data > Reasons of Transportation

☰ Inventory > DdT Data > Methods of Transportation



Usage | Utilizzo
----------------

You can automatically create a DDT From a Sale Order, setting
'Automatically create the DDT' field that will automatically create the DDT on
Sale Order confirmation.

You can also directly create a DDT using

☰ Inventory > Operations > DDT

menu and add existing delivery orders to it, in the [`transfers`] tab.

When you work with delivery orders, you can create a DDT selecting 1 or more
pickings and launching the action [DDT from pickings].

Also, you can select 1 or more pickings and run [add pickings to DDT] to add
the selected delivery orders to an existing DDT

If the state of the delivery orders allows it, you can deliver them from the
DDT directly, clicking [put in pack] and [package done]

Finally you can create your invoice directly from the DDT using the
'Create Invoice' button that creates a new Invoice with the ddt lines as
invoice lines



Getting started | Primi passi
=============================

|Try Me|


Prerequisites | Prerequisiti
----------------------------

* python 2.7+ (best 2.7.5+)
* postgresql 9.2+ (best 9.5)

::

    cd $HOME
    # Follow statements activate deployment, installation and upgrade tools
    cd $HOME
    [[ ! -d ./tools ]] && git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -pUT
    source $HOME/devel/activate_tools



Installation | Installazione
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
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__ |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| $HOME/10.0 |
+----------------------------------------------------------------------------+

::

    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r l10n-italy -b 10.0 -G zero -p $HOME/10.0
    # Upgrade virtual environment
    vem amend $HOME/10.0/venv_odoo



Upgrade | Aggiornamento
-----------------------

::

    deploy_odoo update -r l10n-italy -b 10.0 -G zero -p $HOME/10.0
    vem amend $HOME/10.0/venv_odoo
    # Adjust following statements as per your system
    sudo systemctl restart odoo



Support | Supporto
------------------

|Zeroincombenze| This module is supported by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved | Ci mettiamo in gioco
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



ChangeLog History | Cronologia modifiche
----------------------------------------

10.0.1.8.26 (2024-05-30)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Wrong inheritance for delivery values
* [IMP] Delivery Carrier Notes
* [QUA] Test coverage 67% (1385: 454+931) [266 TestPoints] - quality rating 72 (target 100)

10.0.1.8.25 (2023-06-13)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Cancel DdT from order with invoice / Annullo DdT da ordine con fattura
* [IMP] Cancel DdT check for backorder / Annullo DdT controlla se creato ordine saldo
* [QUA] Coverage 67% (1377/453) + 247cp

10.0.1.8.24 (2023-05-31)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] DdT from 'done' order / Emissione DdT da ordini bloccati
* [IMP] Check for dependecies version / Controllo versione dipendenze

10.0.1.8.23 (2023-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Wrong line weight evaluation / Errato calcolo peso riga

10.0.1.8.22 (2023-05-03)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Report wrong carrier value / Errato valore vettore in stampa

10.0.1.8.21 (2023-04-17)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Delivery price from DN or Sale Order / Calcolo trasporto da DdT o Ordine
* [FIX] Crash with module sale order revision
* [IMP] New test coverage 67% (1373/449/+247)

10.0.1.8.20 (2023-02-16)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Field carrier_partner moved on other module / Il campo anagrfaica vettore spostato su altro modulo

10.0.1.8.19 (2023-01-20)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Sale confirm remove duplicate delivery lines / Conferma ordine rimuove righe consegna duplicate


10.0.1.8.18 (2022-12-14)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Delivery price in invoice / Calcolo totale spedizioni
* [IMP] Test coverage increased

10.0.1.8.17 (2022-11-24)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Order.carrier_id when import / Metodo di consegna impostato durante import record


10.0.1.8.16 (2022-10-06)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Delivery carrier / Metodo di consegna

10.0.1.8.15 (2022-10-04)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Delivery to no contact customer / Consegna a soggetto non contatto del cliente



Credits | Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* Odoo Community Association (OCA) and other subjects <False>
* `Abstract <https://www.abstract.it>`__
* `Agile Business Group sagl <https://www.agilebg.com>`__
* `Apulia Software s.r.l. <https://www.apuliasoftware.it>`__
* `Open Force <https://www.openforce.it>`__
* `Dinamiche Aziendali <https://www.dinamicheaziendali.it>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Partecipanti
---------------------------

* `Davide Corio <davide.corio@abstract.it>`__
* `Nicola Malcontenti <nicola.malcontenti@agilebg.com>`__
* `Lorenzo Battistini <lorenzo.battistini@agilebg.com>`__
* `Francesco Apruzzese <f.apruzzese@apuliasoftware.it>`__
* `Andrea Gallina <a.gallina@apuliasoftware.it>`__
* `Alex Comba <alex.comba@agilebg.com>`__
* `Alessandro Camilli <alessandrocamilli@openforce.it>`__
* `Gianmarco Conte <gconte@dinamicheaziendali.it>`__
* `Antonio M. Vigliotti <info@shs-av.com>`__



Maintainer | Manutenzione
-------------------------

* `Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>`__



----------------

|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://www.zeroincombenze.it/>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://www.zeroincombenze.it/>`__ è progettata per le esigenze del mercato italiano.


|
|

This module is part of l10n-italy project.

Last Update / Ultimo aggiornamento: 2024-05-30

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-black.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
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
