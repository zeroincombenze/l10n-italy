|Maturity| |Build Status| |license gpl| |Coverage Status| |Codecov Status| |OCA project| |Tech Doc| |Help| |Try Me|

|en|

============================
Odoo 10.0 (formerly OpenERP)
============================

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an Open Source CRM and Enterprise Resource Planning. The main ERP modules are: Warehouse Management, Project Management, Billing AND Accounting, Point of Sale, Human Resources, Manufacturing, Purchase Management, Sale Management and other modules.


|it|

=======================
Odoo 10.0 (già OpenERP)
=======================

Odoo è una suite di prodotti web open-source.

Le principali applicazioni di Odoo includono un Open Source CRM e Enterprise Resource Planning. I principali moduli ERP sono: gestione Magazzino, gestione Progetti, Contabilità e Fatturazione, Punto vendite, Dipendenti, Produzione, gestione Acquisti, gestione vendite e molto altro ancora.



Distributions / Distribuzioni Odoo 10.0:
========================================



+-------------+----------------------------------+------------------------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------+
| name / nome | description / descrizione        | Italy / Localizzazione Italiana    | Maintainers                                                  | License / Licenza                                                                  |
+-------------+----------------------------------+------------------------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------+
|             | Odoo EE - Enterprise Edition     | |check| Tramite partner        (1) | `Odoo S.A. <https://www.odoo.com/>`__                        | `OPL <https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html>`__ |
+-------------+----------------------------------+------------------------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------+
| odoo        | Odoo CE - Community Edition      | |no_check|                         | `Odoo S.A. <https://www.odoo.com/>`__                        | |license gpl|                                                                      |
+-------------+----------------------------------+------------------------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------+
| oca         | Odoo CE by OCA                   | |warning| Norme fiscali < 2107 (2) | `Odoo Community Association <http://odoo-community.org/>`__  | |license gpl|                                                                      |
+-------------+----------------------------------+------------------------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------+
| oia         | Odoo CE by OIA                   | |warning| Norme fiscali < 2107 (3) | `Associazione Odoo Italia <https://www.odoo-italia.org/>`__  | |license gpl|                                                                      |
+-------------+----------------------------------+------------------------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------+
| zero        | Zeroincombenze(R)                | |warning| Norme fiscali < 2107 (3) | `SHS-AV s.r.l. <http://www.shs-av.com/>`__                   | |license gpl|                                                                      |
+-------------+----------------------------------+------------------------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------+

Notes / Note:
-------------

1. Localizzazione con supporto a pagamento tramite partner
2. Manca software per norme fiscali 2017; OCA sta sviluppando il supporto per la Fattura Elettronica B2B
3. Software per Fattura elettronica B2B in sviluppo



OCA Differences / Differenze da OCA
------------------------------------

+--------------------------------------+------------------+-----------------+-----------------------------------------------------------------------------+
| Description / Descrizione            | Odoo Italia      | OCA             | Notes / Note                                                                |
+--------------------------------------+------------------+-----------------+-----------------------------------------------------------------------------+
| Ricerca per CAP, città e provincia   | |check|          | |no_check|      |                                                                             |
+--------------------------------------+------------------+-----------------+-----------------------------------------------------------------------------+
| Dati comuni/province italiane        | 2014             | 2013            |                                                                             |
+--------------------------------------+------------------+-----------------+-----------------------------------------------------------------------------+
| Piano dei conti evoluto              | |check|          | |no_check|      |                                                                             |
+--------------------------------------+------------------+-----------------+-----------------------------------------------------------------------------+
| Codici IVA completi                  | |check|          | |no_check|      |                                                                             |
+--------------------------------------+------------------+-----------------+-----------------------------------------------------------------------------+
| Validazione Codice Fiscale           | |check|          | |no_check|      |                                                                             |
+--------------------------------------+------------------+-----------------+-----------------------------------------------------------------------------+



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
| **/opt/odoo/10.0**                                                         |
+----------------------------------------------------------------------------+

|

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository OCB -b 10.0 -O zero
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 10.0 -vsy -o /opt/odoo/10.0

Upgrade / Aggiornamento
------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| When you want upgrade and you   | Per aggiornare, se avete installato con  |
| installed using above           | le istruzioni di cui sopra:              |
| statements:                     |                                          |
+---------------------------------+------------------------------------------+

::

    cd /opt/odoo/10.0
    git pull origin 10.0
    # Adjust following statements as per your system
    sudo systemctl restart odoo




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
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/OCB.svg?branch=10.0
    :target: https://travis-ci.org/zeroincombenze/OCB
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/OCB/badge.svg?branch=10.0
    :target: https://coveralls.io/github/zeroincombenze/OCB?branch=10.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/OCB/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/OCB/branch/10.0
    :alt: Codecov
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg
    :target: https://github.com/OCA/OCB/tree/10.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/10.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/10.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
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

