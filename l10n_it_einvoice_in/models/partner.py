# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
import logging
from odoo import api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    e_invoice_default_product_id = fields.Many2one(
        comodel_name='product.product',
        string='E-bill Default Product',
        help="Used by electronic invoice XML import. "
             "If filled in, generated bill lines will use this product when "
             "no other possible product is found."
    )
    e_invoice_default_account_id = fields.Many2one(
        comodel_name='account.account',
        string='E-bill Default Account',
        help="Used by electronic invoice XML import. "
             "If filled in, generated bill lines will use this account when "
             "no other possible product is found."
    )
    e_invoice_detail_level = fields.Selection([
        ('0', 'Minimum'),
        ('1', 'Aliquote'),
        ('2', 'Maximum'),
    ], string="E-bills Detail Level",
        help="Minimum level: Bill is created with no lines; "
             "User will have to create them, according to what specified in "
             "the electronic bill.\n"
             # "Livello Aliquote: viene creata una riga fattura per ogni "
             # "aliquota presente nella fattura elettronica\n"
             "Maximum level: every line contained in the electronic bill "
             "will create a line in the bill.",
        default='2', required=True
    )

    @api.multi
    def synchro(self, model, values, skeys=None, constraints=None,
                keep=None, default=None):
        vals = values.copy()
        skeys = skeys or []
        ir_model = self.env[model]
        MAGIC_FIELDS = {'company_id': False,
                        'is_company': True,
                        'supplier': True,
        }
        keep = keep or []
        default = default or {}
        id = -1
        for keys in skeys:
            where = []
            for key in keys:
                if key not in vals and key in MAGIC_FIELDS:
                    if MAGIC_FIELDS[key]:
                        where.append((key, '=', MAGIC_FIELDS[key]))
                elif key not in vals:
                    where = []
                    break
                else:
                    where.append((key, '=', vals[key]))
            if where:
                for constr in constraints:
                    add_where = False
                    if constr[0] in vals:
                        constr[0] = vals[constr[0]]
                        add_where = True
                    if constr[-1] in vals:
                        constr[-1] = vals[constr[-1]]
                        add_where = True
                    if add_where:
                        where.append(constr)
                rec = ir_model.search(where)
                if rec:
                    id = rec[0].id
                    break
        if id > 0:
            try:
                cur_rec = ir_model.browse(id)
                for field in keep:
                    if (field in vals and cur_rec[field] and
                            isinstance(vals[field], basestring) and
                            ir_model.dim_text(
                                cur_rec[field]) == ir_model.dim_text(
                                    vals[field])):
                        del vals[field]
                for field in default:
                    if not vals.get(field) and field in default:
                        vals[field] = default[field]
                cur_rec.write(vals)
            except:
                _logger.error('Error writing %s ID=%d' %
                              (model, id))
                return -2
        else:
            try:
                id = ir_model.create(vals).id
            except:
                _logger.error('Error creating %s' % model)
                return -1
        return id

    def CountryByCode(self, CountryCode):
        country_model = self.env['res.country']
        return country_model.search([('code', '=', CountryCode)])

    def ProvinceByCode(self, provinceCode):
        province_model = self.env['res.country.state']
        return province_model.search([
            ('code', '=', provinceCode),
            ('country_id.code', '=', 'IT')
        ])

    def getPartnerBase(self, partner_xml, fatturapa=None):
        '''Get data from xml and write or create partner'''
        if not partner_xml:
            return -1
        if hasattr(partner_xml, 'DatiAnagrafici'):
            DatiAnagrafici = partner_xml.DatiAnagrafici
        else:
            return -1
        if hasattr(DatiAnagrafici, 'Anagrafica'):
            Anagrafica = DatiAnagrafici.Anagrafica
        else:
            return -1
        fiscalPosModel = self.env['fatturapa.fiscal_position']
        vals = {
            'customer': False,
            'supplier': True,
            'is_company': True,
            'street': partner_xml.Sede.Indirizzo,
            'zip': partner_xml.Sede.CAP,
            'city': partner_xml.Sede.Comune,
        }
        if partner_xml.Sede.Provincia:
            Provincia = partner_xml.Sede.Provincia
            prov_sede = self.ProvinceByCode(Provincia)
            if not prov_sede:
                if fatturapa:
                    self.log_inconsistency(
                        _('Province ( %s ) not present in your system')
                        % Provincia
                    )
                else:
                    raise UserError(
                        _('Province ( %s ) not present in your system')
                        % Provincia
                    )
            else:
                vals['state_id'] = prov_sede[0].id

        if partner_xml.Contatti:
            vals['phone'] = partner_xml.Contatti.Telefono
            vals['email'] = partner_xml.Contatti.Email
            vals['fax'] = partner_xml.Contatti.Fax

        if DatiAnagrafici.AlboProfessionale:
            vals['register'] = DatiAnagrafici.AlboProfessionale
            if DatiAnagrafici.ProvinciaAlbo:
                ProvinciaAlbo = DatiAnagrafici.ProvinciaAlbo
                prov = self.ProvinceByCode(ProvinciaAlbo)
                if not prov:
                    self.log_inconsistency(
                        _('Register Province ( %s ) not present '
                          'in your system')
                        % ProvinciaAlbo
                    )
                else:
                    vals['register_province'] = prov[0].id
            vals['register_code'] = DatiAnagrafici.NumeroIscrizioneAlbo or ''
            vals['register_regdate'] = DatiAnagrafici.DataIscrizioneAlbo or ''

        if DatiAnagrafici.RegimeFiscale:
            rfPos = DatiAnagrafici.RegimeFiscale
            FiscalPos = fiscalPosModel.search(
                [('code', '=', rfPos)]
            )
            if not FiscalPos:
                raise UserError(
                    _('Tax Regime %s not present in your system.')
                    % rfPos
                )
            else:
                vals['register_fiscalpos'] = FiscalPos[0].id

        if partner_xml.IscrizioneREA:
            REA = partner_xml.IscrizioneREA
            vals['rea_code'] = REA.NumeroREA
            offices = self.ProvinceByCode(REA.Ufficio)
            if not offices:
                if fatturapa:
                    self.log_inconsistency(
                        _(
                            'REA Office Province Code ( %s ) not present in '
                            'your system'
                        ) % REA.Ufficio
                    )
                else:
                    raise UserError(
                        _(
                            'REA Office Province Code ( %s ) not present in '
                            'your system'
                        ) % REA.Ufficio
                    )
            else:
                office_id = offices[0].id
                vals['rea_office'] = office_id
            vals['rea_capital'] = REA.CapitaleSociale or 0.0
            vals['rea_member_type'] = REA.SocioUnico or False
            vals['rea_liquidation_state'] = REA.StatoLiquidazione or False

        if DatiAnagrafici.CodiceFiscale:
            vals['fiscalcode'] = DatiAnagrafici.CodiceFiscale
        if DatiAnagrafici.IdFiscaleIVA:
            vals['vat'] = "%s%s" % (
                DatiAnagrafici.IdFiscaleIVA.IdPaese,
                DatiAnagrafici.IdFiscaleIVA.IdCodice
            )

        if (hasattr(partner_xml,'DatiAnagraficiVettore') and
                partner_xml.DatiAnagraficiVettore and
                partner_xml.DatiAnagraficiVettore.NumeroLicenzaGuida):
            vals['license_number'] = \
                partner_xml.DatiAnagraficiVettore.NumeroLicenzaGuida

        if DatiAnagrafici.IdFiscaleIVA:
            CountryCode = DatiAnagrafici.IdFiscaleIVA.IdPaese
            countries = self.CountryByCode(CountryCode)
            if countries:
                country_id = countries[0].id
            else:
                raise UserError(
                    _("Country Code %s not found in the system.") % CountryCode
                )
            vals['country_id'] = country_id
        if Anagrafica.CodEORI:
            vals['eori_code'] = Anagrafica.CodEORI
        if Anagrafica.Denominazione:
            vals['name'] = Anagrafica.Denominazione
        else:
            vals['name'] = '%s %s' % (Anagrafica.Cognome,
                                      Anagrafica.Nome)
        partner_id = self.synchro(
            'res.partner',
            vals,
            skeys=(['vat', 'fiscalcode', 'is_company', 'type'],
                   ['rea_code', 'type'],
                   ['vat', 'name', 'is_company', 'type'],
                   ['fiscalcode', 'type'],
                   ['vat', 'is_company', 'supplier'],
                   ['name', 'is_company', 'supplier'],
                   ['vat'],
                   ['name']),
            constraints=[('id', '!=', 'parent_id')],
            keep = ['customer', 'country_id',
                    'name', 'street', 'zip',
                    'city', 'state_id',
                   ],
            default = {
                'rea_member_type': 'SM',
                'rea_liquidation_state': 'LN',
                'type': 'contact',
            }
        )
        partner = self.browse(partner_id)
        if partner.name != vals['name']:
            vals['type'] = 'invoice'
            vals['parent_id'] = partner_id
            for nm in ('rea_code', 'rea_office', 'rea_capital'):
                if nm in vals:
                    del vals[nm]
            self.synchro(
                'res.partner',
                vals,
                skeys=(['type', 'parent_id']),
                constraints=[('id', '!=', 'parent_id')],
            )
        return partner_id
