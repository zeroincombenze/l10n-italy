[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=7.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=7.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/7.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](https://odoo7.odoo-italia.org)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Odoo Italia Modules
===================

Italian modules for Odoo (formerly OpenERP) 7.0


[//]: # (addons)


Available addons
----------------
addon | version | summary
--- | --- | ---
[account_central_journal](account_central_journal/) | 3 | Account Central Journal
[account_fiscal_year_closing](account_fiscal_year_closing/) | 1.0 | Fiscal Year Closing
[account_invoice_entry_date](account_invoice_entry_date/) | 0.1 | Account Invoice entry Date
[account_vat_period_end_statement](account_vat_period_end_statement/) | 7.0.4.0.5 | Period End VAT Statement
[l10n_it_CEE_balance_generic](l10n_it_CEE_balance_generic/) | 0.1 | Italy - 4th EU Directive - Consolidation Chart of Accounts
[l10n_it_DDT_webkit](l10n_it_DDT_webkit/) | 1.0 | DDT report using Webkit Library
[l10n_it_abicab](l10n_it_abicab/) | 1.0 | Italian Localisation - Base Bank ABI/CAB codes
[l10n_it_ade](l10n_it_ade/) | 7.0.0.1.9 | Codice con le definizioni dei file xml Agenzia delle Entrate
[l10n_it_base](l10n_it_base/) | 7.0.0.2.13 | Italian Localisation - Base
[l10n_it_base_crm](l10n_it_base_crm/) | 0.1 | Italian Localisation - CRM
[l10n_it_bill_of_entry](l10n_it_bill_of_entry/) | 0.1 | Italian Localisation - Bill of Entry
[l10n_it_corrispettivi](l10n_it_corrispettivi/) | 0.1 | Italian Localisation - Corrispettivi
[l10n_it_fatturapa](l10n_it_fatturapa/) | 7.0.2.1.0 | Electronic invoices
[l10n_it_fatturapa_out](l10n_it_fatturapa_out/) | 7.0.2.0.1 | Electronic invoices emission
[l10n_it_fiscal](l10n_it_fiscal/) | 7.0.0.2.1 | Italy - Fiscal localization by zeroincombenze(R)
[l10n_it_fiscalcode](l10n_it_fiscalcode/) | 7.0.0.2.1 | Italian Localisation - Fiscal Code
[l10n_it_ipa](l10n_it_ipa/) | 7.0.1.0.0 | IPA Code (IndicePA)
[l10n_it_partially_deductible_vat](l10n_it_partially_deductible_vat/) | 0.1 | Italy - Partially Deductible VAT
[l10n_it_pec](l10n_it_pec/) | 0.1 | Pec Mail
[l10n_it_pec_messages](l10n_it_pec_messages/) | 1.0 | Pec Messages
[l10n_it_prima_nota_cassa](l10n_it_prima_nota_cassa/) | 0.1 | Italian Localisation - Prima Nota Cassa
[l10n_it_rea](l10n_it_rea/) | 0.1 | Manage fields for Economic Administrative catalogue
[l10n_it_ricevute_bancarie](l10n_it_ricevute_bancarie/) | 1.3 | Ricevute Bancarie
[l10n_it_sale](l10n_it_sale/) | 7.0.0.2.1 | Italian Localisation - Sale
[l10n_it_split_payment](l10n_it_split_payment/) | 8.0.1.0.0 | Split Payment
[l10n_it_vat_communication](l10n_it_vat_communication/) | 7.0.0.1.12 | Comunicazione periodica IVA
[l10n_it_vat_registries](l10n_it_vat_registries/) | 0.2 | Italian Localisation - VAT Registries
[l10n_it_withholding_tax](l10n_it_withholding_tax/) | 7.0.0.2.1 | Italian Localisation - Withholding tax


Unported addons
---------------
addon | version | summary
--- | --- | ---
[l10n_it_fatturapa_in](__unported__/l10n_it_fatturapa_in/) | deprecated | Electronic invoices reception
[l10n_it_fatturapa_in_notifications](__unported__/l10n_it_fatturapa_in_notifications/) | deprecated | Supplier electronic invoices notifications
[l10n_it_fatturapa_notifications](__unported__/l10n_it_fatturapa_notifications/) | deprecated | Electronic invoices notifications
[account_invoice_sequential_dates](account_invoice_sequential_dates/) | 7.0.0.1.4 (unported) | Check invoice date consistency

[//]: # (end addons)


[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Moduli Odoo Italia
==================

Differenze rispetto localizzazione ufficiale Odoo/OCA

Descrizione | Odoo Italia | OCA
--- | --- | ---
Coverage |  [![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/7.0) | [![Coverage Status](https://coveralls.io/repos/OCA/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/r/OCA/l10n-italy?branch=7.0)
Test compatibilità OCA e Odoo | :x: | [Errore import decimal precision](https://github.com/OCA/OCB/issues/629)
[l10n_it_base](https://github.com/OCA/l10n-italy/tree/7.0/l10n_it_base) | [ricerca CAP, città e provincia](https://www.zeroincombenze.it/nuova-anagrafica-per-il-software-gestionale/) | Ricerca città
[l10n_it_base](https://github.com/OCA/l10n-italy/tree/7.0/l10n_it_base) | Ricerca provincia Italia e estero (compatibile con OCA) | Ricerca provincia Italia (non compatibile con OCA)
[l10n_it_base](https://github.com/OCA/l10n-italy/tree/7.0/l10n_it_base) | [Dati comuni italiani 2014](http://www.shs-av.com/variazione-denominazione-comuni-italiani-2014/) | Dati comuni 2013
[l10n_it_fiscal](https://github.com/OCA/l10n-italy/tree/7.0/l10n_it_fiscal) | [piano dei conti evoluto](https://www.zeroincombenze.it/il-piano-dei-conti-2/) | :x:
[l10n_it_fiscal](https://github.com/OCA/l10n-italy/tree/7.0/l10n_it_fiscal) | [codici IVA completi](http://wiki.zeroincombenze.org/it/Odoo/7.0/man/codici_IVA) | :x:
[account_vat_period_end_statement](https://github.com/zeroincombenze/l10n-italy/tree/7.0/account_vat_period_end_statement) | :calendar: Normativa IP17,  presentazione della liquidazione IVA in formato xml | :x: Normativa 2016
[account_invoice_sequential_dates](https://github.com/zeroincombenze/l10n-italy/tree/7.0/account_invoice_sequential_dates) | Validazione fatture vendita e acquisti con accavallamento esercizi fiscali | Validazione fatture di vendita; no accavallamento
[l10n_it_fatturapa](l10n_it_fatturapa/)| :calendar: FatturaPA v1.2 (normativa 2017) | :x: FatturaPA v1.1 (Normativa 2016)
[l10n_it_fatturapa](l10n_it_fatturapa/)| :white_check_mark: Compatibile con Spesometro | :x: Incompatibile con Spesometro
[l10n_it_fiscalcode](l10n_it_fiscalcode/)| :white_check_mark: Controllo CF in tempo reale | :x: CF senza controllo
[l10n_it_fiscalcode](l10n_it_fiscalcode/)| :white_check_mark: Separazione cognome e nome | :x:
[l10n_it_vat_communication](l10n_it_vat_communication/) | :white_check_mark: | :x: Non disponibile

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017 Odoo Italia Associazione issues modules for Italian localization not developed by OCA
or available only with Odoo Proprietary License.
Odoo Italia Associazione distributes code under [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) or [LGPL](https://www.gnu.org/licenses/lgpl.html) free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 rilascia moduli per la localizzazione italiana non sviluppati da OCA
o disponibili solo con [Odoo Proprietary License](https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html).

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) o [LGPL](https://www.gnu.org/licenses/lgpl.html)

[//]: # (end copyright)


