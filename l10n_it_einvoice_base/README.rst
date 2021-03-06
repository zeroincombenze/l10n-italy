
=======================================
|icon| EInvoice + FatturaPA 10.0.2.1.13
=======================================


**Infrastructure for Italian Electronic Invoice + FatturaPA**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/10.0/l10n_it_einvoice_base/static/description/icon.png

|Maturity| |Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en| EInvoice + FatturaPA
-------------------------

This module manage infrastructure to manage Italian E Invoice and FatturaPA
as per send to the SdI (Exchange System by Italian Tax Authority)

|

|it| Fattura Elettronica + FatturaPA
------------------------------------

Questo modulo gestisce l'infrastruttura per generare il file xml della Fattura 
Elettronica e della FatturaPA, versione 1.2.1, da trasmettere al sistema di interscambio SdI.

In anagrafica clienti i dati per la fattura elettronica sono inseribili nella scheda "Agenzia delle Entrate".
Le casistiche previste sono:

::

    Fattura elettronica a soggetto IVA

Si tratta della casistica più comune. Selezionare "Soggetto a fattura elettronica"
e compilare il "Codice destinatario" o la "PEC".
La partita IVA è un dato obligatorio ai fini dell'invio.
L'eventuale invio di una fattura in formato PDF è una fattura di cortesia e non
ha valore legale.

::

    Fattura elettronica a PA

Questa casistica è attiva già dal 2016. Impostare "Pubblica Amministrazione"
e compilare il "Codice ufficio".

::

    Fattura elettronica a privato senza partita IVA

La legge non prevede l'obbligo di emissione della fattura elettronica ma è
ammessa l'emissione a condizione che venga inviata una fattura in formato PDF
al cliente. Inserire il valore "0000000" nel codice destinatario
e il codice fiscale.

::

    Fattura elettronica a soggetto IVA senza Codice Destinatario ne PEC

Casistica in cui un cliente con partita IVA che non abbia fornito
ne il proprio Codice Destinatario ne la propria PEC. Si riconduce al caso
precedente, inserendo il valore "0000000" nel codice destinatario ed il
codice fiscale. Anche in questo caso è obbligatorio inviare una fattura in
formato PDF al cliente.

::

    Fattura elettronica a rappresentante fiscale in Italia

Casistica di aziende estere con rappresentanza fiscale in Italia.
Inserire nei contatti un indirizzo di fatturazione di tipo "Rappresentante fiscale"
con la partita IVA italiana ed i dati per la fatturazione elettronica.
La fattura va emessa al rappresentante fiscale.

::

    Fattura elettronica a stabile organizzazione

Casistica di aziende estere con stabile organizzazione in Italia.
Inserire nei contatti un indirizzo di fatturazione di tipo "Stabile organizzazione"
con la partita IVA italiana ed i dati per la fatturazione elettronica.
La fattura va emessa alla stabile organizzazione.

::

    Fattura elettronica a soggetto estero

Inserire il valore XXXXXXX nel codice destinatario. Il file XML viene generato
con le opportune correzione per la validazioni dell'Agenzia delle Entrate.
Anche in questo caso è obbligatorio inviare una fattura in
formato PDF al cliente.

Se il soggetto non ha ne partita IVA ne codice fiscale il campo viene compilato
con il valore di configurazione "No EU customer TIN" del menù
`Contabilità > Configurazione > Configurazione`
Il valore predefinito è "%(iso)s99999999999" che inserisce la partita IVA di 11 cifre 9
precedute dal codice ISO del cliente.
Il valore potrebbe cambiare in quanto il terzo incaricato potrebbe effettuare
controlli di validazione prima dell'invio all'Agenzia delle Entrate.

::

Configurare le imposte riguardo a "Natura non imponibile",
"Riferimento legislativo" ed "Esigibilità IVA"

Configurare i dati della fattura elettronica nella configurazione della contabilità, dove necessario

::

    Destinatari:

Il modulo è destinato a tutte le aziende che dal 2019 dovranno emettere fattura elettronica


::

    Normativa e prassi:

Le leggi inerenti la fattura elettronica sono numerose. Potete consultare la `normativa fattura elettronica <https://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm>`__

Note fiscali da circolare Agenzia delle Entrate su tipo documento fiscale:

* Il codice TD20 è utilizzabile solo per le autofatture rif. art. 6 c.8 D.Lgs 471/97 (fatture non ricevute dopo 4 mesi)
* Le autofatture in reverse charge devono avere il codice TD01


|
|

