================================================================================
|icon| ITA - Fattura elettronica - Supporto PEC/l10n_it_fatturapa_pec 12.0.2.2.1
================================================================================

**Invio fatture elettroniche tramite PEC**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/12.0/l10n_it_fatturapa_pec/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| **Italiano**

Questo modulo consente di inviare e ricevere i file XML della fattura elettronica versione 1.2

http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm

via PEC.

Analizza le notifiche provenienti dallo SdI e monitora lo stato della trasmissione.

**English**

This module allows you to send and receive electronic invoice/bill XML files version 1.2

http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm

via PEC.

Notifications from ES are parsed and transmission state is tracked.


|it| Descrizione non disponibile


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/12.0/l10n_it_fatturapa_pec/static/description/


Configuration | Configurazione
------------------------------

**Italiano**

Consultare il modulo `l10n_it_sdi_channel`.

Creare un nuovo canale di tipo PEC (unico supportato per ora) e indicare:

- Il server PEC da utilizzare per inviare/ricevere attraverso lo SdI
- La email PEC dello SdI, inizialmente uguale a sdi01@pec.fatturapa.it

Dopo il primo invio, lo SdI risponderà segnalando l'indirizzo da utilizzare per gli invii successivi, da inserire nella configurazione del server PEC dedicato.

Nella configurazione del server smtp, sezione "PEC e fattura elettronica", selezionare la casella "Server PEC e-fattura".

Indicare quindi la email da usare per l'invio e la ricezione, solitamente è uguale al nome utente di connessione (può essere diversa in casi particolari).

È preferibile avere una email dedicata solo alla fatturazione elettronica, in quanto i messaggi di altro tipo non possono essere gestiti da Odoo (verrebbero marcati comunque come letti).

Se si usano altri server SMTP per l'invio di email non PEC, è necessario aumentare la loro priorità rispetto a quella del server PEC.

Lo stato dell'esportazione XML può essere forzato impostando 'Permettere di forzare lo stato dell'esportazione e-fattura' nelle impostazioni tecniche dell'utente.

Per ogni azienda, in

Contabilità → Configurazione → Impostazioni → Fatture elettroniche

specificare l'utente che sarà utilizzato come creatore delle e-fatture fornitore create dalla PEC.

**English**

See `l10n_it_sdi_channel` module.

Create a new PEC channel type (the only one supported right now) and indicate:

- PEC server to be used for sending to/receiving from ES
- ES PEC email, initially equal to sdi01@pec.fatturapa.it

After sending the first email, ES will reply indicating the address to use for all the others, to be entered in dedicated PEC server configuration.

In smtp server configuration, select 'E-invoice PEC server' in 'PEC and Electronic Invoice' section.

Then specify the email to use for sending and receiving, it is usually equal to connection username (can be different in special cases).

It would be better to have a dedicated email for electronic invoicing, because other kind of messages can't be managed by Odoo (they would be marked as seen).

If you use other SMTP servers for non-PEC email sending, you need to increase their priority as compared to PEC server one.

XML export state can ba forced setting 'Allow to force the supplier e-bill export state' in user's technical settings.

For every company, in

Accounting → Configuration → Settings → Electronic Invoices

set the user who will be used as creator of supplier e-bill automatically created from PEC.



Usage | Utilizzo
----------------

**Italiano**

Nell'allegato fattura elettronica in uscita fare clic sul pulsante "Invia con PEC".

Le fatture elettroniche fornitore vengono create in modo automatico, prelevate dalla casella PEC.

**English**

In electronic invoice out attachment you can click "Send Via PEC" button.

Supplier electronic bills are automatically created, fetched from PEC mailbox.



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

* Openforce Srls Unipersonale <False>
* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Partecipanti
---------------------------

* `Andrea Colangelo <andreacolangelo@openforce.it>`__
* `Sergio Corato <info@efatto.it>`__
* `Lorenzo Battistini <https://github.com/eLBati>`__
* `Sergio Zanchetta <https://github.com/primes2h>`__
* `Tecnativa <https://www.tecnativa.com>`__
* * Víctor Martínez <False>
* `Ooops <https://www.ooops404.com>`__
* `* Giovanni Serra <giovanni@gslab.it>`__
* Maintainers <False>
* ~~~~~~~~~~~ <False>
* This module is maintained by the OCA. <False>
* .. image:: https://odoo-community.org/logo.png <False>
* :alt: Odoo Community Association <False>
* :target: https://odoo-community.org <False>
* OCA, or the Odoo Community Association, is a nonprofit organization whose <False>
* mission is to support the collaborative development of Odoo features and <False>
* promote its widespread use. <False>
* `This module is part of the OCA/l10n-italy <https://github.com/OCA/l10n-italy/tree/12.0/l10n_it_fatturapa_pec>`__
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
