# -*- coding: utf-8 -*-
#    Copyright (C) 2014-2018 Associazione Odoo Italia (<http://www.odoo-italia.org>)
#    Copyright (C) 2016      Andrea Gallina (Apulia Software)
#    Copyright (C) 2018      Antonio Vigliotti <https://www.zeroincombenze.it>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)
try:
    import codicefiscale
except ImportError as err:
    _logger.debug(err)


SPLIT_MODE = [('LF', 'Last/First'),
              ('FL', 'First/Last'),
              ('LFM', 'Last/First Middle'),
              ('L2F', 'Last last/First'),
              ('L2FM', 'Last last/First Middle'),
              ('FML', 'First middle/Last'),
              ('FL2', 'First/Last last'),
              ('FML2', 'First Middle/Last last')]


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _commercial_fields(self):
        res = super(ResPartner, self)._commercial_fields()
        res += ['fiscalcode']
        return res

    @api.multi
    def check_fiscalcode(self):
        for partner in self:
            if not partner.fiscalcode:
                return True
            elif len(partner.fiscalcode) != 16 and partner.individual:
                return False
            else:
                return True

    fiscalcode = fields.Char(
        'Fiscal Code', size=16, help="Italian Fiscal Code")
    splitmode = fields.Selection(SPLIT_MODE,
                                 'First Last format',
                                 default='LF')
    # firstname = fields.Char('First Name',
    #                         compute='_split_first_name',
    #                         store=True,
    #                         readonly=True)
    # lastname = fields.Char('Last Name',
    #                        compute='_split_last_name',
    #                        store=True,
    #                        readonly=True)
    split_next = fields.Boolean(
        'Change format name',
        default=False,
        help="Check for change first/last name format")

    _constraints = [
        (check_fiscalcode,
         "The fiscal code doesn't seem to be correct.", ["fiscalcode"])
    ]


    @api.onchange('fiscalcode')
    def onchange_fiscalcode(self):
        name = 'fiscalcode'
        if self.fiscalcode:
            if self.country_id and self.country_id.code != 'IT':
                return
            elif len(self.fiscalcode) == 11:
                res_partner_model = self.env['res.partner']
                chk = res_partner_model.simple_vat_check('it', self.fiscalcode)
                if not chk:
                    return {'value': {name: False},
                            'warning': {
                        'title': 'Invalid fiscalcode!',
                        'message': 'Invalid vat number'}
                    }
                self.company_type = 'Individual'
            elif len(self.fiscalcode) != 16:
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid len!',
                    'message': 'Fiscal code len must be 11 or 16'}
                }
            else:
                self.fiscalcode = self.fiscalcode.upper()
                chk = codicefiscale.control_code(self.fiscalcode[0:15])
                if chk != self.fiscalcode[15]:
                    value = self.fiscalcode[0:15] + chk
                    return {'value': {name: value},
                            'warning': {
                                'title': 'Invalid fiscalcode!',
                                'message': 'Fiscal code could be %s' % (value)}
                            }
                self.company_type = 'Individual'
