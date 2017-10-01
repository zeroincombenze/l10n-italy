# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
#
from openerp.osv import fields, orm
from openerp.tools.translate import _
# from openerp import release
import logging
# import pdb
_logger = logging.getLogger(__name__)
try:
    from openerp.addons.l10n_it_ade.bindings.dati_fattura_v_2_0 import (
        DatiFattura,
        VersioneType,
        DatiFatturaHeaderType,
        DichiaranteType,
        CodiceFiscaleType,
        DTEType,
        CedentePrestatoreDTEType,
        IdentificativiFiscaliType,
        IdentificativiFiscaliITType,
        IdFiscaleITType,
        IdFiscaleType,
        CessionarioCommittenteDTEType,
        AltriDatiIdentificativiNoSedeType,
        AltriDatiIdentificativiNoCAPType,
        IdentificativiFiscaliNoIVAType,
        IndirizzoType,
        IndirizzoNoCAPType,
        # RettificaType,
        DatiFatturaBodyDTEType,
        DatiGeneraliType,
        DatiRiepilogoType,
        DatiIVAType,
        DTRType,
        CessionarioCommittenteDTRType,
        CedentePrestatoreDTRType,
        DatiFatturaBodyDTRType,
        DatiGeneraliDTRType,
    )
    #   ANNType)
except ImportError as err:
    _logger.debug(err)

_logger.setLevel(logging.DEBUG)

VERSIONE = 'DAT20'


