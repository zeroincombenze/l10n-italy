# -*- coding: utf-8 -*-
#
# Copyright 2014    - Davide Corio <davide.corio@lsweb.it>
# Copyright 2015    - Lorenzo Battistini <lorenzo.battistini@agilebg.com>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
import re
import base64
import logging
from xml.sax.saxutils import escape

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import UserError

from odoo.addons.l10n_it_ade.bindings.fatturapa_v_1_2 import (
    AllegatiType,
    AnagraficaType,
    CedentePrestatoreType,
    CessionarioCommittenteType,
    ContattiTrasmittenteType,
    ContattiType,
    CodiceArticoloType,
    DatiAnagraficiCedenteType,
    DatiAnagraficiCessionarioType,
    DatiAnagraficiRappresentanteType,
    DatiAnagraficiTerzoIntermediarioType,
    DatiBeniServiziType,
    DatiDocumentiCorrelatiType,
    DatiGeneraliDocumentoType,
    DatiGeneraliType,
    DatiPagamentoType,
    DatiRiepilogoType,
    DatiTrasmissioneType,
    DettaglioLineeType,
    DettaglioPagamentoType,
    FatturaElettronica,
    FatturaElettronicaBodyType,
    FatturaElettronicaHeaderType,
    IdFiscaleType,
    IndirizzoType,
    IscrizioneREAType,
    RappresentanteFiscaleType,
    RappresentanteFiscaleCessionarioType,
    ScontoMaggiorazioneType,
    TerzoIntermediarioSoggettoEmittenteType,)
from odoo.addons.l10n_it_einvoice_base.models.account_invoice import (
    RELATED_DOCUMENT_TYPES)

_logger = logging.getLogger(__name__)

try:
    from unidecode import unidecode
    from pyxb.exceptions_ import SimpleFacetValueError, SimpleTypeValueError
except ImportError as err:
    _logger.debug(err)

CODE_NONE_IT = '0000000'
CODE_NONE_EU = 'XXXXXXX'
PAYTYPE_BNK_CUSTOMER = ('MP11', 'MP12', 'MP16', 'MP17', 'MP19', 'MP20', 'MP21')
PAYTYPE_BNK_COMPANY = ('MP05', 'MP07', 'MP08', 'MP13', 'MP18')
XML_ESCAPE = {
    u'\'': u' ',
    u'\n': u' ',
    u'\r': u' ',
    u'\t': u' ',
    u'€': u'EUR',
    u'©': u'(C)',
    u'®': u'(R)',
    # u'à': u'&agrave;',
    # u'á': u'&aacute;',
    # u'è': u'&egrave;',
    # u'é': u'&eacute;',
    # u'ì': u'&igrave;',
    # u'í': u'&iacute;',
    # u'ò': u'&ograve;',
    # u'ó': u'&oacute;',
    # u'ù': u'&ugrave;',
    # u'ú': u'&uacute;',
    # u'°': u'&deg;',
    u'«': u'&laquo;',
    u'»': u'&raquo;',
    u'Ø': u'&Oslash;',
    u'ø': u'&oslash;',
    u'ß': u'&szlig;',
}
IBAN_PATTERN = re.compile('[A-Z]{2}[0-9]{2}[A-Z][0-9A-Z]+')
INHERITED_FLDS = ['codice_destinatario', 'name']


