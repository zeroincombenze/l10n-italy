=============================================================================
|icon| ITA - Fattura elettronica - Emissione/l10n_it_fatturapa_out 12.0.3.2.3
=============================================================================

**Emissione fatture elettroniche**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/12.0/l10n_it_fatturapa_out/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| **Italiano**

Questo modulo consente di generare i file XML della fattura elettronica versione 1.2

http://www.fatturapa.gov.it/export/fatturazione/it/normativa/f-2.htm

da inviare al Sistema di Interscambio (SdI).

http://www.fatturapa.gov.it/export/fatturazione/it/sdi.htm

**English**

This module allows you to generate the Electronic Invoice XML files version 1.2

http://www.fatturapa.gov.it/export/fatturazione/en/normativa/f-2.htm

to be sent to the Exchange System (ES).

http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm


|it| Descrizione non disponibile


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/12.0/l10n_it_fatturapa_out/static/description/


Configuration | Configurazione
------------------------------

**Italiano**

Consultare il file README di l10n_it_fatturapa.

É possibile esportare le fatture cliente con le righe articolo con un CodiceTipo diverso dallo standard 'ODOO' creando un parametro 'fatturapa.codicetipo.odoo' (in Configurazione > Funzioni tecniche > Parametri > Parametri di sistema) con il codice voluto (tipicamente su richiesta del cliente).
Non è possibile impostare un diverso CodiceTipo per cliente, al momento.

**English**

See l10n_it_fatturapa README file.

It is possible to export invoices with rows with a different CodiceTipo from the default 'ODOO' by creating a parameter 'fatturapa.codicetipo.odoo' (in Settings > Technical > Parameters > System Parameters) with the desired code (tipically on customer's request).
It is not possible to set a different CodiceTipo by customer, until now.



Usage | Utilizzo
----------------

**Italiano**

 * Compilare la fattura con i dati necessari per l'esportazione: per esempio, nella scheda "Allegati fattura elettronica"
 * Selezionare 1 o N fatture ed eseguire la procedura guidata "Esporta fattura elettronica"
 * Per le fatture estere, è possibile inviarle a soli fini fiscali inserendo il codice identificativo XXXXXXX (7 volte X) ed avendo cura di indicare il paese del partner.
   Le fatture vanno comunque spedite al cliente, ma si evita la predisposizione dell'esterometro.

**English**

 * Fill invoice data you need to export: For instance, in 'Electronic Invoice Attachments' TAB
 * Select 1 or N invoices and run 'Export Electronic Invoice' wizard
 * For foreign invoices, it is possible to send them only for tax purposes with code XXXXXXX (7 times X) and assuring to set the country of the partner.
   Invoices must be sent anyway to the customer, but in this way it is not needed to prepare esterometro.



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



Credits | Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* Davide Corio <False>
* Agile Business Group <False>
* Innoviu <False>
* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Partecipanti
---------------------------

* Davide Corio <False>
* `Lorenzo Battistini <https://github.com/eLBati>`__
* Roberto Onnis <False>
* Alessio Gerace <False>
* Alex Comba <False>
* `Sergio Zanchetta <https://github.com/primes2h>`__
* `Giovanni Serra <giovanni@gslab.it>`__
* `Tecnativa <https://www.tecnativa.com>`__
* * Víctor Martínez <False>
* Maintainers <False>
* ~~~~~~~~~~~ <False>
* This module is maintained by the OCA. <False>
* .. image:: https://odoo-community.org/logo.png <False>
* :alt: Odoo Community Association <False>
* :target: https://odoo-community.org <False>
* OCA, or the Odoo Community Association, is a nonprofit organization whose <False>
* mission is to support the collaborative development of Odoo features and <False>
* promote its widespread use. <False>
* `This module is part of the OCA/l10n-italy <https://github.com/OCA/l10n-italy/tree/12.0/l10n_it_fatturapa_out>`__
* You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute. <False>



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

Last Update / Ultimo aggiornamento: 2026-03-08

.. |Maturity| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
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
