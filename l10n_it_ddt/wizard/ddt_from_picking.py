# -*- coding: utf-8 -*-
#    Author: Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
#    Author: Gianmarco Conte <gconte@dinamicheaziendali.it>
#    Author: Gabriele Baldessari <gabriele.baldessari@abstract-technology.com>
#    Copyright (C) Francesco Apruzzese
#    Copyright (C) 2014-2015 Agile Business Group (http://www.agilebg.com)
#    License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _
from odoo.exceptions import Warning as UserError


class StockPickingPackagePreparation(models.Model):
    _inherit = 'stock.picking.package.preparation'

    FIELD_MAP = {
        'res.partner': {
            'ddt_type_id': False,
            'carrier_id': 'property_carrier_id',
            'parcels': False,
            'ddt_carrier_id': False,
            'show_price': 'ddt_show_price',
            'note': False},
        'stock.ddt.type': {
            'ddt_type_id': '',
            'carrier_id': False,
            'goods_description_id': 'default_goods_description_id',
            'carriage_condition_id': 'default_carriage_condition_id',
            'transportation_reason_id': 'default_transportation_reason_id',
            'transportation_method_id': 'default_transportation_method_id',
            'parcels': False,
            'ddt_carrier_id': False,
            'show_price': False},
        'delivery.carrier': {
            'ddt_type_id': False,
            'carrier_id': '',
            'parcels': False,
            'show_price': False},
        'sale.order': {
            'ddt_carrier_id': False,
            'parcels': False,
            'show_price': False},
        'stock.picking': {
            'ddt_type_id': 'ddt_type',
            'goods_description_id': False,
            'carriage_condition_id': False,
            'transportation_reason_id': False,
            'transportation_method_id': False,
            'parcels': 'number_of_packages',
            'ddt_carrier_id': False,
            'show_price': False,
            'note': False,
            'gross_weight': 'shipping_weight'},
        'stock.picking.package.preparation': {
            'carrier_id': False,
            'weight': 'weight_manual',
            'ddt_carrier_id': 'carrier_id'}
    }

    def fieldname_of_model(self, model, fieldname):
        if fieldname not in self.FIELD_MAP[model]:
            return fieldname
        return self.FIELD_MAP[model][fieldname]


