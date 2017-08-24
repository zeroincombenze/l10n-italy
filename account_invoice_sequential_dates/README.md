[![Build Status](https://travis-ci.org/zeroincombenze/account_vat_period_end_statement.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/account_vat_period_end_statement)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account_vat_period_end_statement/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/account_vat_period_end_statement?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account_vat_period_end_statement/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account_vat_period_end_statement/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/account_vat_period_end_statement/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/dev/7.0)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/l10n-italy)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)

[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

Invoice Sequential Dates
========================

This module check for sequential invoice date because Italian law.

Like OCA module, out_invoice dates are checked.
Also in_invoice registration date are checked (this function is not [yet]
implemented in OCA module).


[![it](http://www.shs-av.com/wp-content/it_IT.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

Controllo sequenza data fattura
===============================

Questo modulo controlla la sequenza delle date della fattura per onorare la
legge fiscale italiana.

Come il modulo OCA è controllata la sequenza delle date della fatture di
vendita.
Inoltre è verificata la sequenza della date di registrazione delle fatture
di acquisto (queste funzione non è [ancora] implementata nel modulo OCA).

Il controllo è effettuato sull'anno fiscale e permette la registrazione
contestuale di fatture su 2 anni fiscali diversi durante il periodo di
accavallamento degli esercizi.


Credits
=======

Contributors
------------

-   Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>


Maintainer
----------

This module is maintained by Odoo Italia Associazione

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

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
