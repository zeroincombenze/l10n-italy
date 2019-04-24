# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class FatturaPAAttachmentIn(orm.Model):
    _name = "fatturapa.attachment.in"
    _description = "E-bill import file"
    _inherits = {'ir.attachment': 'ir_attachment_id'}
    _inherit = ['mail.thread']
    _order = 'id desc'

    def _compute_xml_data(self, cr, uid, ids, name, unknow_none, context={}):
        ret = {}
        for att in self.browse(cr, uid, ids, context):
            fatt = self.pool['wizard.import.fatturapa'].get_invoice_obj(
                cr, uid, att)
            cedentePrestatore = fatt.FatturaElettronicaHeader.CedentePrestatore
            partner_id = self.pool.get('wizard.import.fatturapa').getCedPrest(
                cr, uid,
                cedentePrestatore)
            vals = {
                'xml_supplier_id': partner_id,
                'invoices_number': len(fatt.FatturaElettronicaBody),
                'invoices_total': 0,
                }
            invoices_total = 0
            for invoice_body in fatt.FatturaElettronicaBody:
                invoices_total += float(
                    invoice_body.DatiGenerali.DatiGeneraliDocumento.ImportoTotaleDocumento or 0
                )
            vals['invoices_total'] = invoices_total
            ret[att.id] = vals.get(name, False)
        return ret

    def _compute_registered(self, cr, uid, ids, name, unknow_none, context=None):
        ret = {}
        for att in self.browse(cr, uid, ids, context):
            if (att.in_invoice_ids and len(att.in_invoice_ids) == att.invoices_number):
                ret[att.id] = True
            else:
                ret[att.id] = False
        return ret

    _columns = {
        'ir_attachment_id': fields.many2one(
            'ir.attachment', 'Attachment', required=True, ondelete="cascade"),
        'in_invoice_ids': fields.one2many(
            'account.invoice', 'fatturapa_attachment_in_id',
            string="In Invoices", readonly=True),
        'xml_supplier_id': fields.function(_compute_xml_data, 
                                           method=True, 
                                           string="Supplier", 
                                           relation="res.partner",
                                           type="many2one"),
        'invoices_number': fields.function(_compute_xml_data, 
                                           method=True, 
                                           string="Invoices number", 
                                           type="integer"),
        'invoices_total': fields.function(_compute_xml_data, 
                                           method=True, 
                                           string="Invoices total", 
                                           type="float",
                                           help="Se indicato dal fornitore, Importo totale del documento al "
                 "netto dell'eventuale sconto e comprensivo di imposta a debito "
                 "del cessionario / committente"),
        'registered': fields.function(_compute_registered,
                                           string="Registered", 
                                           type="boolean"),
    }

    def get_xml_string(self, cr, uid, ids, context={}):
        for fattAttInBrws in self.browse(cr, uid, ids, context):
            return fattAttInBrws.ir_attachment_id.get_xml_string(cr, uid, fattAttInBrws.ir_attachment_id.id)
        return ''

    def set_name(self, cr, uid, ids, datas_fname, context=None):
        return {'value': {'name': datas_fname}}

