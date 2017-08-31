[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/l10n-italy/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)


Odoo Italia Modules
===================

Italian modules for Odoo (formerly OpenERP) 7.0


Translation Status
[![Transifex Status](https://www.transifex.com/projects/p/OCA-l10n-italy-7-0/chart/image_png)](https://www.transifex.com/projects/p/OCA-l10n-italy-7-0)



[![it](http://www.shs-av.com/wp-content/it_IT.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

Moduli Odoo Italia
==================

Differenze rispetto localizzazione ufficiale Odoo/OCA:

- Disabilitati test con repository OCA e Odoo e corretto [Errore import decimal precision](https://github.com/OCA/OCB/issues/629)
- Maggiore copertura coverage tramite unit test aggiuntive
- Il modulo [l10n_it_base](https://github.com/OCA/l10n-italy/tree/7.0/l10n_it_base) è basato su [ricerca con CAP] (https://www.zeroincombenze.it/nuova-anagrafica-per-il-software-gestionale/);
- Inoltre il campo provincia è allineato ai moduli internazionali (utilizzo del campo state_id al posto del campo personalizzato province) ma per compatibilità con i moduli della Community Italiana, agisce anche sul campo province.
- Aggiunti test yaml di validazione
- Basato su [piano dei conti](https://www.zeroincombenze.it/il-piano-dei-conti-2/) personalizzato  in [l10n-italy-supplemental](https://github.com/zeroincombenze/l10n-italy-supplemental/tree/7.0/l10n_it_fiscal)
- Basato su [codici IVA](http://wiki.zeroincombenze.org/it/Odoo/7.0/man/codici_IVA) personalizzati in [l10n-italy-supplemental](https://github.com/zeroincombenze/l10n-italy-supplemental/tree/7.0/l10n_it_fiscal)
- Classificazione [comuni italiani](http://www.shs-av.com/variazione-denominazione-comuni-italiani-2014/) aggiornata ai nuovi comuni
- Il modulo [account_vat_period_end_statement](https://github.com/zeroincombenze/l10n-italy/tree/7.0/account_vat_period_end_statement) è stato modificato per adattarlo all normativa IP17 per la presentazione della liquidazione IVA in formato xml
- il modulo [account_invoice_sequential_dates](https://github.com/zeroincombenze/l10n-italy/tree/7.0/account_invoice_sequential_dates) è stato modificato; ora gestisce la validazione delle date sia per le fatture clienti (come il modulo OCA) che per le fatture fornitori (attraverso il campo data di registrazione). Gestisce più numerazion1 durante la fase di accavallamento degli esercizi.


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


Available addons
----------------
addon | version | OCA version | summary
--- | --- | --- | ---
[account_central_journal](account_central_journal/) | 3 |  N/D  | Account Central Journal
[account_fiscal_year_closing](account_fiscal_year_closing/) | 1.0 |  N/D  | Fiscal Year Closing
[account_invoice_entry_date](account_invoice_entry_date/) | 0.1 |  N/D  | Account Invoice entry Date
[account_invoice_sequential_dates](account_invoice_sequential_dates/) | 7.0.0.1.3 |  N/D  | Check invoice date consistency
[account_vat_period_end_statement](account_vat_period_end_statement/) | 7.0.2.1.9 |  N/D  | Period End VAT Statement
[l10n_it_CEE_balance_generic](l10n_it_CEE_balance_generic/) | 0.1 |  N/D  | Italy - 4th EU Directive - Consolidation Chart of Accounts
[l10n_it_DDT_webkit](l10n_it_DDT_webkit/) | 1.0 |  N/D  | DDT report using Webkit Library
[l10n_it_abicab](l10n_it_abicab/) | 1.0 |  N/D  | Italian Localisation - Base Bank ABI/CAB codes
[l10n_it_base](l10n_it_base/) | 7.0.0.2.10 |  N/D  | Italian Localisation - Base
[l10n_it_base_crm](l10n_it_base_crm/) | 0.1 |  N/D  | Italian Localisation - CRM
[l10n_it_bill_of_entry](l10n_it_bill_of_entry/) | 0.1 |  N/D  | Italian Localisation - Bill of Entry
[l10n_it_corrispettivi](l10n_it_corrispettivi/) | 0.1 |  N/D  | Italian Localisation - Corrispettivi
[l10n_it_fiscalcode](l10n_it_fiscalcode/) | 0.1 |  N/D  | Italian Localisation - Fiscal Code
[l10n_it_ipa](l10n_it_ipa/) | 1.0 |  N/D  | IPA Code (IndicePA)
[l10n_it_partially_deductible_vat](l10n_it_partially_deductible_vat/) | 0.1 |  N/D  | Italy - Partially Deductible VAT
[l10n_it_pec](l10n_it_pec/) | 0.1 |  N/D  | Pec Mail
[l10n_it_pec_messages](l10n_it_pec_messages/) | 1.0 |  N/D  | Pec Messages
[l10n_it_prima_nota_cassa](l10n_it_prima_nota_cassa/) | 0.1 |  N/D  | Italian Localisation - Prima Nota Cassa
[l10n_it_rea](l10n_it_rea/) | 0.1 |  N/D  | Manage fields for Economic Administrative catalogue
[l10n_it_reverse_charge](l10n_it_reverse_charge/) | 7.0.0.1.0 |  N/D  | Invoice Intra CEE
[l10n_it_ricevute_bancarie](l10n_it_ricevute_bancarie/) | 1.3 |  N/D  | Ricevute Bancarie
[l10n_it_sale](l10n_it_sale/) | 0.2 |  N/D  | Italian Localisation - Sale
[l10n_it_split_payment](l10n_it_split_payment/) | 8.0.1.0.0 |  N/D  | Split Payment
[l10n_it_vat_registries](l10n_it_vat_registries/) | 0.2 |  N/D  | Italian Localisation - VAT Registries
[l10n_it_withholding_tax](l10n_it_withholding_tax/) | 0.2 |  N/D  | Italian Localisation - Withholding tax


Unported addons
---------------
addon | version | OCA version | summary
--- | --- | --- | ---
[l10n_it_fatturapa](l10n_it_fatturapa/) | 0.1 (unported) |  N/D  | Electronic invoices
[l10n_it_fatturapa_in](l10n_it_fatturapa_in/) | 7.0.0.1.0 (unported) |  N/D  | Electronic invoices reception
[l10n_it_fatturapa_in_notifications](l10n_it_fatturapa_in_notifications/) | 7.0.1.0.0 (unported) |  N/D  | Supplier electronic invoices notifications
[l10n_it_fatturapa_notifications](l10n_it_fatturapa_notifications/) | 7.0.1.0.0 (unported) |  N/D  | Electronic invoices notifications
[l10n_it_fatturapa_out](l10n_it_fatturapa_out/) | 7.0.0.1.1 (unported) |  N/D  | Electronic invoices emission

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
