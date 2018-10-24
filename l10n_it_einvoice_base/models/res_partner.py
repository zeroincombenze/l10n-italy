# -*- coding: utf-8 -*-
#
# Copyright 2014    - Davide Corio <davide.corio@lsweb.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class AccountFiscalPosition(orm.Model):
    _inherit = 'account.fiscal.position'

    regime_fiscale = fields.many2one(
        'fatturapa.fiscal_position', string='Regime Fiscale')


class ResPartner(orm.Model):
    _inherit = "res.partner"

    _columns = {
        # 1.2.6 RiferimentoAmministrazione
        'pa_partner_code': fields.char('PA Code for partner', size=20),
        # 1.2.1.4
        'register': fields.char('Professional Register', size=60),
        # 1.2.1.5
        'register_province': fields.many2one(
            'res.country.state', string='Register Province'),
        # 1.2.1.6
        'register_code': fields.char('Register Code', size=60),
        # 1.2.1.7
        'register_regdate': fields.date('Register Registration Date'),
        # 1.2.1.8
        'register_fiscalpos': fields.many2one(
            'fatturapa.fiscal_position',
            string="Register Fiscal Position"),
        # 1.1.6
        'pec_destinatario': fields.char(
            "PEC destinatario",
            help="Indirizzo PEC al quale inviare la fattura elettronica. "
                 "Da valorizzare "
                 "SOLO nei casi in cui l'elemento informativo "
                 "<CodiceDestinatario> vale '0000000'")
    }
