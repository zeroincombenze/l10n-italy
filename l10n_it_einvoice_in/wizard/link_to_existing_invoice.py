# -*- coding: utf-8 -*-
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _

from odoo.addons.l10n_it_ade.bindings import fatturapa_v_1_2


class WizardLinkToInvoice(models.TransientModel):
    _name = "wizard.link.to.invoice"
    _description = "Link to Bill"

    invoice_id = fields.Many2one(
        'account.invoice', string="Bill", required=True)

    def get_invoice_obj(self, fatturapa_attachment):
        xml_string = fatturapa_attachment.get_xml_string()
        if xml_string:
            return fatturapa_v_1_2.CreateFromDocument(xml_string)
        return False


    def invoiceUpdate(
        self, invoice, fatt, fatturapa_attachment, FatturaBody, partner_id
    ):
        invoice_model = self.env['account.invoice']
        invoice_line_model = self.env['account.invoice.line']
        ftpa_doctype_model = self.env['italy.ade.invoice.type']
        rel_docs_model = self.env['fatturapa.related_document_type']
        # WelfareFundLineModel = self.env['welfare.fund.data.line']
        SalModel = self.env['faturapa.activity.progress']
        DdTModel = self.env['fatturapa.related_ddt']
        PaymentDataModel = self.env['fatturapa.payment.data']
        PaymentTermsModel = self.env['fatturapa.payment_term']
        SummaryDatasModel = self.env['faturapa.summary.data']

        invoice_data, company, partner, wt_found = invoice_model.xml_get_header_data(
            self, fatt, fatturapa_attachment, FatturaBody, partner_id)
        invoice.write(invoice_data)


    @api.multi
    def link(self):
        self.ensure_one()
        fatturapa_attachment_ids = self.env.context.get('active_ids', False)
        if len(fatturapa_attachment_ids) != 1:
            raise UserError(_("You can select only one XML file to link."))
        self.invoice_id.fatturapa_attachment_in_id = fatturapa_attachment_ids[0]
        # extract pdf if attached
        fatturapa_attachment_model = self.env['fatturapa.attachment.in']
        partner_model = self.env['res.partner']
        for fatturapa_attachment_id in fatturapa_attachment_ids:
            fatturapa_attachment = fatturapa_attachment_model.browse(
                fatturapa_attachment_id)
            fatt = self.get_invoice_obj(fatturapa_attachment)
            cedentePrestatore = fatt.FatturaElettronicaHeader.CedentePrestatore
            # 1.2
            partner_id = partner_model.getPartnerBase(cedentePrestatore,
                                                      fatturapa=self)
            generic_inconsistencies = ''
            if self.env.context.get('inconsistencies'):
                generic_inconsistencies = (
                    self.env.context['inconsistencies'] + '\n\n')
            # 2
            for FatturaBody in fatt.FatturaElettronicaBody:
                # reset inconsistencies
                self.__dict__.update(
                    self.with_context(inconsistencies='').__dict__
                )
                # Variabiles to make code quite equal to import fatturapa
                self.invoiceUpdate(
                    self.invoice_id,
                    fatt, fatturapa_attachment, FatturaBody, partner_id)
                # 2.5
                AttachmentsData = FatturaBody.Allegati
                if AttachmentsData and self.invoice_id:
                    fatturapa_attachment_model.extract_attachments(
                        AttachmentsData, self.invoice_id.id)
