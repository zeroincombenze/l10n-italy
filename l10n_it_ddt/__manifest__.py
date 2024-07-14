# -*- coding: utf-8 -*-
#
#    License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
{
    "name": "DDT",
    "version": "10.0.1.8.27",
    "category": "Localization/Italy",
    "summary": "Delivery Document Type",
    "author": ("Odoo Community Association (OCA) and other subjects,Abstract"
               ",Agile Business Group sagl,Apulia Software s.r.l.,Open Force"
               ",Dinamiche Aziendali,SHS-AV s.r.l."),
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "depends": [
        "l10n_it_ade",
        "sale_stock",
        "stock",
        "stock_account",
        "delivery",
        "stock_picking_package_preparation_line",
        "account_invoice_pricelist",
        "account_invoice_partner_carrier",
    ],
    "version_depends": ["stock_picking_package_preparation_line>=10.0.1.0.5"],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "data/ddt_data.xml",
        "views/stock_picking_package_preparation.xml",
        "views/ddt_data.xml",
        "views/stock_picking.xml",
        "views/partner_view.xml",
        "views/product.xml",
        "views/account.xml",
        "views/sale.xml",
        "views/stock_location.xml",
        "views/delivery_carrier_view.xml",
        "views/config_view.xml",
        "wizard/add_picking_to_ddt.xml",
        "wizard/ddt_from_picking.xml",
        "wizard/ddt_create_invoice.xml",
        "wizard/ddt_line_create_invoice.xml",
        "wizard/ddt_invoicing.xml",
        "wizard/create_ddt.xml",
        "views/report_ddt.xml",
        "data/mail_template_data.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
