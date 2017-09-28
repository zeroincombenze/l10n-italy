# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
#
import base64
from openerp.tools.translate import _
# import datetime
import logging

from openerp.addons.l10n_it_ade.bindings.dati_fattura_v_2_0 import (
    DatiFatturaHeaderType,
    DTEType,
    DTRType,)
#   ANNType)
from openerp.osv import fields, orm
# from openerp.tools import DEFAULT_SERVER_DATE_FORMAT


_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


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

    def set_progressivo_telematico(self, cr, uid, statement, context=None):
        context = context or {}
        company_id = statement.company_id.id
        sequence_obj = self.pool['ir.sequence']
        sequence_ids = sequence_obj.search(
            cr, uid, [('name', '=', 'vat_communication'),
                      ('company_id', '=', company_id)])
        if len(sequence_ids) != 1:
            raise orm.except_orm(
                _('Error!'), _('VAT communication sequence not set!'))
        number = sequence_obj.next_by_id(
            cr, uid, sequence_ids[0], context=context)
        statement.progressivo_telematico = number

    def export_vat_communication(self, cr, uid, ids, context=None):
        context = context or {}
        model_data_obj = self.pool['ir.model.data']
        statement_obj = self.pool['account.vat.communication']
        statement_ids = context.get('active_ids', False)
        if statement_ids:
            for statement in statement_obj.browse(
                    cr, uid, statement_ids, context=context):
                if not statement.progressivo_telematico:
                    self.set_progressivo_telematico(cr, uid, statement,
                                                    context)
                communication = DatiFatturaHeaderType()
                communication.DTE = (DTEType())
                communication.DTR = (DTRType())
                fn_name = 'test'
                vat_communication_xml = communication.toDOM().toprettyxml(
                    encoding="latin1")
                attach_vals = {
                    'name': fn_name,
                    'datas_fname': fn_name,
                    'datas': base64.encodestring(vat_communication_xml),
                    'res_model': 'account.vat.communication',
                    'res_id': communication.id
                }
                vat_communication_attachment_out_id = self.pool[
                    'account.vat.communication.attachment'].create(
                        cr, uid, attach_vals, context={})
                view_rec = model_data_obj.get_object_reference(
                    cr, uid, 'account_vat_period_communication',
                    'view_vat_communication_attachment_form')
                if view_rec:
                    view_id = view_rec and view_rec[1] or False
            return {
                'view_type': 'form',
                'name': "Export Comunicazione IVA",
                'view_id': [view_id],
                'res_id': vat_communication_attachment_out_id,
                'view_mode': 'form',
                'res_model': 'account.vat.communication.attachment',
                'type': 'ir.actions.act_window',
                'context': context
            }
