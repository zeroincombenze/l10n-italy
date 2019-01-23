# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class MultireportStyle(models.Model):
    _name = "multireport.style"
    _description = "Multi Report Document Style"

    name = fields.Char(
        'Name of Style',
        required=True,
        help="Give a unique name for this report style")
    origin = fields.Selection(
        [('odoo', 'Original Odoo Model'),
         ('odoo_based', 'Odoo based Model'),
         ('vg7', 'VG7 Model')],
        'Report origin/indentity',
        required=True,
        help="Original report",
        default='odoo')
    pdf_watermark = fields.Binary(
        'Watermark PDF',
        help='Upload your company letterhead PDF to form the background '
             'of every page of your reports.')
    pdf_watermark_expression = fields.Char(
        'Watermark expression',
        help='An expression yielding the base64 '
             'encoded data to be used as watermark. \n'
             'You have access to variables `env` and `docs`')
    pdf_ending_page = fields.Binary(
        'Ending Page PDF',
        help='Here you can upload a PDF document that contain '
             'some specific content. '
             'This document will be appended to the printed report')
    pdf_watermark_sale_order = fields.Binary(
        'Sale Order Watermark PDF',
        help='Specific background for Sale Orders')
    pdf_watermark_stock_picking_package_preparation = fields.Binary(
        'Packing List Watermark PDF',
        help='Specific background for Packing List')
    pdf_watermark_account_invoice = fields.Binary(
        'Sale Invoice Watermark PDF',
        help='Specific background for Sale Invoices')
    pdf_watermark_purchase_order = fields.Binary(
        'Purchase Order Watermark PDF',
        help='Specific background for Purchase Orders')
    # TODO: in template
    custom_header = fields.Boolean('Custom Header')
    no_header_logo = fields.Boolean('No Header Logo')
    description_mode_sale_order = fields.Selection(
        [('as_is', 'As is'),
         ('line1', 'Only first line'),
         ('nocode', 'No code'),
         ('nocode1', 'No code & Only first line'),
         ],
        'Description line print',
        help="Which content is printed in document",
        default='as_is')
    description_mode_stock_picking_package_preparation = fields.Selection(
        [('as_is', 'As is'),
         ('line1', 'Only first line'),
         ('nocode', 'No code'),
         ('nocode1', 'No code & Only first line'),
         ],
        'Description line print',
        help="Which content is printed in document",
        default='as_is')
    description_mode_account_invoice = fields.Selection(
        [('as_is', 'As is'),
         ('line1', 'Only first line'),
         ('nocode', 'No code'),
         ('nocode1', 'No code & Only first line'),
         ],
        'Description line print',
        help="Which content is printed in document",
        default='as_is')
    description_mode_purchase_order = fields.Selection(
        [('as_is', 'As is'),
         ('line1', 'Only first line'),
         ('nocode', 'No code'),
         ('nocode1', 'No code & Only first line'),
         ],
        'Description line print',
        help="Which content is printed in document",
        default='as_is')
    header_sale_order = fields.Selection(
        [('standard', 'Full Standard'),
         ('logo', 'Only logo'),
         ('no_header', 'No print Header'),
         ],
        'Heaser Print Mode',
        help="Which content is printed in document",
        default='standard')
    header_stock_picking_package_preparation = fields.Selection(
        [('standard', 'Full Standard'),
         ('logo', 'Only logo'),
         ('no_header', 'No print Header'),
         ],
        'Heaser Print Mode',
        help="Which content is printed in document",
        default='standard')
    header_account_invoice = fields.Selection(
        [('standard', 'Full Standard'),
         ('logo', 'Only logo'),
         ('no_header', 'No print Header'),
         ],
        'Heaser Print Mode',
        help="Which content is printed in document",
        default='standard')
    header_purchase_order = fields.Selection(
        [('standard', 'Full Standard'),
         ('logo', 'Only logo'),
         ('no_header', 'No print Header'),
         ],
        'Heaser Print Mode',
        help="Which content is printed in document",
        default='standard')
