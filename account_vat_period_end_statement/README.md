[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=6.1)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=6.1)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=6.1)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/6.1/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/6.1)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-6.svg)](https://github.com/OCA/l10n-italy/tree/6.1)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-6.svg)](http://wiki.zeroincombenze.org/en/Odoo/6.1/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-6.svg)](http://wiki.zeroincombenze.org/en/Odoo/6.1/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-6.svg)](http://erp6.zeroincombenze.it)

[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/6.1/man)

Period End VAT Statement
========================

This module helps to register the VAT statement of period end.

In order to load correct amount from tax code, the tax code has to be
associated to account involved in statement, through tax code form.

The 'VAT statement' object allows to specify every amount and relative account
used by the statement.
By default, amounts of debit and credit taxes are automatically loaded
from tax codes of selected periods.
Previous debit or credit is loaded from previous VAT statement, according
to its payments status.
Confirming the statement, the 'account.move' is created. If you select
a payment term, the due date(s) will be set.

The 'tax authority' tab contains information about payment(s).
You can see statement's result ('authority VAT amount') and residual
amount to pay ('Balance').
The statement can be paid like every other debit: by voucher or 'move.line'
reconciliation.

If you need to calculate interest, you can add default information in your
company data (percentage and account).


Installation
------------



Configuration
-------------



Usage
-----

-----

-----

Known issues / Roadmap
----------------------



Bug Tracker
-----------



Credits
-------




[![Odoo Italia Associazione]]



### Contributors




-   Lorenzo Battistini <lorenzo.battistini@agilebg.com>
-   Marco Marchiori <marcomarkiori@gmail.com>
-   Sergio Corato <sergiocorato@gmail.com>
-   Andrei Levin <andrei.levin@didotech.com>
-   Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>


### Funders

### Maintainer






This module is maintained by Odoo Italia Associazione

Odoo Italia is a nonprofit organization whose develops Italian Localization for
Odoo.

To contribute to this module, please visit <https://odoo-italia.org/>.



[![it](http://www.shs-av.com/wp-content/it_IT.png)](http://wiki.zeroincombenze.org/it/Odoo/6.1/man)

Liquidazione IVA periodica
==========================

Gestione liquidazione IVA periodica.

Questo modulo calcola l'IVA da pagare (o a credito) sia per i contribuenti
mensili che trimestrali.

L'utente può aggiungere l'eventuale credito/debito del periodo precedente e
calcolare gli interessi; può anche registrare l'utilizzo del credito in
compensazione.
Dal 2017 gestisce la liquidazione elettronica IP17.


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
