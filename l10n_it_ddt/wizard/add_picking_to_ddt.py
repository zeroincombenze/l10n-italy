# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2015 Nicola Malcontenti - Agile Business Group
#    Copyright (C) 2015 Apulia Software s.r.l. (http://www.apuliasoftware.it)
#    @author Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
#
#    License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
##############################################################################


from odoo import fields, models, api, _
from odoo.exceptions import Warning as UserError


class AddPickingToDdt(models.TransientModel):

    _name = "add.pickings.to.ddt"

    ddt_id = fields.Many2one('stock.picking.package.preparation')

    @api.model
    def check_4_delivery_value(self, picking, fieldname, condition_help):
        '''Check if current delivery condition is equal to DdT condition.
        See file "ddt_from_picking" to furthermo information.'''
        ddt_model = self.env['stock.picking.package.preparation']
        pp_fieldname = ddt_model.fieldname_of_model(
            'stock.picking.package.preparation', fieldname)
        sp_fieldname = ddt_model.fieldname_of_model(
            'stock.picking', fieldname)
        so_fieldname = ddt_model.fieldname_of_model(
            'sale.order', fieldname)
        # check on picking, if field is valid
        if sp_fieldname and picking[sp_fieldname]:
             if picking[sp_fieldname] != self.ddt_id[pp_fieldname]:
                 raise UserError(
                     _('Selected Pickings have different %s' %
                       condition_help))
        # otherwise check in sale order of picking (if exists)
        elif (so_fieldname and
              picking.sale_id and
              picking.sale_id[so_fieldname] and
              picking.sale_id[so_fieldname] != self.ddt_id[pp_fieldname]):
            raise UserError(
                _('Selected Picking %s has different %s' %
                  (picking.name, condition_help)))

    @api.multi
    def add_to_ddt(self):
        pickings = self.env['stock.picking'].browse(
            self.env.context['active_ids'])
        for picking in pickings:
            # check if picking is already linked to a DDT
            self.env['stock.picking.package.preparation'].check_linked_picking(
                picking)
            current_ddt_shipping_partner = picking.get_ddt_shipping_partner()
            if picking.ddt_ids and \
                    self.ddt_id.id in [d.id for d in picking.ddt_ids]:
                raise UserError(
                    _("Picking %s already in ddt") % picking.name)
            elif (
                current_ddt_shipping_partner != self.ddt_id.partner_shipping_id
            ):
                raise UserError(
                    _("Selected Picking %s have"
                      " different Partner") % picking.name)

            if picking.sale_id:
                for fieldname, condition_help in (
                        ('carriage_condition_id', _('carriage condition')),
                        ('goods_description_id', _('goods description')),
                        ('transportation_reason_id', _('transportation reason')),
                        ('transportation_method_id', _('transportation method')),
                        ('ddt_carrier_id', _('carrier'))):
                    self.check_4_delivery_value(
                        picking, fieldname, condition_help)
            self.ddt_id.picking_ids = [(4, picking.id)]
        ir_model_data = self.env['ir.model.data']
        form_res = ir_model_data.get_object_reference(
            'stock_picking_package_preparation',
            'stock_picking_package_preparation_form')
        form_id = form_res and form_res[1] or False
        tree_res = ir_model_data.get_object_reference(
            'stock_picking_package_preparation',
            'stock_picking_package_preparation_tree')
        tree_id = tree_res and tree_res[1] or False
        return {
            'name': 'DdT',
            'view_type': 'form',
            'view_mode': 'form,tree',
            'res_model': 'stock.picking.package.preparation',
            'res_id': self.ddt_id.id,
            'view_id': False,
            'views': [(form_id, 'form'), (tree_id, 'tree')],
            'type': 'ir.actions.act_window',
        }
