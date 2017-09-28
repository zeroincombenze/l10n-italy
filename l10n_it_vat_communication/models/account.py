# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
#
# from openerp.tools.translate import _
# import math
# import decimal_precision as dp
import logging
from openerp.osv import fields, orm
import decimal_precision as dp
_logger = logging.getLogger(__name__)
try:
    import codicefiscale
except ImportError as err:
    _logger.debug(err)


class AccountVatCommunication(orm.Model):

    _name = "account.vat.communication"
    _columns = {
        'company_id': fields.many2one('res.company', 'Azienda', required=True),
        'progressivo_telematico':
            fields.integer('Progressivo telematico', readonly=True),
        'soggetto_codice_fiscale':
            fields.char('Codice fiscale dichiarante',
                        size=16, required=True,
                        help="CF del soggetto che presenta la comunicazione "
                             "se PF o DI o con la specifica carica"),
        'codice_carica': fields.selection([
            ('0', 'Azienda PF (Ditta indivisuale/Professionista/eccetera)'),
            ('1', 'Legale rappresentante, socio amministratore'),
            ('2', 'Rappresentante di minore,interdetto,eccetera'),
            ('3', 'Curatore fallimentare'),
            ('4', 'Commissario liquidatore'),
            ('5', 'Custode giudiziario'),
            ('6', 'Rappresentante fiscale di soggetto non residente'),
            ('7', 'Erede'),
            ('8', 'Liquidatore'),
            ('9', 'Obbligato di soggetto estinto'),
            ('10', 'Rappresentante fiscale art. 44c3 DLgs 331/93'),
            ('11', 'Tutore di minore'),
            ('12', 'Liquidatore di DI'),
            ('13', 'Amministratore di condominio'),
            ('14', 'Pubblica Amministrazione'),
            ('15', 'Commissario PA'), ],
            'Codice carica',),
        'state': fields.selection([
            ('draft', 'Draft'),
            ('open', 'Open'),
            ('confirmed', 'Confirmed'), ],
            'State', readonly=True),
        'period_ids': fields.one2many(
            'account.period', 'vat_commitment_id', 'Periods'),
        'account_vat_communication_dte_line_ids': fields.one2many(
            'account.vat.communication.dte.line', 'commitment_id',
            'Sale invoices',
            help='Sale invoices to export in VAT communication',
            states={
                'draft': [('readonly', False)],
                'open': [('readonly', False)],
                'confirmed': [('readonly', True)]
            }),
        'account_vat_communication_dtr_line_ids': fields.one2many(
            'account.vat.communication.dtr.line', 'commitment_id',
            'Purchase invoices',
            help='Purchase invoices to export in VAT communication',
            states={
                'draft': [('readonly', False)],
                'open': [('readonly', False)],
                'confirmed': [('readonly', True)]
            }),
    }

    _defaults = {
        'company_id': lambda self, cr, uid, c:
            self.pool['res.company']._company_default_get(
                cr, uid, 'account.vat.communication', context=c),
        'state': 'draft',
    }

    def create(self, cr, uid, vals, context=None):
        res = super(AccountVatCommunication, self).create(
            cr, uid, vals, context)
        self.create_sequence(cr, uid, vals, context)
        return res

    def create_sequence(self, cr, uid, vals, context=None):
        """ Create new no_gap entry sequence for progressivo_telematico
        """
        seq = {
            'name': 'vat_communication',
            'implementation': 'no_gap',
            'prefix': '',
            'number_increment': 1
        }
        if 'company_id' in vals:
            seq['company_id'] = vals['company_id']
        return self.pool['ir.sequence'].create(cr, uid, seq)

    def test_open(self, cr, uid, ids, *args):
        return True

    def communication_draft(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'draft'})

    def communication_open(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'open'})

    def load_DTE(self, cr, uid, commitment, context=None):
        """Read all sale invoices in periods"""
        context = context or {}
        invoice_obj = self.pool['account.invoice']
        commitment_DTE_line_obj = self.pool[
            'account.vat.communication.dte.line']

        period_ids = [x.id for x in commitment.period_ids]
        company_id = commitment.company_id.id
        where = [('company_id', '=', company_id),
                 ('period_id', 'in', period_ids),
                 ('type', '=', 'out_invoice')]
        invoices = invoice_obj.search(cr, uid, where)

        lines = commitment_DTE_line_obj.search(
            cr, uid, [('commitment_id', '=', commitment.id)])
        for line_id in lines:
            if line_id not in invoices:
                commitment_DTE_line_obj.unlink(cr, uid, [line_id])
        for invoice_id in invoices:
            invoice = invoice_obj.browse(cr, uid, invoice_id)
            line = {'commitment_id': commitment.id}
            line['partner_id'] = invoice.partner_id.id
            line['amount_total'] = invoice.amount_total
            commitment_DTE_line_obj.create(cr, uid, line)
        return invoices

    def load_DTR(self, cr, uid, commitment, context=None):
        """Read all purchase invoices in periods"""
        context = context or {}
        invoice_obj = self.pool['account.invoice']
        commitment_DTR_line_obj = self.pool[
            'account.vat.communication.dtr.line']

        period_ids = [x.id for x in commitment.period_ids]
        company_id = commitment.company_id.id
        where = [
            ('company_id', '=', company_id),
            ('period_id', 'in', period_ids),
            ('type', '=', 'in_invoice')
        ]
        invoices = invoice_obj.search(cr, uid, where)

        lines = commitment_DTR_line_obj.search(
            cr, uid, [('commitment_id', '=', commitment.id)])

        for line_id in lines:
            if line_id not in invoices:
                commitment_DTR_line_obj.unlink(cr, uid, [line_id])

        for invoice_id in invoices:
            invoice = invoice_obj.browse(cr, uid, invoice_id)
            line = {'commitment_id': commitment.id}
            line['partner_id'] = invoice.partner_id.id
            line['amount_total'] = invoice.amount_total
            commitment_DTR_line_obj.create(cr, uid, line)
        return invoices

    def compute_amounts(self, cr, uid, ids, context=None):
        context = {} if context is None else context

        for commitment in self.browse(cr, uid, ids, context):
            self.load_DTE(cr, uid, commitment, context)
            self.load_DTR(cr, uid, commitment, context)
        return True

    def onchange_fiscalcode(self, cr, uid, ids, fiscalcode, name,
                            context=None):
        if fiscalcode:
            if len(fiscalcode) == 11:
                chk = self.pool['res.partner'].simple_vat_check(
                    cr, uid, 'it', fiscalcode)
                if not chk:
                    return {
                        'value': {name: False},
                        'warning': {
                            'title': 'Invalid fiscalcode!',
                            'message': 'Invalid vat number'
                        }
                    }
            elif len(fiscalcode) != 16:
                return {
                    'value': {name: False},
                    'warning': {
                        'title': 'Invalid len!',
                        'message': 'Fiscal code len must be 11 or 16'
                    }
                }
            else:
                fiscalcode = fiscalcode.upper()
                chk = codicefiscale.control_code(fiscalcode[0:15])
                if chk != fiscalcode[15]:
                    value = fiscalcode[0:15] + chk
                    return {
                        'value': {name: value},
                        'warning': {
                            'title': 'Invalid fiscalcode!',
                            'message': 'Fiscal code could be %s' % value
                        }
                    }
            return {'value': {name: fiscalcode}}
        return {}


