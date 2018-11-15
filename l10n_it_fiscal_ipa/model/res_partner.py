# -*- coding: utf-8 -*-
#
# Copyright 2014    KTec S.r.l.
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class ResPartner(orm.Model):
    _inherit = 'res.partner'
    _columns = {
        'ipa_code': fields.char('IPA Code',
                                size=128),
        'is_pa': fields.boolean("Public administration"),
        'codice_destinatario': fields.char(
            "Recipient Code",
            help="Il codice, di 7 caratteri, assegnato dal Sdi ai soggetti che "
                 "hanno accreditato un canale; qualora il destinatario non abbia "
                 "accreditato un canale presso Sdi e riceva via PEC le fatture, "
                 "l'elemento deve essere valorizzato con tutti zeri ('0000000'). "),
        'electronic_invoice_subjected': fields.boolean(
            "Subjected to electronic invoice"),
        'eori_code': fields.char('EORI Code', size=20),
        'license_number': fields.char('License Code', size=20),
        'pec_destinatario': fields.char(
            "PEC destinatario",
            help="Indirizzo PEC al quale inviare la fattura elettronica, "
                 "se diversa da PEC legale. Viene utilizzata solo "
                 "se il codice destinatario vale '0000000'"),
    }

    def onchange_electronic_invoice_subjected(self, cr, uid, ids,
            vat, fiscalcode, is_pa, ipa_code,
            electronic_invoice_subjected, codice_destinatario):
        if vat and not codice_destinatario:
            codice_destinatario = '0000000'
        return self.check_codice_destinatario(cr, uid, ids,
            vat, fiscalcode, is_pa, ipa_code,
            electronic_invoice_subjected, codice_destinatario)

    def check_codice_destinatario(self, cr, uid, ids,
            vat, fiscalcode, is_pa, ipa_code,
            electronic_invoice_subjected, codice_destinatario):
        vals = {'is_pa': is_pa,
                'ipa_code': ipa_code,
                'electronic_invoice_subjected': electronic_invoice_subjected,
                'codice_destinatario': codice_destinatario}
        if electronic_invoice_subjected and is_pa:
            return {
                'value': vals,
                'warning': {
                    'title': 'Invalid values!',
                    'message': 'Partner dichiarato sia PA che Fattura B2B!'}
            }
        if is_pa and (
            not ipa_code or len(ipa_code) != 6
        ):
            return {
                'value': vals,
                'warning': {
                    'title': 'Invalid values!',
                    'message': 'Partner PA senza codice IPA di 6 caratteri'}
            }
        if electronic_invoice_subjected:
            if not vat and not fiscalcode:
                return {
                    'value': vals,
                    'warning': {
                        'title': 'Invalid values!',
                        'message': 'Partner senza P.IVA ne codice fiscale'}
                }
            if (
                not codice_destinatario or
                len(codice_destinatario) != 7
            ):
                return {
                    'value': vals,
                    'warning': {
                        'title': 'Invalid values!',
                        'message': 'Partner senza codice destinatario '
                                   'di 7 caratteri o 0000000'}
                }
        return {'value': vals}