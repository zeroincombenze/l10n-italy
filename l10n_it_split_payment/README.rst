|Build Status| |license lgpl| |Coverage Status| |codecov| |OCA project| |Tech Doc| |Help| |try it|

|en|

===========================
Split Payment Sale Invoices
===========================

Module to generate Split Payment accounting entries on sale invoices.

|it|

================================
Fatture clienti in split-payment
================================

Il modulo permette di emettere fatture e note credito
a clienti in regime di split-payment.
L'IVA viene calcolata e inserita in fattura ma il credito risultante
dal totale da pagare è detratto dell'IVA.

La registrazione contabile contiene le righe di storno
dell'IVA (riconciliata con il credito cliente) e la riga
di IVA in regime di split payment.

Law: http://def.finanze.it/DocTribFrontend/getAttoNormativoDetail.do?ACTION=getArticolo&id={75A4827C-3766-4ECC-9C45-00C8D6CDC552}&codiceOrdinamento=200001700000300&articolo=Articolo%2017%20ter (Articolo 17 ter)


Funzionalità, Certificati & Differenze da OCA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  =================================   ======   ====   ==========================================
  Funzione                            Status   OCA    Note
  =================================   ======   ====   ==========================================
  Fattura con split payment [IVA]_.    |ok|    |ok|   Richiede modifica report di stampa
  Nota Credito con split payment       |ok|    |ok|   Richiede modifica report di stampa
  Cancellazione fattura/NC             |ok|    |ok|   Prima occore cancellare la riconciliazione
  =================================   ======   ====   ==========================================


.. [IVA] La registrazione della fattura differisce dal modulo OCA. Vedi esempio a seguito.


Registrazione fattura con split payment

  =========================   =====   =====   =========================================
  Conto                       Dare    Avere   Note
  =========================   =====   =====   =========================================
  Crediti vs. clienti           122       .   Modulo OCA registra 100
  Conto di ricavo                 .     100
  IVA                             .      22
  Storno IVA split payment       22       .
  Crediti vs. clienti             .      22   Riga riconciliata (assente in modulo OCA)
  =========================   =====   =====   =========================================



Installation
------------

These instruction are just an example to remember what you have to do:
::

    $ ODOO\_DIR=/opt/odoo/10.0/l10n-italy # here your Odoo dir
    $ BACKUP\_DIR=/opt/odoo/backup # here your backup dir
    # Check for modules
    $ cd /tmp
    $ git clone https://github.com/zeroincombenze/l10n-italy.git l10n-italy
    $ mv $ODOO\_DIR/l10n-italy/l10n\_it\_split\_payment/ $BACKUP\_DIR/
    $ mv /tmp/l10n-italy/l10n\_it\_split\_payment/ $ODOO\_DIR/



Configuration
=============

To configure this module, you need to:

* go to Accounting, Configuration, Settings and configure 'Split Payment Write-off account' (like 'IVA n/debito sospesa SP'). Write-off account should be different from standard debit VAT, in order to separately add it in VAT statement.
* configure the fiscal position (Accounting, Configuration, Accounting, Fiscal Positions) used for split payment, setting 'Split Payment' flag. In fiscal position, map standard VAT with SP VAT, like the following:

.. figure:: static/fiscal_position.png
   :alt: Fiscal position
   :width: 600 px


-------------------------------------------------------------------------------

IVA al 22% SPL is configured like the following:


.. figure:: static/SP.png
   :alt: 22SPL
   :width: 600 px

.. figure:: static/SP2.png
   :alt: 22SPL
   :width: 600 px


Usage
-----

For furthermore information, please visit
http://wiki.zeroincombenze.org/it/Odoo/10.0/man/FI


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/l10n-italy/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.


Credits
=======

Contributors
------------

* Davide Corio <davide.corio@abstract.it>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Alessio Gerace <alessio.gerace@agilebg.com>
* Antonio Maria Vigliotti antoniomaria.vigliotti@gmail.com

Maintainer
~~~~~~~~~~

|Odoo Italia Associazione|

| Odoo Italia is a nonprofit organization whose develops Italian
Localization for
| Odoo.

To contribute to this module, please visit https://odoo-italia.org/.

--------------

**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP, formerly TinyERP)

| **OCA**, or the `Odoo Community
Association <http://odoo-community.org/>`__, is a nonprofit organization
whose
| mission is to support the collaborative development of Odoo features
and
| promote its widespread use.

| **zeroincombenze®** is a trademark of `SHS-AV
s.r.l. <http://www.shs-av.com/>`__
| which distributes and promotes **Odoo** ready-to-use on its own cloud
infrastructure.
| `Zeroincombenze®
distribution <http://wiki.zeroincombenze.org/en/Odoo>`__
| is mainly designed for Italian law and markeplace.
| Everytime, every Odoo DB and customized code can be deployed on local
server too.

|chat with us|

.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0
   :target: https://travis-ci.org/zeroincombenze/l10n-italy
.. |license lgpl| raw:: html

    <a href="https://www.gnu.org/licenses/lgpl.html"><img src="https://img.shields.io/badge/licence-LGPL--3-7379c3.svg"/></a>

.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0
   :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0
.. |codecov| raw:: html

    <a href="https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0"><img src="https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg"/></a>

.. |OCA project| raw:: html

    <a href="https://github.com/OCA/l10n-italy/tree/10.0"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg"/></a>

.. |Tech Doc| raw:: html

    <a href="http://wiki.zeroincombenze.org/en/Odoo/10.0/dev"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg"/></a>

.. |Help| raw:: html

    <a href="http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg"/></a>

.. |try it| raw:: html

    <a href="http://erp10.zeroincombenze.it"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg"/></a>

.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
.. |chat with us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
.. |ok| raw:: html

   <i class="fa fa-check-square" style="font-size:24px;color:green"></i>
.. |No| raw:: html

   <i class="fa fa-minus-circle" style="font-size:24px;color:red"></i>
.. |hand right| raw:: html

   <i class="fa fa-hand-o-right" style="font-size:12px"></i>