class WizardVatCommunication(orm.TransientModel):
    _name = "wizard.vat.communication"

    _columns = {
        'data': fields.binary("File", readonly=True),
        'name': fields.char('Filename', 32, readonly=True),
        'state': fields.selection((
            ('create', 'create'),  # choose
            ('get', 'get'),  # get the file
        )),
    }

    _defaults = {
        'state': lambda *a: 'create',
    }

    def get_dati_fattura_header(self, cr, uid,
                                commitment_model, commitment, context=None):
        context = context or {}
        fields = commitment_model.get_xml_fattura_header(
            cr, uid, commitment, context)
        header = (DatiFatturaHeaderType())
        header.ProgressivoInvio = fields['xml_ProgressivoInvio']
        if 'xml_CodiceFiscale' in fields:
            header.Dichiarante = (DichiaranteType())
            header.Dichiarante.Carica = fields['xml_Carica']
            header.Dichiarante.CodiceFiscale = CodiceFiscaleType(
                fields['xml_CodiceFiscale'])
        return header

    def get_sede(self, cr, uid, fields, dte_dtr_id, selector, context=None):
        if selector == 'supplier' or (selector == 'company' and
                                      dte_dtr_id == 'DTE'):
            sede = (IndirizzoType())
        elif selector == 'customer' or (selector == 'company' and
                                        dte_dtr_id == 'DTR'):
            sede = (IndirizzoNoCAPType())
        else:
            raise orm.except_orm(
                _('Error!'),
                _('Internal error: invalid parter selector'))
        sede.Indirizzo = fields['xml_Indirizzo']
        sede.Comune = fields['xml_Comune']
        if 'xml_CAP' in fields:
            sede.CAP = fields['xml_CAP']
        elif selector == 'company':
            raise orm.except_orm(
                _('Error!'),
                _('Missed zip code'))
        if 'xml_Provincia' in fields and fields['xml_Nazione'] == 'IT':
            sede.Provincia = fields['xml_Provincia']
        sede.Nazione = fields['xml_Nazione']
        return sede

    def get_name(self, cr, uid, fields, dte_dtr_id, selector, context=None):
        if selector == 'supplier' or selector == 'company':
            AltriDatiIdentificativi = (AltriDatiIdentificativiNoSedeType())
        elif selector == 'customer':
            AltriDatiIdentificativi = (AltriDatiIdentificativiNoCAPType())
        else:
            raise orm.except_orm(
                _('Error!'),
                _('Internal error: invalid parter selector'))
        if 'xml_Denominazione' in fields:
            AltriDatiIdentificativi.Denominazione = fields['xml_Denominazione']
        else:
            AltriDatiIdentificativi.Nome = fields['xml_Nome']
            AltriDatiIdentificativi.Cognome = fields['xml_Cognome']
        AltriDatiIdentificativi.Sede = self.get_sede(
            cr, uid, fields, dte_dtr_id, selector, context=context)
        return AltriDatiIdentificativi

    def get_company_data(self, cr, uid,
                         commitment_model, commitment, dte_dtr_id,
                         context=None):
        fields = commitment_model.get_xml_company(
            cr, uid, commitment, dte_dtr_id, context)
        if dte_dtr_id == 'DTE':
            CedentePrestatore = (CedentePrestatoreDTEType())
            CedentePrestatore.IdentificativiFiscali = (
                IdentificativiFiscaliITType())
        elif dte_dtr_id == 'DTR':
            CedentePrestatore = (CessionarioCommittenteDTRType())
            CedentePrestatore.IdentificativiFiscali = (
                IdentificativiFiscaliType())
        else:
            raise orm.except_orm(
                _('Error!'),
                _('Internal error: invalid parter selector'))
        # Company VAT number must be present
        CedentePrestatore.IdentificativiFiscali.IdFiscaleIVA = (
            IdFiscaleITType())
        CedentePrestatore.IdentificativiFiscali.IdFiscaleIVA.\
            IdPaese = fields['xml_IdPaese']
        CedentePrestatore.IdentificativiFiscali.IdFiscaleIVA.\
            IdCodice = fields['xml_IdCodice']
        CedentePrestatore.IdentificativiFiscali.CodiceFiscale = \
            CodiceFiscaleType(fields['xml_CodiceFiscale'])
        CedentePrestatore.AltriDatiIdentificativi = \
            self.get_name(cr, uid, fields, dte_dtr_id, 'company', context)
        return CedentePrestatore

    def get_customer_data(self, cr, uid,
                          commitment_model, commitment, fields, dte_dtr_id,
                          context=None):
        partner = (CessionarioCommittenteDTEType())
        partner.IdentificativiFiscali = (IdentificativiFiscaliNoIVAType())
        if 'xml_IdPaese' in fields:
            partner.IdentificativiFiscali.IdFiscaleIVA = (IdFiscaleType())
            partner.IdentificativiFiscali.IdFiscaleIVA.\
                IdPaese = fields['xml_IdPaese']
            partner.IdentificativiFiscali.IdFiscaleIVA.\
                IdCodice = fields['xml_IdCodice']
            if fields['xml_IdPaese'] == 'IT' and 'xml_CodiceFiscale' in fields:
                partner.IdentificativiFiscali.\
                    CodiceFiscale = CodiceFiscaleType(
                        fields['xml_CodiceFiscale'])
        else:
            partner.IdentificativiFiscali.CodiceFiscale = CodiceFiscaleType(
                fields['xml_CodiceFiscale'])
        # row 44: 2.2.2   <AltriDatiIdentificativi>
        partner.AltriDatiIdentificativi = \
            self.get_name(cr, uid, fields, dte_dtr_id, 'customer', context)
        return partner

    def get_supplier_data(self, cr, uid,
                          commitment_model, commitment, fields, dte_dtr_id,
                          context=None):
        partner = (CedentePrestatoreDTRType())
        partner.IdentificativiFiscali = (IdentificativiFiscaliITType())
        if 'xml_IdPaese' in fields:
            partner.IdentificativiFiscali.IdFiscaleIVA = (IdFiscaleITType())
            partner.IdentificativiFiscali.IdFiscaleIVA.\
                IdPaese = fields['xml_IdPaese']
            partner.IdentificativiFiscali.IdFiscaleIVA.\
                IdCodice = fields['xml_IdCodice']
            if fields['xml_IdPaese'] == 'IT' and 'xml_CodiceFiscale' in fields:
                partner.IdentificativiFiscali.\
                    CodiceFiscale = CodiceFiscaleType(
                        fields['xml_CodiceFiscale'])
        else:
            partner.IdentificativiFiscali.CodiceFiscale = CodiceFiscaleType(
                fields['xml_CodiceFiscale'])
        # row 44: 2.2.2   <AltriDatiIdentificativi>
        partner.AltriDatiIdentificativi = \
            self.get_name(cr, uid, fields, dte_dtr_id, 'supplier', context)
        return partner

    def get_dte(self, cr, uid,
                commitment_model, commitment, dte_dtr_id, context=None):
        context = context or {}
        dte = (DTEType())
        partners = []
        partner_ids = commitment_model.get_partner_list(
            cr, uid, commitment, dte_dtr_id, context)
        for partner_id in partner_ids:
            fields = commitment_model.get_xml_cessionario_cedente(
                cr, uid, commitment, partner_id, dte_dtr_id, context)
            # Missed mandatory data: skip record
            if 'xml_IdPaese' not in fields and \
                    'xml_CodiceFiscale' not in fields:
                continue
            dte.CedentePrestatoreDTE = self.get_company_data(
                cr, uid, commitment_model, commitment, dte_dtr_id, context)
            # TODO: StabileOrganizzazione
            # TODO: RappresentanteFiscale
            partner = self.get_customer_data(
                cr, uid, commitment_model, commitment, fields, dte_dtr_id,
                context)
            invoices = []
            # Iterate over invoices of current partner
            invoice_ids = commitment_model.get_invoice_list(
                cr, uid, commitment, partner_id, dte_dtr_id, context)
            for invoice_id in invoice_ids:
                fields = commitment_model.get_xml_invoice(
                    cr, uid, commitment, invoice_id, dte_dtr_id, context)
                invoice = (DatiFatturaBodyDTEType())
                invoice.DatiGenerali = (DatiGeneraliType())
                invoice.DatiGenerali.TipoDocumento = fields[
                    'xml_TipoDocumento']
                invoice.DatiGenerali.Data = fields['xml_Data']
                invoice.DatiGenerali.Numero = fields['xml_Numero']
                dati_riepilogo = []
                line_ids = commitment_model.get_riepilogo_list(
                    cr, uid, commitment, invoice_id, dte_dtr_id, context)
                for line_id in line_ids:
                    fields = commitment_model.get_xml_riepilogo(
                        cr, uid, commitment, line_id, dte_dtr_id, context)
                    riepilogo = (DatiRiepilogoType())
                    riepilogo.ImponibileImporto = '{:.2f}'.format(
                        fields['xml_ImponibileImporto'])
                    riepilogo.DatiIVA = (DatiIVAType())
                    riepilogo.DatiIVA.Imposta = '{:.2f}'.format(
                        fields['xml_Imposta'])
                    riepilogo.DatiIVA.Aliquota = '{:.2f}'.format(
                        fields['xml_Aliquota'])
                    if 'xml_Natura' in fields:
                        riepilogo.Natura = fields['xml_Natura']
                    # riepilogo.Detraibile = dte_line.xml_
                    # riepilogo.Deducibile = dte_line.xml_
                    # riepilogo.EsigibilitaIVA = dte_line.xml_
                    # riepilogo.Detraibile = '0.00'
                    # riepilogo.Deducibile = 'SI'
                    riepilogo.EsigibilitaIVA = fields['EsigibilitaIVA']
                    dati_riepilogo.append(riepilogo)
                invoice.DatiRiepilogo = dati_riepilogo
            invoices.append(invoice)
            partner.DatiFatturaBodyDTE = invoices
            partners.append(partner)
        dte.CessionarioCommittenteDTE = partners

        # dte.Rettifica = (RettificaType())

        return dte

    def get_dtr(self, cr, uid,
                commitment_model, commitment, dte_dtr_id, context=None):
        context = context or {}
        dtr = (DTRType())
        partners = []
        partner_ids = commitment_model.get_partner_list(
            cr, uid, commitment, dte_dtr_id, context)
        for partner_id in partner_ids:
            fields = commitment_model.get_xml_cessionario_cedente(
                cr, uid, commitment, partner_id, dte_dtr_id, context)
            # Missed mandatory data: skip record
            if 'xml_IdPaese' not in fields and \
                    'xml_CodiceFiscale' not in fields:
                continue
            dtr.CessionarioCommittenteDTR = self.get_company_data(
                cr, uid, commitment_model, commitment, dte_dtr_id, context)
            # TODO: StabileOrganizzazione
            # TODO: RappresentanteFiscale
            partner = self.get_supplier_data(
                cr, uid, commitment_model, commitment, fields, dte_dtr_id,
                context)
            invoices = []
            # Iterate over invoices of current partner
            invoice_ids = commitment_model.get_invoice_list(
                cr, uid, commitment, partner_id, dte_dtr_id, context)
            for invoice_id in invoice_ids:
                fields = commitment_model.get_xml_invoice(
                    cr, uid, commitment, invoice_id, dte_dtr_id, context)
                invoice = (DatiFatturaBodyDTRType())
                invoice.DatiGenerali = (DatiGeneraliDTRType())
                invoice.DatiGenerali.TipoDocumento = fields[
                    'xml_TipoDocumento']
                invoice.DatiGenerali.Data = fields['xml_Data']
                invoice.DatiGenerali.Numero = fields['xml_Numero']
                invoice.DatiGenerali.DataRegistrazione = fields[
                    'xml_DataRegistrazione']
                dati_riepilogo = []
                line_ids = commitment_model.get_riepilogo_list(
                    cr, uid, commitment, invoice_id, dte_dtr_id, context)
                for line_id in line_ids:
                    fields = commitment_model.get_xml_riepilogo(
                        cr, uid, commitment, line_id, dte_dtr_id, context)
                    riepilogo = (DatiRiepilogoType())
                    riepilogo.ImponibileImporto = '{:.2f}'.format(
                        fields['xml_ImponibileImporto'])
                    riepilogo.DatiIVA = (DatiIVAType())
                    riepilogo.DatiIVA.Imposta = '{:.2f}'.format(
                        fields['xml_Imposta'])
                    riepilogo.DatiIVA.Aliquota = '{:.2f}'.format(
                        fields['xml_Aliquota'])
                    if 'xml_Natura' in fields:
                        riepilogo.Natura = fields['xml_Natura']
                    # riepilogo.Detraibile = dte_line.xml_
                    # riepilogo.Deducibile = dte_line.xml_
                    # riepilogo.EsigibilitaIVA = dte_line.xml_
                    # riepilogo.Detraibile = '0.00'
                    # riepilogo.Deducibile = 'SI'
                    riepilogo.EsigibilitaIVA = fields['EsigibilitaIVA']
                    dati_riepilogo.append(riepilogo)
                invoice.DatiRiepilogo = dati_riepilogo
            invoices.append(invoice)
            partner.DatiFatturaBodyDTE = invoices
            partners.append(partner)
        dtr.CessionarioCommittenteDTE = partners

        # dtr.Rettifica = (RettificaType())

        return dtr

    def export_vat_communication(self, cr, uid, ids, context=None):
        context = context or {}
        commitment_model = self.pool['account.vat.communication']
        commitment_ids = context.get('active_ids', False)
        if commitment_ids:
            for commitment in commitment_model.browse(
                    cr, uid, commitment_ids, context=context):

                communication = DatiFattura()
                communication.versione = VersioneType(VERSIONE)
                communication.DatiFatturaHeader = self.get_dati_fattura_header(
                    cr, uid, commitment_model, commitment)
                communication.DTE = self.get_dte(
                    cr, uid, commitment_model, commitment, 'DTE', context)
                # communication.DTR = self.get_dtr(
                #     cr, uid, commitment_model, commitment, 'DTR', context)

                file_name = 'Comunicazine_IVA-{}.xml'.format(
                    commitment.progressivo_telematico)

                vat_communication_xml = communication.toDOM().toprettyxml(
                    encoding="latin1")

                out = vat_communication_xml.encode("base64")

                attach_vals = {
                    'name': file_name,
                    'datas_fname': file_name,
                    'datas': out,
                    'res_model': 'account.vat.communication',
                    'res_id': commitment.id,
                    'type': 'binary'
                }

                self.pool['ir.attachment'].create(cr, uid, attach_vals)

                return self.write(
                    cr, uid, ids, {
                        'state': 'get',
                        'data': out,
                        'name': file_name
                    }, context=context
                )
