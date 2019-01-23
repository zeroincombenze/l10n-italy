# -*- coding: utf-8 -*-
# Copyright 2016-2019 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                     Odoo Italia Associazione
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'base_rule_multireport',
    'summary': 'Manage document multiple reports',
    'version': '10.0.0.2.1',
    'category': 'Generic Modules/Accounting',
    'author': 'SHS-AV s.r.l.',
    'website': 'https://www.zeroincombenze.it/',
    'depends': ['account',
                'sale',
                'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/multireport_style.xml',
        'data/multireport_template.xml',
        'data/multireport_model.xml',
        'data/multireport_selection_rules.xml',
        'views/multireport_style_view.xml',
        'views/multireport_model_view.xml',
        'views/multireport_template_view.xml',
        'views/multireport_selection_rules_view.xml',
        'views/config_view.xml',
        'views/sale_order_view.xml',
        'report/paper_format.xml',
        'report/header-footer.xml',
        'report/header-footer_vg7.xml',
        'report/multireport_sale_order.xml',
        'report/multireport_ddt.xml',
        'report/multireport_invoice.xml',
        'report_ddt/report_ddt.xml',
        'report_sale_order/report_sale_order.xml',
        'report_sale_order/report_sale_order_vg7.xml',
        'report_account_invoice/report_invoice.xml',
    ],
    'external_dependencies': {
        'python': [
            'PyPDF2',
        ],
    },
    'installable': True,
}
