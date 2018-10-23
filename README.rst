|Maturity| |Build Status| |license gpl| |Coverage Status| |Codecov Status| |OCA project| |Tech Doc| |Help| |Try Me|

============================
Odoo 11.0 (formerly OpenERP)
============================

.. contents::

|en|



|it|


Avaiable Addons / Moduli disponibili
-------------------------------------

+-----------------------------+------------+------------+----------------------------------------------------+
| Name / Nome                 | Version    | OCA Ver.   | Description / Descrizione                          |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_einvoice_out        | 11.0.1.0.0 | |no_check| | Electronic invoices emission                       |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_vat_communication   | 11.0.0.1.1 | |no_check| | Comunicazione periodica IVA                        |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_ade                 | 11.0.0.1.1 | |no_check| | Codice con le definizioni dei file xml Agenzia del |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscalcode          | 11.0.1.0.2 | |no_check| | Italian Localisation - Fiscal Code                 |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscal              | 11.0.10.0. | |no_check| | Italy - Fiscal localization by Zeroincombenze(R)   |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_abicab              | 11.0.1.0.0 | |no_check| | Base Bank ABI/CAB codes                            |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscal_payment_term | 11.0.1.0.0 | |no_check| | Electronic invoices payment                        |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_rea                 | 11.0.1.0.1 | |no_check| | Manage fields for  Economic Administrative catalog |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_split_payment       | 11.0.1.0.2 | |no_check| | Split Payment                                      |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_pec                 | 11.0.1.0.0 | |no_check| | Pec Mail                                           |
+-----------------------------+------------+------------+----------------------------------------------------+
| multibase_plus              | 11.0.0.1.2 | |no_check| | Enhanced Odoo Features                             |
+-----------------------------+------------+------------+----------------------------------------------------+
| account_invoice_entry_date  | 11.0.0.1.0 | |no_check| | Account Invoice entry Date                         |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_base                | 11.0.0.1.3 | |no_check| | Italian Localisation - Base                        |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscal_ipa          | 11.0.1.1.0 | |no_check| | IPA Code and Destination Code in Partner Record    |
+-----------------------------+------------+------------+----------------------------------------------------+
| l10n_it_einvoice_base       | 11.0.2.0.1 | |no_check| | Electronic invoices                                |
+-----------------------------+------------+------------+----------------------------------------------------+



|en|


Installation / Installazione
=============================

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is based on:       | L'installazione è basata su:             |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__         |
+---------------------------------+------------------------------------------+
| Suggested deployment is         | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| **/opt/odoo/11.0/l10n-italy/**                                             |
+----------------------------------------------------------------------------+

|

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 11.0 -O zero
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 11.0 -vsy -o /opt/odoo/11.0




Maintainers / Manutezione
-------------------------

|Odoo Italia Associazione|

This module is maintained by the Odoo Italia Associazione.

To contribute to this module, please visit https://odoo-italia.org/.


----------------

**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP)

**OCA**, or the `Odoo Community Association <http://odoo-community.org/>`__,
is a nonprofit organization whose mission is to support
the collaborative development of Odoo features and promote its widespread use.

**zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed for Italian law and markeplace.

Users can download from `Zeroincombenze® distribution <https://github.com/zeroincombenze/OCB>`__
and deploy on local server.


|

Last Update / Ultimo aggiornamento: 2018-10-22

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
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-11.svg
    :target: https://github.com/OCA/l10n-italy/tree/11.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-11.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/11.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-11.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/11.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-11.svg
    :target: https://erp11.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov Status| image:: badge-oca-codecov
    :target: oca-codecov-URL
    :alt: Codecov
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
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md

