# -*- coding: utf-8 -*-
#
# Copyright 2018-23 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#

from odoo import api, models, _
from odoo.exceptions import UserError


class WizardLineSettlement(models.TransientModel):
    _name = "wizard.line.settlement"

    @api.multi
    def line_settlement(self):
        self.ensure_one()
        move_lines = self.env[self.env.context["active_model"]].browse(
            self.env.context["active_ids"]
        )
        for move_line in move_lines:
            if not move_line.riba:
                raise UserError(_("Not all entries are C/O"))
            for riba_move_line in move_line.distinta_line_ids:
                if riba_move_line.riba_line_id.state not in ("accredited", "unsolved"):
                    raise UserError(_("Some entries is not accredited or unsolved"))
        move_lines.registra_incasso_riba()
        return {"type": "ir.actions.act_window_close"}
