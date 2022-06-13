# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import os
from datetime import datetime
import json
import requests
from odoo import fields, models, api
from odoo.addons.l10n_it_einvoice_send2sdi.models.attachment import Evolve


class ItalyAdeSender(models.Model):
    _inherit = "italy.ade.sender"

    def _compute_available(self):
        for chn in self:
            chn.avail_invoices_ctr = (
                chn.max_invoices_ctr
                - chn.used_invoices_ctr
                - chn.bonus_invoices_ctr
                - 10
            )
            if (chn.avail_invoices_ctr < 0
                    and datetime.today() < datetime(2022, 6, 26)
                    and chn.bonus_invoices_ctr == 0):
                chn.bonus_invoices_ctr = 5 - chn.avail_invoices_ctr
                chn.avail_invoices_ctr = (
                    chn.max_invoices_ctr
                    - chn.used_invoices_ctr
                    - chn.bonus_invoices_ctr
                    - 10
                )
        if chn.avail_invoices_ctr <= 0:
            chn.avail_message = (
                _("You cannot send invoices. Please buy a new invoices pack!"))
        elif chn.avail_invoices_ctr <= 20:
            chn.avail_message = _("Not many invoices!")
        else:
            chn.avail_message = ""

    max_invoices_ctr = fields.Integer(
        string="Max invoices",
        readonly=True,
        help="Total # of invoices to send or receive",
    )
    used_invoices_ctr = fields.Integer(
        string="Sent/Received invoices",
        readonly=True,
        help="Total # of invoices sent and received",
    )
    bonus_invoices_ctr = fields.Integer(
        string="# of bonus invoices",
        readonly=True,
        help="Total # of bonus invoices",
    )
    avail_invoices_ctr = fields.Integer(
        string="# of invoices available",
        readonly=True,
        compute="_compute_available",
        help="Total # of invoices you can still send or receive",
    )
    avail_message = fields.Char(
        string="Availability message",
        readonly=True,
        compute="_compute_available",
    )

    @api.multi
    def count_xml_invoice(self):
        out_invs = in_invs = 0
        if not self.sender_url:
            return out_invs, in_invs
        headers = Evolve.header(self)
        url = os.path.join(self.sender_url, "Cerca")
        chn_inv_in = int(self.param2) if self.param2 else 2
        chn_inv_out = int(self.param1) if self.param1 else 1
        # chn_inv_sent = int(self.param3) if self.param3 else 3

        data = {
            "IdAzienda": int(self.sender_company_id),
            "IdArchivio": chn_inv_in,
            "Filtri": [],
        }
        try:
            response = requests.post(
                url, headers=headers, data=json.dumps(data, ensure_ascii=False)
            )
        except BaseException:
            return out_invs, in_invs
        if not (200 <= response.status_code < 300):
            return out_invs, in_invs
        try:
            documenti = response.json()
            if documenti["EsitoChiamata"] > 0:
                return out_invs, in_invs
        except BaseException:
            return out_invs, in_invs
        in_invs = len(documenti["Documenti"])

        data = {
            "IdAzienda": int(self.sender_company_id),
            "IdArchivio": chn_inv_out,
            "Filtri": [],
        }
        try:
            response = requests.post(
                url, headers=headers, data=json.dumps(data, ensure_ascii=False)
            )
        except BaseException:
            return out_invs, in_invs
        if not (200 <= response.status_code < 300):
            return out_invs, in_invs
        try:
            documenti = response.json()
            if documenti["EsitoChiamata"] > 0:
                return out_invs, in_invs
        except BaseException:
            return out_invs, in_invs

        out_invs = len(documenti["Documenti"])

        return out_invs, in_invs
