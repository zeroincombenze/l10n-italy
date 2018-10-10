#
# Copyright 2014    - KTec S.r.l. <http://www.ktec.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    ipa_code = fields.Char(string='IPA Code')
