
=========================================================================
|icon| Italian Localization - Fattura elettronica - Ricezione 10.0.1.3.25
=========================================================================


**Ricezione fatture elettroniche**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_einvoice_in/static/description/icon.png

|Maturity| |Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en| EInvoice in
----------------

This module allows to import Electronic Bill XML files version 1.2.1

http://www.fatturapa.gov.it/export/fatturazione/en/normativa/f-2.htm

received through the Exchange System (SdI).

http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm

For every supplier, it is possible to set the 'E-bills Detail Level':

 - Minimum level: Bill is created with no lines; User will have to create them, according to what specified in the electronic bill
 - VAT code level: Line are cumulated by VAT code
 - Maximum level: Every line contained in electronic bill will create a line in bill

Moreover, in supplier form you can set the 'E-bill Default Product': this product will be used, during generation of bills, when no other possible product is found. Tax and account of bill line will be set according to what configured in the product.

Every product code used by suppliers can be set, in product form, in

Inventory →  Products

If supplier specifies a known code in XML, the system will use it to retrieve the correct product to be used in bill line, setting the related tax and account.

 * Go to Accounting →  Purchases →  Electronic Bill
 * Upload XML file
 * View bill content clicking on 'Show preview'
 * Run 'Import e-bill' wizard to create a draft bill or run 'Link to existing bill' to link the XML file to an already (automatically) created bill

In the incoming electronic bill files list you will see, by default, files to be registered. These are files not yet linked to one or more bills.


|

|it| Fattura Elettronica in
---------------------------

Questo modulo consente di importare i file XML della fattura elettronica versione 1.2.1

http://www.fatturapa.gov.it/export/fatturazione/it/normativa/f-2.htm

ricevuti attraverso il Sistema di Interscambio (SdI).

http://www.fatturapa.gov.it/export/fatturazione/it/sdi.htm


::

    Destinatari:

Il modulo è destinato a tutte le aziende che dal 2019 dovranno emettere fattura elettronica


::

    Normativa e prassi:

Le leggi inerenti la fattura elettronica sono numerose. Potete consultare la `normativa fattura elettronica <https://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm>`__


Per ciascun fornitore è possibile impostare il "Livello dettaglio e-fatture":

 - Livello minimo: la fattura fornitore viene creata senza righe, che dovranno essere create dall'utente in base a quanto indicato nella fattura elettronica
 - Livello codice IVA: le righe sono cumulate per codice IVA
 - Livello massimo: le righe della fattura fornitore verranno generate a partire da tutte quelle presenti nella fattura elettronica

Nella scheda fornitore è inoltre possibile impostare il "Prodotto predefinito per e-fattura": verrà usato, durante la generazione delle fatture fornitore, quando non sono disponibili altri prodotti adeguati. Il conto e l'imposta della riga fattura verranno impostati in base a quelli configurati nel prodotto.

Tutti i codici prodotto usati dai fornitori possono essere impostati nella relativa scheda, in

Magazzino →  Prodotti


|

Features / Caratteristiche
--------------------------

+--------------------------------------------------------+------------+---------------------------------+
| Descrizione                                            | Stato      | Note                            |
+--------------------------------------------------------+------------+---------------------------------+
| e-fattura da fornitore, righe con IVA                  | |check|    |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| e-fattura da fornitore, righe senza IVA                | |check|    | Non riconosce esatto codice IVA |
+--------------------------------------------------------+------------+---------------------------------+
| e-fattura da fornitori con ritenuta d'acconto          | |check|    |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| e-fattura da fornitori da agenti (enasarco)            | |check|    |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| e-fattura da fornitori con controllo su totale fattura | |check|    |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| e-fattura da fornitori con split-payment               | |no_check| |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| e-fattura da fornitori con reverse charge              | |info|     | Non riconosce esatto codice IVA |
+--------------------------------------------------------+------------+---------------------------------+
| E-Nota Credito da fornitore                            | |check|    |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| Gestione multi-aziendale                               | |check|    |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| Validazione e-fattura per azienda                      | |check|    |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| Generazione scadenzario passivo da e-fattura           | |check|    |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| Livello contabile solo testata senza dettagli          | |check|    | Per collegare fatture manuali   |
+--------------------------------------------------------+------------+---------------------------------+
| Livello righe contabili per aliquote IVA               | |check|    | Per fatture con troppe righe    |
+--------------------------------------------------------+------------+---------------------------------+
| Livelllo righe contabili in dettaglio                  | |check|    |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| e-fattura da stabile organizzazione estera             | |info|     |                                 |
+--------------------------------------------------------+------------+---------------------------------+
| e-fattura da rappresentante fiscale                    | |info|     |                                 |
+--------------------------------------------------------+------------+---------------------------------+


