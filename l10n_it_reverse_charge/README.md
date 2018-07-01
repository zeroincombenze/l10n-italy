[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/l10n-italy/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Reverse Charge VAT
==================

Module to handle reverse charge VAT on supplier invoices...


[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)


Reverse Charge IVA
==================

Gestione IVA in Reverse Charge.

Il modulo permette di automatizzare le registrazioni contabili derivate dalle fatture fornitori intra UE ed extra UE mediante il reverse charge IVA. Inoltre è automatizzata la procedura di annullamento e riapertura della fattura fornitore.

E' anche possibile utilizzare la modalità "con autofattura fornitore aggiuntiva". Questo tipicamente è usato per i fornitori extra UE, con lo scopo di mostrare, nel registro IVA acquisti, una fattura intestata alla propria azienda, che verrà poi totalmente riconciliata con l'autofattura attiva, sempre intestata alla propria azienda

**NOTA**: al momento è gestito solo il metodo **Autofattura** e non quello **Integrazione IVA**.


### Funzionalità & Certificati

Funzione | Status | Note
--- | --- | ---
Fattura Reverse Charge Italia | :white_check_mark: | Fatture da soggetti italiani
Fattura Reverse Charge IntraUE | :white_check_mark: | Fatture da fornitori UE
Fattura Reverse Charge ExtraUE | :white_check_mark: | Fatture da fornitori extra-UE
Cancellazione fattura | :white_check_mark: | Cancella le registrazioni collegate


Installation
------------

These instruction are just an example to remember what you have to do:
[//]: # (install)
    ODOO_DIR=/opt/odoo/10.0/l10n-italy  # here your Odoo dir
    BACKUP_DIR=/opt/odoo/backup  # here your backup dir
    # Check for <account_accountant account_cancel> modules
    cd /tmp
    git clone https://github.com/zeroincombenze/l10n-italy.git l10n-italy
    mv $ODOO_DIR/l10n-italy/l10n_it_reverse_charge/ $BACKUP_DIR/
    mv /tmp/l10n-italy/l10n_it_reverse_charge/ $ODOO_DIR/
[//]: # (end install)



Configuration
-------------

:it:

Creare l'imposta **22% intra UE** Vendita:

![](/l10n_it_reverse_charge/static/description/tax_22_v_i_ue.png)

Creare l'imposta **22% intra UE** Acquisti:

![](/l10n_it_reverse_charge/static/description/tax_22_a_i_ue.png)

> alt  
> 22% intra UE Acqisti
>
> width  
> 600 px
>
Creare l'imposta **22% extra UE** Vendita:

![](/l10n_it_reverse_charge/static/description/tax_22_v_e_ue.png)

Creare l'imposta **22% extra UE** Acquisti:

![](/l10n_it_reverse_charge/static/description/tax_22_a_e_ue.png)

> alt  
> 22% extra UE Acqisti
>
> width  
> 600 px
>
Creare il tipo reverse charge **Intra UE (autofattura)**:

![](/l10n_it_reverse_charge/static/description/rc_selfinvoice.png)

> alt  
> reverse charge con Autofattura
>
> width  
> 600 px
>
Il sezionale autofattura deve essere di tipo 'vendita'

Creare il tipo reverse charge **Extra-EU (autofattura)** :

![](/l10n_it_reverse_charge/static/description/rc_selfinvoice_extra.png)

> alt  
> reverse charge con Autofattura
>
> width  
> 600 px
>
Il 'Sezionale autofattura passiva' deve essere di tipo 'acquisto'

Il 'Conto transitorio autofattura' va configurato come segue:

![](/l10n_it_reverse_charge/static/description/temp_account_auto_inv.png)

> alt  
> conto transitorio Autofattura
>
> width  
> 600 px
>
Il 'Sezionale pagamento autofattura' deve essere configurato con il 'Conto transitorio autofattura':

![](/l10n_it_reverse_charge/static/description/sezionale_riconciliazione.png)

> alt  
> Sezionale pagamento autofattura
>
> width  
> 600 px
>
Nella posizione fiscale, impostare il tipo reverse charge

![](/l10n_it_reverse_charge/static/description/fiscal_pos_intra.png)

> alt  
> Impostazione posizioni fiscali Intra CEE
>
> width  
> 600 px
>
![](/l10n_it_reverse_charge/static/description/fiscal_pos_extra.png)

> alt  
> Impostazione posizioni fiscali Extra CEE
>
> width  
> 600 px
>


Usage
-----

For furthermore information, please visit http://wiki.zeroincombenze.org/it/Odoo/10.0/man/FI


Bug Tracker
-----------

Bugs are tracked on [GitHub Issues](https://github.com/OCA/l10n-italy/issues). In case of trouble, please check there if your issue has already been reported. If you spotted it first, help us smash it by providing detailed and welcomed feedback.

Credits
-------

### Contributors

* Davide Corio
* Alex Comba <alex.comba@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>


### Funders

This module has been financially supported by

* Agile BG <https://www.agilebg.com/>
* SHS-AV s.r.l. <https://www.zeroincombenze.it/>


### Maintainer

[![Odoo Italia Associazione](https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png)](https://odoo-italia.org)

Odoo Italia is a nonprofit organization whose develops Italian Localization for
Odoo.

To contribute to this module, please visit <https://odoo-italia.org/>.


[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be deployed on local server too.

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
