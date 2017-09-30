# flake8: noqa
# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
#
import base64
from openerp.osv import fields, orm
from openerp.tools.translate import _
from openerp import release
# import datetime
# from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
import logging
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
        RettificaType,
        DatiFatturaBodyDTEType,
        DatiGeneraliType,
        DatiRiepilogoType,
        DatiIVAType,
        DTRType,
        CessionarioCommittenteDTRType,
        CedentePrestatoreDTRType,
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

    def dati_fattura_header(self, cr, uid, statement, context=None):
        context = context or {}
        statement_model = self.pool['account.vat.communication']
        fields = statement_model.get_dati_fattura_header(
            cr, uid, statement, context)

        header = (DatiFatturaHeaderType())
        header.ProgressivoInvio = fields['xml_ProgressivoInvio']
        if 'xml_CodiceFiscale' in fields:
            header.Dichiarante = (DichiaranteType())
            header.Dichiarante.Carica = fields['xml_Carica']
            header.Dichiarante.CodiceFiscale = CodiceFiscaleType(
                fields['xml_CodiceFiscale'])
        return header

    def get_sede(self, cr, uid, fields, dte_dtr_id, context=None):
        if 'xml_CAP' in fields:
            sede = (IndirizzoType())
        else:
            sede = (IndirizzoNoCAPType())
        sede.Indirizzo = res['xml_Indirizzo']
        sede.Comune = res['xml_Comune']
        if 'xml_Provincia' in fields:
            sede.Provincia = res['xml_Provincia']
        sede.Nazione = res['xml_Nazione']
        return sede

    def get_company_data(self, cr, uid, fields, dte_dtr_id, context=None):
        if dte_dtr_id == 'DTE':
            fields = statement_model.get_cedente_cessionario_company(
                cr, uid, statement, dte_dtr_id, context)
            dte.CedentePrestatoreDTE = (CedentePrestatoreDTEType())
            dte.CedentePrestatoreDTE.IdentificativiFiscali = (
                IdentificativiFiscaliITType())
            dte.CedentePrestatoreDTE.IdentificativiFiscali.IdFiscaleIVA = (
                IdFiscaleITType())
            dte.CedentePrestatoreDTE.IdentificativiFiscali.IdFiscaleIVA.\
                IdPaese = fields['xml_IdPaese']
            dte.CedentePrestatoreDTE.IdentificativiFiscali.IdFiscaleIVA.\
                IdCodice = fields['xml_IdCodice']
            dte.CedentePrestatoreDTE.IdentificativiFiscali.CodiceFiscale = \
                CodiceFiscaleType(fields['xml_CodiceFiscale'])
            dte.CedentePrestatoreDTE.AltriDatiIdentificativi = \
                (AltriDatiIdentificativiNoSedeType())
            if 'xml_Denominazione' in fields:
                dte.CedentePrestatoreDTE.AltriDatiIdentificativi.\
                    Denominazione = fields['xml_Denominazione']
            else:
                dte.CedentePrestatoreDTE.AltriDatiIdentificativi.\
                    Nome = fields['xml_Nome']
                dte.CedentePrestatoreDTE.AltriDatiIdentificativi.\
                    Cognome = fields['xml_Cognome']
            client.AltriDatiIdentificativi.Sede = self.get_sede(
                cr, uid, fields, dte_dtr_id, context=context)

    def get_customer_data(self, cr, uid, fields, dte_dtr_id, context=None):
        client = (CessionarioCommittenteDTEType())
        client.IdentificativiFiscali = (IdentificativiFiscaliNoIVAType())
        if 'xml_IdPaese' in fields:
            client.IdentificativiFiscali.IdFiscaleIVA = (IdFiscaleType())
            client.IdentificativiFiscali = (
                IdentificativiFiscaliNoIVAType())
            client.IdentificativiFiscali.IdFiscaleIVA.\
                IdPaese = fields['xml_IdPaese']
            client.IdentificativiFiscali.IdFiscaleIVA.\
                IdCodice = fields['xml_IdCodice']
        if fields['xml_IdPaese'] == 'IT' and 'xml_CodiceFiscale' in fields:
            client.IdentificativiFiscali.CodiceFiscale = CodiceFiscaleType(
                fields['xml_CodiceFiscale'])
        client.AltriDatiIdentificativi = (
            AltriDatiIdentificativiNoCAPType())
        # row 44: 2.2.2   <AltriDatiIdentificativi>
        if 'xml_Denominazione' in fields:
            client.AltriDatiIdentificativi.Denominazione = fields[
                'xml_Denominazione']
        else:
            client.AltriDatiIdentificativi.Nome = fields['xml_Nome']
            client.AltriDatiIdentificativi.Cognome = fields['xml_Cognome']

        dte.CedentePrestatoreDTE.AltriDatiIdentificativi.\
            Sede = self.get_sede(cr, uid, fields, dte_dtr_id,
                                 context=context)

    def get_dte(self, cr, uid, statement, dte_dtr_id, context=None):
        context = context or {}
        statement_model = self.pool['account.vat.communication']
        partner_ids = statement_model.get_partner_list(
            cr, uid, statement, dte_dtr_id, context)
        dte = (DTEType())
        for partner_id in partner_ids:
            fields = statement_model.get_cessionario_cedente(
                cr, uid, statement, dte_dtr_id, partner_id, context)
            if 'xml_IdPaese' not in fields and \
                    'xml_CodiceFiscale' not in fields:
                continue
            statement_model.get_company_data(
                self, cr, uid, fields, dte_dtr_id, context)
            # TODO: StabileOrganizzazione
            # TODO: RappresentanteFiscale
            statement_model.get_customer_data(
                self, cr, uid, fields, dte_dtr_id, context)


            invoices = []
            # for dte_invoice in
            invoice = (DatiFatturaBodyDTEType())
            invoice.DatiGenerali = (DatiGeneraliType())
            invoice.DatiGenerali.TipoDocumento = dte_line.xml_TipoDocumento
            invoice.DatiGenerali.Data = dte_line.invoice_id.date_invoice
            invoice.DatiGenerali.Numero = dte_line.invoice_id.number

            dati_riepilogo = []

            riepilogo = (DatiRiepilogoType())
            riepilogo.ImponibileImporto = '{:.2f}'.format(dte_line.xml_ImponibileImporto)
            riepilogo.DatiIVA = (DatiIVAType())
            riepilogo.DatiIVA.Imposta = '{:.2f}'.format(dte_line.xml_Imposta)
            riepilogo.DatiIVA.Aliquota = '{:.2f}'.format(dte_line.xml_Aliquota)
            if dte_line.xml_Natura:
                riepilogo.Natura = dte_line.xml_Natura
            # riepilogo.Detraibile = dte_line.xml_
            # riepilogo.Deducibile = dte_line.xml_
            # riepilogo.EsigibilitaIVA = dte_line.xml_
            # riepilogo.Detraibile = '0.00'
            # riepilogo.Deducibile = 'SI'
            riepilogo.EsigibilitaIVA = 'I'
            dati_riepilogo.append(riepilogo)

            invoice.DatiRiepilogo = dati_riepilogo

            invoices.append(invoice)

            client.DatiFatturaBodyDTE = invoices
            clients.append(client)

        dte.CessionarioCommittenteDTE = clients

        # dte.Rettifica = (RettificaType())

        return dte

    def get_dtr(self, cr, uid, statement, context):
        dtr = (DTRType())
        # dtr.CessionarioCommittenteDTR = (CessionarioCommittenteDTRType())
        #
        # dtr.CedentePrestatoreDTR = (CedentePrestatoreDTRType())

        return dtr

    def export_vat_communication(self, cr, uid, ids, context=None):
        context = context or {}
        statement_obj = self.pool['account.vat.communication']
        statement_ids = context.get('active_ids', False)
        if statement_ids:
            for statement in statement_obj.browse(
                    cr, uid, statement_ids, context=context):

                communication = DatiFattura()
                communication.versione = VersioneType(VERSIONE)
                communication.DatiFatturaHeader = self.dati_fattura_header(
                    cr, uid, statement)
                communication.DTE = self.get_dte(
                    cr, uid, statement, 'DTE', context)
                # communication.DTR = self.get_dtr(cr, uid, statement, context)

                file_name = 'Comunicazine_IVA-{}.xml'.format(statement.progressivo_telematico)

                vat_communication_xml = communication.toDOM().toprettyxml(
                    encoding="latin1")

                out = vat_communication_xml.encode("base64")

                attach_vals = {
                    'name': file_name,
                    'datas_fname': file_name,
                    'datas': out,
                    'res_model': 'account.vat.communication',
                    'res_id': statement.id,
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
