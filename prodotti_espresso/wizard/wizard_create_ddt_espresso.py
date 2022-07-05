# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#

from odoo import _, api, fields, models


class WizardCreateDdtEspresso(models.TransientModel):
    _name = "wizard.create.ddt.espresso"

    def create_ddt_espresso(self):
        self.env["sale.order"].generate_ddt_espresso()
