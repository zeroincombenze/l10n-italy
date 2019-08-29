# -*- coding: utf-8 -*-
#
#    Copyright (C) 2014 Abstract (http://www.abstract.it)
#    @author Davide Corio <davide.corio@abstract.it>
#    Copyright (C) 2014-2017 Agile Business Group (http://www.agilebg.com)
#    Copyright (C) 2015 Apulia Software s.r.l. (http://www.apuliasoftware.it)
#    @author Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
#
#    License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
{
    'name': 'DDT',
    'summary': 'Delivery Document to Transfer',
    'version': '10.0.1.5.5',
    'category': 'Localization/Italy',
    'author': 'Odoo Community Association (OCA) and other subjects',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/',
    'license': 'AGPL-3',
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
        'views/stock_picking.xml',
        'views/partner.xml',
        'views/product.xml',
        'views/account.xml',
        'views/sale.xml',
        'views/stock_location.xml',
        'wizard/add_picking_to_ddt.xml',
        'wizard/ddt_from_picking.xml',
        'wizard/ddt_create_invoice.xml',
        'wizard/ddt_invoicing.xml',
        'views/report_ddt.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True,
}
