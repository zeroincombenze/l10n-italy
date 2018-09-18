# -*- coding: utf-8 -*-
#    Copyright (C) 2010-2012 Associazione Odoo Italia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import datetime
import logging
from openerp.osv import fields, orm, osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)
try:
    from codicefiscale import build
except ImportError:
    _logger.warning(
        'codicefiscale library not found. '
        'If you plan to use it, please install the codicefiscale library '
        'from https://pypi.python.org/pypi/codicefiscale')


class WizardComputeFc(orm.TransientModel):

    _name = "wizard.compute.fc"
    _description = "Compute Fiscal Code"
    _columns = {
        'fiscalcode_surname': fields.char('Surname', size=64),
        'fiscalcode_firstname': fields.char('First name', size=64),
        'birth_date': fields.date('Date of birth'),
        'birth_city': fields.many2one('res.city', 'City of birth'),
        'sex': fields.selection([('M', 'Male'),
                                 ('F', 'Female'),
                                 ], "Sex"),
    }

    def compute_fc(self, cr, uid, ids, context):
        active_id = context.get('active_id', [])
        partner = self.pool.get('res.partner').browse(
            cr, uid, active_id, context)
        form_obj = self.browse(cr, uid, ids, context)
        for wizard in form_obj:
            if (
                not wizard.fiscalcode_surname or
                not wizard.fiscalcode_firstname or not wizard.birth_date or
                not wizard.birth_city or not wizard.sex
            ):
                raise osv.except_osv(
                    _('Error'), _('One or more fields are missing'))
            if not wizard.birth_city.cadaster_code:
                raise osv.except_osv(_('Error'), _('Cataster code is missing'))
            birth_date = datetime.datetime.strptime(
                wizard.birth_date, "%Y-%m-%d")
            # CF = self._codicefiscale(
            #     wizard.fiscalcode_surname, wizard.fiscalcode_firstname, str(
            #         birth_date.day),
            #     str(birth_date.month), str(birth_date.year), wizard.sex,
            #     wizard.birth_city.cadaster_code)
            CF = build(wizard.fiscalcode_surname,
                       wizard.fiscalcode_firstname,
                       birth_date,
                       wizard.sex,
                       wizard.birth_city.cadaster_code)
            if partner.fiscalcode and partner.fiscalcode != CF:
                raise osv.except_osv(
                    _('Error'),
                    _('Existing fiscal code %s is different from the computed '
                      'one (%s). If you want to use the computed one, remove '
                      'the existing one') % (partner.fiscalcode, CF))
            self.pool.get('res.partner').write(
                cr, uid, active_id, {'fiscalcode': CF, 'individual': True})
        return {}