Certifications / Certificazioni
-------------------------------

+----------------------+------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| Logo                 | Ente/Certificato                                                                                     | Data inizio   | Da fine      | Note                                         |
+----------------------+------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |xml\_schema|        | `ISO + Agenzia delle Entrate <https://www.fatturapa.gov.it/export/fatturazione/it/strumenti.htm>`__  | 01-06-2017    | 31-12-2019   | Validazione contro schema xml                |
+----------------------+------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |FatturaPA|          | `FatturaPA <https://www.fatturapa.gov.it/export/fatturazione/it/index.htm>`__                        | 01-06-2017    | 31-12-2019   | Controllo tramite sito Agenzia delle Entrate |
+----------------------+------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+

|

Usage / Utilizzo
----------------

Usage / Uso
===========

|menu| Contabilità > Configurazione > Configurazione

* Posizione fiscale: impostare la posizione fiscale da inserire in fattura elettronica. Solitamente "Regime Ordinario"
* Sequenza: numeratore dei file XML
* REA Office: provincia della CCIAA dell'azienda
* REA number: numero di iscrizione dell'azienda alla CCIAA (senza sigla provincia)
* REA capital: capitale sociale, espresso in €
* REA copartner: impostare se socio unico e più soci
* REA liquidation: impostare attivo a meno che l'azienda sia in cessazione attività
* No EU customer TIN: valore da inserire come P.IVA nel file XML in caso di emissione di fatture elettroniche a clienti extra-UE, senza P.IVA
* No EU customer fc: valore da inserire come CF nel file XML in caso di emissione di fatture elettroniche a clienti extra-UE, senza P.IVA


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
* |menu| Setting > Apps |right_do| Select **l10n_it_einvoice_base** > Install


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
* |menu| Setting > Apps |right_do| Select **l10n_it_einvoice_base** > Update

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

|

Known issues / Roadmap
----------------------

|en| Please, do not mix the following module with OCA Italy modules.

This module may be conflict with some OCA modules with error:

|exclamation| name CryptoBinary used for multiple values in typeBinding


|it| Si consiglia di non mescolare i seguenti moduli con i moduli di OCA Italia.

Lo schema di definizione xml, pubblicato con
urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
in formato xml da inviare all'Agenzia delle Entrate; come conseguenza
nasce un conflitto tra moduli diversi che utilizzano uno schema che riferisce 
all'urn dell'Agenzia delle Entrate, di cui sopra, segnalato dall'errore:

|exclamation| name CryptoBinary used for multiple values in typeBinding

* This module replaces l10n_it_fatturapa of OCA distribution.
* Do not use l10n_it_base module of OCA distribution
* Do not use l10n_it_split_payment module of OCA distribution
* Do not use l10n_it_reverse_charge of OCA distribution
* Do not install l10n_it_codici_carica module of OCA distribution
* Do not install l10n_it_fiscal_document_type module of OCA distribution
* Do not install l10n_it_fiscalcode_invoice module of OCA distribution
* Do not install l10n_it_ipa module of OCA distribution
* Do not install l10n_it_esigibilita_iva of OCA distribution

Proposals for enhancement
-------------------------


|en| If you have a proposal to change this module, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare questo modulo, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.

ChangeLog History / Cronologia modifiche
----------------------------------------

10.0.2.1.13 (202\-01-12)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] 4 custom communication values / 4 Valori di configurazione per comunicazione

10.0.2.1.12 (2020-01-17)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] XML Preview / Anteprima file XML


10.0.2.1.11 (2020-01-17)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Custom communication values / Valori di configurazione per comunicazione


10.0.2.1.10 (2019-11-07)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Flag no equal FC and TIN / Indicatore no codice fiscale se eguale alla partita IVA


10.0.2.1.9 (2019-09-27)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] No EU customer TIN / Impostazione P.IVA in file XML per clienti no UE senza P.IVA


10.0.2.1.8 (2019-09-26)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Foreign customer w/o vat / I clienti esteri senza P.IVA ne CF se cod.destinatario = 'XXXXXXX'


10.0.2.1.7 (2019-06-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Create refund from invoice set wrong fiscal document type / NC da fattura generava tipo documento errato



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


* `Abstract <https://abstract.it/>`__
* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Collaboratori
----------------------------


* Davide Corio <davide.corio@abstract.it>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

Translations by / Traduzioni a cura di
--------------------------------------

* Sergio Zanchetta <https://github.com/primes2h>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

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

Last Update / Ultimo aggiornamento: 2021-01-13

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

