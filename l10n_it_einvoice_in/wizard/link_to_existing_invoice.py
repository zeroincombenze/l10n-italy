# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class WizardLinkToInvoice(models.TransientModel):
    _name = "wizard.link.to.invoice"
    _description = "Link to Bill"
    invoice_id = fields.Many2one(
        'account.invoice', string="Bill", required=True)

    @api.multi
    def link(self):
        self.ensure_one()
        active_ids = self.env.context.get('active_ids')
        if len(active_ids) != 1:
            raise UserError(_("You can select only one XML file to link."))
        self.invoice_id.fatturapa_attachment_in_id = active_ids[0]
