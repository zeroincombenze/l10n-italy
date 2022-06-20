# -*- coding: utf-8 -*-
from odoo import models, _
# from odoo.exceptions import UserError
# from odoo.addons.l10n_it_account.tools.account_tools import encode_for_export
# from odoo.addons.l10n_it_fatturapa.bindings.fatturapa import (
#     IdFiscaleType,
#     AnagraficaType,
#     IndirizzoType
# )

SELF_INVOICE_TD = ('TD17', 'TD18', 'TD19')

class WizardExportFatturapa(models.TransientModel):
    _inherit = "wizard.export.fatturapa"


    def exportInvoiceXML(
            self, company, partner, parent, invoice, attach=False, context=None):
        context = context or {}

        is_self_invoice = True if (
            invoice.fiscal_document_type_id.code in SELF_INVOICE_TD) else False
