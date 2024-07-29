# -*- coding: utf-8 -*-

import logging

from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    e_invoice_default_product_id = fields.Many2one(
        comodel_name="product.product",
        string="E-bill Default Product",
        help="Used by electronic invoice XML import. "
        "If filled in, generated bill lines will use this product when "
        "no other possible product is found.",
    )
    e_invoice_default_account_id = fields.Many2one(
        comodel_name="account.account",
        string="E-bill Default Account",
        help="Used by electronic invoice XML import. "
        "If filled in, generated bill lines will use this account when "
        "no other possible product is found.",
    )
    e_invoice_detail_level = fields.Selection(
        [
            ("0", "Minimum"),
            ("1", "Aliquote"),
            ("2", "Maximum"),
        ],
        string="E-bills Detail Level",
        help="Minimum level: Bill is created with no lines; "
        "User will have to create them, according to what specified in "
        "the electronic bill.\n"
        # "Livello Aliquote: viene creata una riga fattura per ogni "
        # "aliquota presente nella fattura elettronica\n"
        "Maximum level: every line contained in the electronic bill "
        "will create a line in the bill.",
        default="2",
        required=True,
    )

    def check_vat(self, vat):
        country, code = vat[:2].lower(), vat[2:].replace(" ", "")
        return self.simple_vat_check(country, code)

    def CountryByCode(self, CountryCode):
        country_model = self.env["res.country"]
        return country_model.search([("code", "=", CountryCode)])

    def ProvinceByCode(self, provinceCode, country_code="IT"):
        province_model = self.env["res.country.state"]
        return province_model.search(
            [("code", "=", provinceCode), ("country_id.code", "=", country_code)]
        )

    def check_partner_base_data(self, partner_id, DatiAnagrafici, fatturapa):
        partner = self.env["res.partner"].browse(partner_id)
        if (
            DatiAnagrafici.Anagrafica.Denominazione
            and partner.name != DatiAnagrafici.Anagrafica.Denominazione
        ):
            fatturapa.log_inconsistency(
                _("Ragione sociale da XML '%s' " "differisce da dato in sistema'%s'.")
                % (DatiAnagrafici.Anagrafica.Denominazione, partner.name)
            )
        if (
            DatiAnagrafici.Anagrafica.Nome
            and partner.firstname != DatiAnagrafici.Anagrafica.Nome
        ):
            fatturapa.log_inconsistency(
                _("Nome da XML '%s' " "differisce da dato in sistema'%s'.")
                % (DatiAnagrafici.Anagrafica.Nome, partner.firstname or partner.name)
            )
        if (
            DatiAnagrafici.Anagrafica.Cognome
            and partner.lastname != DatiAnagrafici.Anagrafica.Cognome
        ):
            fatturapa.log_inconsistency(
                _("Cognome da XML '%s' " "differisce da dato in sistema'%s'.")
                % (DatiAnagrafici.Anagrafica.Cognome, partner.lastname or partner.name)
            )

    def getPartnerBase(self, partner_xml, fatturapa=None):
        """Get data from xml and write or create partner"""
        if not partner_xml:
            return -1
        Sede = None
        if hasattr(partner_xml, "DatiAnagrafici"):
            DatiAnagrafici = partner_xml.DatiAnagrafici
            if hasattr(DatiAnagrafici, "Anagrafica"):
                Anagrafica = DatiAnagrafici.Anagrafica
            else:
                return -1
            if hasattr(partner_xml, "Sede"):
                Sede = partner_xml.Sede
        elif hasattr(partner_xml, "Anagrafica"):
            DatiAnagrafici = partner_xml
            Anagrafica = partner_xml.Anagrafica
        else:
            return -1
        IdFiscaleIVA = DatiAnagrafici.IdFiscaleIVA

        FatturapaFiscalPosition = self.env["fatturapa.fiscal_position"]
        if Sede:
            vals = {
                "customer": False,
                "supplier": True,
                "is_company": True,
                "street": Sede.Indirizzo,
                "zip": Sede.CAP,
                "city": Sede.Comune,
            }
            if hasattr(Sede, "NumeroCivico") and Sede.NumeroCivico:
                vals["street"] += ", " + Sede.NumeroCivico
            if (
                    Sede.Provincia
                    and Sede.Provincia != "EE"
                    and IdFiscaleIVA.IdPaese not in ("EU", "SM")
            ):
                Provincia = Sede.Provincia
                prov_sede = self.ProvinceByCode(
                    Provincia, country_code=IdFiscaleIVA.IdPaese)
                if not prov_sede:
                    if fatturapa:
                        fatturapa.log_inconsistency(
                            _('Provincia "%s" non presente in archivio') % Provincia
                        )
                    else:
                        raise UserError(
                            _('Provincia "%s" non presente in archivio') % Provincia
                        )
                else:
                    vals["state_id"] = prov_sede[0].id
        else:
            vals = {
                "customer": False,
                "supplier": True,
                "is_company": True,
                "type": "contact",
            }

        if hasattr(partner_xml, "Contatti") and partner_xml.Contatti:
            vals["phone"] = partner_xml.Contatti.Telefono
            vals["email"] = partner_xml.Contatti.Email
            vals["fax"] = partner_xml.Contatti.Fax

        if hasattr(DatiAnagrafici,
                   "AlboProfessionale") and DatiAnagrafici.AlboProfessionale:
            vals["register"] = DatiAnagrafici.AlboProfessionale
            if DatiAnagrafici.ProvinciaAlbo:
                prov = self.ProvinceByCode(DatiAnagrafici.ProvinciaAlbo)
                if not prov:
                    if fatturapa:
                        fatturapa.log_inconsistency(
                            _('Provincia albo "%s" non presente in archivio ')
                            % DatiAnagrafici.ProvinciaAlbo
                        )
                else:
                    vals["register_province"] = prov[0].id
            vals["register_code"] = DatiAnagrafici.NumeroIscrizioneAlbo or ""
            vals["register_regdate"] = datetime.strftime(
                DatiAnagrafici.DataIscrizioneAlbo, "%Y-%m-%d") or ""

        if hasattr(DatiAnagrafici, "RegimeFiscale") and DatiAnagrafici.RegimeFiscale:
            rf_code = DatiAnagrafici.RegimeFiscale
            regime_fiscale = FatturapaFiscalPosition.search([("code", "=", rf_code)])
            if not regime_fiscale:
                raise UserError(
                    _("Tax Regime %s not present in your system.") % rf_code)
            else:
                vals["register_fiscalpos"] = regime_fiscale[0].id
                vals["type"] = "contact"

        if hasattr(partner_xml, "IscrizioneREA") and partner_xml.IscrizioneREA:
            vals["rea_code"] = partner_xml.IscrizioneREA.NumeroREA
            offices = self.ProvinceByCode(partner_xml.IscrizioneREA.Ufficio)
            if not offices:
                if fatturapa:
                    fatturapa.log_inconsistency(
                        _('Provincia ufficio REA "%s" non presente in ' "archivio")
                        % partner_xml.IscrizioneREA.Ufficio
                    )
            else:
                office_id = offices[0].id
                vals["rea_office"] = office_id
                vals["type"] = "contact"
            vals["rea_capital"] = partner_xml.IscrizioneREA.CapitaleSociale or 0.0
            vals["rea_member_type"] = partner_xml.IscrizioneREA.SocioUnico or False
            vals["rea_liquidation_state"] = (partner_xml.IscrizioneREA.StatoLiquidazione
                                             or False)

        if hasattr(DatiAnagrafici, "CodiceFiscale") and DatiAnagrafici.CodiceFiscale:
            vals["fiscalcode"] = DatiAnagrafici.CodiceFiscale
        if IdFiscaleIVA:
            if IdFiscaleIVA.IdPaese == "SM":
                vals["vat"] = "%s%s" % (
                    IdFiscaleIVA.IdPaese,
                    IdFiscaleIVA.IdCodice[-5:],
                )
            else:
                vals["vat"] = "%s%s" % (
                    IdFiscaleIVA.IdPaese,
                    IdFiscaleIVA.IdCodice,
                )

        if (
            hasattr(partner_xml, "DatiAnagraficiVettore")
            and partner_xml.DatiAnagraficiVettore
            and partner_xml.DatiAnagraficiVettore.NumeroLicenzaGuida
        ):
            vals[
                "license_number"
            ] = partner_xml.DatiAnagraficiVettore.NumeroLicenzaGuida

        if IdFiscaleIVA:
            country_code = IdFiscaleIVA.IdPaese
            if country_code != "EU":
                countries = self.CountryByCode(country_code)
                if countries:
                    country_id = countries[0].id
                else:
                    raise UserError(
                        _("Country Code %s not found in the system.") % country_code
                    )
                vals["country_id"] = country_id
        if Anagrafica.CodEORI:
            vals["eori_code"] = Anagrafica.CodEORI
        if Anagrafica.Denominazione:
            vals["name"] = Anagrafica.Denominazione
        else:
            vals["name"] = "%s %s" % (Anagrafica.Cognome, Anagrafica.Nome)
        SKEYS = (
            ["rea_office", "rea_code"],
            ["vat", "fiscalcode", "is_company", "type"],
            ["vat", "name", "is_company", "type"],
            ["fiscalcode", "%name", "is_company", "type"],
            ["vat", "%name", "is_company", "type"],
            ["vat", "is_company", "type"],
            ["name", "!vat", "is_company", "type"],
        )
        partner_id = self.synchro2(
            "res.partner",
            vals,
            skeys=SKEYS,
            constraints=[("id", "!=", "parent_id")],
            keep=[
                "customer",
                "country_id",
                "name",
                "street",
                "zip",
                "city",
                "state_id",
                "phone",
            ],
            default={
                "rea_member_type": "SM",
                "rea_liquidation_state": "LN",
                "type": "contact",
                "supplier": True,
            },
        )
        if partner_id > 0:
            partner = self.browse(partner_id)
            if partner.type == "invoice":
                partner_id = partner.parent_id.id
            if fatturapa:
                self.check_partner_base_data(partner_id, DatiAnagrafici, fatturapa)
        return partner_id

    @api.model
    def synchro2(
        self, model, values, skeys=None, constraints=None, keep=None, default=None
    ):
        def is_the_same(rec, vals):
            for field in ("name", "street", "zip", "city"):
                if field == "zip" and (vals[field] == "00000" or rec[field] == "00000"):
                    continue
                if self.dim_text(rec[field]) != self.dim_text(vals.get(field, "")):
                    rec = None
                    break
            return rec

        def rec_with_valid_vat(rec):
            if (
                rec
                and rec.vat
                and rec.parent_id
                and rec.parent_id.vat
                and rec.vat != rec.parent_id.vat
            ):
                rec.parent_id = False
                return None
            return rec

        def clear_dup_rea_code(vals):
            if "rea_code" in vals:
                for rec in self.search([("rea_code", "=", vals["rea_code"])]):
                    if rec.type != "contact" or rec.parent_id:
                        rec.write({"rea_code": False})

        vals = values.copy()
        clear_dup_rea_code(vals)
        skeys = skeys or []
        MAGIC_FIELDS = {
            "company_id": False,
            "is_company": True,
            "supplier": True,
        }
        keep = keep or []
        default = default or {}
        rec = False
        for keys in skeys:
            domain = []
            for key in keys:
                ilike = False
                if key.startswith("!"):
                    key = key[1:]
                    domain.append([key, "=", False])
                    continue
                if key.startswith(("%", "_")):
                    ilike = key[0]
                    key = key[1:]
                if key not in vals and key == "type":
                    domain.append([key, "=", "contact"])
                elif key not in vals and key in MAGIC_FIELDS:
                    if MAGIC_FIELDS[key]:
                        domain.append([key, "=", MAGIC_FIELDS[key]])
                elif key not in vals or not vals[key]:
                    domain = []
                    break
                elif ilike:
                    domain.append([key,
                                   "ilike",
                                   vals[key].replace(" ", ilike).replace(".", ilike)])
                else:
                    domain.append([key, "=", vals[key]])
            if domain:
                for constr in constraints:
                    add_domain = False
                    if constr[0] in vals:
                        constr[0] = vals[constr[0]]
                        add_domain = True
                    if constr[-1] in vals:
                        constr[-1] = vals[constr[-1]]
                        add_domain = True
                    if add_domain:
                        domain.append(constr)
                rec = self.search(domain)
                if rec:
                    rec = rec_with_valid_vat(rec[0])
                    if rec:
                        break
        if rec:
            if rec.parent_id and rec.type == "invoice":
                rec = rec.parent_id
            if rec == self.env.user.company_id.partner_id:
                # Avoid company update form self invoice
                return rec.id
            if not is_the_same(rec, vals):
                found = False
                for rec_inv in self.search(
                        [("parent_id", "=", rec.id), ("type", "=", "invoice")]):
                    if is_the_same(rec_inv, vals):
                        found = True
                        break
                if not found:
                    vals_inv = vals.copy()
                    vals_inv["type"] = "invoice"
                    vals_inv["parent_id"] = rec.id
                    for field in ("rea_code",
                                  "rea_office",
                                  "rea_capital",
                                  "rea_member_type",
                                  "rea_liquidation_state"):
                        if field in vals_inv:
                            del vals_inv[field]
                    if rec.name == rec.parent_id.name:
                        vals_inv["name"] = False
                    self.env["res.partner"].create(vals_inv)
            try:
                for field in keep:
                    if field in vals and rec[field]:
                        del vals[field]
                for field in default:
                    if not vals.get(field) and field in default:
                        vals[field] = default[field]
                for item in vals.keys():
                    if (
                        vals[item] is None
                        or isinstance(rec[item], (basestring, bool, int, float))
                        and rec[item] == vals[item]
                    ):
                        del vals[item]
                if vals.get("vat") and not self.check_vat(vals["vat"]):
                    del vals["vat"]
                if vals:
                    rec.write(vals)
                id = rec.id
            except BaseException as e:
                raise UserError(e)
        else:
            vals["type"] = "contact"
            vals["is_company"] = True
            vals["supplier"] = True
            if vals.get("vat") and not self.check_vat(vals["vat"]):
                del vals["vat"]
            try:
                id = self.create(vals).id
            except BaseException as e:
                raise UserError(e)
        return id
