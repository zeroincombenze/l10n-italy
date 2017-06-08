# -*- coding: utf-8 -*-
#    Copyright (C) 2011-12 Domsense s.r.l. <http://www.domsense.com>.
#    Copyright (C) 2012-15 Agile Business Group sagl <http://www.agilebg.com>
#    Copyright (C) 2012-15 LinkIt Spa <http://http://www.linkgroup.it>
#    Copyright (C) 2015-17 Associazione Odoo Italia
#                          <http://www.odoo-italia.org>
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2011: domsense] First version
# [2012: agilebg] Various enhancements
# [2013: openerp-italia] Various enhancements
# [2017: odoo-italia] Electronic VAT statement
{
    "name": "Period End VAT Statement",
    "version": "8.0.3.0.1",
    'category': 'Generic Modules/Accounting',
    'license': 'AGPL-3',
    "depends": [
        "l10n_it_account",
        "account_voucher",
        "report",
        "l10n_it_vat_registries",
        "l10n_it_fiscalcode",
    ],
    "author": "Agile Business Group, Odoo Italia Associazione,"
              " Odoo Community Association (OCA)",
    'website': 'https://odoo-italia.org',
    'data': [
        'wizard/add_period.xml',
        'wizard/remove_period.xml',
        'statement_workflow.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'reports.xml',
        'views/report_vatperiodendstatement.xml',
        'views/config.xml',
        'views/account_view.xml',
    ],
    'installable': True,
}
