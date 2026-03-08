==============================================================================
|icon| ITA - Fattura elettronica - Ricezione/l10n_it_fatturapa_in 12.0.2.6.1_5
==============================================================================

**Ricezione fatture elettroniche**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/12.0/l10n_it_fatturapa_in/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| **Italiano**

Questo modulo consente di importare i file XML della fattura elettronica versione 1.2

http://www.fatturapa.gov.it/export/fatturazione/it/normativa/f-2.htm

ricevuti attraverso il Sistema di Interscambio (SdI).

http://www.fatturapa.gov.it/export/fatturazione/it/sdi.htm

**English**

This module allows to import Electronic Bill XML files version 1.2

http://www.fatturapa.gov.it/export/fatturazione/en/normativa/f-2.htm

received through the Exchange System (ES).

http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm


|it| Nessuna informazione disponibile

|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/12.0/l10n_it_fatturapa_in/static/description/


Configuration | Configurazione
------------------------------

**Italiano**

Consultare anche il file README del modulo l10n_it_fatturapa.

Per ciascun fornitore è possibile impostare il "Livello dettaglio e-fatture":

 - Livello minimo: la fattura fornitore viene creata senza righe, che dovranno essere create dall'utente in base a quanto indicato nella fattura elettronica
 - Livello massimo: le righe della fattura fornitore verranno generate a partire da tutte quelle presenti nella fattura elettronica

Nella scheda fornitore è inoltre possibile impostare il "Prodotto predefinito per e-fattura": verrà usato, durante la generazione delle fatture fornitore, quando non sono disponibili altri prodotti adeguati. Il conto e l'imposta della riga fattura verranno impostati in base a quelli configurati nel prodotto.

Tutti i codici prodotto usati dai fornitori possono essere impostati nella relativa scheda, in

Magazzino →  Prodotti

Se il fornitore specifica un codice noto nell'XML, questo verrà usato dal sistema per recuperare il prodotto corretto da usare nella riga fattura, impostando il conto e l'imposta collegati.

**English**

See also the README file of l10n_it_fatturapa module.

For every supplier, it is possible to set the 'E-bills Detail Level':

 - Minimum level: Bill is created with no lines; User will have to create them, according to what specified in the electronic bill 
 - Maximum level: Every line contained in electronic bill will create a line in bill

Moreover, in supplier form you can set the 'E-bill Default Product': this product will be used, during generation of bills, when no other possible product is found. Tax and account of bill line will be set according to what configured in the product.

Every product code used by suppliers can be set, in product form, in

Inventory →  Products

If supplier specifies a known code in XML, the system will use it to retrieve the correct product to be used in bill line, setting the related tax and account.



Usage | Utilizzo
----------------

**Italiano**

 * Andare in Contabilità →  Acquisti →  Fattura elettronica
 * Caricare un file XML
 * Visualizzare il contenuto della fattura facendo clic su "Mostra anteprima"
 * Eseguire la procedura guidata "Importa e-fattura" per creare una fattura in bozza oppure "Collega a fattura esistente" per collegare il file XML a una fattura già (automaticamente) creata

Nell'elenco file delle fatture elettroniche in ingresso saranno presenti, in modo predefinito, quelli da registrare. Sono i file che devono ancora essere collegati a una o più fatture fornitore.

**English**

 * Go to Accounting →  Purchases →  Electronic Bill
 * Upload XML file
 * View bill content clicking on 'Show preview'
 * Run 'Import e-bill' wizard to create a draft bill or run 'Link to existing bill' to link the XML file to an already (automatically) created bill

In the incoming electronic bill files list you will see, by default, files to be registered. These are files not yet linked to one or more bills.



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



Known issues | Roadmap
----------------------

Il modulo contiene un cambiamento alla firma di un metodo in ``models/account.py``
il quale cambia da

``compute_xml_amount_untaxed(self, DatiRiepilogo)``

a

``compute_xml_amount_untaxed(self, FatturaBody)``

Il cambiamento è dovuto all'implementazione della gestione degli arrotondamenti
che posso essere presenti in 2 sezioni diverse del file XML della fattura elettronica.

La soluzione ottimale è stata di cambiare la firma del metodo per consentire
la visibilità delle sezioni ``FatturaElettronicaBody.DatiBeniServizi.DatiRiepilogo`` e
``FatturaElettronicaBody.DatiGenerali.DatiGeneraliDocumento`` dove è presente il nodo ``Arrotondamento``

Pertanto, al fine di ottenere il corretto valore del totale imponibile, i moduli che
avessero ridefinito il metodo ``compute_xml_amount_untaxed`` nel modello ``account.invoice``
dovranno adeguare la chiamata al metodo stesso preoccupandosi di utilizzare come primo parametro l'oggetto ``FatturaElettronicaBody``.



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

* Agile Business Group <False>
* Innoviu <False>
* `Odoo Community Association (OCA) <https://odoo-community.org>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Partecipanti
---------------------------

* `Lorenzo Battistini <lorenzo.battistini@agilebg.com>`__
* Roberto Onnis <False>
* Alessio Gerace <False>
* `Sergio Zanchetta <https://github.com/primes2h>`__
* `Giovanni Serra <giovanni@gslab.it>`__
* `Gianmarco Conte <gconte@dinamicheaziendali.it>`__
* Maintainers <False>
* ~~~~~~~~~~~ <False>
* This module is maintained by the OCA. <False>
* .. image:: https://odoo-community.org/logo.png <False>
* :alt: Odoo Community Association <False>
* :target: https://odoo-community.org <False>
* OCA, or the Odoo Community Association, is a nonprofit organization whose <False>
* mission is to support the collaborative development of Odoo features and <False>
* promote its widespread use. <False>
* `This module is part of the OCA/l10n-italy <https://github.com/OCA/l10n-italy/tree/12.0/l10n_it_fatturapa_in>`__
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
