# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class MultireportModel(models.Model):
    _name = "multireport.model"
    _description = "Multi Report Default Model Values"

    name = fields.Char(
        'Name of model',
        required=True,
        help="Give a unique name for this report model")
    model_id = fields.Many2one(
        'ir.model',
        string='Odoo Model (change only)',
        help="Model to which this values will be applied")
    header_mode = fields.Selection(
        [('', 'From style'),
         ('standard', 'Full Odoo Standard'),
         ('logo', 'Only wide logo'),
         ('only_logo', 'Only wide logo / no sep. line'),
         ('line-up', 'Line-up logo / slogan'),
         ('line-up2', 'Line-up logo / slogan / no sep. line'),
         ('line-up3', 'Line-up: logo / company data'),
         ('lin3-up4', 'Line-up: logo / company data / no sep. line'),
         ('line-up5', 'Line-up: logo / custom_header'),
         ('lin3-up6', 'Line-up: logo / custom header / no sep. line'),
         ('no_header', 'No print Header'),
         ],
        'Header Print Mode',
        help="Which content is printed in document header",
    )
    payment_term_position = fields.Selection(
        [('', 'From default style'),
         ('odoo', 'Odoo'),
         ('auto', 'Auto'),
         ('footer', 'On Footer'),
         ('header', 'On Header'),
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
        [('', 'From default style'),
         ('standard', 'Odoo Standard'),
         ('auto', 'Automatic Footer'),
         ('custom', 'Customized Footer'),
         ('no_footer', 'No print Footer'),
         ],
        'Footer Print Mode',
        help='Which content is printed in document footer\n'
             'If "standard", footer is printed as "auto" or "custom"\n'
             'based on company.custom_footer field (Odoo standaed behavior)\n'
             'If "auto", footer is printed with automatic data\n'
             'If "custom", footer is printed from user data written\n',
    )
    custom_header = fields.Html(
        'Html custon headet')
