|Maturity| |Build Status| |license gpl| |Coverage Status| |Codecov Status| |OCA project| |Tech Doc| |Help| |Try Me|

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/7.0/multibase_plus/static/src/img/icon.png

=====================
|icon| multibase_plus
=====================

.. contents::


|en|

Odoo Features Plus
===================

Table of features available on all Odoo versions:

+-----------------------------------+-------+-------+-------+-------+-------+-------+
| Features                          |  6.1  |  7.0  |  8.0  |  9.0  | 10.0  | 11.0  |
+-----------------------------------+-------+-------+-------+-------+-------+-------+
| Customer ref in Sale Order tree   |   no  |   no  |   no  |   no  |  YES  |   no  |
+-----------------------------------+-------+-------+-------+-------+-------+-------+
| Refund (credit note) invoice menu |       |       |       |       |  YES  |       |
+-----------------------------------+-------+-------+-------+-------+-------+-------+
| Invoice group by company          |   no  |   no  |   no  |  YES  |  YES  |   no  |
+-----------------------------------+-------+-------+-------+-------+-------+-------+




|it|

Caratteristiche Aggiuntive per Odoo
====================================

Caratteristiche disponibili per ogni versione:

+-----------------------------------------+-------+-------+-------+-------+-------+-------+
| Caratteristiche                         |  6.1  |  7.0  |  8.0  |  9.0  | 10.0  | 11.0  |
+-----------------------------------------+-------+-------+-------+-------+-------+-------+
| Rif. cliente in vista Ordini di vendita |   no  |   no  |   no  |   no  |  YES  |   no  |
+-----------------------------------------+-------+-------+-------+-------+-------+-------+
| Note Credito in menù fatturazione       |       |       |       |       |  YES  |       |
+-----------------------------------------+-------+-------+-------+-------+-------+-------+
| Raggruppamento fatture per Azienda      |   no  |   no  |   no  |  YES  |  YES  |   no  |
+-----------------------------------------+-------+-------+-------+-------+-------+-------+




|en|


Installation
=============

These instruction are just an example to remember what you have to do.
Installation is based on `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__
Deployment is ODOO_DIR/REPOSITORY_DIR/MODULE_DIR where:

| ODOO_DIR is root Odoo directory, i.e. /opt/odoo/7.0
| REPOSITORY_DIR is downloaded git repository directory, currently is: l10n-italy
| MODULE_DIR is module directory, currently is: multibase_plus
| MYDB is the database name
|

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 7.0 -O zero


From UI: go to:

* Setting > Modules > Update Modules List
* Setting > Local Modules > Select multibase_plus > Install

Warning: if your Odoo instance crashes, you can do following instruction
to recover installation:

``run_odoo_debug 7.0 -um multibase_plus -s -d MYDB``







|it| Known issues / Roadmap
============================

None Known





Issue Tracker
==============

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.


Proposals for enhancement
--------------------------

If you have a proposal to change this module, you may want to send an email to
<moderatore@odoo-italia.org> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.




Credits
========

Authors
--------

* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


Contributors
-------------

* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>


Funders
--------

The development of this module has been financially supported by:

* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


Maintainers
------------

|Odoo Italia Associazione|

This module is maintained by the Odoo Italia Associazione.

To contribute to this module, please visit https://odoo-italia.org/.




----------------

**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP)

**OCA**, or the `Odoo Community Association <http://odoo-community.org/>`__,
is a nonprofit organization whose mission is to support
the collaborative development of Odoo features and promote its widespread use.

**zeroincombenze®** is a trademark of `SHS-AV s.r.l. <http://www.shs-av.com/>`__
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <http://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed for Italian law and markeplace.

Users can download from `Zeroincombenze® distribution <https://github.com/zeroincombenze/OCB>`__
and deploy on local server.



.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0
    :alt: Codecov
.. |OCA project| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg
    :target: https://github.com/OCA/l10n-italy/tree/7.0
    :alt: OCA
.. |Tech Doc| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg
    :target: http://wiki.zeroincombenze.org/en/Odoo/7.0/dev
    :alt: Technical Documentation
.. |Help| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg
    :target: http://wiki.zeroincombenze.org/it/Odoo/7.0/man
    :alt: Technical Documentation
.. |Try Me| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg
    :target: https://erp7.zeroincombenze.it
    :alt: Try Me
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/


