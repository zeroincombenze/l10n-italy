========================================================
|icon| Reverse Charge Tax/IVA in reverse charge 10.0.1.8
========================================================

**Manage Reverse Charge Tax for Italy**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_reverse_charge/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| Module to manage reverse charge tax in vendor bills and customer invoices.

Tis module allows you to automate the accounting entries linked to invoices from
intra-EU and extra-EU suppliers.
In order to manage the reverse charge tax a self-invoice is created and an account
entry is created too.
After these 3 entries, the amount to pay to supplier is the invoice total without tax.

All fiscal and legal Italian laws are satisfied,

When supplier invoice is cancelled, the self invoice is cancelled too and account
entry is deleted.

For customer invoices tha due amount is evaluated.


|it| Modulo per gestire l'inversione contabile (reverse charge) nelle fatture fornitore e
nelle fatture clienti.

Questo modulo permette di automatizzare le registrazioni contabili collegate alle
fatture fornitori intra UE ed extra UE, necessarie per gestire l'inversione
contabile IVA.
Per gestire l'inversione contabile viene generata un'auto-fattura di vendita che
storna l'IVA in acquisto e una registrazione di giroconto per azzerare il credito
derivante dall'auto-fattura.
Con queste 3 operazioni il debito verso la fattura di acquisto è pari alla sola
imponibile e l'IVA è riportata nei documenti fiscali come previsto dalla normativa.

L'annullo della fattura fornitore, annulla anche l'auto-fattura ed elimina la
registrazione di giroconto.

Per le fatture di vendita viene soltanto calcolato l'importo da incassare.


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_reverse_charge/static/description/description.png


Configuration | Configurazione
------------------------------

☰ Accounting > Configuration > Account > Taxes

Create sale tax **22% intra UE**:

.. figure:: /l10n_it_reverse_charge/static/description/tax_22_v_i_ue.png
   :alt: 22% intra UE Vendita
   :width: 400px

Create purchase tax **22% intra UE**:

Create sale tax **22% extra UE**:

Create purchase tax **22% extra UE**:

.. figure:: /l10n_it_reverse_charge/static/description/tax_22_a_e_ue.png
  :alt: 22% extra UE Acqisti
  :width: 400px

☰ Accounting > Configuration > Account > RC Types

Create reverse chare tye **Intra UE (autofattura)**:

☰ Accounting > Configuration > Account > Fiscal Position



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

10.0.1.8 (2024-06-28)
~~~~~~~~~~~~~~~~~~~~~

* [IMP] Function get_receivable_line_ids moved to l10n_it_account
* [QUA] Test coverage 64% (404: 146+258) [26 TestPoints] - quality rating 49 (target 100)

10.0.1.7 (2024-06-09)
~~~~~~~~~~~~~~~~~~~~~

* [FIX] Tax with RC requires RC fiscal position / Controllo codici IVA con RC e posizione fiscale
* [IMP] Show net to pay (see l10n_it_account) / Visualizza netto a pagare (vedere l10n_it_account)
* [IMP] RC Amount stored in invoice record / Importo IVA RC in fattura
* [IMP] Sale invoice / Gestione fatture di vendita con RC e netto a pagare
* [IMP] Regression tests
* [QUA] Test coverage 64% (410: 147+263) [26 TestPoints] - quality rating 49 (target 100)

10.0.1.6 (2023-02-20)
~~~~~~~~~~~~~~~~~~~~~

* [IMP] The invoice date of self invoice is the same of the date of purchase invoice / Data auto-fattura come data contabile fattura di acquisto

10.0.1.5 (2023-02-13)
~~~~~~~~~~~~~~~~~~~~~

* [IMP] The date may be different from invoice date for self invoice / Data fattura e contabile diverse per le auto-fatture



Credits | Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* `Odoo Italia Network <https://www.odoo-italia.net>`__
* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Partecipanti
---------------------------

* `Davide Corio <davide.corio@abstract.it>`__
* `Alex Comba <alex.comba@agilebg.com>`__
* `Lorenzo Battistini <lorenzo.battistini@agilebg.com>`__
* `Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>`__



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

Last Update / Ultimo aggiornamento: 2024-06-28

.. |Maturity| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
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
