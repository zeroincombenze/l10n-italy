# -*- coding: utf-8 -*-
#
# Copyright 2016-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from past.builtins import basestring
from builtins import int

from odoo import api, fields, models
from odoo.exceptions import UserError

HEADER_DEFAULT = '''
<p class="small">%(name)s</p>
<p class="small">%(street)s</p>
<p class="small">%(zip)s %(city)s (%(state_id)s)</p>
<p class="small">P.IVA: %(vat)s</p>
<p class="small">CF: %(fiscalcode)s</p>'''

FOOTER_DEFAULT = '''<ul class="list-inline">
    <li>Telefono: %(phone)s</li>
    <li>&bull;</li>
    <li>Fax: %(fax)s</li>
    <li>&bull;</li>
    <li>Email: %(email)s</li>
    <li>&bull;</li>
    <li>Sito web: %(website)s</li>
    <li>&bull;</li>
    <li>Partita IVA: %(vat)s</li>
    <li>&bull;</li>
    <li>Codice destinatario: %(codice_destinatario)s</li>
    <li>&bull;</li>
    <li>IBAN: %(banks)s</li>
</ul>'''


class WizardBuildReport(models.TransientModel):
    _name = "wizard.build.report"
    _description = "Create or update a report"

    make_custom_header = fields.Boolean('Write customized header',
                                        default=False)
    default_body_header = fields.Boolean('Set default body header',
                                         default=False)
    make_custom_footer = fields.Boolean('Write customized footer',
                                        default=False)

    def build_report(self, ctx=None):
        ctx = ctx or {}
        cls = self.env[ctx['active_model']]
        rec_id = ctx['active_id']
        wizard = self
        self = cls.browse(rec_id)
        if wizard.make_custom_header:
            self.custom_header = HEADER_DEFAULT
            self.header_mode = 'line-up5'
        elif self.header_mode == 'line-up5':
            self.footer_mode = 'standard' if ctx[
                'active_model'] == 'multireport.style' else ''
        if wizard.make_custom_footer:
            self.custom_footer = FOOTER_DEFAULT
            self.footer_mode = 'custom'
        elif self.footer_mode == 'custom':
            self.footer_mode = 'standard' if ctx[
                'active_model'] == 'multireport.style' else ''
        if wizard.default_body_header:
            model = False
            if ctx['active_model'] == 'multireport.template':
                if self.ir_model_id:
                    model = self.ir_model_id.model
        return

