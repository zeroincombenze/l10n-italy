==============================================================
|icon| ITA - VAT Statetement/ITA - Liquidazione IVA 12.0.1.7.0
==============================================================

**Allow to create the periodic 'VAT Statement'**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/12.0/account_vat_period_end_statement/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| In order to create a 'VAT Statement', open Accounting > Adviser > VAT Statements, this menu is only visible when the group 'Show Full Accounting Features' is enabled.
Select a Journal that will contain the journal entries of the statement.
The field 'Tax authority VAT' account contains the account where the statement balance will be registered.

The 'VAT statement' object allows to specify every amount and relative account
used by the statement.
By default, amounts of debit and credit taxes are automatically loaded
from taxes of the selected periods (see Configuration to correctly generate the periods).
Previous debit or credit is loaded from previous VAT statement, according
to its payments status.

In order to generate the journal entry, click on 'Create move' button, inside the 'Accounts' tab.
If you select a payment term, the due date(s) will be set.

The 'tax authority' tab contains information about payment(s),
here you can see statement's result ('authority VAT amount') and residual
amount to pay ('Balance').
The statement can be paid like every other debit, by journal item
reconciliation.

It is also possible to print the 'VAT statement' clicking on print > Print VAT period end statement.


|it| Per fare la liquidazione IVA, aprire Fatturazione > Contabilità > Liquidazioni IVA, il menù è visibile solo quando è abilitato il gruppo 'Mostrare funzionalità contabili complete'.
Selezionare un registro che conterrà le registrazioni contabili della liquidazione.
Il campo 'Conto IVA erario' contiene il conto dove verrà effettuata la registrazione della liquidazione IVA.

L'oggetto 'Liquidazione IVA' permette di specificare ogni importo e il conto utilizzato dalla liquidazione.
Di norma, gli importi di debito e credito delle imposte vengono caricati automaticamente dai periodi selezionati
(vedere Configurazione per generare correttamente i periodi).
I debiti e crediti precedenti vengono caricati dalle liquidazioni IVA precedenti, in base allo stato del loro pagamento.

Per creare la registrazione contabile, fare clic sul pulsante 'Crea movimento', dentro la scheda 'Conti'.
Se i termini di pagamento sono impostati viene scritta anche la scadenza (o le scadenze).

La scheda 'Erario' contiene informazioni sui pagamenti,
qui si possono visualizzare i risultati della liquidazione ('Importo IVA erario')
e l'importo residuo da pagare ('Importo a saldo').
La liquidazione può essere pagata come qualunque altro debito, con la riconciliazione delle registrazioni contabili.

È inoltre possibile stampare la liquidazione IVA facendo clic su Stampa > Stampa liquidazione IVA.


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/12.0/account_vat_period_end_statement/static/description/description.png


Configuration | Configurazione
------------------------------

In order to generate VAT statement's periods,
open Accounting > Configuration > Date ranges > Generate Date Ranges and select:

* range name prefix: prefix identifying the periods to be generated (usually the year)
* duration: 1 month
* number of ranges to generate: 12
* type: create a type or use an existing one, no specific configuration is required
* date start: first day of the first period to be generated (usually the first day of the year e.g. 01/01/2018)

In order to load the correct amount from tax, the tax has to be
associated to the account involved in the statement:

#. open a tax in Accounting > Configuration > Accounting > Taxes,
#. in the tab 'Advanced Options' select the correct account (for instance the account debit VAT)
   for the field 'Account used for VAT statement'.

If you need to calculate interest, you can add default information in your
company data (percentage and account), in the 'VAT statement' tab.



Getting started | Primi passi
=============================

|Try Me|


Prerequisites | Prerequisiti
----------------------------

* python 3.7
* postgresql 9.6+ (best 10.0+)

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
| $HOME/12.0 |
+----------------------------------------------------------------------------+

::

    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r l10n-italy -b 12.0 -G zero -p $HOME/12.0
    # Upgrade virtual environment
    vem amend $HOME/12.0/venv_odoo



Upgrade | Aggiornamento
-----------------------

::

    deploy_odoo update -r l10n-italy -b 12.0 -G zero -p $HOME/12.0
    vem amend $HOME/12.0/venv_odoo
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

12.0.0.1.0 (2018-10-04)
~~~~~~~~~~~~~~~~~~~~~~~

* Initial implementation / Implementazione iniziale



Credits | Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* `Agile Business Group sagl <https://www.agilebg.com>`__
* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `Link It Spa <https://www.linkgroup.it>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__
* `Didotech s.r.l. <https://www.didotech.com>`__



Contributors | Contributi da
----------------------------

* `Lorenzo Battistini <https://github.com/eLBati>`__
* Elena Carlesso <False>
* `Marco Marchiori <marcomarkiori@gmail.com>`__
* `Sergio Corato <sergiocorato@gmail.com>`__
* `Andrea Gallina <a.gallina@apuliasoftware.it>`__
* `Alex Comba <alex.comba@agilebg.com>`__
* `Alessandro Camilli <camillialex@gmail.com>`__
* `Simone Rubino <simone.rubino@agilebg.com>`__
* `Giacomo Grasso <giacomo.grasso.82@gmail.com>`__
* `Link It Spa <https://www.linkgroup.it>`__
* `Gianmarco Conte <gconte@dinamicheaziendali.it>`__



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

Last Update / Ultimo aggiornamento: 2024-01-27

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-black.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-12.svg
    :target: https://erp12.zeroincombenze.it
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