class commitment_line(orm.Model):
    _name = 'account.vat.communication.line'

    def _idpaese(self, cr, uid, line, arg, context=None):
        vat = line.partner_id.vat
        if vat:
            return vat[0:2]
        return ''

    def _idcodice(self, cr, uid, line, arg, context=None):
        vat = line.partner_id.vat
        if vat:
            return vat[2:]
        return ''

    def _codicefiscale(self, cr, uid, line, arg, context=None):
        return line.partner_id.fiscalcode

    def _tipodocumento(self, cr, uid, line, arg, context=None):
        doctype = line.partner_id.type
        if doctype in ('out_invoice', 'in_invoice'):
            return 'TD01'
        elif doctype in ('out_refund', 'in_refund'):
            return 'TD04'
        return False


class commitment_DTE_line(commitment_line):

    def _xml_idpaese(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._idpaese(cr, uid, line, arg, context=None)
        return res

    def _xml_idcodice(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._idcodice(cr, uid, line, arg, context=None)
        return res

    def _xml_codicefiscale(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._codicefiscale(cr, uid, line, arg,
                                               context=None)
        return res

    def _xml_tipodocumento(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._tipodocumento(cr, uid, line, arg,
                                               context=None)
        return res

    _name = 'account.vat.communication.dte.line'
    _columns = {
        'commitment_id': fields.many2one(
            'account.vat.communication', 'VAT commitment'),
        'partner_id': fields.many2one(
            'res.partner', 'Partner'),
        'xml_IdPaese': fields.function(
            _xml_idpaese,
            string="Country",
            type="char",
            store=True,
            select=True,
            readonly=True),
        'xml_IdCodice': fields.function(
            _xml_idcodice,
            string="Country",
            type="char",
            store=True,
            select=True,
            readonly=True),
        'xml_CodiceFiscale': fields.function(
            _xml_codicefiscale,
            string="Fiscalcode",
            type="char",
            store=True,
            select=True,
            readonly=True),
        'xml_TipoDocumento': fields.function(
            _xml_tipodocumento,
            string="Document type",
            help="Values: TD01=invoice, TD04=refund",
            type="char",
            store=True,
            select=True,
            readonly=True),
        'amount_total': fields.float(
            'Amount', digits_compute=dp.get_precision('Account')),
    }


class commitment_DTR_line(commitment_line):

    def _xml_idpaese(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._idpaese(cr, uid, line, arg, context=None)
        return res

    def _xml_idcodice(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._idcodice(cr, uid, line, arg, context=None)
        return res

    def _xml_codicefiscale(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._codicefiscale(cr, uid, line, arg,
                                               context=None)
        return res

    def _xml_tipodocumento(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._tipodocumento(cr, uid, line, arg,
                                               context=None)
        return res

    _name = 'account.vat.communication.dtr.line'
    _columns = {
        'commitment_id': fields.many2one(
            'account.vat.communication', 'VAT commitment'),
        'partner_id': fields.many2one(
            'res.partner', 'Partner'),
        'xml_IdPaese': fields.function(
            _xml_idpaese,
            string="Country",
            type="char",
            store=True,
            select=True,
            readonly=True),
        'xml_IdCodice': fields.function(
            _xml_idcodice,
            string="Country",
            type="char",
            store=True,
            select=True,
            readonly=True),
        'xml_CodiceFiscale': fields.function(
            _xml_codicefiscale,
            string="Fiscalcode",
            type="char",
            store=True,
            select=True,
            readonly=True),
        'xml_TipoDocumento': fields.function(
            _xml_tipodocumento,
            string="Document type",
            help="Values: TD01=invoice, TD04=refund",
            type="char",
            store=True,
            select=True,
            readonly=True),
        'amount_total': fields.float(
            'Amount', digits_compute=dp.get_precision('Account')),
    }


class AccountPeriod(orm.Model):
    _inherit = "account.period"
    _columns = {
        'vat_commitment_id': fields.many2one(
            'account.vat.communication', "VAT commitment"),
    }
