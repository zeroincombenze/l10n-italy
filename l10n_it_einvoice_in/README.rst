========================================================
|icon| ITA - Fattura elettronica - Ricezione 10.0.1.3.51
========================================================

**E-invoice receive**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_einvoice_in/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| This module allows to import
`Electronic Bill XML files version 1.2.1 <http://www.fatturapa.gov.it/export/fatturazione/en/normativa/f-2.htm>`__
received through the `
Exchange System (SdI) <http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm>`__


|it| Questo modulo consente di importare i file
`XML della fattura elettronica versione 1.2.1 <http://www.fatturapa.gov.it/export/fatturazione/it/normativa/f-2.htm>`__
ricevuti attraverso il
`Sistema di Interscambio (SdI) <http://www.fatturapa.gov.it/export/fatturazione/it/sdi.htm>`__

Destinatari
-----------

Il modulo è destinato a tutte le aziende che dal 2019 emettono fattura elettronica


Normativa e prassi
------------------

Le leggi inerenti la fattura elettronica sono numerose. Consultare la
`normativa fattura elettronica <https://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm>`__


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_einvoice_in/static/description/description.png


Features | Caratteristiche
--------------------------

+--------------------------------------------------------------+----------+-----+---------------------------------+
| Description | Descrizione                                    | Z0incomb | OCA | Note(s)                         |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | e-fattura da fornitore, righe con IVA                  | ✅       | ✅  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | e-fattura da fornitore, righe senza IVA                | ✅       | ✅  | Non riconosce esatto codice IVA |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | e-fattura da fornitori con ritenuta d'acconto          | ✅       | ✅  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | e-fattura da fornitori da agenti (enasarco)            | ✅       | ✅  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | e-fattura da fornitori con controllo su totale fattura | ✅       | ❌  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | e-fattura da fornitori con split-payment               | ❌       | ❌  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | e-fattura da fornitori con reverse charge              | |info|   | ❌  | Non riconosce esatto codice IVA |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | E-Nota Credito da fornitore                            | ✅       | ✅  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | Gestione multi-aziendale                               | ✅       | ❌  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | Validazione e-fattura per azienda                      | ✅       | ❌  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | Generazione scadenzario passivo da e-fattura           | ✅       | ✅  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | Livello contabile solo testata senza dettagli          | ✅       | ✅  | Per collegare fatture manuali   |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | Livello righe contabili per aliquote IVA               | ✅       | ❌  | Per fatture con troppe righe    |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | Livelllo righe contabili in dettaglio                  | ✅       | ✅  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A |e-fattura da stabile organizzazione estera              | ✅       | ❌  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+
| N/A | e-fattura da rappresentante fiscale                    | ✅       | ❌  |                                 |
+--------------------------------------------------------------+----------+-----+---------------------------------+



Configuration | Configurazione
------------------------------

For every supplier, it is possible to set the 'E-bills Detail Level':

* Minimum level: Bill is created with no lines; User will have to create them, according to what specified in the electronic bill
* VAT code level: Line are cumulated by VAT code
* Maximum level: Every line contained in electronic bill will create a line in bill

Moreover, in supplier form you can set the **E-bill Default Product**:
this product will be used, during generation of bills,
when no other possible product is found.
Tax and account of bill line will be set according to what configured in the product.

Every product code used by suppliers can be set, in product form, in

☰ Inventory > Inventory Control > Products

If supplier specifies a known code in XML, the system will use it to retrieve the
correct product to be used in bill line, setting the related tax and account.



Usage | Utilizzo
----------------

* ☰ Accounting > Purchases > Electronic Bill > [Create]
* Upload XML file and click on [Save]


If you use the module *l10n_it_einvoice_send2sdi* you will see records from SdI.

* View bill content clicking on [Show preview]
* Click in [Action] and run 'Import e-bill' wizard to create a draft bill or run 'Link to existing bill' to link the XML file to an already (automatically) created bill

In the incoming electronic bill files list you will see, by default, files to be registered.
These are files not yet linked to one or more bills.



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

