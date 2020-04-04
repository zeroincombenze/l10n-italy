# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
{
    'name': 'DDT',
    'summary': 'Delivery Document to Transfer',
    'version': '10.0.1.8.3',
    'category': 'Localization/Italy',
    'author': 'Odoo Community Association (OCA) and other subjects',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/',
    'license': 'LGPL-3',
    'depends': [
        'sale_stock',
        'stock_account',
        'delivery',
        'stock_picking_package_preparation_line',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ddt_data.xml',
        'views/stock_picking_package_preparation.xml',
        'views/ddt_data.xml',
        'views/stock_picking.xml',
        'views/partner.xml',
        'views/product.xml',
        'views/account.xml',
        'views/sale.xml',
        'views/stock_location.xml',
        'views/delivery_carrier_view.xml',
        'wizard/add_picking_to_ddt.xml',
        'wizard/ddt_from_picking.xml',
        'wizard/ddt_create_invoice.xml',
        'wizard/ddt_line_create_invoice.xml',
        'wizard/ddt_invoicing.xml',
        'views/report_ddt.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True,
}

