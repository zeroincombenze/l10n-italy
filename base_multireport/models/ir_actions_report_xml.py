# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models, api


class IrActionsReportXml(models.Model):
    _inherit = 'ir.actions.report.xml'

    def line_model(self):
        # return '%s.line' % self.model
        return 'account.invoice.line'

    def _default_fields(self):
        fields_model = self.env['ir.model.fields']
        printable_fields = [
            'name',
            'quantity',
            'product_qty',
            'uom_id',
            'product_uos',
            'product_uom',
            'price_unit',
            'discount',
            'invoice_line_tax_ids',
            'tax_id',
            'price_subtotal',
        ]
        field_list = []
        for field_name in printable_fields:
            ids = fields_model.search([('model', '=', self.line_model()),
                                       ('name', '=', field_name)])
            if ids:
                field_list.append(ids[0].id)
        return list([(6, 0, field_list)])

    @api.model
    def _domain_fields(self):
        return [('model', '=', self.line_model())]

    # field2print_ids = fields.Many2many(
    #     comodel_name='ir.model.fields',
    #     string='Fields to print in document body',
    #     default=lambda self: self._default_fields(),
    #     domain=_domain_fields,
    # )
    code_mode = fields.Selection(
        [('noprint', 'No print'),
         ('print', 'Print'),
         ],
        'Print code in document line',
        help="If choice print, set description to <nocode>",
        default='noprint'
    )
    description_mode = fields.Selection(
        [('as_is', 'As is'),
         ('line1', 'Only first line'),
         ('nocode', 'No code'),
         ('nocode1', 'No code & Only first line'),
         ],
        'Print description in document line',
        help="Which content is printed in document line",
        default='as_is'
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
        default='odoo'
    )
    order_ref_text = fields.Char(
        'Text with order ref',
        help='Use text with tag {0} that means order.name '
            'and or {1} taht means order.client_order_ref.\n'
            'i.e. Our order {0} - Your order {1}',
        default='>Vs. Ordine: {1} - '
    )
    pdf_watermark = fields.Binary('Watermark')
    pdf_watermark_expression = fields.Char(
        'Watermark expression',
        help='An expression yielding the base64 '
             'encoded data to be used as watermark. \n'
             'You have access to variables `env` and `docs`')
    pdf_ending_page = fields.Binary(
        'Ending Page PDF',
        help='If you want the last page of every document printed '
             'to contain some specific content such as Advertisement, '
             'your business terms and Conditions, '
             'upload a PDF with those content here and '
             'it will be appended to every document you print.')