class DdTFromPickings(models.TransientModel):
    _name = "ddt.from.pickings"

    def _get_picking_ids(self):
        return self.env['stock.picking'].browse(self.env.context['active_ids'])

    picking_ids = fields.Many2many('stock.picking', default=_get_picking_ids)


    @api.multi
    def create_ddt(self):

        def get_delivery_value(vals, picking, fieldname, condition_help):
            '''Set specific condition of delivey. Inherit condition from
            picking > sale order > ddt type > delivery method > customer
            Workflow (rp=res.partner, dt=stock.ddt.type dc=delivery.carrier,
                      so=sale.order, sp=stock.picking,
                      pp=stock.picking.package.preparation):
            Field name               | rp | dt | dc | so | sp | pp
            -------------------------|----|----|----|----|----|---
            ddt_type_id              | X  | ID | X  | Ok | 3. | Ok
            carrier_id               | 1. | X  | ID | Ok | Ok | X
            goods_description_id     | Ok | 2. | Ok | Ok | X  | Ok
            carriage_condition_id    | Ok | 2. | Ok | Ok | X  | Ok
            transportation_reason_id | Ok | 2. | Ok | Ok | X  | Ok
            transportation_method_id | Ok | 2. | Ok | Ok | X  | Ok
            ddt_carrier_id           | X  | X  | Ok | X  | X  | 5.
            show_price               | 6. | X  | X  | X  | X  | Ok
            note                     | X  | Ok | Ok | Ok | X  | Ok
            parcels (*)              |    |    |    | Ok | 4. | Ok
            weight (*)               |    |    |    | Ok | Ok | Ok
            gross_weight (*)         |    |    |    | Ok | 7. | Ok
            where:
            Ok: field in model
            X:  field not in model
            ID: field is key of model
            1.  field name is "property_carrier_id"
            2.  field name is prefixed with "default_"
            3.  field name is ddt_type
            4.  field name is "number_of packages"
            5.  field name is "carrier_id"
            6.  field name is "ddt_show_price"
            7.  field name is "shipping_weight"
            (*) field evaluated by sum, searched only in <sp> and <so>
            '''
            ddt_model = self.env['stock.picking.package.preparation']
            pp_fieldname = ddt_model.fieldname_of_model(
                'stock.picking.package.preparation', fieldname)
            if not pp_fieldname:
                return vals
            if not vals.get(fieldname):
                sp_fieldname = ddt_model.fieldname_of_model(
                    'stock.picking', fieldname)
                so_fieldname = ddt_model.fieldname_of_model(
                    'sale.order', fieldname)
                dc_fieldname = ddt_model.fieldname_of_model(
                    'delivery.carrier', fieldname)
                dt_fieldname = ddt_model.fieldname_of_model(
                    'stock.ddt.type', fieldname)
                rp_fieldname = ddt_model.fieldname_of_model(
                    'res.partner', fieldname)
                # field from picking ?
                if (sp_fieldname and
                        picking[sp_fieldname]):
                    if fieldname.endswith('_id'):
                        vals[pp_fieldname] = picking[sp_fieldname].id
                    else:
                        vals[pp_fieldname] = picking[sp_fieldname]
                # field from sale.order ?
                elif (so_fieldname and
                        picking.sale_id and
                        picking.sale_id[so_fieldname]):
                    if fieldname.endswith('_id'):
                        vals[pp_fieldname] = picking.sale_id[so_fieldname].id
                    else:
                        vals[pp_fieldname] = picking.sale_id[so_fieldname]
                # field from delivery.carrier?
                elif (dc_fieldname and
                        picking.sale_id and
                        picking.sale_id.carrier_id and
                        picking.sale_id.carrier_id[dc_fieldname]):
                    if fieldname.endswith('_id'):
                        vals[pp_fieldname] = picking.sale_id.carrier_id[
                            dc_fieldname].id
                    else:
                        vals[pp_fieldname] = picking.sale_id.carrier_id[
                            dc_fieldname]
                # field from stock.ddt.type ?
                elif (dt_fieldname and
                        picking.ddt_type and
                        picking.ddt_type[dt_fieldname]):
                    if fieldname.endswith('_id'):
                        vals[pp_fieldname] = picking.ddt_type[dt_fieldname].id
                    else:
                        vals[pp_fieldname] = picking.ddt_type[dt_fieldname]
                # field from partner ?
                elif (rp_fieldname and
                        picking.partner_id and
                        picking.partner_id[rp_fieldname]):
                    if fieldname.endswith('_id'):
                        vals[pp_fieldname] = picking.partner_id[rp_fieldname].id
                    else:
                        vals[pp_fieldname] = picking.partner_id[rp_fieldname]
            elif fieldname != 'note':
                # check on picking, if field is valid
                if sp_fieldname and picking[sp_fieldname]:
                     if picking[sp_fieldname].id != vals[pp_fieldname]:
                         raise UserError(
                             _('Selected Pickings have different %s' %
                               condition_help))
                # otherwise check in sale order of picking (if exists)
                elif (picking.sale_id and
                      picking.sale_id[so_fieldname] and
                      picking.sale_id[so_fieldname].id != vals[pp_fieldname]):
                    raise UserError(
                        _('Selected Pickings have different %s' %
                          condition_help))
            return vals

        def sum_delivery_value(vals, picking, fieldname):
            ddt_model = self.env['stock.picking.package.preparation']
            pp_fieldname = ddt_model.fieldname_of_model(
                'stock.picking.package.preparation', fieldname)
            so_fieldname = ddt_model.fieldname_of_model(
                'sale.order', fieldname)
            sp_fieldname = ddt_model.fieldname_of_model(
                'stock.picking', fieldname)
            if not vals.get(pp_fieldname):
                vals[pp_fieldname] = 0
            # field from picking ?
            if sp_fieldname and picking[sp_fieldname]:
                vals[pp_fieldname] += picking[sp_fieldname]
            # field from sale.order ?
            elif so_fieldname and picking.sale_id:
                vals[pp_fieldname] += picking.sale_id[so_fieldname]
            return vals

        vals = { 'partner_id': False }
        partner = False
        for picking in self.picking_ids:
            # check if picking is already linked to a DDT
            self.env['stock.picking.package.preparation'].check_linked_picking(
                picking)
            current_ddt_shipping_partner = picking.get_ddt_shipping_partner()
            if partner and partner != current_ddt_shipping_partner:
                raise UserError(
                    _("Selected Pickings have different Partner"))
            partner = current_ddt_shipping_partner
            sale_order = picking.sale_id
            if sale_order:
                vals['partner_id'] = sale_order.partner_id.id
            else:
                vals['partner_id'] = partner.commercial_partner_id.id
            if not picking.picking_type_code == 'internal':
                vals['partner_shipping_id'] = partner.id
            else:
                vals['partner_shipping_id'] = (
                    picking.location_dest_id.partner_id.id)
        # check if selected picking have different destinations
        if len(self.picking_ids.mapped('location_dest_id')) > 1:
            raise UserError(_("Selected pickings have different destinations"))
        for picking in self.picking_ids:
            vals = get_delivery_value(
                vals, picking, 'ddt_type_id', _('ddt type'))
        if not vals.get('ddt_type_id'):
            ddt_type = self.env['stock.ddt.type'].search([], limit=1)
            if ddt_type:
                vals['ddt_type_id'] = ddt_type[0].id
        for picking in self.picking_ids:
            vals = get_delivery_value(
                vals, picking, 'carrier_id', _('delivery method'))
        for picking in self.picking_ids:
            vals = get_delivery_value(
                vals, picking, 'ddt_carrier_id', _('carrier'))
            vals = get_delivery_value(
                vals, picking, 'show_price', _('show price'))
            vals = get_delivery_value(
                vals, picking, 'note', _('note'))
            vals = get_delivery_value(
                vals, picking, 'carriage_condition_id',
                _('carriage condition'))
            vals = get_delivery_value(
                vals, picking, 'goods_description_id',
                _('goods description'))
            vals = get_delivery_value(
                vals, picking, 'transportation_reason_id',
                _('transportation reason'))
            vals = get_delivery_value(
                vals, picking, 'transportation_method_id',
                _('transportation method'))
            vals = sum_delivery_value(vals, picking, 'parcels')
            vals = sum_delivery_value(vals, picking, 'weight') 
            vals = sum_delivery_value(vals, picking, 'gross_weight')
            vals = sum_delivery_value(vals, picking, 'volume')
        if not vals.get('parcels'):
            vals['parcels'] = 1

        picking_ids = [p.id for p in self.picking_ids]
        vals.update({'picking_ids': [(6, 0, picking_ids)]})
        ddt = self.env['stock.picking.package.preparation'].create(vals)
        # ----- Show new ddt
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
            'res_id': ddt.id,
            'view_id': False,
            'views': [(form_id, 'form'), (tree_id, 'tree')],
            'type': 'ir.actions.act_window',
        }


class StockPicking(models.Model):
    _inherit = "stock.picking"

    ddt_type = fields.Many2one(
        'stock.ddt.type',
        related='picking_type_id.default_location_src_id.type_ddt_id')
