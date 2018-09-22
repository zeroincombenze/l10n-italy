[![Build Status](https://travis-ci.org/zeroincombenze/tools.svg?branch=9.0)](https://travis-ci.org/zeroincombenze/tools)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/tools/badge.svg?branch=9.0)](https://coveralls.io/github/zeroincombenze/tools?branch=9.0)
[![codecov](https://codecov.io/gh/zeroincombenze/tools/branch/9.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/tools/branch/9.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-9.svg)](https://github.com/OCA/tools/tree/9.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-9.svg)](http://wiki.zeroincombenze.org/en/Odoo/9.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-9.svg)](http://wiki.zeroincombenze.org/en/Odoo/9.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-9.svg)](https://erp9.zeroincombenze.it)


[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License

Italian Localization - FatturaPA
================================

Base module to handle FatturaPA data.
http://fatturapa.gov.it

See l10n_it_fatturapa_out and l10n_it_fatturapa_in.


Installation
------------

This module requires PyXB 1.2.4
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
