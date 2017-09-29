# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#    Copyright (C) 2017    Didotech srl <http://www.didotech.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
#
import logging
from openerp.osv import fields, orm
import openerp.addons.decimal_precision as dp
_logger = logging.getLogger(__name__)
try:
    from openerp.addons.l10n_it_ade import ade
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
        'codice_carica': fields.selection(
            ade.ADE_LEGALS['codice_carica'],
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

    def build_tax_tree(self, cr, uid, company_id, context=None):
        """
        account.tax.code records cannot be recognized as VAT or base amount and
        Italian law requires to couple base and VAT amounts,
        thats is stored on account.tax model.
        This function rebuilds (base,VAT) couples throught account.tax.
        Warning: end-user could have set many-2-many base,VAT relationship;
        in this case some couple (base,VAT) may be wrong.
        However, all tutorial of Odoo Italian Comunity and standard Italian
        Localization have just one-2-one relationshiop on (base,VAT).
        return: tax_tree[type][basevat][left], where
        - type may be 'sale', 'purchase' or 'all'
        - basevat may be 'tax_code_id', 'base_code_id', 'ref_tax_code_id' or
              'ref_base_code_id'
        - left is id of account.tax.code record
        """
        context = context or {}
        tax_model = self.pool['account.tax']
        tax_ids = tax_model.search(
            cr, uid, [('company_id', '=', company_id)])
        tax_tree = {}
        for tax_id in tax_ids:
            tax = tax_model.browse(cr, uid, tax_id)
            type = tax.type_tax_use
            if type not in tax_tree:
                tax_tree[type] = {}
            for basevat in ('tax_code_id', 'base_code_id',
                            'ref_tax_code_id', 'ref_base_code_id'):
                if basevat[-11:] == 'tax_code_id':
                    vatbase = basevat[0:-11] + 'base_code_id'
                elif basevat[-12:] == 'base_code_id':
                    vatbase = basevat[0:-12] + 'tax_code_id'
                else:
                    vatbase = False             # never should run here!
                if basevat not in tax_tree[type]:
                    tax_tree[type][basevat] = {}
                if getattr(tax, basevat):
                    left = getattr(tax, basevat).id
                    if getattr(tax, vatbase):
                        right = getattr(tax, vatbase).id
                        tax_tree[type][basevat][left] = right
                    elif left not in tax_tree[type][basevat]:
                        tax_tree[type][basevat][left] = False
        return tax_tree

    def load_invoices(self, cr, uid, commitment, commitment_line_obj,
                      dte_dtr_id, where, comm_lines, context=None):
        """Read all in/out invoices and return amount and fiscal parts"""
        invoice_obj = self.pool['account.invoice']
        account_tax_obj = self.pool['account.tax']
        for invoice_id in invoice_obj.search(cr, uid, where):
            inv_line = {}
            invoice = invoice_obj.browse(cr, uid, invoice_id)
            for invoice_tax in invoice.tax_line:
                tax_type = False
                tax_rate = 0.0
                if invoice_tax.tax_code_id:
                    taxbase_id = invoice_tax.tax_code_id.id
                    tax_vat_id = False
                    # for vat in invoice_tax.tax_code_id.tax_ids:
                    for vat_id in account_tax_obj.search(
                            cr, uid, [('tax_code_id', '=', taxbase_id)]):
                        vat = account_tax_obj.browse(cr, uid, vat_id)
                        if vat and vat.amount > tax_rate:
                            tax_rate = vat.amount
                else:
                    taxbase_id = invoice_tax.base_code_id.id
                    tax_vat_id = invoice_tax.tax_code_id.id
                    tax_type = 'N'
                if taxbase_id not in inv_line:
                    inv_line[taxbase_id] = {}
                    inv_line[taxbase_id]['amount_taxable'] = 0.0
                    inv_line[taxbase_id]['amount_tax'] = 0.0
                    inv_line[taxbase_id]['amount_total'] = 0.0
                    inv_line[taxbase_id]['tax_vat_id'] = tax_vat_id
                    inv_line[taxbase_id]['tax_rate'] = tax_rate
                    inv_line[taxbase_id]['tax_type'] = tax_type
                inv_line[taxbase_id]['amount_taxable'] += invoice_tax.base
                inv_line[taxbase_id]['amount_tax'] += invoice_tax.amount
                inv_line[taxbase_id]['amount_total'] += round(
                    invoice_tax.base + invoice_tax.amount, 2)
            if inv_line:
                comm_lines[invoice_id] = {}
                comm_lines[invoice_id]['partner_id'] = invoice.partner_id.id
                comm_lines[invoice_id]['taxes'] = inv_line
        return comm_lines

    def load_DTE_DTR(self, cr, uid, commitment, commitment_line_obj,
                     dte_dtr_id, context=None):
        journal_obj = self.pool['account.journal']
        exclude_journal_ids = journal_obj.search(
            cr, uid, [('rev_charge', '=', False)])
        period_ids = [x.id for x in commitment.period_ids]
        company_id = commitment.company_id.id
        # tax_tree = self.build_tax_tree(cr, uid, company_id, context)
        where = [('company_id', '=', company_id),
                 ('period_id', 'in', period_ids),
                 ('journal_id', 'not in', exclude_journal_ids)]
        if dte_dtr_id == 'DTE':
            where.append(('type', 'in', ['out_invoice', 'out_refund']))
        elif dte_dtr_id == 'DTR':
            where.append(('type', 'in', ['in_invoice', 'in_refund']))
        else:
            return

        comm_lines = self.load_invoices(cr, uid,
                                        commitment, commitment_line_obj,
                                        dte_dtr_id, where, {}, context)
        if comm_lines:
            for line_id in commitment_line_obj.search(
                cr, uid, [('commitment_id', '=', commitment.id),
                          ('invoice_id', 'not in', comm_lines.keys()), ]):
                commitment_line_obj.unlink(cr, uid, [line_id])
        for invoice_id in comm_lines:
            for line_id in commitment_line_obj.search(
                cr, uid, [('commitment_id', '=', commitment.id),
                          ('invoice_id', '=', invoice_id),
                          ('tax_id', 'not in', comm_lines[
                              invoice_id]['taxes'].keys()),
                          ]):
                commitment_line_obj.unlink(cr, uid, [line_id])
            for tax_id in comm_lines[invoice_id]['taxes']:
                line = {'commitment_id': commitment.id,
                        'invoice_id': invoice_id,
                        'tax_id': tax_id,
                        'partner_id': comm_lines[invoice_id]['partner_id'],
                        }
                for f in ('amount_total',
                          'amount_taxable',
                          'amount_tax',
                          'tax_vat_id',
                          'tax_rate',
                          'tax_type'):
                    line[f] = comm_lines[invoice_id]['taxes'][tax_id][f]
                ids = commitment_line_obj.search(
                    cr, uid, [('commitment_id', '=', commitment.id),
                              ('invoice_id', '=', invoice_id),
                              ('tax_id', '=', tax_id), ])
                if ids:
                    commitment_line_obj.write(cr, uid, ids, line)
                else:
                    commitment_line_obj.create(cr, uid, line)

    def load_DTE(self, cr, uid, commitment, context=None):
        """Read all sale invoices in periods"""
        context = context or {}
        commitment_DTE_line_obj = self.pool[
            'account.vat.communication.dte.line']
        self.load_DTE_DTR(
            cr, uid, commitment, commitment_DTE_line_obj, 'DTE', context)

    def load_DTR(self, cr, uid, commitment, context=None):
        """Read all purchase invoices in periods"""
        context = context or {}
        commitment_DTR_line_obj = self.pool[
            'account.vat.communication.dtr.line']
        self.load_DTE_DTR(
            cr, uid, commitment, commitment_DTR_line_obj, 'DTR', context)

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

    def _paese_codice(self, cr, uid, line, arg, context=None):
        vat = line.partner_id.vat
        return {'xml_IdPaese': vat and vat[0:2] or '',
                'xml_IdCodice': vat and vat[2:] or ''}

    def _dati_line(self, cr, uid, line, arg, context=None):
        if line.partner_id.individual or line.partner_id.fiscalcode:
            res = {'xml_CodiceFiscale': line.partner_id.fiscalcode}
        else:
            res = {'xml_CodiceFiscale':
                   line.partner_id.vat and line.partner_id.vat[2:] or ''}
        res['xml_ImponibileImporto'] = line.amount_taxable
        res['xml_Imposta'] = line.amount_tax
        res['xml_Aliquota'] = line.tax_rate
        res['xml_Natura'] = line.tax_type
        return res

    def _codicefiscale(self, cr, uid, line, arg, context=None):
        if line.partner_id.individual or line.partner_id.fiscalcode:
            return line.partner_id.fiscalcode
        else:
            return line.partner_id.vat and line.partner_id.vat[2:] or ''

    def _tipodocumento(self, cr, uid, line, arg, context=None):
        doctype = line.invoice_id.type
        if doctype in ('out_invoice', 'in_invoice'):
            return 'TD01'
        elif doctype in ('out_refund', 'in_refund'):
            return 'TD04'
        return False


class commitment_DTE_line(commitment_line):
    _name = 'account.vat.communication.dte.line'

    def _xml_paese_codice(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._paese_codice(cr, uid, line, arg, context=None)
        return res

    def _xml_dati_line(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._dati_line(cr, uid, line, arg,
                                           context=None)
        return res

    def _xml_tipodocumento(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._tipodocumento(cr, uid, line, arg,
                                               context=None)
        return res

    _columns = {
        'commitment_id': fields.many2one(
            'account.vat.communication', 'VAT commitment'),
        'invoice_id': fields.many2one(
            'account.invoice', 'Invoice'),
        'tax_id': fields.many2one(
            'account.tax.code', 'VAT code'),
        'partner_id': fields.many2one(
            'res.partner', 'Partner',
            readony=True),
        'tax_vat_id': fields.many2one(
            'account.tax.code', 'VAT code',
            readony=True),
        'tax_rate': fields.float(
            'VAT rate',
            readony=True),
        'tax_type': fields.char(
            'VAT type',
            readony=True),
        'amount_total': fields.float(
            'Amount', digits_compute=dp.get_precision('Account')),
        'amount_taxable': fields.float(
            'Taxable amount', digits_compute=dp.get_precision('Account')),
        'amount_tax': fields.float(
            'Tax amount', digits_compute=dp.get_precision('Account')),
        'xml_IdPaese': fields.function(
            _xml_paese_codice,
            string="Country",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_IdCodice': fields.function(
            _xml_paese_codice,
            string="VAT number",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_CodiceFiscale': fields.function(
            _xml_dati_line,
            string="Fiscalcode",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_TipoDocumento': fields.function(
            _xml_tipodocumento,
            string="Document type",
            help="Values: TD01=invoice, TD04=refund",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_ImponibileImporto': fields.function(
            _xml_dati_line,
            string="Taxable",
            type="float",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_Imposta': fields.function(
            _xml_dati_line,
            string="Tax",
            type="float",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_Aliquota': fields.function(
            _xml_dati_line,
            string="Tax rate",
            type="float",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_Natura': fields.function(
            _xml_dati_line,
            string="Tax type",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
    }


class commitment_DTR_line(commitment_line):
    _name = 'account.vat.communication.dtr.line'

    def _xml_paese_codice(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._paese_codice(cr, uid, line, arg, context=None)
        return res

    def _xml_dati_line(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._dati_line(cr, uid, line, arg,
                                           context=None)
        return res

    def _xml_tipodocumento(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = self._tipodocumento(cr, uid, line, arg,
                                               context=None)
        return res

    _columns = {
        'commitment_id': fields.many2one(
            'account.vat.communication', 'VAT commitment'),
        'invoice_id': fields.many2one(
            'account.invoice', 'Invoice'),
        'tax_id': fields.many2one(
            'account.tax.code', 'VAT code'),
        'partner_id': fields.many2one(
            'res.partner', 'Partner',
            readony=True),
        'tax_vat_id': fields.many2one(
            'account.tax.code', 'VAT code',
            readony=True),
        'tax_rate': fields.float(
            'VAT rate',
            readony=True),
        'tax_type': fields.char(
            'VAT type',
            readony=True),
        'amount_total': fields.float(
            'Amount', digits_compute=dp.get_precision('Account')),
        'amount_taxable': fields.float(
            'Taxable amount', digits_compute=dp.get_precision('Account')),
        'amount_tax': fields.float(
            'Tax amount', digits_compute=dp.get_precision('Account')),
        'xml_IdPaese': fields.function(
            _xml_paese_codice,
            string="Country",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_IdCodice': fields.function(
            _xml_paese_codice,
            string="VAT number",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_CodiceFiscale': fields.function(
            _xml_dati_line,
            string="Fiscalcode",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_TipoDocumento': fields.function(
            _xml_tipodocumento,
            string="Document type",
            help="Values: TD01=invoice, TD04=refund",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_ImponibileImporto': fields.function(
            _xml_dati_line,
            string="Taxable",
            type="float",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_Imposta': fields.function(
            _xml_dati_line,
            string="Tax",
            type="float",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_Aliquota': fields.function(
            _xml_dati_line,
            string="Tax rate",
            type="float",
            multi=True,
            store=False,
            select=True,
            readonly=True),
        'xml_Natura': fields.function(
            _xml_dati_line,
            string="Tax type",
            type="char",
            multi=True,
            store=False,
            select=True,
            readonly=True),
    }


class AccountPeriod(orm.Model):
    _inherit = "account.period"
    _columns = {
        'vat_commitment_id': fields.many2one(
            'account.vat.communication', "VAT commitment"),
    }