|

Usage / Utilizzo
----------------

Se il fornitore specifica un codice noto nell'XML, questo verrà usato dal sistema per recuperare il prodotto corretto da usare nella riga fattura, impostando il conto e l'imposta collegati.

|menu| Contabilità > Acquisti > Fattura elettronica

Caricare un file XML
Visualizzare il contenuto della fattura facendo clic su "Mostra anteprima"
Eseguire la procedura guidata "Importa e-fattura" per creare una fattura in bozza oppure "Collega a fattura esistente" per collegare il file XML a una fattura già (automaticamente) creata


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
* |menu| Setting > Apps |right_do| Select **l10n_it_einvoice_in** > Install


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
* |menu| Setting > Apps |right_do| Select **l10n_it_einvoice_in** > Update

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

10.0.1.3.25 (2021-01-25)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Received date / Data di ricezione fattura

10.0.1.3.24 (2021-01-12)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Disabled xml validation / Validazione file xml disabilitata

10.0.1.3.23 (2021-01-05)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Accept old nature code / Accetta codici natura 2020

10.0.1.3.22 (2020-12-20)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Avoid invoice address duplicate / Evita duplicazione indirizzi di fatturazione impport ft. fornitori


10.0.1.3.21 (2020-11-24)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Wrong address number / Ignora numero civico non valido


10.0.1.3.20 (2020-09-09)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Invalid carrier VAT / Ignora PIVA corriere non valida


10.0.1.3.19 (2020-07-29)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] No import if company IBAN in xml / Non importa fattura se IBAN azienda in file XML


10.0.1.3.18 (2020-07-28)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Duplicare rea_code when invoice address / Codice rea duplicato se uso indirizzo fatturazione


10.0.1.3.17 (2020-07-07)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import error level 2 / Errore importazione livello 2


10.0.1.3.16 (2020-06-16)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] No import self-invoice / Non importa autofatture


10.0.1.3.15 (2020-05-22)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if supplier invoice w/o due_adate / Errore importazione se xml senza date scadenza


10.0.1.3.15 (2020-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash import rated invoice if supplier w/o account / Errore importazione per aliquote e fornitore senza conto


10.0.1.3.13 (2020-04-06)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if wrong invoice date (i.e. 2020-04-06Z) / Errore se data formattata erroneamente


10.0.1.3.13 (2020-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if invoice address / Errore durante importazione con indirizzo di fatturazione

10.0.1.3.12 (2020-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Partner data / Dati fornitore non modificati. Se diversi creato indirizzo fatturazione
* [FIX] Crash in some cases / Errore durante importazione in alcuni casi
* [IMP] More incisive message / Messagi più precisi


10.0.1.3.11 (2020-02-17)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor change / Modifiche interne


10.0.1.3.10 (2020-02-04)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] XML Preview / Anteprima file XML


10.0.1.3.9 (2019-12-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] synchro2 error / Errore sunchro2


10.0.1.3.9 (2019-12-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import e-invoice with RF19 / Errore in importazione fattura da forfettario
* [FIX] Conflict with connector_vg7 module / Conflitto con modulo connector_vg7


10.0.1.3.8 (2019-10-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Link to existent invoice set header data / Il collegamento ad una fattura esistente imposta i dati di testata
* [FIX] Unicode error in delivery address / Errore unicode in indirizzo di consegan
* [IMP] Some supplier invoices have natura N6 without vax rate / Fattura fornitori con natura N6 e senza aliquota IVA


10.0.1.3.7 (2019-06-25)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Without province, cannot import e-invoice


10.0.1.3.6 (2019-06-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Some supplier invoces with empty tags fail schema validation / Alcune fatture fornitori con tag vuoti non erano validate dallo schema
* [FIX] Invoice supplier with existent REA code crashes / Fatture fornitori con codice REA esistente mandavano in crash il sistema
* [IMP] New search algorithm finds similar names / Nuovo algoritmo di ricerca che trova nomi simili


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

* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `Innoviu srl <http://www.innoviu.com>`__
* `Pointec s.r.l. <https://www.pointec.it/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Collaboratori
----------------------------

* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Roberto Onnis <roberto.onnis@innoviu.com>
* Alessio Gerace <alessio.gerace@agilebg.com>
* Cesare Pellegrini <cesare@pointec.it>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

Translations by / Traduzioni a cura di
--------------------------------------

* Sergio Zanchetta <https://github.com/primes2h>


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

Last Update / Ultimo aggiornamento: 2021-01-25

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

