# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import codicefiscale
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def check_fiscalcode(self):
        for partner in self:
            if not partner.fiscalcode:
                continue
            elif (
                    partner.country_id
                    and partner.parent_id is False
                    and self.country_id.code == "IT"
                    and len(partner.fiscalcode) not in (11, 16)
            ):
                return False
            else:
                continue
        return True

    fiscalcode = fields.Char(
        'Fiscal Code', size=16, help="Italian Fiscal Code")

    _constraints = [
        (check_fiscalcode,
         "The fiscal code doesn't seem to be correct.", ["fiscalcode"])
    ]

    @api.onchange("fiscalcode")
    def onchange_fiscalcode(self):
        name = "fiscalcode"
        if self.fiscalcode:
            if self.country_id and self.country_id.code != "IT":
                self.individual = True
            elif len(self.fiscalcode) == 11:
                res_partner_model = self.env["res.partner"]
                chk = res_partner_model.simple_vat_check("it", self.fiscalcode)
                if not chk:
                    return {
                        "value": {name: False},
                        "warning": {
                            "title": "Invalid fiscalcode!",
                            "message": "Invalid vat number",
                        },
                    }
                self.individual = False
            elif len(self.fiscalcode) != 16:
                return {
                    "value": {name: False},
                    "warning": {
                        "title": "Invalid len!",
                        "message": "Fiscal code len must be 11 or 16",
                    },
                }
            else:
                self.individual = True
                self.fiscalcode = self.fiscalcode.upper()
                chk = codicefiscale.control_code(self.fiscalcode[0:15])
                if chk != self.fiscalcode[15]:
                    value = self.fiscalcode[0:15] + chk
                    return {
                        "value": {name: value},
                        "warning": {
                            "title": "Invalid fiscalcode!",
                            "message": "Fiscal code could be %s" % (value),
                        },
                    }
        else:
            self.individual = False
