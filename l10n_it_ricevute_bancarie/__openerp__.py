# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#
# Copyright 2012    - Andrea Cometa <http://www.andreacometa.it>
# Copyright 2012    - Associazione Odoo Italia <https://www.odoo-italia.org>
# Copyright 2012-17 - Lorenzo Battistini <https://www.agilebg.com>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Ricevute Bancarie',
    'version': '9.0.1.3.1',
    'category': 'Accounting & Finance',
    'author': 'Odoo Community Association (OCA)',
    'website': 'https://odoo-community.org/',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'account_voucher',
        'l10n_it_fiscalcode',
        'account_due_list',
    ],
    'data': [
        'views/partner_view.xml',
        'views/configuration_view.xml',
        'riba_sequence.xml',
        'views/wizard_accreditation.xml',
        'views/wizard_unsolved.xml',
        'views/riba_view.xml',
        'views/account_view.xml',
        'views/wizard_riba_issue.xml',
        'views/wizard_riba_file_export.xml',
        'views/account_config_view.xml',
        'riba_workflow.xml',
        'views/distinta_report.xml',
        'security/ir.model.access.csv',
    ],
    'demo': ['demo/riba_demo.xml'],
    'installable': True,
}
