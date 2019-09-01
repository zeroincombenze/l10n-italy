# -*- coding: utf-8 -*-
#
# Copyright 2012    - Andrea Cometa <http://www.andreacometa.it>
# Copyright 2012    - Associazione Odoo Italia <https://www.odoo-italia.org>
# Copyright 2012-17 - Lorenzo Battistini <https://www.agilebg.com>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from openerp import fields, models


class ResPartner(models.Model):

    _name = "res.partner"
    _inherit = "res.partner"

    group_riba = fields.Boolean(
        "Group Ri.Ba.",
        help="Group Ri.Ba. by customer while issuing")
