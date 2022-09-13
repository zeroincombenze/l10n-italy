# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#

from odoo import models


class WizardCreateDdtEspresso(models.TransientModel):
    _name = "wizard.create.ddt.espresso"

    def create_ddt_espresso(self):
        orders = self.env["sale.order"]
        for sale_id in self.env.context['active_ids']:
            orders += self.env["sale.order"].browse(sale_id)
        return orders.generate_ddt_espresso()
