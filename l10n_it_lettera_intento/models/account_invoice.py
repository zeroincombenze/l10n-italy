# -*- coding: utf-8 -*-
#
# Copyright 2019-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    lettera_intento = fields.Boolean(
        "Lettera di intento",
        related="fiscal_position_id.lettera_intento",
        store=True,
        readonly=True,
    )
    lettera_intento_id = fields.Many2one(
        comodel_name="italy.lettera.intento",
        string="Num. Lettera di intento",
        # domain=lambda self: [('partner_id', '=', self.partner_id.id)],
    )

    @api.model
    def set_values(self, invoice, vals):
        fiscalpos = lettera_intento = False
        if "fiscal_position_id" in vals:
            fiscalpos = self.env["account.fiscal.position"].browse(
                vals["fiscal_position_id"]
            )
        elif invoice:
            fiscalpos = invoice.fiscal_position_id
        if invoice:
            lettera_intento = invoice.lettera_intento_id
        if fiscalpos and fiscalpos.lettera_intento:
            if "lettera_intento_id" in vals or not lettera_intento:
                partner_id = (
                    vals.get("partner_id")
                    or (invoice and invoice.partner_id.id)
                    or False
                )
                if partner_id:
                    lettera_ids = self.env["italy.lettera.intento"].search(
                        [("partner_id", "=", partner_id)], order="date desc"
                    )
                    if lettera_ids:
                        vals["lettera_intento_id"] = lettera_ids[0].id
            vals["tax_stamp"] = True
            if not invoice:
                if vals.get("comment"):
                    if vals["comment"].find(fiscalpos.note) < 0:
                        vals["comment"] += "\n%s" % fiscalpos.note
                else:
                    vals["comment"] = fiscalpos.note
        return vals

    @api.model
    def create(self, vals):
        vals = self.set_values(None, vals)
        return super(AccountInvoice, self).create(vals)

    @api.multi
    def write(self, vals):
        vals = self.set_values(self, vals)
        return super(AccountInvoice, self).write(vals)
