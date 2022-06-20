# -*- coding: utf-8 -*-
from odoo import models

# from odoo.exceptions import UserError
# from odoo.addons.l10n_it_account.tools.account_tools import encode_for_export
# from odoo.addons.l10n_it_fatturapa.bindings.fatturapa import (
#     IdFiscaleType,
#     AnagraficaType,
#     IndirizzoType
# )

SELF_INVOICE_TD = ("TD17", "TD18", "TD19")


class WizardExportFatturapa(models.TransientModel):
    _inherit = "wizard.export.fatturapa"

    def exportInvoiceXML(
        self, company, partner, parent, invoice, attach=False, context=None
    ):
        context = context or {}

        is_self_invoice = (
            True if (invoice.fiscal_document_type_id.code in SELF_INVOICE_TD) else False
        )
        rc_suppliers = invoice._get_original_suppliers()
        if rc_suppliers:
            context["rc_supplier"] = rc_suppliers[0]
            context[
                "invoices_fiscal_document_type_codes"
            ] = invoice.fiscal_document_type_id.code
        return super(WizardExportFatturapa, self).exportInvoiceXML(
            company, partner, parent, invoice, attach, context=context
        )