10.0.1.3.51 (2024-08-02)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Errore DatiAnagrafici.DataIscrizioneAlbo, "%Y-%m-%d")
* [QUA] Test coverage 70% (1480: 446+1034) [0 TestPoints] - quality rating 42 (target 100)

10.0.1.3.50 (2024-07-29)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Sometime invoice address duplicated / A volte veniva creato un duplicato dell'indirizzo di fatturazione
* [IMP] Revaluate amount_untaxed by e-invoice / Forza imponibile da e-fattura se diff < 1 cent
* [IMP] Revaluate amount_tax by e-invoice / Forza IVA da e-fattura se diff < 1 cent
* [IMP] Ingloba numero civico se separato
* [QUA] Test coverage 70% (1479: 446+1033) [0 TestPoints] - quality rating 42 (target 100)

10.0.1.3.49 (2024-07-23)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Force validation
* [QUA] Test coverage 70% (1460: 444+1016) [0 TestPoints] - quality rating 42 (target 100)

10.0.1.3.48 (2024-07-22)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Wrong invoice total if wrong rounding / Totale fattura errato in caso di errato arrotondamento
* [IMP] Store and show e-invoice totals / Memorizza e mostra totali e-fattura
* [IMP] Dati terzo intermediario in fattura
* [IMP] Cassa previdenziale in fattura
* [IMP] Best partner searching / Migliorie ricerca partner
* [QUA] Test coverage 69% (1386: 424+962) [0 TestPoints] - quality rating 42 (target 100)

10.0.1.3.47 (2024-06-14)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash with <AdministrativeReference></AdministrativeReference>
* [QUA] Test coverage 63% (1337: 498+839) [0 TestPoints] - quality rating 38 (target 100)


10.0.1.3.46 (2024-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Again weird error linking self-invoice
* [FIX] Avoid company data update from self-invoice / Non cambia dati aziendali da auto-fattura
* [FIX] Cannot import e-invoice with wrong vat / Ignora PI se errata in e-fattura
* [QUA] Test coverage 63% (1337: 498+839) [0 TestPoints] - quality rating 38 (target 100)

10.0.1.3.45 (2024-05-05)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Weird error linking self-invoice
* [IMP] Avoid company data update from self-invoice
* [QUA] Test coverage 63% (1330: 495+835) [0 TestPoints] - quality rating 38 (target 100)

10.0.1.3.44 (2024-02-06)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] E-Lines detail: name changed

10.0.1.3.43 (2024-01-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash with <RiferimentoTesto></RiferimentoTesto> / Crash in alcuni casi
* [FIX] Search state/district by country code from vat / Ricerca provincia con nazione da PI
* [QUA] Test coverage 63% (1326: 493+833) [0 TestPoints] - quality rating 38 (target 100)

10.0.1.3.42 (2023-10-23)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash with <DatiOrdineAcquisto></DatiOrdineAcquisto> / Crash in alcuni casi
* [QUA] Test coverage 63% (1326: 493+833) [0 TestPoints] - quality rating 38 (target 100)

10.0.1.3.41 (2023-04-11)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash in some strange email
* [FIX] Crash when xml tag with extra property

10.0.1.3.40 (2023-04-11)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Import e-invoice from RSM / Importazione file XML da San Marino
* [FIX] Crash when two emails



Credits | Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* `Agile Business Group sagl <https://www.agilebg.com>`__
* Innoviu srl <False>
* `Pointec s.r.l. <https://www.pointec.it>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__
* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `Innoviu Srl <http://www.innoviu.com>`__



Contributors | Partecipanti
---------------------------

* `Lorenzo Battistini <lorenzo.battistini@agilebg.com>`__
* `Roberto Onnis <roberto.onnis@innoviu.com>`__
* `Alessio Gerace <alessio.gerace@agilebg.com>`__
* `Cesare Pellegrini <cesare@pointec.it>`__
* `Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>`__



Translations by | Traduzioni a cura di
--------------------------------------

* `Sergio Zanchetta <https://github.com/primes2h>`__



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

Last Update / Ultimo aggiornamento: 2024-08-02

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
