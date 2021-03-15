# -*- coding: utf-8 -*-
#
# Copyright 2012    - Andrea Cometa <http://www.andreacometa.it>
# Copyright 2012    - Associazione Odoo Italia <https://www.odoo-italia.org>
# Copyright 2012-17 - Lorenzo Battistini <https://www.agilebg.com>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import api, models


class DistintaReportQweb(models.AbstractModel):

    _name = 'report.l10n_it_ricevute_bancarie.distinta_qweb'

    @api.multi
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        docargs = {
            'doc_ids': docids,
            'doc_model': 'riba.distinta',
            'docs': self.env['riba.distinta'].browse(docids),
        }
        return report_obj.render(
            'l10n_it_ricevute_bancarie.distinta_qweb',
            values=docargs)
