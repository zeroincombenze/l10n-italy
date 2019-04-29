# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#    Copyright (C) 2017    Didotech srl <http://www.didotech.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
#
# from openerp import release
import logging
import os
import base64
from odoo import api, fields, models, exceptions, _

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)
try:
    from unidecode import unidecode
    if os.environ.get('SPESOMETRO_VERSION', '2.1') == '2.0':
        SPESOMETRO_VERSION = '2.0'
        from odoo.addons.l10n_it_ade.bindings.dati_fattura_v_2_0 import (
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
            # IndirizzoNoCAPType,
            RettificaType,
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
    else:
        SPESOMETRO_VERSION = '2.1'
        from odoo.addons.l10n_it_ade.bindings.dati_fattura_v_2_1 import (
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
            AltriDatiIdentificativiITType,
            AltriDatiIdentificativiType,
            IdentificativiFiscaliNoIVAType,
            IndirizzoType,
            # IndirizzoNoCAPType,
            RettificaType,
            DatiFatturaBodyDTEType,
            DatiGeneraliDTEType,
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
    raise


VERSIONE = 'DAT20'


class WizardVatCommunication(models.TransientModel):
    _name = "wizard.vat.communication"

    data = fields.Binary("File", readonly=True)
    name = fields.Char('Filename', size=32, readonly=True)
    state = fields.Selection((('create', 'create'), ('get', 'get')), default='create')
    target = fields.Char('Customers/Suppliers', size=4, readonly=True)

    def str60Latin(self, s):
        # t = s.encode('latin-1', 'ignore')
        return unidecode(s)[:60]

    def str80Latin(self, s):
        return unidecode(s)[:80]

    def old_get_dati_fattura_header(self, cr, uid, commitment_model, commitment, context=None):
        context = context or {}
        fields = commitment_model.get_xml_fattura_header(
            cr, uid, commitment, context)
        header = (DatiFatturaHeaderType())
        if 'xml_CodiceFiscale' in fields:
            header.Dichiarante = (DichiaranteType())
            header.Dichiarante.Carica = fields['xml_Carica']
            header.Dichiarante.CodiceFiscale = CodiceFiscaleType(
                fields['xml_CodiceFiscale'])
        return header

    @api.model
    def get_dati_fattura_header(self, commitment_model, commitment):
        return self.old_get_dati_fattura_header(cr=self.env.cr,
                                                uid=self.env.user.id,
                                                commitment_model=commitment_model,
                                                commitment=commitment,
                                                context=self.env.context)

    def old_get_sede(self, cr, uid, fields, dte_dtr_id, selector, context=None):
        if dte_dtr_id == 'DTE':
            if selector == 'company':
                sede = (IndirizzoType())
            elif selector == 'customer':
                if SPESOMETRO_VERSION == '2.0':
                    sede = (IndirizzoNoCAPType())
                else:
                    sede = (IndirizzoType())
            elif selector == 'supplier':
                sede = (IndirizzoType())
            else:
                raise exceptions.Warning(
                    _('Internal error: invalid partner selector'))
        else:
            if selector == 'company':
                sede = (IndirizzoType())
            elif selector == 'customer':
                if SPESOMETRO_VERSION == '2.0':
                    sede = (IndirizzoNoCAPType())
                else:
                    sede = (IndirizzoType())
            elif selector == 'supplier':
                if SPESOMETRO_VERSION == '2.0':
                    sede = (IndirizzoNoCAPType())
                else:
                    sede = (IndirizzoType())
            else:
                raise exceptions.Warning(
                    _('Internal error: invalid partner selector'))

        if fields.get('xml_Nazione'):
            sede.Nazione = fields['xml_Nazione']
        else:
            raise exceptions.Warning(
                _('Unknow country of %s %s %S' %
                  (fields.get('xml_Denominazione'),
                   fields.get('xml_Nome'),
                   fields.get('xml_Cognome'))))

        if fields.get('xml_Indirizzo'):
            sede.Indirizzo = self.str60Latin(fields['xml_Indirizzo'])
        else:
            raise exceptions.Warning(
                _('Error!'),
                _('Missed address %s %s %S' %
                  (fields.get('xml_Denominazione'),
                   fields.get('xml_Nome'),
                   fields.get('xml_Cognome'))))
        if fields.get('xml_Comune'):
            sede.Comune = self.str60Latin(fields['xml_Comune'])
        else:
            raise exceptions.Warning(
                _('Missed city %s %s %S' %
                  (fields.get('xml_Denominazione'),
                   fields.get('xml_Nome'),
                   fields.get('xml_Cognome'))))
        if fields.get('xml_CAP') and fields['xml_Nazione'] == 'IT':
            sede.CAP = fields['xml_CAP']
        elif selector == 'company':
            raise exceptions.Warning(
                _('Missed company zip code'))
        if fields.get('xml_Provincia') and fields['xml_Nazione'] == 'IT':
            sede.Provincia = fields['xml_Provincia']
        return sede

    @api.model
    def get_sede(self, fields, dte_dtr_id, selector):
        return self.old_get_sede(cr=self.env.cr,
                                 uid=self.env.user.id,
                                 fields=fields,
                                 dte_dtr_id=dte_dtr_id,
                                 selector=selector,
                                 context=self.env.context)

    def old_get_name(self, cr, uid, fields, dte_dtr_id, selector, context=None):
        if dte_dtr_id == 'DTE':
            if selector == 'company':
                if SPESOMETRO_VERSION == '2.0':
                    AltriDatiIdentificativi = \
                        (AltriDatiIdentificativiNoSedeType())
                else:
                    AltriDatiIdentificativi = \
                        (AltriDatiIdentificativiITType())
            elif selector == 'customer' or selector == 'supplier':
                if SPESOMETRO_VERSION == '2.0':
                    AltriDatiIdentificativi = \
                        (AltriDatiIdentificativiNoCAPType())
                else:
                    AltriDatiIdentificativi = \
                        (AltriDatiIdentificativiType())
            else:
                raise exceptions.Warning(
                    _('Error!'),
                    _('Internal error: invalid partner selector'))
        else:
            if selector == 'company':
                if SPESOMETRO_VERSION == '2.0':
                    AltriDatiIdentificativi = \
                        (AltriDatiIdentificativiNoSedeType())
                else:
                    AltriDatiIdentificativi = (AltriDatiIdentificativiITType())
            elif selector == 'customer' or selector == 'supplier':
                if SPESOMETRO_VERSION == '2.0':
                    AltriDatiIdentificativi = \
                        (AltriDatiIdentificativiNoCAPType())
                else:
                    AltriDatiIdentificativi = (AltriDatiIdentificativiType())
            else:
                raise exceptions.Warning(
                    _('Error!'),
                    _('Internal error: invalid partner selector'))

        if 'xml_Denominazione' in fields:
            AltriDatiIdentificativi.Denominazione = self.str80Latin(
                fields['xml_Denominazione'])
        else:
            AltriDatiIdentificativi.Nome = self.str60Latin(
                fields['xml_Nome'])
            AltriDatiIdentificativi.Cognome = self.str60Latin(
                fields['xml_Cognome'])
        AltriDatiIdentificativi.Sede = self.old_get_sede(
            cr, uid, fields, dte_dtr_id, selector, context=context)
        return AltriDatiIdentificativi

    @api.model
    def get_name(self, fields, dte_dtr_id, selector):
        return self.old_get_name(cr=self.env.cr,
                                 uid=self.env.user.id,
                                 fields=fields,
                                 dte_dtr_id=dte_dtr_id,
                                 selector=selector,
                                 context=self.env.context)

    def old_get_cedente_prestatore(self, cr, uid, fields, dte_dtr_id, context=None):

        if dte_dtr_id == 'DTE':
            CedentePrestatore = (CedentePrestatoreDTEType())
            CedentePrestatore.IdentificativiFiscali = (
                IdentificativiFiscaliITType())
            # Company VAT number must be present
            CedentePrestatore.IdentificativiFiscali.IdFiscaleIVA = (
                IdFiscaleITType())
            partner_type = 'company'
        elif dte_dtr_id == 'DTR':
            CedentePrestatore = (CedentePrestatoreDTRType())
            CedentePrestatore.IdentificativiFiscali = (
                IdentificativiFiscaliType())
            # Company VAT number must be present
            CedentePrestatore.IdentificativiFiscali.IdFiscaleIVA = (
                IdFiscaleType())
            partner_type = 'supplier'
        else:
            raise exceptions.Warning(
                _('Error!'),
                _('Internal error: invalid partner selector'))

        if fields.get('xml_IdPaese') and fields.get('xml_IdCodice'):
            CedentePrestatore.IdentificativiFiscali.IdFiscaleIVA.\
                IdPaese = fields['xml_IdPaese']
            CedentePrestatore.IdentificativiFiscali.IdFiscaleIVA.\
                IdCodice = fields['xml_IdCodice']
        if fields.get('xml_CodiceFiscale'):
            CedentePrestatore.IdentificativiFiscali.CodiceFiscale = \
                CodiceFiscaleType(fields['xml_CodiceFiscale'])
        CedentePrestatore.AltriDatiIdentificativi = \
            self.old_get_name(cr, uid, fields, dte_dtr_id, partner_type, context)
        return CedentePrestatore

    @api.model
    def get_cedente_prestatore(self, fields, dte_dtr_id):
        return self.old_get_cedente_prestatore(cr=self.env.cr,
                                               uid=self.env.user.id,
                                               fields=fields,
                                               dte_dtr_id=dte_dtr_id,
                                               context=self.env.context)

    def old_get_cessionario_committente(self, cr, uid, fields, dte_dtr_id, context=None):

        if dte_dtr_id == 'DTE':
            partner = (CessionarioCommittenteDTEType())
            partner_type = 'customer'
            partner.IdentificativiFiscali = (IdentificativiFiscaliNoIVAType())
        else:
            # DTR
            partner = (CessionarioCommittenteDTRType())
            partner_type = 'company'
            partner.IdentificativiFiscali = (IdentificativiFiscaliITType())

        if fields.get('xml_IdPaese') and fields.get('xml_IdCodice'):
            if dte_dtr_id == 'DTE':
                partner.IdentificativiFiscali.IdFiscaleIVA = (IdFiscaleType())
            else:
                partner.IdentificativiFiscali.IdFiscaleIVA = (
                    IdFiscaleITType())

            partner.IdentificativiFiscali.IdFiscaleIVA.\
                IdPaese = fields['xml_IdPaese']
            partner.IdentificativiFiscali.IdFiscaleIVA.\
                IdCodice = fields['xml_IdCodice']

            if fields.get('xml_IdPaese') == 'IT' and fields.get(
                    'xml_CodiceFiscale'):
                partner.IdentificativiFiscali.\
                    CodiceFiscale = CodiceFiscaleType(
                        fields['xml_CodiceFiscale'])
        else:
            partner.IdentificativiFiscali.CodiceFiscale = CodiceFiscaleType(
                fields['xml_CodiceFiscale'])
        # row 44: 2.2.2   <AltriDatiIdentificativi>
        partner.AltriDatiIdentificativi = \
            self.old_get_name(cr, uid, fields, dte_dtr_id, partner_type, context)
        return partner

    @api.model
    def get_cessionario_committente(self, fields, dte_dtr_id):
        return self.old_get_cessionario_committente(cr=self.env.cr, 
                                                    uid=self.env.user.id,
                                                    fields=fields,
                                                    dte_dtr_id=dte_dtr_id,
                                                    context=self.env.context)

    def old_get_dte_dtr(self, cr, uid, commitment_model, commitment, dte_dtr_id, context=None):
        context = context or {}

        partners = []
        partner_ids = commitment_model.get_partner_list(
            cr, uid, commitment, dte_dtr_id, context)
        for partner_id in partner_ids:
            fields_partner = commitment_model.get_xml_cessionario_cedente(
                cr, uid, commitment, partner_id, dte_dtr_id, context)
            _logger.debug('partner_id=%d %s VAT=%s%s CF=%s' % (
                partner_id,
                fields_partner.get('xml_Denominazione'),
                fields_partner.get('xml_IdPaese'),
                fields_partner.get('xml_IdCodice'),
                fields_partner.get('xml_CodiceFiscale')))

            if dte_dtr_id == 'DTE':
                partner = self.old_get_cessionario_committente(
                    cr, uid, fields_partner, dte_dtr_id, context)
            else:
                partner = self.old_get_cedente_prestatore(
                    cr, uid, fields_partner, dte_dtr_id, context
                )

            invoices = []
            # Iterate over invoices of current partner
            invoice_ids = commitment_model.get_invoice_list(
                cr, uid, commitment, partner_id, dte_dtr_id, context)
            for invoice_id in invoice_ids:
                fields = commitment_model.get_xml_invoice(
                    cr, uid, commitment, invoice_id, dte_dtr_id, context)

                if dte_dtr_id == 'DTE':
                    invoice = (DatiFatturaBodyDTEType())
                    if SPESOMETRO_VERSION == '2.0':
                        invoice.DatiGenerali = (DatiGeneraliType())
                    else:
                        invoice.DatiGenerali = (DatiGeneraliDTEType())
                else:
                    invoice = (DatiFatturaBodyDTRType())
                    invoice.DatiGenerali = (DatiGeneraliDTRType())

                invoice.DatiGenerali.TipoDocumento = fields[
                    'xml_TipoDocumento']
                invoice.DatiGenerali.Data = fields['xml_Data']
                invoice.DatiGenerali.Numero = fields['xml_Numero']
                if dte_dtr_id == 'DTR':
                    invoice.DatiGenerali.DataRegistrazione = fields[
                        'xml_DataRegistrazione']

                if dte_dtr_id == 'DTR' and \
                        fields['xml_TipoDocumento'] != 'TD12' and \
                        not fields_partner.get('xml_IdPaese') and \
                        not fields_partner.get('xml_IdCodice') and \
                        not fields_partner.get('xml_CodiceFiscale'):
                    raise exceptions.Warning(
                        _('Error 00464: Partner id %d without fiscal data' % (
                            partner_id)))

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
                    if fields.get('xml_Detraibile', None) != None:
                        riepilogo.Detraibile = '{:.2f}'.format(
                            fields['xml_Detraibile'])
                    if fields.get('xml_Deducibile', None) != None:
                        riepilogo.Deducibile = fields['xml_Deducibile']
                    if fields.get('xml_Natura', False):
                        riepilogo.Natura = fields['xml_Natura']
                    if fields.get('xml_EsigibilitaIVA', False):
                        riepilogo.EsigibilitaIVA = fields['xml_EsigibilitaIVA']
                    dati_riepilogo.append(riepilogo)
                invoice.DatiRiepilogo = dati_riepilogo
                invoices.append(invoice)

            if dte_dtr_id == 'DTE':
                partner.DatiFatturaBodyDTE = invoices
            else:
                partner.DatiFatturaBodyDTR = invoices
            partners.append(partner)

        fields = commitment_model.get_xml_company(
            cr, uid, commitment, dte_dtr_id, context)
        if dte_dtr_id == 'DTE':
            dte = (DTEType())

            dte.CedentePrestatoreDTE = self.old_get_cedente_prestatore(
                cr, uid, fields, dte_dtr_id, context)
            dte.CessionarioCommittenteDTE = partners

            # dte.Rettifica = (RettificaType())

            return dte
        else:
            dtr = (DTRType())

            dtr.CessionarioCommittenteDTR = self.old_get_cessionario_committente(
                cr, uid, fields, dte_dtr_id, context
            )

            dtr.CedentePrestatoreDTR = partners

            # dtr.Rettifica = (RettificaType())

            return dtr

    @api.model
    def get_dte_dtr(self, commitment_model, commitment, dte_dtr_id):
        return self.old_get_dte_dtr(cr=self.env.cr,
                                    uid=self.env.user.id,
                                    commitment_model=commitment_model,
                                    commitment=commitment,
                                    dte_dtr_id=dte_dtr_id,
                                    context=self.env.context)

    def old_export_vat_communication_DTE(self, cr, uid, ids, context=None):
        context = context or {}
        context = context.copy()
        context.update({'dte_dtr_id': 'DTE'})
        return self.old_export_vat_communication(cr, uid, ids, context)

    @api.multi
    def export_vat_communication_DTE(self):
        return self.old_export_vat_communication_DTE(cr=self.env.cr,
                                                     uid=self.env.user.id,
                                                     ids=self.ids,
                                                     context=self.env.context)

    def old_export_vat_communication_DTR(self, cr, uid, ids, context=None):
        context = context or {}
        context = context.copy()
        context['dte_dtr_id'] = 'DTR'
        return self.old_export_vat_communication(cr, uid, ids, context)

    @api.multi
    def export_vat_communication_DTR(self):
        return self.old_export_vat_communication_DTR(cr=self.env.cr,
                                                     uid=self.env.user.id,
                                                     ids=self.ids,
                                                     context=self.env.context)

    def old_export_vat_communication(self, cr, uid, ids, context=None):
        context = context or {}
        dte_dtr_id = context.get('dte_dtr_id', 'DTE')
        commitment_model = self.env['account.vat.communication']
        commitment_ids = context.get('active_ids', False)
        if commitment_ids:
            for commitment in commitment_model.browse(commitment_ids):

                communication = DatiFattura()
                communication.versione = VersioneType(VERSIONE)
                communication.DatiFatturaHeader = self.old_get_dati_fattura_header(
                    cr, uid, commitment_model, commitment)

                if dte_dtr_id == 'DTE':
                    communication.DTE = self.old_get_dte_dtr(
                        cr, uid, commitment_model, commitment, dte_dtr_id,
                        context)
                elif dte_dtr_id == 'DTR':
                    communication.DTR = self.old_get_dte_dtr(
                        cr, uid, commitment_model, commitment, dte_dtr_id,
                        context)
                else:
                    raise exceptions.Warning(
                        _('Internal error: invalid partner selector'))
                progr_invio = commitment_model.set_progressivo_telematico(
                    cr, uid, commitment, context)
                _logger.debug('Progressivo invio %d' % progr_invio)
                file_name = 'IT%s_DF_%05d.xml' % (
                    commitment.soggetto_codice_fiscale, progr_invio)
                try:
                    vat_communication_xml = communication.toDOM().toprettyxml()
                except Exception as e:
                    print(e.details())
                    raise

                out = base64.b64encode(vat_communication_xml.encode('ascii'))

                attach_vals = {
                    'name': file_name,
                    'datas_fname': file_name,
                    'datas': out,
                    'res_model': 'account.vat.communication',
                    'res_id': commitment.id,
                    'type': 'binary',
                }

                self.env['ir.attachment'].create(attach_vals)

                return self.write(
                    {
                        'state': 'get',
                        'data': out,
                        'name': file_name,
                        'target': dte_dtr_id,
                    }
                )

    @api.multi
    def export_vat_communication(self):
        return self.old_export_vat_communication(cr=self.env.cr,
                                                 uid=self.env.user.id,
                                                 ids=self.ids,
                                                 context=self.env.context)
