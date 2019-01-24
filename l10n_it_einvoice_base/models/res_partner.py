# -*- coding: utf-8 -*-
#
# Copyright 2014    - Davide Corio <davide.corio@lsweb.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm
from openerp.tools.translate import _


class AccountFiscalPosition(orm.Model):
    _inherit = 'account.fiscal.position'

    _columns = {
        'regime_fiscale': fields.many2one(
            'fatturapa.fiscal_position', string='Regime Fiscale'),
    }


class ResPartner(orm.Model):
    _inherit = "res.partner"

    _columns = {
        # 1.2.6 RiferimentoAmministrazione
        'pa_partner_code': fields.char('PA Code for Partner', size=20),
        # 1.2.1.4
        'register': fields.char('Professional Register', size=60),
        # 1.2.1.5
        'register_province': fields.many2one(
            'res.country.state', string='Register Province'),
        # 1.2.1.6
        'register_code': fields.char('Register Registration Number', size=60),
        # 1.2.1.7
        'register_regdate': fields.date('Register Registration Date'),
        # 1.2.1.8
        'register_fiscalpos': fields.many2one(
            'fatturapa.fiscal_position',
            string="Register Fiscal Position"),
        # 1.1.6
        'pec_destinatario': fields.char(
            "Addressee PEC",
            help="PEC to which the electronic invoice will be sent. "
                 "Must be filled "
                 "ONLY when the information element "
                 "<CodiceDestinatario> is '0000000'")
    }

    def _check_ftpa_partner_data(self, cr, uid,
                                 name, lastname, firstname,
                                 electronic_invoice_subjected, customer,
                                 is_pa, ipa_code, company_type, 
                                 codice_destinatario, vat, fiscalcode,
                                 zip, street, city, country_id, context=None):
        if electronic_invoice_subjected and customer:
            # These checks must be done for customers only, as only
            # needed for XML generation
            if is_pa and (
                not ipa_code or len(ipa_code) != 6
            ):
                raise orm.except_orm(_('Error!'),
                    _("As a Public Administration, partner %s IPA Code "
                      "must be 6 characters long."
                    ) % name)
            if company_type == 'person' and (
                not lastname or not firstname
            ):
                raise orm.except_orm(_('Error!'),
                    _("As a natural person, partner %s "
                      "must have Name and Surname."
                    ) % name)
            if not is_pa and (
                not codice_destinatario or
                len(codice_destinatario) != 7
            ):
                raise orm.except_orm(_('Error!'),
                    _("Partner %s Addressee Code "
                      "must be 7 characters long."
                    ) % name)
            if not vat and not fiscalcode:
                raise orm.except_orm(_('Error!'),
                    _("Partner %s must have VAT Number or Fiscal Code."
                    ) % name)
            if not street:
                raise orm.except_orm(_('Error!'),
                    _('Customer %s: street is needed for XML generation.'
                    ) % name)
            if not zip:
                raise orm.except_orm(_('Error!'),
                    _('Customer %s: ZIP is needed for XML generation.'
                    ) % name)
            if not city:
                raise orm.except_orm(_('Error!'),
                    _('Customer %s: city is needed for XML generation.'
                    ) % name)
            if not country_id:
                raise orm.except_orm(_('Error!'),
                    _('Customer %s: country is needed for XML'
                      ' generation.'
                    ) % name)
