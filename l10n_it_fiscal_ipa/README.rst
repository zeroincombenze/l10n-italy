|Maturity| |Build Status| |license gpl| |Coverage Status| |Codecov Status| |OCA project| |Tech Doc| |Help| |Try Me|

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/11.0/l10n_it_fiscal_ipa/static/description/icon.png

==========================
|icon| IPA Code (IndicePA)
==========================

.. contents::


|en|

IPA Code
=========

This module adds IPA (IndicePA) code and Recipient Code fields to partner,
used by Italian Electronic Invoice.

http://www.indicepa.gov.it




|it|

Codice IPA (IndicePA)
======================

Questo modulo permette l'inseriento del codice IPA (IndicePA) e del Codice Destinatario
nell'anagrafica cliente.

Questi dati sono indispensabili per la gestione della Fattura Elettronica B2B e
per la FatturaPA.

http://www.indicepa.gov.it



Features / Funzioni
--------------------

+-------------------------------------------------+----------+----------------------------------------------+
| Feature / Funzione                              |  Status  | Notes / Note                                 |
+-------------------------------------------------+----------+----------------------------------------------+
| Parter: IPA Code / Codice IPA                   | |check|  | Per FatturaPA                                |
+-------------------------------------------------+----------+----------------------------------------------+
| Partner: Recipient Code / Codice Destinatario   | |check|  | EInvoice / Per Fattura Elettronica B2B       |
+-------------------------------------------------+----------+----------------------------------------------+



OCA Differences / Differenze da OCA
------------------------------------

+--------------------------------------+-------------+-------------------+--------------------------------+
| Description / Descrizione            | Odoo Italia | OCA               | Notes / Note                   |
+--------------------------------------+-------------+-------------------+--------------------------------+
| Partner view / Vista cliente         | This Module | This Module       | Different layout               |
+--------------------------------------+-------------+-------------------+--------------------------------+
| IPA Code                             | This Module | This Module       |                                |
+--------------------------------------+-------------+-------------------+--------------------------------+
| Recipient Code / Codice Destinatario | This Module | l10n_it_fatturapa | |warning| Different deployment |
+--------------------------------------+-------------+-------------------+--------------------------------+





|en|


Installation
=============

These instruction are just an example to remember what you have to do.
Installation is based on `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__
Deployment is ODOO_DIR/REPOSITORY_DIR/MODULE_DIR where:

| ODOO_DIR is root Odoo directory, i.e. /opt/odoo/11.0
| REPOSITORY_DIR is downloaded git repository directory, currently is: l10n-italy
| MODULE_DIR is module directory, currently is: l10n_it_fiscal_ipa
| MYDB is the database name
|

::

    pip install codicefiscale
    pip install unidecode
    pip install pyxb==1.2.4
    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 11.0 -O zero


From UI: go to:

|menu| Setting > Activate Developer mode 

|menu| Apps > Update Apps List

|menu| Setting > Apps |right_do| Select **l10n_it_fiscal_ipa** > Install

|warning| If your Odoo instance crashes, you can do following instruction
to recover installation status:

``run_odoo_debug 11.0 -um l10n_it_fiscal_ipa -s -d MYDB``








Known issues / Roadmap
=======================

|warning| Questo modulo rimpiazza il modulo OCA. Leggete attentamente il
paragrafo relativo alle funzionalità e differenze.





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


* `KTec S.r.l. <https://www.ktec.it/>`__
* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors
-------------


* Luigi Di Naro <luigi.dinaro@ktec.it>
* Alex Comba <alex.comba@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

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
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=11.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=11.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=11.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/11.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/11.0
    :alt: Codecov
.. |OCA project| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-11.svg
    :target: https://github.com/OCA/l10n-italy/tree/11.0
    :alt: OCA
.. |Tech Doc| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-11.svg
    :target: http://wiki.zeroincombenze.org/en/Odoo/11.0/dev
    :alt: Technical Documentation
.. |Help| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-11.svg
    :target: http://wiki.zeroincombenze.org/it/Odoo/11.0/man
    :alt: Technical Documentation
.. |Try Me| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-11.svg
    :target: https://erp11.zeroincombenze.it
    :alt: Try Me
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md
   

