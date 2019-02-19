# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
import base64
import os
import shlex
import subproces
from lxml import etree
import logging

from openerp.osv import orm, fields
from openerp.addons.base_iban import base_iban
from odoo.addons.l10n_it_ade.bindings import fatturapa_v_1_2
from openerp.osv.osv import except_osv
from odoo.tools import float_is_zero
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class WizardImportFatturapa(orm.TransientModel):
    _name = "wizard.import.fatturapa"
    _description = "Import E-bill"

    _columns = {
        'e_invoice_detail_level': fields.selection([
            ('0', 'Minimo'),
            # ('1', 'Aliquote'),
            ('2', 'Massimo'),
        ], string="Livello di dettaglio Fatture elettroniche",
            help="Livello minimo: La fattura passiva viene creata senza righe; "
                 "sara' l'utente a doverle creare in base a quanto indicato dal "
                 "fornitore nella fattura elettronica\n"
                 # "Livello Aliquote: viene creata una riga fattura per ogni "
                 # "aliquota presente nella fattura elettronica\n"
                 "Livello Massimo: tutte le righe presenti nella fattura "
                 "elettronica vengono create come righe della fattura passiva",
            required=True
        )
    }

    def default_get(self, cr, uid, fields, context={}):
        res = super(WizardImportFatturapa, self).default_get(cr, uid, fields, context)
        res['e_invoice_detail_level'] = '2'
        fatturapa_attachment_ids = context.get('active_ids', False)
        fatturapa_attachment_obj = self.pool.get('fatturapa.attachment.in')
        partnerList = []
        for fatturapa_attachment_id in fatturapa_attachment_ids:
            fatturapa_attachment = fatturapa_attachment_obj.browse(cr, uid,
                fatturapa_attachment_id)
            if fatturapa_attachment.in_invoice_ids:
                raise except_osv(_('Error' ),
                             _("File %s is linked to invoices yet") % fatturapa_attachment.name)
            if fatturapa_attachment.xml_supplier_id not in partnerList:
                partnerList.append(fatturapa_attachment.xml_supplier_id)
            if len(partnerList) == 1:
                res['e_invoice_detail_level'] = (
                    partnerList[0].e_invoice_detail_level)
        return res

    def CountryByCode(self, cr, uid, CountryCode, context=None):
        country_model = self.pool['res.country']
        return country_model.search(
            cr, uid, [('code', '=', CountryCode)], context=context)

    def ProvinceByCode(self, cr, uid, provinceCode, context=None):
        province_model = self.pool['res.country.state']
        return province_model.search(cr, uid, [
            ('code', '=', provinceCode),
            ('country_id.code', '=', 'IT')
        ])

    def log_inconsistency(self, message, context):
        if context.get('inconsistencies'):
                context['inconsistencies'] += '\n'
        context['inconsistencies'] += message

    def check_partner_base_data(
        self, cr, uid, partner_id, DatiAnagrafici, context=None
    ):
        context = context or {}
        context['inconsistencies'] = ''
        partner = self.pool['res.partner'].browse(
            cr, uid, partner_id, context=context)
        if (
            DatiAnagrafici.Anagrafica.Denominazione and
            partner.name != DatiAnagrafici.Anagrafica.Denominazione
        ):
            self.log_inconsistency(_(
                "Company Name field contains '%s'."
                " Your System contains '%s'"
            ) % (DatiAnagrafici.Anagrafica.Denominazione, partner.name),
            context)
        if (
            DatiAnagrafici.Anagrafica.Nome and
            partner.firstname != DatiAnagrafici.Anagrafica.Nome
        ):
            self.log_inconsistency(_(
                "Name field contains '%s'."
                " Your System contains '%s'"
            ) % (DatiAnagrafici.Anagrafica.Nome, partner.firstname),
            context)
        if (
            DatiAnagrafici.Anagrafica.Cognome and
            partner.lastname != DatiAnagrafici.Anagrafica.Cognome
        ):
            self.log_inconsistency(
                _(
                    "Surname field contains '%s'."
                    " Your System contains '%s'"
                )
                % (DatiAnagrafici.Anagrafica.Cognome, partner.lastname),
            context)

    def getCompany(self, DatiAnagrafici):
        companies = []
        vat = ''
        if DatiAnagrafici:
            company_model = self.pool['res.company']
            if DatiAnagrafici.IdFiscaleIVA:
                vat = "%s%s" % (
                    DatiAnagrafici.IdFiscaleIVA.IdPaese,
                    DatiAnagrafici.IdFiscaleIVA.IdCodice
                )
                where = [('vat', '=', vat)]
                companies = company_model.search(where)
        if not vat:
            self.log_inconsistency(
                _('E-Invoice without VAT number'))
            return self.pool.user.company_id
        if not companies and vat:
            raise UserError(
                _("VAT number %s of customer invoice "
                  "is not the same of the current company" % vat))
        return companies[0]

    def getPartnerBase(self, DatiAnagrafici):
        if not DatiAnagrafici:
            return False
        partner_model = self.pool['res.partner']
        cf = DatiAnagrafici.CodiceFiscale or False
        vat = False
        if DatiAnagrafici.IdFiscaleIVA:
            vat = "%s%s" % (
                DatiAnagrafici.IdFiscaleIVA.IdPaese,
                DatiAnagrafici.IdFiscaleIVA.IdCodice
            )
        where = []
        partner_ids = []
        if vat:
            where.append(('vat', '=', vat))
        if cf:
            where.append(('fiscalcode', '=', cf))
        if where:
            partner_ids = partner_model.search(cr, uid, where)
        if not partner_ids and vat:
            where = [('vat', '=', vat)]
            partner_ids = partner_model.search(cr, uid, where)
        commercial_partner = False
        if len(partner_ids) > 1:
            for partner in partner_model.browse(
                cr, uid, partner_ids, context=context
            ):
                if (
                    commercial_partner and
                    partner.commercial_partner_id.id != commercial_partner
                ):
                    raise orm.except_orm(
                        _('Error !'),
                        _("Two distinct partners with "
                          "VAT number %s and Fiscal Code %s already "
                          "present in db." %
                          (vat, cf))
                    )
        if partner_ids:
            commercial_partner_id = partner_ids[0]
            self.check_partner_base_data(
                cr, uid, commercial_partner_id, DatiAnagrafici, context=context)
            return commercial_partner_id
        else:
            # partner to be created
            country_id = False
            if DatiAnagrafici.IdFiscaleIVA:
                CountryCode = DatiAnagrafici.IdFiscaleIVA.IdPaese
                country_ids = self.CountryByCode(
                    cr, uid, CountryCode, context=context)
                if country_ids:
                    country_id = country_ids[0]
                else:
                    raise orm.except_orm(
                        _('Error !'),
                        _("Country Code %s not found in system") % CountryCode
                    )
            vals = {
                'vat': vat,
                'fiscalcode': cf,
                'customer': False,
                'supplier': True,
                'is_company': (
                    DatiAnagrafici.Anagrafica.Denominazione and True or False),
                'eori_code': DatiAnagrafici.Anagrafica.CodEORI or '',
                'country_id': country_id,
            }
            if DatiAnagrafici.Anagrafica.Denominazione:
                vals['name'] = DatiAnagrafici.Anagrafica.Denominazione
            else:
                vals['name'] = '%s %s' % (DatiAnagrafici.Anagrafica.Cognome,
                                          DatiAnagrafici.Anagrafica.Nome)
            return partner_model.create(cr, uid, vals, context=context)

    def getCedPrest(self, cr, uid, cedPrest, context=None):
        context = context or {}
        context['inconsistencies'] = ''
        partner_model = self.pool['res.partner']
        partner_id = self.getPartnerBase(
            cr, uid, cedPrest.DatiAnagrafici, context=context)
        fiscalPosModel = self.pool['fatturapa.fiscal_position']
        vals = {}
        if partner_id:
            vals = {
                'street': cedPrest.Sede.Indirizzo,
                'zip': cedPrest.Sede.CAP,
                'city': cedPrest.Sede.Comune,
                'register': cedPrest.DatiAnagrafici.AlboProfessionale or ''
            }
            if cedPrest.DatiAnagrafici.ProvinciaAlbo:
                ProvinciaAlbo = cedPrest.DatiAnagrafici.ProvinciaAlbo
                prov_ids = self.ProvinceByCode(
                    cr, uid, ProvinciaAlbo, context=context)
                if not prov_ids:
                    self.log_inconsistency(
                        _('Register Province ( %s ) not present '
                          'in your system')
                        % ProvinciaAlbo,
                    context)
                else:
                    vals['register_province'] = prov[0]
            if cedPrest.Sede.Provincia:
                Provincia = cedPrest.Sede.Provincia
                prov_sede = self.ProvinceByCode(cr, uid, Provincia, context)
                if not prov_sede:
                    self.log_inconsistency(
                        _('Province ( %s ) not present in your system')
                        % Provincia,
                    context)
                else:
                    vals['state_id'] = prov_sede[0].id

            vals['register_code'] = (
                cedPrest.DatiAnagrafici.NumeroIscrizioneAlbo)
            vals['register_regdate'] = (
                cedPrest.DatiAnagrafici.DataIscrizioneAlbo)

            if cedPrest.DatiAnagrafici.RegimeFiscale:
                rfPos = cedPrest.DatiAnagrafici.RegimeFiscale
                FiscalPos = fiscalPosModel.search(
                    cr, uid,
                    [('code', '=', rfPos)]
                )
                if not FiscalPos:
                    raise UserError(
                        _('Tax Regime %s not present in your system.')
                        % rfPos,
                    context)
                else:
                    vals['register_fiscalpos'] = FiscalPos[0]

            if cedPrest.IscrizioneREA:
                REA = cedPrest.IscrizioneREA
                vals['rea_code'] = REA.NumeroREA
                office_ids = self.ProvinceByCode(
                    cr, uid, REA.Ufficio, context=context)
                if not office_ids:
                    self.log_inconsistency(
                        _(
                            'REA Office Province Code ( %s ) not present in '
                            'your system'
                        ) % REA.Ufficio,
                    context)
                else:
                    office_id = office_ids[0]
                    vals['rea_office'] = office_id
                    vals['rea_capital'] = REA.CapitaleSociale or 0.0
                    vals['rea_member_type'] = REA.SocioUnico or False
                    vals['rea_liquidation_state'] = REA.StatoLiquidazione or False

            if cedPrest.Contatti:
                vals['phone'] = cedPrest.Contatti.Telefono
                vals['email'] = cedPrest.Contatti.Email
                vals['fax'] = cedPrest.Contatti.Fax
            partner_model.write(cr, uid, partner_id, vals, context=context)
        return partner_id

    def getCarrirerPartner(self, cr, uid, Carrier, context=None):
        partner_model = self.pool['res.partner']
        partner_id = self.getPartnerBase(
            cr, uid, Carrier.DatiAnagraficiVettore, context=context)
        if partner_id:
            vals = {
                'license_number':
                Carrier.DatiAnagraficiVettore.NumeroLicenzaGuida or '',
            }
            partner_model.write(cr, uid, partner_id, vals, context=context)
        return partner_id

    def _prepareInvoiceLine(
        self, cr, uid, invoice_id, line, type, credit_account_id, context=None
    ):
        retLine = self._prepare_generic_line_data(line)
        retLine.update({
            'name': line.Descrizione,
            'sequence': int(line.NumeroLinea),
            'account_id': credit_account_id,
        })
        if line.PrezzoUnitario:
            retLine['price_unit'] = float(line.PrezzoUnitario)
        if line.Quantita:
            retLine['quantity'] = float(line.Quantita)
        if (
            line.PrezzoTotale and line.PrezzoUnitario and line.Quantita and
            line.ScontoMaggiorazione
        ):
            retLine['discount'] = self._computeDiscount(line)
        if line.RiferimentoAmministrazione:
            retLine['admin_ref'] = line.RiferimentoAmministrazione
        if wt_found and line.Ritenuta:
            retLine['invoice_line_tax_wt_ids'] = [(6, 0, [wt_found.id])]

        return retLine

    def get_tax(self, cr, uid, company_id, AliquotaIVA, Natura):
        account_tax_model = self.pool['account.tax']
        ir_values = self.pool['ir.values']
        AliquotaIVA_fp = float(AliquotaIVA)
        supplier_taxes_ids = ir_values.get_default(
            cr, uid, 'product.product', 'supplier_taxes_id',
            company_id=company_id
        )
        def_purchase_tax = False
        if supplier_taxes_ids:
            def_purchase_tax = account_tax_model.browse(
                cr, uid, supplier_taxes_ids, context=context)[0]
        where = []
        where.append(('company_id', '=', company_id))
        where.append(('type_tax_use', 'in', ('purchase', 'all')))
        where.append(('amount', '=', AliquotaIVA_fp))
        if Natura:
            where.append(('nature_id.code', '=', Natura))
        account_taxes = account_tax_model.search(where, order="sequence")
        if not account_taxes:
            raise UserError(
                _('No tax with percentage '
                  '%s and nature %s found. Please configure this tax.')
                % (AliquotaIVA, Natura))
        if len(account_taxes) > 1:
            self.log_inconsistency(
                _('Too many taxes with percentage '
                  '%s and nature %s found.')
                % (AliquotaIVA, Natura))
        if def_purchase_tax and def_purchase_tax.amount == AliquotaIVA_fp:
            account_tax_id = def_purchase_tax.id
        else:
            account_tax_id = account_taxes[0]
        return account_tax_id

    def get_natura(self, cr, uid, Natura):
        if Natura:
            tax_nature_ids = self.pool['italy.ade.tax.nature'].search(cr, uid, [
                ('code', '=', Natura)
            ])
            if not tax_nature_ids:
                self.log_inconsistency(
                    _("Tax kind %s not found") % Natura,
                )
                return False
            else:
                return tax_nature_ids[0]
        return False

    def _prepare_generic_line_data(self, line):
        retLine = {}
        company_id = self.pool['res.company']._company_default_get(
            'account.invoice.line').id
        account_tax = self.get_tax(company_id, line.AliquotaIVA, line.Natura)
        if account_tax:
            retLine['invoice_line_tax_ids'] = [(6, 0, [account_tax])]
        return retLine

    def get_line_product(self, cr, uid, line, partner):
        product = None
        supplier_info = self.pool['product.supplierinfo']
        if len(line.CodiceArticolo) == 1:
            supplier_code = line.CodiceArticolo[0].CodiceValore
            supplier_infos = supplier_info.search(cr, uid, [
                ('product_code', '=', supplier_code),
                ('name', '=', partner.id)
            ])
            if supplier_infos:
                products = supplier_infos.mapped('product_id')
                if len(products) == 1:
                    product = products[0]
                else:
                    templates = supplier_infos.mapped('product_tmpl_id')
                    if len(templates) == 1:
                        product = templates.product_variant_ids[0]
        if not product and partner.e_invoice_default_product_id:
            product = partner.e_invoice_default_product_id
        return product

    def adjust_accounting_data(self, cr, uid, product, line_vals, context={}):
        if product.product_tmpl_id.property_account_expense_id:
            line_vals['account_id'] = (
                product.product_tmpl_id.property_account_expense_id.id)
        elif (
            product.product_tmpl_id.categ_id.property_account_expense_categ_id
        ):
            line_vals['account_id'] = (
                product.product_tmpl_id.categ_id.
                property_account_expense_categ_id.id
            )
        account = self.pool['account.account'].browse(cr, uid, line_vals['account_id'])
        new_tax = None
        if len(product.product_tmpl_id.supplier_taxes_id) == 1:
            new_tax = product.product_tmpl_id.supplier_taxes_id[0]
        elif len(account.tax_ids) == 1:
            new_tax = account.tax_ids[0]
        if new_tax:
            line_tax_id = (
                line_vals.get('invoice_line_tax_ids') and
                line_vals['invoice_line_tax_ids'][0][2][0]
            )
            line_tax = self.pool['account.tax'].browse(cr, uid, line_tax_id)
            if new_tax.id != line_tax_id:
                if new_tax._get_tax_amount() != line_tax._get_tax_amount():
                    self.log_inconsistency(_(
                        "XML contains tax %s. Product %s has tax %s. Using "
                        "the XML one"
                    ) % (line_tax.name, product.name, new_tax.name))
                else:
                    # If product has the same amount of the one in XML,
                    # I use it. Typical case: 22% det 50%
                    line_vals['invoice_line_tax_ids'] = [
                        (6, 0, [new_tax.id])]

    def _prepareRelDocsLine(
        self, cr, uid, invoice_id, line, type, context=None
    ):
        res = []
        lineref = line.RiferimentoNumeroLinea or False
        IdDoc = line.IdDocumento or 'Error'
        Data = line.Data or False
        NumItem = line.NumItem or ''
        Code = line.CodiceCommessaConvenzione or ''
        Cig = line.CodiceCIG or ''
        Cup = line.CodiceCUP or ''
        invoice_lineid = False
        if lineref:
            for numline in lineref:
                invoice_lineid = False
                invoice_line_model = self.pool['account.invoice.line']
                invoice_line_ids = invoice_line_model.search(
                    cr, uid,
                    [
                        ('invoice_id', '=', invoice_id),
                        ('sequence', '=', int(numline)),
                    ], context=context)
                if invoice_line_ids:
                    invoice_lineid = invoice_line_ids[0]
                val = {
                    'type': type,
                    'name': IdDoc,
                    'lineRef': numline,
                    'invoice_line_id': invoice_lineid,
                    'invoice_id': invoice_id,
                    'date': Data,
                    'numitem': NumItem,
                    'code': Code,
                    'cig': Cig,
                    'cup': Cup,
                }
                res.append(val)
        else:
            val = {
                'type': type,
                'name': IdDoc,
                'invoice_line_id': invoice_lineid,
                'invoice_id': invoice_id,
                'date': Data,
                'numitem': NumItem,
                'code': Code,
                'cig': Cig,
                'cup': Cup
            }
            res.append(val)
        return res

    def _prepareWelfareLine(
        self, cr, uid, invoice_id, line, context=None
    ):
        res = []
        TipoCassa = line.TipoCassa or False
        AlCassa = line.AlCassa and (float(line.AlCassa) / 100) or None
        ImportoContributoCassa = (
            line.ImportoContributoCassa and
            float(line.ImportoContributoCassa) or None)
        ImponibileCassa = (
            line.ImponibileCassa and float(line.ImponibileCassa) or None)
        AliquotaIVA = (
            line.AliquotaIVA and (float(line.AliquotaIVA) / 100) or None)
        Ritenuta = line.Ritenuta or ''
        Natura = line.Natura or False
        tax_nature_id = self.get_natura(Natura)
        RiferimentoAmministrazione = line.RiferimentoAmministrazione or ''
        WelfareTypeModel = self.pool['welfare.fund.type']
        if not TipoCassa:
            raise orm.except_orm(
                _('Error!'),
                _('TipoCassa is not defined ')
            )
        WelfareTypeId = WelfareTypeModel.search(
            cr, uid,
            [('name', '=', TipoCassa)],
            context=context
        )

        res = {
            'welfare_rate_tax': AlCassa,
            'welfare_amount_tax': ImportoContributoCassa,
            'welfare_taxable': ImponibileCassa,
            'welfare_Iva_tax': AliquotaIVA,
            'subjected_withholding': Ritenuta,
            'tax_nature_id': tax_nature_id,
            'pa_line_code': RiferimentoAmministrazione,
            'invoice_id': invoice_id,
        }
        if not WelfareTypeId:
            raise orm.except_orm(
                _('Error'),
                _('TipoCassa %s is not present in your system') % TipoCassa)
        else:
            res['name'] = WelfareTypeId[0]

        return res

    def _prepareDiscRisePriceLine(
        self, cr, uid, id, line, context=None
    ):
        res = []
        Tipo = line.Tipo or False
        Percentuale = line.Percentuale and float(line.Percentuale) or 0.0
        Importo = line.Importo and float(line.Importo) or 0.0
        res = {
            'percentage': Percentuale,
            'amount': Importo,
            context.get('drtype'): id,
        }
        res['name'] = Tipo

        return res

    def _computeDiscount(
        self, cr, uid, DettaglioLinea, context=None
    ):
        line_total = float(DettaglioLinea.PrezzoTotale)
        line_unit = line_total / float(DettaglioLinea.Quantita)
        discount = (
            1 - (line_unit / float(DettaglioLinea.PrezzoUnitario))
        ) * 100.0
        return discount

    def _addGlobalDiscount(
        self, cr, uid, invoice_id, DatiGeneraliDocumento, context=None
    ):
        discount = 0.0
        if (
            DatiGeneraliDocumento.ScontoMaggiorazione and
            self.e_invoice_detail_level == '2'
        ):
            invoice = self.pool['account.invoice'].browse(
                cr, uid, invoice_id, context=context)
            invoice.button_compute(context=context, set_total=True)
            for DiscRise in DatiGeneraliDocumento.ScontoMaggiorazione:
                if DiscRise.Percentuale:
                    amount = (
                        invoice.amount_total * (
                            float(DiscRise.Percentuale) / 100))
                    if DiscRise.Tipo == 'SC':
                        discount -= amount
                    elif DiscRise.Tipo == 'MG':
                        discount += amount
                elif DiscRise.Importo:
                    if DiscRise.Tipo == 'SC':
                        discount -= float(DiscRise.Importo)
                    elif DiscRise.Tipo == 'MG':
                        discount += float(DiscRise.Importo)
            journal = self.get_purchase_journal(
                cr, uid, invoice.company_id, context=context)
            credit_account_id = journal.default_credit_account_id.id
            line_vals = {
                'invoice_id': invoice_id,
                'name': _(
                    "Global bill discount from document general data"),
                'account_id': credit_account_id,
                'price_unit': discount,
                'quantity': 1,
            }
            if self.pool.user.company_id.sconto_maggiorazione_product_id:
                sconto_maggiorazione_product = (
                    self.pool.user.company_id.sconto_maggiorazione_product_id)
                line_vals['product_id'] = sconto_maggiorazione_product.id
                line_vals['name'] = sconto_maggiorazione_product.name
                self.adjust_accounting_data(
                    sconto_maggiorazione_product, line_vals
                )
            self.pool['account.invoice.line'].create(line_vals)
        return True

    def _createPayamentsLine(
        self, cr, uid, payment_id, line, partner_id,
        context=None
    ):
        PaymentModel = self.pool['fatturapa.payment.detail']
        PaymentMethodModel = self.pool['fatturapa.payment_method']
        details = line.DettaglioPagamento or False
        if details:
            for dline in details:
                BankModel = self.pool['res.bank']
                PartnerBankModel = self.pool['res.partner.bank']
                method_id = PaymentMethodModel.search(
                    cr, uid,
                    [('code', '=', dline.ModalitaPagamento)],
                    context=context
                )
                if not method_id:
                    raise orm.except_orm(
                        _('Error!'),
                        _(
                            'Payment method %s is not defined in your system.'
                            % dline.ModalitaPagamento
                        )
                    )
                val = {
                    'recipient': dline.Beneficiario,
                    'fatturapa_pm_id': method_id[0],
                    'payment_term_start':
                    dline.DataRiferimentoTerminiPagamento or False,
                    'payment_days':
                    dline.GiorniTerminiPagamento or 0,
                    'payment_due_date':
                    dline.DataScadenzaPagamento or False,
                    'payment_amount':
                    dline.ImportoPagamento or 0.0,
                    'post_office_code':
                    dline.CodUfficioPostale or '',
                    'recepit_surname':
                    dline.CognomeQuietanzante or '',
                    'recepit_name':
                    dline.NomeQuietanzante or '',
                    'recepit_cf':
                    dline.CFQuietanzante or '',
                    'recepit_title':
                    dline.TitoloQuietanzante or '1',
                    'payment_bank_name':
                    dline.IstitutoFinanziario or '',
                    'payment_bank_iban':
                    dline.IBAN or '',
                    'payment_bank_abi':
                    dline.ABI or '',
                    'payment_bank_cab':
                    dline.CAB or '',
                    'payment_bank_bic':
                    dline.BIC or '',
                    'payment_bank': False,
                    'prepayment_discount':
                    dline.ScontoPagamentoAnticipato or 0.0,
                    'max_payment_date':
                    dline.DataLimitePagamentoAnticipato or False,
                    'penalty_amount':
                    dline.PenalitaPagamentiRitardati or 0.0,
                    'penalty_date':
                    dline.DataDecorrenzaPenale or False,
                    'payment_code':
                    dline.CodicePagamento or '',
                    'payment_data_id': payment_id
                }
                bankid = False
                payment_bank_id = False
                if dline.BIC:
                    bankids = BankModel.search(
                        cr, uid,
                        [('bic', '=', dline.BIC.strip())], context=context
                    )
                    if not bankids:
                        if not dline.IstitutoFinanziario:
                            self.log_inconsistency(
                                _("Name of Bank with BIC '%s' is not set."
                                  " Can't create bank") % dline.BIC
                            )
                        else:
                            bankid = BankModel.create(
                                cr, uid,
                                {
                                    'name': dline.IstitutoFinanziario,
                                    'bic': dline.BIC,
                                },
                                context=context
                            )
                    else:
                        bankid = bankids[0]
                if dline.IBAN:
                    SearchDom = [
                        ('state', '=', 'iban'),
                        (
                            'acc_number', '=',
                            base_iban._pretty_iban(dline.IBAN.strip())
                        ),
                        ('partner_id', '=', partner_id),
                    ]
                    payment_bank_id = False
                    payment_bank_ids = PartnerBankModel.search(
                        cr, uid, SearchDom, context=context)
                    if not payment_bank_ids and not bankid:
                        self.log_inconsistency(
                            _(
                                'BIC is required and not exist in Xml\n'
                                'Curr bank data is: \n'
                                'IBAN: %s\n'
                                'Bank Name: %s\n'
                            )
                            % (
                                dline.IBAN.strip() or '',
                                dline.IstitutoFinanziario or ''
                            )
                        )

                    elif not payment_bank_ids and bankid:
                        payment_bank_id = PartnerBankModel.create(
                            cr, uid,
                            {
                                'state': 'iban',
                                'acc_number': dline.IBAN.strip(),
                                'partner_id': partner_id,
                                'bank': bankid,
                                'bank_name': dline.IstitutoFinanziario,
                                'bank_bic': dline.BIC
                            },
                            context=context
                        )
                    if payment_bank_ids:
                        payment_bank_id = payment_bank_ids[0]

                if payment_bank_id:
                    val['payment_bank'] = payment_bank_id
                PaymentModel.create(cr, uid, val, context=context)
        return True

    # TODO sul partner?
    def set_StabileOrganizzazione(self, CedentePrestatore, invoice):
        if CedentePrestatore.StabileOrganizzazione:
            invoice.efatt_stabile_organizzazione_indirizzo = (
                CedentePrestatore.StabileOrganizzazione.Indirizzo)
            invoice.efatt_stabile_organizzazione_civico = (
                CedentePrestatore.StabileOrganizzazione.NumeroCivico)
            invoice.efatt_stabile_organizzazione_cap = (
                CedentePrestatore.StabileOrganizzazione.CAP)
            invoice.efatt_stabile_organizzazione_comune = (
                CedentePrestatore.StabileOrganizzazione.Comune)
            invoice.efatt_stabile_organizzazione_provincia = (
                CedentePrestatore.StabileOrganizzazione.Provincia)
            invoice.efatt_stabile_organizzazione_nazione = (
                CedentePrestatore.StabileOrganizzazione.Nazione)

    def get_purchase_journal(self, cr, uid, company, context=None):
        journal_model = self.pool['account.journal']
        journal_ids = journal_model.search(
            cr, uid,
            [
                ('type', '=', 'purchase'),
                ('company_id', '=', company.id),
                ('default_credit_account_id', '!=', False)
            ],
            limit=1, context=context)
        if not journal_ids:
            raise orm.except_orm(
                _('Error!'),
                _(
                    "Define a purchase journal "
                    "for this company: '%s' (id: %d)."
                ) % (company.name, company.id)
            )
        purchase_journal = journal_model.browse(
            cr, uid, journal_ids[0], context=context)
        return purchase_journal

    def create_e_invoice_line(self, line):
        vals = {
            'line_number': int(line.NumeroLinea or 0),
            'service_type': line.TipoCessionePrestazione,
            'name': line.Descrizione,
            'qty': float(line.Quantita or 0),
            'uom': line.UnitaMisura,
            'period_start_date': line.DataInizioPeriodo,
            'period_end_date': line.DataFinePeriodo,
            'unit_price': float(line.PrezzoUnitario or 0),
            'total_price': float(line.PrezzoTotale or 0),
            'tax_amount': float(line.AliquotaIVA or 0),
            'wt_amount': line.Ritenuta,
            'tax_nature': line.Natura,
            'admin_ref': line.RiferimentoAmministrazione,
        }
        einvoiceline = self.pool['einvoice.line'].create(vals)
        if line.CodiceArticolo:
            for caline in line.CodiceArticolo:
                self.pool['fatturapa.article.code'].create(
                    {
                        'name': caline.CodiceTipo or '',
                        'code_val': caline.CodiceValore or '',
                        'e_invoice_line_id': einvoiceline.id
                    }
                )
        if line.ScontoMaggiorazione:
            for DiscRisePriceLine in line.ScontoMaggiorazione:
                DiscRisePriceVals = self.with_context(
                    drtype='e_invoice_line_id'
                )._prepareDiscRisePriceLine(
                    einvoiceline.id, DiscRisePriceLine
                )
                self.pool['discount.rise.price'].create(DiscRisePriceVals)
        if line.AltriDatiGestionali:
            for dato in line.AltriDatiGestionali:
                self.pool['einvoice.line.other.data'].create(
                    {
                        'name': dato.TipoDato,
                        'text_ref': dato.RiferimentoTesto,
                        'num_ref': float(dato.RiferimentoNumero or 0),
                        'date_ref': dato.RiferimentoData,
                        'e_invoice_line_id': einvoiceline.id
                    }
                )
        return einvoiceline

    def invoiceCreate(
        self, cr, uid, ids, fatt, fatturapa_attachment, FatturaBody,
        partner_id, context=None
    ):
        partner_model = self.pool['res.partner']
        invoice_model = self.pool['account.invoice']
        currency_model = self.pool['res.currency']
        invoice_line_model = self.pool['account.invoice.line']
        ftpa_doctype_model = self.pool['italy.ade.invoice.type']
        rel_docs_model = self.pool['fatturapa.related_document_type']
        WelfareFundLineModel = self.pool['welfare.fund.data.line']
        SalModel = self.pool['faturapa.activity.progress']
        DdTModel = self.pool['fatturapa.related_ddt']
        PaymentDataModel = self.pool['fatturapa.payment.data']
        PaymentTermsModel = self.pool['fatturapa.payment_term']
        SummaryDatasModel = self.pool['faturapa.summary.data']

        # company = self.pool.user.company_id
        company = self.getCompany(
                fatt.FatturaElettronicaHeader.CessionarioCommittente.
                DatiAnagrafici)
        partner = partner_model.browse(partner_id)
        pay_acc_id = partner.property_account_payable_id.id
        # currency 2.1.1.2
        currency_id = currency_model.search(
            cr, uid,
            [
                (
                    'name', '=',
                    FatturaBody.DatiGenerali.DatiGeneraliDocumento.Divisa
                )
            ],
            context=context)
        if not currency_id:
            raise orm.except_orm(
                _('Error!'),
                _(
                    'No currency found with code %s.'
                    % FatturaBody.DatiGenerali.DatiGeneraliDocumento.Divisa
                )
            )
        purchase_journal = self.get_purchase_journal(company)
        # purchase_journal = invoice_model._default_journal()
        credit_account_id = purchase_journal.default_credit_account_id.id
        # credit_account_id = invoice_model._default_account()
        invoice_lines = []
        comment = ''
        # 2.1.1
        docType_id = False
        invtype = 'in_invoice'
        docType = FatturaBody.DatiGenerali.DatiGeneraliDocumento.TipoDocumento
        if docType:
            docType_ids = ftpa_doctype_poll.search(
                cr, uid,
                [
                    ('code', '=', docType)
                ],
                context=context
            )
            if docType_ids:
                docType_id = docType_ids[0]
            else:
                raise UserError(
                    _("Document type %s not handled.")
                    % docType)
            if docType == 'TD04' or docType == 'TD05':
                invtype = 'in_refund'
        # 2.1.1.11
        causLst = FatturaBody.DatiGenerali.DatiGeneraliDocumento.Causale
        if causLst:
            for item in causLst:
                comment += item + '\n'

        invoice_data = {
            'fiscal_document_type_id': docType_id,
            'date_invoice':
            FatturaBody.DatiGenerali.DatiGeneraliDocumento.Data,
            'supplier_invoice_number':
            FatturaBody.DatiGenerali.DatiGeneraliDocumento.Numero,
            'sender': fatt.FatturaElettronicaHeader.SoggettoEmittente or False,
            'account_id': pay_acc_id,
            'type': invtype,
            'partner_id': partner_id,
            'currency_id': currency_id[0],
            'journal_id': purchase_journal.id,
            'invoice_line': [(6, 0, invoice_lines)],
            # 'origin': xmlData.datiOrdineAcquisto,
            'fiscal_position_id': False,
            'payment_term_id': False,
            'company_id': company.id,
            'fatturapa_attachment_in_id': fatturapa_attachment.id,
            'comment': comment
        }
        invoice_data['e_invoice_line_ids'] = [(6, 0, e_invoice_line_ids)]
        # 2.1.1.10
        if FatturaBody.DatiGenerali.DatiGeneraliDocumento.Arrotondamento:
            invoice_data['efatt_rounding'] = float(
                FatturaBody.DatiGenerali.DatiGeneraliDocumento.Arrotondamento
            )
        # 2.1.1.12
        if FatturaBody.DatiGenerali.DatiGeneraliDocumento.Art73:
            invoice_data['art73'] = True

        # 2.1.1.5
        Withholding = FatturaBody.DatiGenerali.\
            DatiGeneraliDocumento.DatiRitenuta
        wt_found = None
        if Withholding:
            wts = self.pool['withholding.tax'].search([
                ('causale_pagamento_id.code', '=',
                 Withholding.CausalePagamento)
            ])
            if not wts:
                raise UserError(_(
                    "The bill contains withholding tax with "
                    "payment reason %s, "
                    "but such a tax is not found in your system. Please "
                    "set it."
                ) % Withholding.CausalePagamento)
            wt_found = False
            for wt in wts:
                if wt.tax == float(Withholding.AliquotaRitenuta):
                    wt_found = wt
                    break
            if not wt_found:
                raise UserError(_(
                    "No withholding tax found with "
                    "document payment reason %s and rate %s."
                ) % (
                    Withholding.CausalePagamento, Withholding.AliquotaRitenuta
                ))
            invoice_data['ftpa_withholding_type'] = Withholding.TipoRitenuta
        # 2.2.1
        e_invoice_line_ids = []
        for line in FatturaBody.DatiBeniServizi.DettaglioLinee:
            if self.e_invoice_detail_level == '2':
                if (partner.e_invoice_default_account_id):
                    credit_account_id = partner.e_invoice_default_account_id.id
                invoice_line_data = self._prepareInvoiceLine(
                    credit_account_id, line, wt_found)
                product = self.get_line_product(line, partner)
                if product:
                    invoice_line_data['product_id'] = product.id
                    self.adjust_accounting_data(product, invoice_line_data)
                invoice_line_id = invoice_line_model.create(
                    invoice_line_data).id
                invoice_lines.append(invoice_line_id)
            einvoiceline = self.create_e_invoice_line(line)
            e_invoice_line_ids.append(einvoiceline.id)
        invoice_data['invoice_line_ids'] = [(6, 0, invoice_lines)]
        invoice_data['e_invoice_line_ids'] = [(6, 0, e_invoice_line_ids)]
        invoice = invoice_model.create(invoice_data)
        # TODO: check from Cesare
        # invoice._onchange_invoice_line_wt_ids()
        invoice.write(invoice._convert_to_write(invoice._cache))
        invoice_id = invoice.id

        # 2.1.1.7
        Walfares = FatturaBody.DatiGenerali.\
            DatiGeneraliDocumento.DatiCassaPrevidenziale
        if Walfares and self.e_invoice_detail_level == '2':
            for walfareLine in Walfares:
                WalferLineVals = self._prepareWelfareLine(
                    invoice_id, walfareLine)
                WelfareFundLineModel.create(WalferLineVals)

        # 2.1.2
        relOrders = FatturaBody.DatiGenerali.DatiOrdineAcquisto
        if relOrders:
            for order in relOrders:
                doc_datas = self._prepareRelDocsLine(
                    invoice_id, order, 'order')
                if doc_datas:
                    for doc_data in doc_datas:
                        rel_docs_model.create(doc_data)
        # 2.1.3
        relContracts = FatturaBody.DatiGenerali.DatiContratto
        if relContracts:
            for contract in relContracts:
                doc_datas = self._prepareRelDocsLine(
                    invoice_id, contract, 'contract')
                if doc_datas:
                    for doc_data in doc_datas:
                        rel_docs_model.create(doc_data)
        # 2.1.4
        relAgreements = FatturaBody.DatiGenerali.DatiConvenzione
        if relAgreements:
            for agreement in relAgreements:
                doc_datas = self._prepareRelDocsLine(
                    invoice_id, agreement, 'agreement')
                if doc_datas:
                    for doc_data in doc_datas:
                        rel_docs_model.create(doc_data)
        # 2.1.5
        relReceptions = FatturaBody.DatiGenerali.DatiRicezione
        if relReceptions:
            for reception in relReceptions:
                doc_datas = self._prepareRelDocsLine(
                    invoice_id, reception, 'reception')
                if doc_datas:
                    for doc_data in doc_datas:
                        rel_docs_model.create(doc_data)
        # 2.1.6
        RelInvoices = FatturaBody.DatiGenerali.DatiFattureCollegate
        if RelInvoices:
            for invoice in RelInvoices:
                doc_datas = self._prepareRelDocsLine(
                    invoice_id, invoice, 'invoice')
                if doc_datas:
                    for doc_data in doc_datas:
                        rel_docs_model.create(doc_data)
        # 2.1.7
        SalDatas = FatturaBody.DatiGenerali.DatiSAL
        if SalDatas:
            for SalDataLine in SalDatas:
                SalModel.create(
                    {
                        'fatturapa_activity_progress': (
                            SalDataLine.RiferimentoFase or 0),
                        'invoice_id': invoice_id
                    }
                )
        # 2.1.8
        DdtDatas = FatturaBody.DatiGenerali.DatiDDT
        if DdtDatas:
            for DdtDataLine in DdtDatas:
                if not DdtDataLine.RiferimentoNumeroLinea:
                    DdTModel.create(
                        {
                            'name': DdtDataLine.NumeroDDT or '',
                            'date': DdtDataLine.DataDDT or False,
                            'invoice_id': invoice_id
                        }
                    )
                else:
                    for numline in DdtDataLine.RiferimentoNumeroLinea:
                        invoice_lines = invoice_line_model.search(
                            [
                                ('invoice_id', '=', invoice_id),
                                ('sequence', '=', int(numline)),
                            ])
                        invoice_lineid = False
                        if invoice_lines:
                            invoice_lineid = invoice_lines[0].id
                        DdTModel.create(
                            {
                                'name': DdtDataLine.NumeroDDT or '',
                                'date': DdtDataLine.DataDDT or False,
                                'invoice_id': invoice_id,
                                'invoice_line_id': invoice_lineid
                            }
                        )
        # 2.1.9
        Delivery = FatturaBody.DatiGenerali.DatiTrasporto
        if Delivery:
            delivery_id = self.getCarrirerPartner(Delivery)
            delivery_dict = {
                'carrier_id': delivery_id,
                'transport_vehicle': Delivery.MezzoTrasporto or '',
                'transport_reason': Delivery.CausaleTrasporto or '',
                'number_items': Delivery.NumeroColli or 0,
                'description': Delivery.Descrizione or '',
                'unit_weight': Delivery.UnitaMisuraPeso or 0.0,
                'gross_weight': Delivery.PesoLordo or 0.0,
                'net_weight': Delivery.PesoNetto or 0.0,
                'pickup_datetime': Delivery.DataOraRitiro or False,
                'transport_date': Delivery.DataInizioTrasporto or False,
                'delivery_datetime': Delivery.DataOraConsegna or False,
                'delivery_address': '',
                'ftpa_incoterms': Delivery.TipoResa,
            }

            if Delivery.IndirizzoResa:
                delivery_dict['delivery_address'] = (
                    '{0}, {1}\n{2} - {3}\n{4} {5}'.format(
                        Delivery.IndirizzoResa.Indirizzo or '',
                        Delivery.IndirizzoResa.NumeroCivico or '',
                        Delivery.IndirizzoResa.CAP or '',
                        Delivery.IndirizzoResa.Comune or '',
                        Delivery.IndirizzoResa.Provincia or '',
                        Delivery.IndirizzoResa.Nazione or ''
                    )
                )
            invoice.write(delivery_dict)
        # 2.2.2
        Summary_datas = FatturaBody.DatiBeniServizi.DatiRiepilogo
        if Summary_datas:
            for summary in Summary_datas:
                summary_line = {
                    'tax_rate': summary.AliquotaIVA or 0.0,
                    'non_taxable_nature': self.get_natura(summary.Natura),
                    'incidental_charges': summary.SpeseAccessorie or 0.0,
                    'rounding': summary.Arrotondamento or 0.0,
                    'amount_untaxed': summary.ImponibileImporto or 0.0,
                    'amount_tax': summary.Imposta or 0.0,
                    'payability': summary.EsigibilitaIVA or False,
                    'law_reference': summary.RiferimentoNormativo or '',
                    'invoice_id': invoice_id,
                }
                SummaryDatasModel.create(summary_line)

        # 2.1.10
        ParentInvoice = FatturaBody.DatiGenerali.FatturaPrincipale
        if ParentInvoice:
            parentinv_vals = {
                'related_invoice_code':
                ParentInvoice.NumeroFatturaPrincipale or '',
                'related_invoice_date':
                ParentInvoice.DataFatturaPrincipale or False
            }
            invoice.write(parentinv_vals)
        # 2.3
        Vehicle = FatturaBody.DatiVeicoli
        if Vehicle:
            veicle_vals = {
                'vehicle_registration': Vehicle.Data or False,
                'total_travel': Vehicle.TotalePercorso or '',
            }
            invoice.write(veicle_vals)
        # 2.4
        PaymentsData = FatturaBody.DatiPagamento
        if PaymentsData:
            for PaymentLine in PaymentsData:
                cond = PaymentLine.CondizioniPagamento or False
                if not cond:
                    raise UserError(
                        _('Payment method code not found in document.')
                    )
                terms = PaymentTermsModel.search([('code', '=', cond)])
                if not terms:
                    raise UserError(
                        _('Payment method code %s is incorrect.') % cond
                    )
                else:
                    term_id = terms[0].id
                PayDataId = PaymentDataModel.create(
                    {
                        'payment_terms': term_id,
                        'invoice_id': invoice_id
                    }
                ).id
                self._createPayamentsLine(PayDataId, PaymentLine, partner_id)
        # 2.5
        AttachmentsData = FatturaBody.Allegati
        if AttachmentsData:
            AttachModel = self.pool['fatturapa.attachments']
            for attach in AttachmentsData:
                if not attach.NomeAttachment:
                    name = _("Attachment without name")
                else:
                    name = attach.NomeAttachment
                content = attach.Attachment
                _attach_dict = {
                    'name': name,
                    'datas': base64.b64encode(str(content)),
                    'datas_fname': name,
                    'description': attach.DescrizioneAttachment or '',
                    'compression': attach.AlgoritmoCompressione or '',
                    'format': attach.FormatoAttachment or '',
                    'invoice_id': invoice_id,
                }
                AttachModel.create(_attach_dict)

        self._addGlobalDiscount(
            invoice_id, FatturaBody.DatiGenerali.DatiGeneraliDocumento)

        # compute the invoice
        invoice.compute_taxes()
        return invoice_id

    def compute_xml_amount_untaxed(self, DatiRiepilogo):
        amount_untaxed = 0.0
        for Riepilogo in DatiRiepilogo:
            amount_untaxed += float(Riepilogo.ImponibileImporto)
        return amount_untaxed

    def check_invoice_amount(self, invoice, FatturaElettronicaBody):
        if (
            FatturaElettronicaBody.DatiGenerali.DatiGeneraliDocumento.
            ScontoMaggiorazione and
            FatturaElettronicaBody.DatiGenerali.DatiGeneraliDocumento.
            ImportoTotaleDocumento
        ):
            # assuming that, if someone uses
            # DatiGeneraliDocumento.ScontoMaggiorazione, also fills
            # DatiGeneraliDocumento.ImportoTotaleDocumento
            ImportoTotaleDocumento = float(
                FatturaElettronicaBody.DatiGenerali.DatiGeneraliDocumento.
                ImportoTotaleDocumento)
            if not float_is_zero(
                invoice.amount_total - ImportoTotaleDocumento, precision_digits=2
            ):
                self.log_inconsistency(
                    _('Bill total %s is different from '
                      'document total amount %s')
                    % (invoice.amount_total, ImportoTotaleDocumento)
                )
        else:
            # else, we can only check DatiRiepilogo if
            # DatiGeneraliDocumento.ScontoMaggiorazione is not present,
            # because otherwise DatiRiepilogo and odoo invoice total would
            # differ
            amount_untaxed = self.compute_xml_amount_untaxed(
                FatturaElettronicaBody.DatiBeniServizi.DatiRiepilogo)
            if not float_is_zero(
                invoice.amount_untaxed - amount_untaxed, precision_digits=2
            ):
                self.log_inconsistency(
                    _('Computed amount untaxed %s is different from'
                      ' summary data %s')
                    % (invoice.amount_untaxed, amount_untaxed)
                )

    def get_invoice_obj(self, fatturapa_attachment):
        xml_string = fatturapa_attachment.get_xml_string()
        return fatturapa_v_1_2.CreateFromDocument(xml_string)

    @api.multi
    def importFatturaPA(self):
        fatturapa_attachment_obj = self.pool['fatturapa.attachment.in']
        fatturapa_attachment_ids = self.pool.context.get('active_ids', False)
        invoice_model = self.pool['account.invoice']
        new_invoices = []
        for fatturapa_attachment_id in fatturapa_attachment_ids:
            self.__dict__.update(
                self.with_context(inconsistencies='').__dict__
            )
            fatturapa_attachment = fatturapa_attachment_obj.browse(
                fatturapa_attachment_id)
            if fatturapa_attachment.in_invoice_ids:
                raise UserError(
                    _("File is linked to bills yet."))
            fatt = self.get_invoice_obj(fatturapa_attachment)
            # company_id = self.getCompany(
            #     fatt.FatturaElettronicaHeader.CessionarioCommittente.
            #     DatiAnagrafici)
            cedentePrestatore = fatt.FatturaElettronicaHeader.CedentePrestatore
            # 1.2
            partner_id = self.getCedPrest(cedentePrestatore)
            # 1.3
            TaxRappresentative = fatt.FatturaElettronicaHeader.\
                RappresentanteFiscale
            # 1.5
            Intermediary = fatt.FatturaElettronicaHeader.\
                TerzoIntermediarioOSoggettoEmittente

            generic_inconsistencies = ''
            if self.pool.context.get('inconsistencies'):
                generic_inconsistencies = (
                    self.pool.context['inconsistencies'] + '\n\n')

            # 2
            for fattura in fatt.FatturaElettronicaBody:

                # reset inconsistencies
                self.__dict__.update(
                    self.with_context(inconsistencies='').__dict__
                )

                invoice_id = self.invoiceCreate(
                    fatt, fatturapa_attachment, fattura, partner_id)
                invoice = invoice_model.browse(invoice_id)
                self.set_StabileOrganizzazione(cedentePrestatore, invoice)
                if TaxRappresentative:
                    tax_partner_id = self.getPartnerBase(
                        TaxRappresentative.DatiAnagrafici)
                    invoice.write(
                        {
                            'tax_representative_id': tax_partner_id
                        }
                    )
                if Intermediary:
                    Intermediary_id = self.getPartnerBase(
                        Intermediary.DatiAnagrafici)
                    invoice.write(
                        {
                            'intermediary': Intermediary_id
                        }
                    )
                new_invoices.append(invoice_id)
                self.check_invoice_amount(invoice, fattura)

                if self.pool.context.get('inconsistencies'):
                    invoice_inconsistencies = (
                        self.pool.context['inconsistencies'])
                else:
                    invoice_inconsistencies = ''
                invoice.inconsistencies = (
                    generic_inconsistencies + invoice_inconsistencies)

        return {
            'view_type': 'form',
            'name': "Electronic Bills",
            'view_mode': 'tree,form',
            'res_model': 'account.invoice',
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', new_invoices)],
        }
