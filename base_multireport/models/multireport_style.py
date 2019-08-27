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
         ('odoo_based', 'Odoo based Model')],
        'Report origin/indentity',
        required=True,
        help="Original report",
        default='odoo')
    # default values
    template_sale_order = fields.Many2one(
        'multireport.template', 'Sale order template',
        help="Sale order model",)
        # default=lambda self: self.env.ref('base_multireport.mr_t_odoo'))
    model_sale_order_id = fields.Many2one(
        'multireport.model', 'Odoo sale order model default',
        # domain=lambda self: [('model_id', '=', self.env.ref('sale.model_sale_order').id)],
    )
    header_mode = fields.Selection(
        [('standard', 'Full Standard'),
         ('logo', 'Only logo'),
         ('no_header', 'No print Header'),
         ],
        'Header Print Mode',
        help="Which content is printed in document",
        required=True,
        default='standard')
    # sale.order values
    header_mode_sale_order = fields.Selection(
        [('', 'From default style'),
         ('standard', 'Full Standard'),
         ('logo', 'Only logo'),
         ('no_header', 'No print Header'),
         ],
        'Header Print Mode',
        help="Which content is printed in document")
    # stock.picking[.package.preparation] values
    header_mode_stock_picking_package_preparation = fields.Selection(
        [('', 'From default style'),
         ('standard', 'Full Standard'),
         ('logo', 'Only logo'),
         ('no_header', 'No print Header'),
         ],
        'Header Print Mode',
        help="Which content is printed in document")
    # account.invoice values
    header_mode_account_invoice = fields.Selection(
        [('', 'From default style'),
         ('standard', 'Full Standard'),
         ('logo', 'Only logo'),
         ('no_header', 'No print Header'),
         ],
        'Header Print Mode',
        help="Which content is printed in document")
    # purchase.order values
    header_mode_purchase_order = fields.Selection(
        [('', 'From default style'),
         ('standard', 'Full Standard'),
         ('logo', 'Only logo'),
         ('no_header', 'No print Header'),
         ],
        'Header Print Mode',
        help="Which content is printed in document")
    # other values
    template_stock_picking_package_preparation = fields.Many2one(
        'multireport.template', 'Delivery document template',
        help="Delivery document model",)
        # default=lambda self: self.env.ref('base_multireport.mr_t_odoo'))
    template_purchase_order = fields.Many2one(
        'multireport.template', 'Purchase order template',
        help="Purchase order model",)
        # default=lambda self: self.env.ref('base_multireport.mr_t_odoo'))
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
    description_mode_sale_order = fields.Selection(
        related='template_sale_order.description_mode',
        readony=True)
    description_mode_stock_picking_package_preparation = fields.Selection(
        related='template_sale_order.description_mode',
        readony=True)
    description_mode_account_invoice = fields.Selection(
        [('', 'From default style'),
         ('as_is', 'As is'),
         ('line1', 'Only first line'),
         ('nocode', 'No code'),
         ('nocode1', 'No code & Only first line'),
         ],
        'Description line print',
        help="Which content is printed in document",
    )
    # FIELD TEMPLATE
    # description_mode_purchase_order = fields.Selection(
    #     related='model_purchase_order_id.description_mode',
    #    readony=True)
    code_mode_sale_order = fields.Selection(
        related='template_sale_order.code_mode',
        readony=True)
    code_mode_stock_picking_package_preparation = fields.Selection(
        related='template_sale_order.code_mode',
        readony=True)
    code_mode_account_invoice = fields.Selection(
        [('', 'From default style'),
         ('noprint', 'No print'),
         ('print', 'Print'),
         ],
        'Print code in document line',
        help="If you choice to print, set description to <nocode>",
    )
    code_mode_purchase_order = fields.Selection(
        related='template_sale_order.code_mode',
        readony=True)
    code_mode = fields.Selection(
        [('noprint', 'No print'),
         ('print', 'Print'),
         ],
        'Print code in document line',
        help="If you choice to print, set description to <nocode>",
        default='noprint',
        required=True,
    )
    description_mode = fields.Selection(
        [('as_is', 'As is'),
         ('line1', 'Only first line'),
         ('nocode', 'No code'),
         ('nocode1', 'No code & Only first line'),
         ],
        'Description line print',
        help="Which content is printed in document",
        default='as_is',
        required=True,
    )
    payment_term_position_account_invoice = fields.Selection(
        [('', 'From default style'),
         ('odoo', 'Odoo'),
         ('auto', 'Auto'),
         ('footer', 'Footer'),
         ('header', 'Header'),
         ('none', 'None')
         ],
        'Payment term layout position',
        help='Where Payment term and due dates are printed: '
             'may be Auto, None, on Footer or on Header\n'
             'With auto, when due payment is whole in one date, '
             'all datas are printed on header otherwise \n'
             'all datas are printed on footer\n'
             'Odoo print only Payment Term notes on Footer',
    )
    payment_term_position = fields.Selection(
        [('odoo', 'Odoo'),
         ('auto', 'Auto'),
         ('footer', 'Footer'),
         ('header', 'Header'),
         ('none', 'None')
         ],
        'Payment term layout position',
        help='Where Payment term and due dates are printed: '
             'may be Auto, None, on Footer or on Header\n'
             'With auto, when due payment is whole in one date, '
             'all datas are printed on header otherwise \n'
             'all datas are printed on footer\n'
             'Odoo print only Payment Term notes on Footer',
        default='odoo',
        required=True,
    )
    footer_mode = fields.Selection(
        [('standard', 'Full Standard'),
         ('custom', 'Customized Footer'),
         ('no_footer', 'No print Footer'),
         ],
        'Footer Print Mode',
        help="Which content is printed in document",
        required=True,
        default='standard'
    )
