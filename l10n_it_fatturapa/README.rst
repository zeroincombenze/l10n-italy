[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/l10n-italy/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](https://erp10.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

Italian Localization - FatturaPA
================================

Base module to handle FatturaPA data.
http://fatturapa.gov.it

See l10n_it_fatturapa_out and l10n_it_fatturapa_in.


Installation
------------

This module requires PyXB 1.2.5
http://pyxb.sourceforge.net/


Configuration
-------------

 * Edit the FatturaPA fields of the partners (in partner form) who will receive (send) the
   electronic invoices. IPA code is mandatory, EORI code is not.
 * Configure payment terms filling the fatturaPA fields related to payment
   terms and payment methods.
 * Configure taxes about 'Non taxable nature', 'Law reference' and 'VAT payability'
 * Configure FatturaPA data in Accounting Configuration. Note that a sequence 'fatturaPA' is already loaded by the module and selectable.

Usage
-----

Known issues / Roadmap
----------------------

Bug Tracker
-----------

Credits
-------

### Contributors

* Davide Corio <davide.corio@abstract.it>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Roberto Onnis <roberto.onnis@innoviu.com>
* Alessio Gerace <alessio.gerace@agilebg.com>

### Funders

### Maintainer

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
[Zeroincombenze® distribution of Odoo](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Users can download from [Zeroincombenze® distribution](https://github.com/zeroincombenze/OCB) and deploy on local server.

[//]: # (end copyright)





[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