class WizardExportFatturapa(models.TransientModel):
    _name = "wizard.export.fatturapa"
    _description = "Export E-invoice"

    @api.model
    def _domain_ir_values(self):
        """Get all print actions for current model"""
        return [('model', '=', self.env.context.get('active_model', False)),
                ('key2', '=', 'client_print_multi')]

    report_print_menu = fields.Many2one(
        comodel_name='ir.values',
        domain=_domain_ir_values,
        help='This report will be automatically included in the created XML')

    def saveAttachment(self, fatturapa, number):
        if 'company_id' in self.env.context:
            company_model = self.env['res.company']
            company = company_model.browse(self.env.context['company_id'])
        else:
            company = self.env.user.company_id
        if not company.vat:
            raise UserError(
                _('Company %s TIN not set.') % company.name)
        if (
            company.fatturapa_sender_partner and not
            company.fatturapa_sender_partner.vat
        ):
            raise UserError(
                _('Partner %s TIN not set.')
                % company.fatturapa_sender_partner.name
            )
        vat = company.vat
        if company.fatturapa_sender_partner:
            vat = company.fatturapa_sender_partner.vat
        vat = self.__wep_vat(vat)
        attach_model = self.env['fatturapa.attachment.out']
        attach_vals = {
            'name': '%s_%s.xml' % (vat, str(number)),
            'datas_fname': '%s_%s.xml' % (vat, str(number)),
            'datas': base64.encodestring(fatturapa.toxml("UTF-8")),
        }
        return attach_model.create(attach_vals)

    def setProgressivoInvio(self, fatturapa):
        if 'company_id' in self.env.context:
            company_model = self.env['res.company']
            company = company_model.browse(self.env.context['company_id'])
        else:
            company = self.env.user.company_id

        fatturapa_sequence = company.fatturapa_sequence_id
        if not fatturapa_sequence:
            raise UserError(
                _('E-invoice sequence not configured.'))
        number = fatturapa_sequence.next_by_id()
        try:
            fatturapa.FatturaElettronicaHeader.DatiTrasmissione.\
                ProgressivoInvio = number
        except (SimpleFacetValueError, SimpleTypeValueError) as e:
            msg = _(
                'FatturaElettronicaHeader.DatiTrasmissione.'
                'ProgressivoInvio:\n%s'
            ) % unicode(e)
            raise UserError(msg)
        return number

    def _wep_phone_number(self, phone):
        """"Remove trailing +39 and all no numeric chars"""
        wep_phone = ''
        if phone:
            if phone[0:3] == '+39':
                phone = phone[3:]
            elif phone[0] == '+':
                phone = '00' + phone[1:]
            for i in range(len(phone)):
                if phone[i].isdigit():
                    wep_phone += phone[i]
        return wep_phone.strip()

    def _wep_text(self, text):
        """"Do xml escape to avoid error StringLatinType"""
        # text.encode('latin', 'ignore').decode('latin')
        if text:
            return escape(unidecode(text), XML_ESCAPE).strip()
        return text

    def __wep_vat(self, vat):
        if vat:
            return vat.replace(
                ' ', '').replace('.', '').replace('-', '').upper()
        return vat

    def _split_vat_n_country(self, vat):
        if vat:
            vat = self.__wep_vat(vat)
            if vat[0:3] != 'IT9':
                country_code = vat[0:2]
                vat_number = vat[2:]
            else:
                country_code = ''
                vat_number = ''
        else:
            country_code = ''
            vat_number = ''
        return country_code, vat_number

    def _get_partner_field(self, partner, parent, field, mode=None):
        """Select field from <invoice address> or <parent>
        Order refers to a <customer> and an <invoice address>.
        <invoice address> should be child of <customer>, when they differ.
        Invoice get <invoice address> from order so here we have:
        - partner is <invoice address> of order (child of <customer>)
        - parent is <customers>  of order (parent of <invoice address>)

        <invoice address> may not have some data, i.e. vat number while
        <parent> contains all customer information.

        Usually, the behavior of this funciotn is fallback:
        return value from <invoice address> field, if present,
        otherwise return <parent> field with the same name.

        When mode in <type_inv_addr> field of <invoice address> is
        'FR' (Fiscal Representative) or 'SO' (Stable Organization),
        some fields are not inherited from <parent>
        """
        mode = mode or 'fallback'
        inherit = False
        if field in INHERITED_FLDS or mode == 'fallback':
            inherit = True
        value = False
        if field == 'company_type':
            if partner.name:
                value = partner[field] or (parent and parent[field])
            else:
                value = (parent and parent[field]) or 'company'
        elif mode == 'parent':
            value = parent and parent[field] or False
        elif field in partner:
            if inherit:
                value = partner[field] or (parent and parent[field])
            else:
                value = partner[field]
        return value

    def _setIdTrasmittente(self, company, fatturapa):
        if not company.country_id:
            raise UserError(
                _('Company Country not set.'))
        IdPaese = company.country_id.code

        IdCodice = company.partner_id.fiscalcode
        if not IdCodice:
            if company.vat:
                IdCodice = company.vat[2:]
        if not IdCodice:
            raise UserError(
                _('Company does not have fiscal code or VAT number.'))

        fatturapa.FatturaElettronicaHeader.DatiTrasmissione.\
            IdTrasmittente = IdFiscaleType(
                IdPaese=IdPaese, IdCodice=IdCodice)

        return True

    def _getFormatoTrasmissione(self, partner, parent):
        if self._get_partner_field(partner, parent, 'is_pa'):
            return 'FPA12'
        else:
            return 'FPR12'

    def _setFormatoTrasmissione(self, partner, parent, fatturapa):
        fatturapa.FatturaElettronicaHeader.DatiTrasmissione.\
                FormatoTrasmissione = self._getFormatoTrasmissione(partner,
                                                                   parent)
        return True

    def _setCodiceDestinatario(self, partner, parent, fatturapa):
        pec_destinatario = None
        if self._get_partner_field(partner, parent, 'is_pa'):
            code = self._get_partner_field(partner, parent, 'ipa_code')
            if not code:
                raise UserError(_(
                    "Partner %s is PA but has not IPA code"
                ) % partner.name)
        else:
            code = self._get_partner_field(
                partner, parent, 'codice_destinatario')
            if not code:
                raise UserError(_(
                    "Partner %s is not PA but does not have Addressee Code."
                ) % partner.name)
            vat = self._get_partner_field(partner, parent, 'vat')
            fiscalcode = self.__wep_vat(
                self._get_partner_field(partner, parent, 'fiscalcode'))
            if code not in (CODE_NONE_IT, CODE_NONE_EU) and \
                    not vat and not fiscalcode:
                raise UserError(_(
                    "Partner %s is not PA "
                    "but does not have vat number neither fiscal code Code."
                ) % partner.name)
        fatturapa.FatturaElettronicaHeader.DatiTrasmissione.\
            CodiceDestinatario = code.upper()
        if code == CODE_NONE_IT:
            pec_destinatario = self._get_partner_field(
                    partner, parent, 'pec_destinatario')
        if pec_destinatario:
            fatturapa.FatturaElettronicaHeader.DatiTrasmissione. \
                PECDestinatario = pec_destinatario
        return True

    def _setContattiTrasmittente(self, company, fatturapa):
        if not company.phone:
            raise UserError(
                _('Company Telephone number not set.'))
        Telefono = self._wep_phone_number(company.phone)
        if not company.email:
            raise UserError(
                _('Company Email not set.'))
        Email = company.email
        fatturapa.FatturaElettronicaHeader.DatiTrasmissione.\
            ContattiTrasmittente = ContattiTrasmittenteType(
                Telefono=Telefono, Email=Email)
        return True

    def setDatiTrasmissione(self, company, partner, parent, fatturapa):
        fatturapa.FatturaElettronicaHeader.DatiTrasmissione = (
            DatiTrasmissioneType())
        self._setIdTrasmittente(company, fatturapa)
        self._setFormatoTrasmissione(partner, parent, fatturapa)
        self._setCodiceDestinatario(partner, parent, fatturapa)
        self._setContattiTrasmittente(company, fatturapa)

    def _setDatiAnagraficiCedente(self, CedentePrestatore, company):
        if not company.vat:
            raise UserError(
                _('Company TIN not set.'))
        CedentePrestatore.DatiAnagrafici = DatiAnagraficiCedenteType()
        fatturapa_fp = company.fatturapa_fiscal_position_id
        if not fatturapa_fp:
            raise UserError(
                _('E-invoice fiscal position not set.'))
        CedentePrestatore.DatiAnagrafici.IdFiscaleIVA = IdFiscaleType(
            IdPaese=company.country_id.code, IdCodice=company.vat[2:])
        CedentePrestatore.DatiAnagrafici.Anagrafica = AnagraficaType(
            Denominazione=company.name)

        if company.partner_id.fiscalcode:
            CedentePrestatore.DatiAnagrafici.CodiceFiscale = (
                company.partner_id.fiscalcode)
        CedentePrestatore.DatiAnagrafici.RegimeFiscale = fatturapa_fp.code
        return True

    def _setAlboProfessionaleCedente(self, CedentePrestatore, company):
        # TODO Albo professionale, for now the main company is considered
        # to be a legal entity and not a single person
        # 1.2.1.4   <AlboProfessionale>
        # 1.2.1.5   <ProvinciaAlbo>
        # 1.2.1.6   <NumeroIscrizioneAlbo>
        # 1.2.1.7   <DataIscrizioneAlbo>
        return True

    def _setSedeCedente(self, CedentePrestatore, company):

        if not company.street:
            raise UserError(
                _('Your company Street is not set.'))
        if not company.zip:
            raise UserError(
                _('Your company ZIP is not set.'))
        if not company.city:
            raise UserError(
                _('Your company City is not set.'))
        if not company.partner_id.state_id:
            raise UserError(
                _('Province not set.'))
        if not company.country_id:
            raise UserError(
                _('Your company Country is not set.'))
        # TODO: manage address number in <NumeroCivico>
        # see https://github.com/OCA/partner-contact/pull/96
        CedentePrestatore.Sede = IndirizzoType(
            Indirizzo=company.street,
            CAP=company.zip,
            Comune=company.city[:60],
            Provincia=company.partner_id.state_id.code,
            Nazione=company.country_id.code)
        return True

    def _setStabileOrganizzazione(self, CedentePrestatore, company):
        if company.fatturapa_stabile_organizzazione:
            stabile_organizzazione = company.fatturapa_stabile_organizzazione
            if not stabile_organizzazione.street:
                raise UserError(
                    _('Street is not set for %s.') %
                    stabile_organizzazione.name)
            if not stabile_organizzazione.zip:
                raise UserError(
                    _('ZIP is not set for %s.') %
                    stabile_organizzazione.name)
            if not stabile_organizzazione.city:
                raise UserError(
                    _('City is not set for %s.') %
                    stabile_organizzazione.name)
            if not stabile_organizzazione.country_id:
                raise UserError(
                    _('Country is not set for %s.') %
                    stabile_organizzazione.name)
            CedentePrestatore.StabileOrganizzazione = IndirizzoType(
                Indirizzo=stabile_organizzazione.street,
                CAP=stabile_organizzazione.zip,
                Comune=stabile_organizzazione.city,
                Nazione=stabile_organizzazione.country_id.code)
            if stabile_organizzazione.state_id:
                CedentePrestatore.StabileOrganizzazione.Provincia = (
                    stabile_organizzazione.state_id.code)
        return True

    def _setRea(self, CedentePrestatore, company):

        if company.fatturapa_rea_office and company.fatturapa_rea_number:
            CedentePrestatore.IscrizioneREA = IscrizioneREAType(
                Ufficio=(
                    company.fatturapa_rea_office and
                    company.fatturapa_rea_office.code or None),
                NumeroREA=company.fatturapa_rea_number or None,
                CapitaleSociale=(
                    company.fatturapa_rea_capital and
                    '%.2f' % company.fatturapa_rea_capital or None),
                SocioUnico=(company.fatturapa_rea_partner or None),
                StatoLiquidazione=company.fatturapa_rea_liquidation or None
                )

    def _setContatti(self, CedentePrestatore, company):
        CedentePrestatore.Contatti = ContattiType(
            Telefono=self._wep_phone_number(company.partner_id.phone) or None,
            Fax=self._wep_phone_number(company.partner_id.fax) or None,
            Email=company.partner_id.email or None
            )

    def _setPubAdministrationRef(self, CedentePrestatore, company):
        if company.fatturapa_pub_administration_ref:
            CedentePrestatore.RiferimentoAmministrazione = (
                company.fatturapa_pub_administration_ref)

    def setCedentePrestatore(self, company, fatturapa):
        fatturapa.FatturaElettronicaHeader.CedentePrestatore = (
            CedentePrestatoreType())
        self._setDatiAnagraficiCedente(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setSedeCedente(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setAlboProfessionaleCedente(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setStabileOrganizzazione(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        # TODO: add Contacts
        self._setRea(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setContatti(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)
        self._setPubAdministrationRef(
            fatturapa.FatturaElettronicaHeader.CedentePrestatore,
            company)

    def _setDatiAnagraficiCessionario(self, partner, parent, fatturapa):
        mode = partner.type_inv_addr
        mode = mode if mode not in ('SO','FR') else 'parent'
        fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
            DatiAnagrafici = DatiAnagraficiCessionarioType()
        vat = self._get_partner_field(
            partner, parent, 'vat', mode=mode)
        fiscalcode = self.__wep_vat(
            self._get_partner_field(
                partner, parent, 'fiscalcode', mode=mode))
        if vat:
            country_code, vat_number = self._split_vat_n_country(vat)
            if country_code and vat_number:
                fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
                    DatiAnagrafici.IdFiscaleIVA = IdFiscaleType(
                        IdPaese=country_code,
                        IdCodice=vat_number)
        else:
            vat = ''
        if fiscalcode:
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
                DatiAnagrafici.CodiceFiscale = fiscalcode
        elif vat[0:3] == 'IT9':
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
                DatiAnagrafici.CodiceFiscale = vat[2:]

        company_type = self._get_partner_field(
            partner, parent, 'company_type', mode=mode)
        if company_type == 'company':
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
                DatiAnagrafici.Anagrafica = AnagraficaType(
                    Denominazione=self._get_partner_field(
                        partner, parent, 'name', mode=mode))
        elif company_type == 'person':
            if not partner.lastname or not partner.firstname:
                raise UserError(
                    _("Partner %s must have name and surname.") %
                    partner.name)
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
                DatiAnagrafici.Anagrafica = AnagraficaType(
                    Cognome=partner.lastname,
                    Nome=partner.firstname
                )
        eori_code = self._get_partner_field(
            partner, parent, 'eori_code', mode=mode)
        if eori_code:
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
                DatiAnagrafici.Anagrafica.CodEORI = eori_code

        return True

    def _setDatiAnagraficiRappresentanteFiscale(self, partner, fatturapa):
        fatturapa.FatturaElettronicaHeader.RappresentanteFiscale = (
            RappresentanteFiscaleType())
        fatturapa.FatturaElettronicaHeader.RappresentanteFiscale.\
            DatiAnagrafici = DatiAnagraficiRappresentanteType()
        if not partner.vat and not partner.fiscalcode:
            raise UserError(
                _('VAT number and fiscal code are not set for %s.') %
                partner.name)
        if partner.fiscalcode:
            fatturapa.FatturaElettronicaHeader.RappresentanteFiscale.\
                DatiAnagrafici.CodiceFiscale = partner.fiscalcode
        if partner.vat:
            fatturapa.FatturaElettronicaHeader.RappresentanteFiscale.\
                DatiAnagrafici.IdFiscaleIVA = IdFiscaleType(
                    IdPaese=partner.vat[0:2], IdCodice=partner.vat[2:])
        fatturapa.FatturaElettronicaHeader.RappresentanteFiscale.\
            DatiAnagrafici.Anagrafica = AnagraficaType(
                Denominazione=partner.name)
        if partner.eori_code:
            fatturapa.FatturaElettronicaHeader.RappresentanteFiscale.\
                DatiAnagrafici.Anagrafica.CodEORI = partner.eori_code

        return True

    def _setTerzoIntermediarioOSoggettoEmittente(self, partner, fatturapa):
        fatturapa.FatturaElettronicaHeader.\
            TerzoIntermediarioOSoggettoEmittente = (
                TerzoIntermediarioSoggettoEmittenteType()
            )
        fatturapa.FatturaElettronicaHeader.\
            TerzoIntermediarioOSoggettoEmittente.\
            DatiAnagrafici = DatiAnagraficiTerzoIntermediarioType()
        if not partner.vat and not partner.fiscalcode:
            raise UserError(
                _('Partner VAT number and fiscal code are not set.'))
        if partner.fiscalcode:
            fatturapa.FatturaElettronicaHeader.\
                TerzoIntermediarioOSoggettoEmittente.\
                DatiAnagrafici.CodiceFiscale = partner.fiscalcode
        if partner.vat:
            fatturapa.FatturaElettronicaHeader.\
                TerzoIntermediarioOSoggettoEmittente.\
                DatiAnagrafici.IdFiscaleIVA = IdFiscaleType(
                    IdPaese=partner.vat[0:2], IdCodice=partner.vat[2:])
        fatturapa.FatturaElettronicaHeader.\
            TerzoIntermediarioOSoggettoEmittente.\
            DatiAnagrafici.Anagrafica = AnagraficaType(
                Denominazione=partner.name)
        if partner.eori_code:
            fatturapa.FatturaElettronicaHeader.\
                TerzoIntermediarioOSoggettoEmittente.\
                DatiAnagrafici.Anagrafica.CodEORI = partner.eori_code
        fatturapa.FatturaElettronicaHeader.SoggettoEmittente = 'TZ'
        return True

    def _setSedeCessionario(self, partner, parent, fatturapa):

        mode = partner.type_inv_addr
        mode = mode if mode not in ('SO','FR') else 'parent'
        country_id = self._get_partner_field(partner, parent,
                                             'country_id', mode=mode)
        if not country_id:
            raise UserError(
                _('Customer country is not set.'))
        street = self._get_partner_field(partner, parent,
                                         'street', mode=mode)
        zip = self._get_partner_field(partner, parent,
                                      'zip', mode=mode)
        city = self._get_partner_field(partner, parent,
                                       'city', mode=mode)
        state_id = self._get_partner_field(partner, parent,
                                           'state_id', mode=mode)
        if not street:
            raise UserError(
                _('Customer street is not set.'))
        if mode == 'parent':
            codice_destinatario = CODE_NONE_EU
        else:
            codice_destinatario = self._get_partner_field(
                partner, parent, 'codice_destinatario', mode=mode)
        if codice_destinatario != CODE_NONE_EU and not zip:
            raise UserError(
                _('Customer ZIP is not set.'))
        if not city:
            raise UserError(
                _('Customer city is not set.'))
        if codice_destinatario != CODE_NONE_EU and not state_id:
            raise UserError(
                _('Customer province is not set.'))

        if codice_destinatario != CODE_NONE_EU:
            zip = zip
        else:
            zip = '00000'
        if codice_destinatario != CODE_NONE_EU:
            province = state_id.code
        else:
            province = 'EE'
        # TODO: manage address number in <NumeroCivico>
        fatturapa.FatturaElettronicaHeader.CessionarioCommittente.Sede = (
            IndirizzoType(
                Indirizzo=street,
                CAP=zip,
                Comune=city,
                Provincia=province,
                Nazione=country_id.code))
        return True

    def _setCessionarioStabileOrganizzazione(self, partner, parent, fatturapa):
        mode = 'SO'
        country_id = self._get_partner_field(partner, parent,
                                             'country_id', mode=mode)
        if not country_id:
            raise UserError(
                _('Customer Stabile Organization country is not set.'))
        country_code = country_id.code
        street = self._get_partner_field(partner, parent,
                                         'street', mode=mode)
        zip = self._get_partner_field(partner, parent,
                                      'zip', mode=mode)
        city = self._get_partner_field(partner, parent,
                                       'city', mode=mode)
        state_id = self._get_partner_field(partner, parent,
                                           'state_id', mode=mode)
        if not street:
            raise UserError(
                _('Customer Stabile Organization street is not set.'))
        if not zip:
            raise UserError(
                _('Customer Stabile Organization ZIP is not set.'))
        if not city:
            raise UserError(
                _('Customer Stabile Organization city is not set.'))
        if not state_id:
            raise UserError(
                _('Customer Stabile Organization province is not set.'))

        zip = zip
        province = state_id.code
        fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
            StabileOrganizzazione = (IndirizzoType(Indirizzo=street,
                                                   CAP=zip,
                                                   Comune=city,
                                                   Provincia=province,
                                                   Nazione=country_code))
        return True

    def _setCessionarioRappresentanteFiscale(self, partner, parent, fatturapa):
        mode = 'FR'
        company_type = self._get_partner_field(
            partner, parent, 'company_type', mode=mode)
        if company_type == 'company':
            name = self._get_partner_field(
                partner, parent, 'name', mode=mode)
            if not name:
                raise UserError(
                    _('Customer Fiscal Representative name is not set.'))
        elif company_type == 'person':
            lastname = self._get_partner_field(
                partner, parent, 'lastname', mode=mode)
            firstname = self._get_partner_field(
                partner, parent, 'firstname', mode=mode)
            if not lastname or not firstname:
                raise UserError(
                    _('Customer Stabile Organization must have '
                      'name and surname.'))
        country_id = self._get_partner_field(partner, parent,
                                             'country_id', mode=mode)
        if not country_id:
            raise UserError(
                _('Customer Stabile Organization country is not set.'))
        vat = self._get_partner_field(
            partner, parent, 'vat', mode=mode)
        if not vat:
            raise UserError(
                _('Customer Stabile Organization vat is not set.'))
        country_code, vat_number = self._split_vat_n_country(vat)
        if country_code != country_id.code:
            raise UserError(
                _('Customer Stabile Organization vat country'
                  ' is different from from address country.'))
        fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
            RappresentanteFiscale = RappresentanteFiscaleCessionarioType()
        if company_type == 'company': 
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
                RappresentanteFiscale.Denominazione=name
        else:
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
                RappresentanteFiscale(Nome=firstname,
                                      Cognome=lastname,)
        if partner.vat:
            fatturapa.FatturaElettronicaHeader.CessionarioCommittente.\
                RappresentanteFiscale.IdFiscaleIVA = IdFiscaleType(
                    IdPaese=country_code,
                    IdCodice=vat_number)
        return True

    def setRappresentanteFiscale(self, company, fatturapa):
        if company.fatturapa_tax_representative:
            self._setDatiAnagraficiRappresentanteFiscale(
                company.fatturapa_tax_representative, fatturapa)
        return True

    def setCessionarioCommittente(self, partner, parent, fatturapa):
        fatturapa.FatturaElettronicaHeader.CessionarioCommittente = (
            CessionarioCommittenteType())
        self._setDatiAnagraficiCessionario(partner, parent, fatturapa)
        self._setSedeCessionario(partner, parent, fatturapa)
        mode = partner.type_inv_addr
        if mode == 'SO':
            self._setCessionarioStabileOrganizzazione(partner,
                                                      parent,
                                                      fatturapa)
        elif mode == 'FR':
            self._setCessionarioRappresentanteFiscale(partner,
                                                      parent,
                                                      fatturapa)

    def setTerzoIntermediarioOSoggettoEmittente(self, company, fatturapa):
        if company.fatturapa_sender_partner:
            self._setTerzoIntermediarioOSoggettoEmittente(
                company.fatturapa_sender_partner, fatturapa)
        return True

    def setTipoDocumento(self, invoice):
        if invoice.invoice_type_id:
            TipoDocumento = invoice.invoice_type_id.code
        elif invoice.type == 'out_refund':
            TipoDocumento = 'TD04'
        else:
            TipoDocumento = 'TD01'
        return TipoDocumento

    def setDatiGeneraliDocumento(self, invoice, body):

        # TODO DatiSAL

        body.DatiGenerali = DatiGeneraliType()
        if not invoice.number:
            raise UserError(
                _('Invoice does not have a number.'))

        TipoDocumento = self.setTipoDocumento(invoice)
        ImportoTotaleDocumento = invoice.amount_total
        # /!\ OCA split payment has total_amount w/o VAT e amount_sp positive
        # OIA split payment has total_amount with VTA and amount_sp negative
        # if invoice.split_payment:
        #     ImportoTotaleDocumento += invoice.amount_sp
        body.DatiGenerali.DatiGeneraliDocumento = DatiGeneraliDocumentoType(
            TipoDocumento=TipoDocumento,
            Divisa=invoice.currency_id.name,
            Data=invoice.date_invoice,
            Numero=invoice.number,
            ImportoTotaleDocumento='%.2f' % ImportoTotaleDocumento)

        # TODO: DatiRitenuta, DatiBollo, DatiCassaPrevidenziale,
        # ScontoMaggiorazione, Arrotondamento,

        if invoice.comment:
            # max length of Causale is 200
            caus_list = invoice.comment.split('\n')
            for causale in caus_list:
                if not causale:
                    continue
                causale = self._wep_text(causale)
                body.DatiGenerali.DatiGeneraliDocumento.Causale.append(causale)

        if invoice.company_id.fatturapa_art73:
            body.DatiGenerali.DatiGeneraliDocumento.Art73 = 'SI'
        return True

    def setRelatedDocumentTypes(self, invoice, body):
        for line in invoice.invoice_line_ids:
            for related_document in line.related_documents:
                doc_type = RELATED_DOCUMENT_TYPES[related_document.type]
                documento = DatiDocumentiCorrelatiType()
                if related_document.name:
                    documento.IdDocumento = related_document.name
                if related_document.lineRef:
                    documento.RiferimentoNumeroLinea.append(
                        line.ftpa_line_number)
                if related_document.date:
                    documento.Data = related_document.date
                if related_document.numitem:
                    documento.NumItem = related_document.numitem
                if related_document.code:
                    documento.CodiceCommessaConvenzione = related_document.code
                if related_document.cup:
                    documento.CodiceCUP = related_document.cup
                if related_document.cig:
                    documento.CodiceCIG = related_document.cig
                getattr(body.DatiGenerali, doc_type).append(documento)
        for related_document in invoice.related_documents:
            doc_type = RELATED_DOCUMENT_TYPES[related_document.type]
            documento = DatiDocumentiCorrelatiType()
            if related_document.name:
                documento.IdDocumento = related_document.name
            if related_document.date:
                documento.Data = related_document.date
            if related_document.numitem:
                documento.NumItem = related_document.numitem
            if related_document.code:
                documento.CodiceCommessaConvenzione = related_document.code
            if related_document.cup:
                documento.CodiceCUP = related_document.cup
            if related_document.cig:
                documento.CodiceCIG = related_document.cig
            getattr(body.DatiGenerali, doc_type).append(documento)
        return True

    def setDatiTrasporto(self, invoice, body):
        return True

    def setDatiDDT(self, invoice, body):
        return True

    def _get_prezzo_unitario(self, line):
        res = line.price_unit
        if (
            line.invoice_line_tax_ids and
            line.invoice_line_tax_ids[0].price_include
        ):
            res = line.price_unit / (
                1 + (line.invoice_line_tax_ids[0].amount / 100))
        return res

    def setDettaglioLinee(self, invoice, body):

        body.DatiBeniServizi = DatiBeniServiziType()
        # TipoCessionePrestazione not handled

        line_no = 1
        price_precision = max(2, self.env['decimal.precision'].precision_get(
            'Product Price'))
        uom_precision = max(2, self.env['decimal.precision'].precision_get(
            'Product Unit of Measure'))
        for line in invoice.invoice_line_ids:
            if not line.invoice_line_tax_ids:
                raise UserError(
                    _("Invoice line %s does not have tax") % line.name)
            if len(line.invoice_line_tax_ids) > 1:
                raise UserError(
                    _("Too many taxes for invoice line %s.") % line.name)
            aliquota = line.invoice_line_tax_ids[0].amount
            AliquotaIVA = '%.2f' % (aliquota)
            line.ftpa_line_number = line_no
            prezzo_unitario = self._get_prezzo_unitario(line)
            DettaglioLinea = DettaglioLineeType(
                NumeroLinea=str(line_no),
                # can't insert newline with pyxb
                # see https://tinyurl.com/ycem923t
                # and '&#10;' would not be correctly visualized anyway
                # (for example firefox replaces '&#10;' with space
                Descrizione=self._wep_text(line.name),
                PrezzoUnitario=('%.' + str(
                    price_precision
                ) + 'f') % prezzo_unitario,
                Quantita=('%.' + str(
                    uom_precision
                ) + 'f') % line.quantity,
                UnitaMisura=line.uom_id and (
                    unidecode(line.uom_id.name)) or None,
                PrezzoTotale='%.2f' % line.price_subtotal,
                AliquotaIVA=AliquotaIVA)
            if line.discount:
                ScontoMaggiorazione = ScontoMaggiorazioneType(
                    Tipo='SC',
                    Percentuale='%.2f' % line.discount
                )
                DettaglioLinea.ScontoMaggiorazione.append(ScontoMaggiorazione)
            if aliquota == 0.0:
                if not line.invoice_line_tax_ids[0].nature_id:
                    raise UserError(
                        _("No 'nature' field for tax %s.") %
                        line.invoice_line_tax_ids[0].name)
                DettaglioLinea.Natura = line.invoice_line_tax_ids[
                    0
                ].nature_id.code
            if line.admin_ref:
                DettaglioLinea.RiferimentoAmministrazione = line.admin_ref
            if line.product_id:
                if line.product_id.default_code:
                    CodiceArticolo = CodiceArticoloType(
                        CodiceTipo='ODOO',
                        CodiceValore=line.product_id.default_code
                    )
                    DettaglioLinea.CodiceArticolo.append(CodiceArticolo)
                if line.product_id.barcode:
                    CodiceArticolo = CodiceArticoloType(
                        CodiceTipo='EAN',
                        CodiceValore=line.product_id.barcode
                    )
                    DettaglioLinea.CodiceArticolo.append(CodiceArticolo)
            line_no += 1

            body.DatiBeniServizi.DettaglioLinee.append(DettaglioLinea)

        return True

    def setDatiRiepilogo(self, invoice, body):
        for tax_line in invoice.tax_line_ids:
            tax = tax_line.tax_id
            riepilogo = DatiRiepilogoType(
                AliquotaIVA='%.2f' % tax.amount,
                ImponibileImporto='%.2f' % tax_line.base,
                Imposta='%.2f' % tax_line.amount
                )
            if tax.amount == 0.0:
                if not tax.nature_id:
                    raise UserError(
                        _("No 'nature' field for tax %s") % tax.name)
                riepilogo.Natura = tax.nature_id.code
                if not tax.law_reference:
                    raise UserError(
                        _("No 'law reference' field for tax %s.") % tax.name)
                riepilogo.RiferimentoNormativo = tax.law_reference
            if tax.payability:
                riepilogo.EsigibilitaIVA = tax.payability
            # TODO

            # el.remove(el.find('SpeseAccessorie'))
            # el.remove(el.find('Arrotondamento'))

            body.DatiBeniServizi.DatiRiepilogo.append(riepilogo)

        return True

    def setDatiBanca(self, DettaglioPagamento, bank_id, company=None):
        if not bank_id and company:
            for bank in company.partner_id.bank_ids:
                if bank.acc_number and IBAN_PATTERN.match(bank.acc_number):
                    bank_id = bank
                    break
        if bank_id:
            if bank_id.bank_name:
                DettaglioPagamento.IstitutoFinanziario = (
                    bank_id.bank_name)
            if bank_id.acc_number:
                DettaglioPagamento.IBAN = (
                    bank_id.acc_number.replace(' ', '')
                )
            if bank_id.bank_bic:
                DettaglioPagamento.BIC = (
                    bank_id.bank_bic)
        return DettaglioPagamento

    def setDatiPagamento(self, invoice, body):
        if invoice.payment_term_id:
            DatiPagamento = DatiPagamentoType()
            if not invoice.payment_term_id.fatturapa_pt_id:
                raise UserError(
                    _('Payment term %s does not have a linked e-invoice '
                      'payment term.') % invoice.payment_term_id.name)
            if not invoice.payment_term_id.fatturapa_pm_id:
                raise UserError(
                    _('Payment term %s does not have a linked e-invoice '
                      'payment method.') % invoice.payment_term_id.name)
            DatiPagamento.CondizioniPagamento = (
                invoice.payment_term_id.fatturapa_pt_id.code)
            move_line_pool = self.env['account.move.line']
            payment_line_ids = invoice.get_receivable_line_ids()
            TipoDocumento = self.setTipoDocumento(invoice)
            credit_amount = 0.0
            for move_line_id in payment_line_ids:
                move_line = move_line_pool.browse(move_line_id)
                # OIA split-payment management
                if TipoDocumento == 'TD04':
                    if move_line.debit > 0.0:
                        credit_amount = move_line.credit
                        continue
                else:
                    if move_line.credit > 0.0:
                        credit_amount = move_line.credit
                        continue
                if TipoDocumento == 'TD04':
                    ImportoPagamento = '%.2f' % (move_line.credit -
                                                 credit_amount)
                else:
                    ImportoPagamento = '%.2f' % (move_line.debit -
                                                 credit_amount)
                credit_amount = 0.0
                if invoice.payment_term_id.note:
                    payment_term_des = invoice.payment_term_id.note
                else:
                    payment_term_des = invoice.payment_term_id.name
                DettaglioPagamento = DettaglioPagamentoType(
                    ModalitaPagamento=(
                        invoice.payment_term_id.fatturapa_pm_id.code),
                    DataScadenzaPagamento=move_line.date_maturity,
                    ImportoPagamento=ImportoPagamento,
                    CodicePagamento=payment_term_des,
                    )
                if invoice.partner_bank_id:
                    DettaglioPagamento = self.setDatiBanca(
                        DettaglioPagamento,
                        invoice.partner_bank_id)
                elif (invoice.payment_term_id.fatturapa_pm_id and
                        invoice.payment_term_id.fatturapa_pm_id.code in
                        PAYTYPE_BNK_CUSTOMER and
                        invoice.partner_id.bank_ids
                ):
                    DettaglioPagamento = self.setDatiBanca(
                        DettaglioPagamento,
                        invoice.partner_id.bank_ids[0])
                elif (invoice.payment_term_id.fatturapa_pm_id and
                        invoice.payment_term_id.fatturapa_pm_id.code in
                        PAYTYPE_BNK_COMPANY and
                        invoice.company_id.partner_id.bank_ids
                ):
                    DettaglioPagamento = self.setDatiBanca(
                        DettaglioPagamento, None, company = invoice.company_id)
                DatiPagamento.DettaglioPagamento.append(DettaglioPagamento)
            body.DatiPagamento.append(DatiPagamento)
        return True

    def setAttachments(self, invoice, body):
        if invoice.fatturapa_doc_attachments:
            for doc_id in invoice.fatturapa_doc_attachments:
                AttachDoc = AllegatiType(
                    NomeAttachment=doc_id.datas_fname,
                    Attachment=base64.decodestring(doc_id.datas)
                )
                body.Allegati.append(AttachDoc)
        return True

    def setFatturaElettronicaHeader(self, company, partner, parent, fatturapa):
        fatturapa.FatturaElettronicaHeader = (
            FatturaElettronicaHeaderType())
        self.setDatiTrasmissione(company, partner, parent, fatturapa)
        self.setCedentePrestatore(company, fatturapa)
        self.setRappresentanteFiscale(company, fatturapa)
        self.setCessionarioCommittente(partner, parent, fatturapa)
        self.setTerzoIntermediarioOSoggettoEmittente(company, fatturapa)

    def setFatturaElettronicaBody(self, inv, FatturaElettronicaBody):

        self.setDatiGeneraliDocumento(inv, FatturaElettronicaBody)
        self.setDettaglioLinee(inv, FatturaElettronicaBody)
        self.setDatiDDT(inv, FatturaElettronicaBody)
        self.setDatiTrasporto(inv, FatturaElettronicaBody)
        self.setRelatedDocumentTypes(inv, FatturaElettronicaBody)
        self.setDatiRiepilogo(inv, FatturaElettronicaBody)
        self.setDatiPagamento(inv, FatturaElettronicaBody)
        self.setAttachments(inv, FatturaElettronicaBody)

    def getPartnerCompanyId(self, invoice_ids):

        invoice_model = self.env['account.invoice']
        partner = False
        parent = False
        company = False
        invoices = invoice_model.browse(invoice_ids)
        for invoice in invoices:
            if not partner:
                partner = invoice.partner_id
            if invoice.partner_id != partner:
                raise UserError(
                    _('Invoices must belong to the same partner.'))
            if not company:
                company = invoice.company_id
            if invoice.company_id != company:
                raise UserError(
                    _('Invoices must belong to the same company'))
        if partner and partner.type == 'invoice':
            parent = partner.parent_id
        return company, partner, parent

    def group_invoices_by_partner(self):
        invoice_ids = self.env.context.get('active_ids', False)
        res = {}
        for invoice in self.env['account.invoice'].browse(invoice_ids):
            if invoice.partner_id.id not in res:
                res[invoice.partner_id.id] = []
            res[invoice.partner_id.id].append(invoice.id)
        return res

    def exportFatturaPA(self):
        invoice_model = self.env['account.invoice']
        invoices_by_partner = self.group_invoices_by_partner()
        attachments = self.env['fatturapa.attachment.out']
        for partner_id in invoices_by_partner:
            invoice_ids = invoices_by_partner[partner_id]
            company, partner, parent = self.getPartnerCompanyId(invoice_ids)
            fatturapa = FatturaElettronica(
                versione=self._getFormatoTrasmissione(partner,
                                                      parent))
            context_partner = self.env.context.copy()
            context_partner.update({'lang': partner.lang,
                                    'company_id': company.id})
            try:
                self.with_context(context_partner).setFatturaElettronicaHeader(
                    company, partner, parent, fatturapa)
                for invoice_id in invoice_ids:
                    inv = invoice_model.with_context(context_partner).browse(
                        invoice_id)
                    if inv.fatturapa_attachment_out_id:
                        raise UserError(
                            _("Invoice %s has e-invoice export file yet.") % (
                                inv.number))
                    invoice_body = FatturaElettronicaBodyType()
                    self.with_context(
                        context_partner
                    ).setFatturaElettronicaBody(
                        inv, invoice_body)
                    fatturapa.FatturaElettronicaBody.append(invoice_body)
                    # TODO DatiVeicoli

                number = self.setProgressivoInvio(fatturapa)
            except (SimpleFacetValueError, SimpleTypeValueError) as e:
                raise UserError(
                    (unicode(e)))

            attach = self.saveAttachment(fatturapa, number)
            attachments |= attach

            for invoice_id in invoice_ids:
                inv = invoice_model.browse(invoice_id)
                inv.write({'fatturapa_attachment_out_id': attach.id})

        action = {
            'view_type': 'form',
            'name': "Export Electronic Invoice",
            'res_model': 'fatturapa.attachment.out',
            'type': 'ir.actions.act_window',
            }
        if len(attachments) == 1:
            action['view_mode'] = 'form'
            action['res_id'] = attachments[0].id
        else:
            action['view_mode'] = 'tree,form'
            action['domain'] = [('id', 'in', attachments.ids)]
        return action
