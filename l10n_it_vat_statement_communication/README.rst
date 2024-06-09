==========================================================================================
|icon| ITA - Comunicazione liquidazione IVA/l10n_it_vat_statement_communication 10.0.1.5.4
==========================================================================================

**Comunicazione liquidazione IVA ed esportazione file xml conforme alle specifiche dell'Agenzia delle Entrate**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_vat_statement_communication/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| Comunicazione liquidazione IVA ed export file XML, conforme alle specifiche dell''Agenzia delle Entrate.

I dati possono essere caricati da liquidazioni IVA effettuate in odoo tramite `account_vat_period_end_statement`


|it| Nessuna informazione disponibile

|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_vat_statement_communication/static/description/


Configuration | Configurazione
------------------------------

|it| Per generare i periodi della dichiarazione IVA,
aprire Impostazioni > Fatturazione > Configurazione > Intervalli data > Generazione intervalli data e selezionare:

* prefisso nome intervallo: prefisso identificativo per i periodi da generare (tipicamente l'anno)
* durata: 1 mese
* numero di intervalli da generare: 12
* tipo: creare un tipo o utilizzarne uno esistente, non è richiesta una configurazione particolare
* data iniziale: primo giorno del primo periodo che sarà generato (tipicamente il primo giorno dell'anno i.e. 01/01/2018)

Per caricare l'importo corretto, un'imposta deve essere associata al conto utilizzato nella liquidazione:

* aprire l'imposta da Fatturazione > Configurazione > Contabilità > Imposte,
* nella scheda 'Opzioni avanzate' selezionare il conto corretto (ad esempio IVA debito)
  per il campo 'Conto utilizzato per la liquidazione IVA'.

Per calcolare gli interessi, è possibile aggiungere le informazioni da utilizzare (conto e percentuale)
nei dati aziendali, nella scheda 'Liquidazione IVA'.


|en| In order to generate VAT statement's periods,
open Accounting > Configuration > Date ranges > Generate Date Ranges and select:

* range name prefix: prefix identifying the periods to be generated (usually the year)
* duration: 1 month
* number of ranges to generate: 12
* type: create a type or use an existing one, no specific configuration is required
* date start: first day of the first period to be generated (usually the first day of the year e.g. 01/01/2018)

In order to load the correct amount from tax, the tax has to be
associated to the account involved in the statement:

* open a tax in Accounting > Configuration > Accounting > Taxes,
* in the tab 'Advanced Options' select the correct account (for instance the account debit VAT)
  for the field 'Account used for VAT statement'.

If you need to calculate interest, you can add default information in your
company data (percentage and account), in the 'VAT statement' tab.



Usage | Utilizzo
----------------

- Creare una nuova comunicazione.
- Nel "Quadro VP" aggiungere una voce selezionando in alto la liquidazione, precedentemente creata, da inserire.



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



Credits | Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* Openforce di Camilli Alessandro <False>
* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Partecipanti
---------------------------

* `Lorenzo Battistini <https://github.com/eLBati>`__
* Elena Carlesso <False>
* `Marco Marchiori <marcomarkiori@gmail.com>`__
* `Sergio Corato <sergiocorato@gmail.com>`__
* `Andrea Gallina <a.gallina@apuliasoftware.it>`__
* `Alex Comba <alex.comba@agilebg.com>`__
* `Alessandro Camilli <camillialex@gmail.com>`__
* `Simone Rubino <simone.rubino@agilebg.com>`__
* `Giacomo Grasso <giacomo.grasso.82@gmail.com>`__
* `LinkIt Spa <http://http://www.linkgroup.it>`__
* `Gianmarco Conte <gconte@dinamicheaziendali.it>`__
* `Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>`__
* Lara Baggio <False>



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

Last Update / Ultimo aggiornamento: 2024-06-06

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
