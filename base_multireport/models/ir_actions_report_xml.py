# -*- coding: utf-8 -*-
#
# Copyright 2016-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import re
from odoo import fields, models, api, _

FOOTER_DEFAULT = '''
<ul class="list-inline">
    <li>Telefono: %(phone)s</li>
    <li>&bull;</li>
    <li>Fax: %(fax)s</li>
    <li>&bull;</li>
    <li>Email: %(email)s</li>
    <li>&bull;</li>
    <li>Sito web: %(website)s</li>
</ul>'''
HELP_HEAFOO = '''You can insert html code to format the field.
You can use following macro:
%(banks)s  -> Company banks      %(codice_destinatario)s
%(city)s   -> Company city       %(fatturapa_rea_capital)s
%(email)s  -> Company email      %(fatturapa_rea_capital)s
%(fax)s    -> Company fax        %(fatturapa_rea_number)s
%(name)    -> Company name       %(fatturapa_rea_office)s
%(phone)s  -> Company phone      %(fiscalcode)s
%(street)s -> Company street     %(ipa_code)s
%(street2)s-> Company street2    %(mobile)s
%(vat)s    -> Company vat
%(website)s-> Company website
%s(zip)    -> Company zip'''


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

    header_mode = fields.Selection(
        [('', 'From template/style'),
         ('standard', 'ⓞ Full Odoo Standard'),
         ('logo', '⌘ Only wide logo'),
         ('only_logo', '⌘ Only wide logo / no sep. line'),
         ('line-up', '⌘ ⌁ Line-up logo / slogan'),
         ('line-up2', '⌘ ⌁ Line-up logo / slogan / no sep. line'),
         ('line-up3', '⌘ ┅ Line-up: logo / company data'),
         ('lin3-up4', '⌘ ┅ Line-up: logo / company data / no sep. line'),
         ('line-up5', '⌘ ☷ Line-up: logo / custom_header'),
         ('line-up6', '⌘ ☷ Line-up: logo / custom header / no sep. line'),
         ('line-up25', '☷ Two lines: logo / custom_header'),
         ('line-up26', '☷ Two lines: logo / custom header / no sep. line'),
         ('no_header', '▭ No print Header'),
         ],
        'Header Print Mode',
        help="Which content is printed in document header",
    )
    address_mode = fields.Selection(
        [('', 'From template/style'),
         ('standard', 'Standard Invoice + Shipping'),
         ('only_one', 'Only specific address'),
         ('docnum', 'Doc. number & Specific address'),
         ],
        'Address Print Mode',
        help="Which addresses are printed in document header",
    )
    logo_style = fields.Char(
        'Html logo style',
        help='Html style attribute for logo <img> tag.\n'
             'i.e. "max-height: 45px;"'
    )
    payment_term_position = fields.Selection(
        [('', 'From template/style'),
         ('odoo', 'Odoo'),
         ('auto', 'Auto'),
         ('footer', 'On Footer'),
         ('footer_no_iban', 'On Footer, no IBAN'),
         ('footer_notes', 'On Footer, only notes'),
         ('header', 'On Header'),
         ('header_no_iban', 'On Header, no IBAN'),
         ('none', 'None')
         ],
        'Payment term layout position',
        help='Where Payment term and due dates are printed:\n'
             'may be Auto, None, on Footer, on Header or None\n'
             'If "auto", when due payment is whole in one date,\n'
             'all datas are printed on header otherwise on footer\n'
             'If "Odoo" print only Payment Term notes on Footer',
    )
    footer_mode = fields.Selection(
        [('', 'From template/style'),
         ('standard', 'Odoo Standard'),
         ('auto', 'Automatic Footer'),
         ('custom', 'Customized Footer'),
         ('no_footer', 'No print Footer'),
         ],
        'Footer Print Mode',
        help='Which content is printed in document footer\n'
             'If "standard", footer is printed as "auto" or "custom"\n'
             'based on company.custom_footer field (Odoo standard behavior)\n'
             'If "auto", footer is printed with automatic data\n'
             'If "custom", footer is printed from user data written\n',
    )
    code_mode = fields.Selection(
        [('', 'From template/style'),
         ('noprint', 'No print'),
         ('print', 'Print'),
         ],
        'Print code in document line',
        help='If you choice "print", please set description mode to "nocode"',
    )
    description_mode = fields.Selection(
        [('', 'From template/style'),
         ('as_is', 'As is'),
         ('line1', 'Only first line'),
         ('nocode', 'No code'),
         ('nocode1', 'No code & Only first line'),
         ],
        'Print description in document line',
        help="Which content is printed in document line",
    )
    order_ref_text = fields.Char(
        'Text with order ref',
        help='Order reference text to print in document body.\n'
            'May be used following macroes:\n'
            '%(client_order_ref)s => Customer reference in order\n'
            '%(order_name)s => Sale order number\n'
            '%(date_order)s => Sale order date.\n'
            'i.e. "Order #: %(order_name)s - Your ref: %(client_order_ref)s"',
    )
    ddt_ref_text = fields.Char(
        'Text with delivery ref',
        help='Delivery reference text to print in document body.\n'
            'May be used following macroes:\n'
            '%(ddt_number)s => Delivery document number.\n'
            '%(date_ddt)s => Delivery document date\n'
            '%(date_done)s => Delivery date\n'
            'i.e. "Ddt #: %(ddt_number)s of %(date_ddt)s"',
    )
    pdf_watermark = fields.Binary('Watermark')
    pdf_watermark_expression = fields.Char(
        'Watermark expression',
        help='An expression yielding the base64 '
             'encoded data to be used as watermark.\n'
             'You have access to variables `env` and `docs`')
    pdf_ending_page = fields.Binary(
        'Ending Page PDF',
        help='If you want the last page of every document printed '
             'to contain some specific content such as Advertisement, '
             'your business terms and Conditions, '
             'upload a PDF with those content here and '
             'it will be appended to every document you print.')
    pdf_ending_page_expression = fields.Char(
        'Ending Page PDF expression',
        help='An expression yielding the base64 '
             'encoded data to be used as Ending Page PDF.\n'
             'You have access to variables `env` and `docs`')
    # mr_model_id = fields.Many2one(
    #     'multireport.model', 'Multi-report Model with fallback values.',
    #     # domain=lambda self: [('model_id.name', '=', self.model)],
    # )
    template = fields.Many2one(
        'multireport.template', 'Model template',
        help="Model template with fallback values.",)
    custom_header = fields.Html(
        'Html custom header',
        help=_(HELP_HEAFOO))
    bottom_text = fields.Text(
        'Bottom text',
        help='Text to print in bottom area of document'
    )
    custom_footer = fields.Html(
        'Html custom footer',
        help=_(HELP_HEAFOO),
        default=FOOTER_DEFAULT)


class View(models.Model):
    _inherit = 'ir.ui.view'

    # @api.multi
    # def name_get(self):
    #     names = []
    #     for view in self:
    #         x = re.search('t-name *= *["\'][^"\']*["\']', view.arch)
    #         if x:
    #             name = view.arch[x.start():x.end()].split('=')[1][1:-1]
    #         else:
    #             name = view.name
    #         names.append((name))
    #    return names

    @api.depends('name', 'arch')
    def _compute_display_name(self):
        for view in self:
            x = re.search('t-name *= *["\'][^"\']*["\']', view.arch)
            if x:
                name = view.arch[x.start():x.end()].split('=')[1][1:-1]
            else:
                name = view.name
            view.display_name = name
