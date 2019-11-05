# -*- coding: utf-8 -*-
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _compute_ddt_ids(self):
        for so in self:
            ddt_ids = []
            for picking in so.picking_ids:
                for ddt in picking.ddt_ids:
                    ddt_ids.append(ddt.id)
            so.ddt_ids = ddt_ids

    def _default_ddt_type(self):
        # TODO: FIX in separate module
        # signature = BeautifulSoup(self.env.user.signature).get_text()
        signature = self.env.user.signature
        if signature:
            a = signature.find('>')
            b = signature.find('<', a)
            signature = signature[a + 1:b]
            res = self.env['stock.ddt.type'].search(
                [('name', 'ilike', signature)], limit=1)
            if res:
                return res
        ids = self.env['stock.ddt.type'].search([], limit=1)
        if not ids:
            return False
        return ids[0].id

    carriage_condition_id = fields.Many2one(
        'stock.picking.carriage_condition', string='Carriage Condition')
    goods_description_id = fields.Many2one(
        'stock.picking.goods_description',
        string='Description of Goods')
    transportation_reason_id = fields.Many2one(
        'stock.picking.transportation_reason',
        string='Reason for Transportation')
    transportation_method_id = fields.Many2one(
        'stock.picking.transportation_method',
        string='Method of Transportation')
    ddt_carrier_id = fields.Many2one(
        'res.partner', string='Carrier')
    parcels = fields.Integer('Parcels')
    weight = fields.Float(string="Weight")
    gross_weight = fields.Float(string="Gross Weight")
    volume = fields.Float('Volume')
    ddt_ids = fields.Many2many(
        'stock.picking.package.preparation',
        string='Related DdTs',
        compute='_compute_ddt_ids')
    # create_ddt = fields.Boolean('Automatically create the DDT')
    ddt_invoicing_group = fields.Selection(
        [('nothing', 'One DDT - One Invoice'),
         ('billing_partner', 'Billing Partner'),
         ('shipping_partner', 'Shipping Partners'),
         ('code_group', 'Code group')], 'DDT invoicing group',
        default='billing_partner')
    ddt_type_id = fields.Many2one(
        'stock.ddt.type', string='DdT Type', default=_default_ddt_type)
    ddt_invoice_exclude = fields.Boolean(
        string='DDT do not invoice services',
        help="If flagged services from this SO will not be automatically "
             "invoiced from DDT. This parameter can be set on partners and "
             "automatically applied to Sale Orders.")
    delivery_data_set = fields.Boolean(
        string="Delivery Data is Set")

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        result = super(SaleOrder, self).onchange_partner_id()
        if self.partner_id:
            self.carriage_condition_id = (
                self.partner_id.carriage_condition_id.id)
            self.goods_description_id = self.partner_id.goods_description_id.id
            self.transportation_reason_id = (
                self.partner_id.transportation_reason_id.id)
            self.transportation_method_id = (
                self.partner_id.transportation_method_id.id)
            self.ddt_invoicing_group = (
                self.partner_id.ddt_invoicing_group)
            self.ddt_invoice_exclude = (
                self.partner_id.ddt_invoice_exclude)
            self.ddt_type = self._default_ddt_type()
        return result

    @api.multi
    @api.onchange('ddt_type_id')
    def onchange_ddt_type(self):
        if (not self.ddt_type_id.company_id
                or self.ddt_type_id.company_id == self.company_id):
            for field in ('carriage_condition_id',
                          'goods_description_id',
                          'transportation_reason_id',
                          'transportation_method_id'):
                default_field = 'default_%s' % field
                if self.ddt_type_id[default_field]:
                    setattr(self, field, self.ddt_type_id[default_field])
            if self.ddt_type_id.note and not self.note:
                self.note = self.ddt_type_id.note
            self.delivery_data_set = True

    @api.multi
    @api.onchange('carrier_id')
    def onchange_carrier_id(self):
        if self.carrier_id:
            for field in ('carriage_condition_id',
                          'goods_description_id',
                          'transportation_reason_id',
                          'transportation_method_id'):
                if self.carrier_id[field]:
                    setattr(self, field, self.carrier_id[field])
            if self.carrier_id.note and not self.note:
                self.note = self.carrier_id.note
            self.delivery_data_set = True

    @api.multi
    def _prepare_invoice(self):
        vals = super(SaleOrder, self)._prepare_invoice()
        vals.update({
            'carriage_condition_id': self.carriage_condition_id.id,
            'goods_description_id': self.goods_description_id.id,
            'transportation_reason_id': self.transportation_reason_id.id,
            'transportation_method_id': self.transportation_method_id.id,
            'carrier_id': self.ddt_carrier_id.id,
            'parcels': self.parcels,
            'weight': self.weight,
            'gross_weight': self.gross_weight,
            'volume': self.volume,
        })
        return vals

    @api.multi
    def action_create_ddt(self):
        ddt_model = self.env['stock.picking.package.preparation']
        for order in self:
            picking_ids = []
            for picking in order.picking_ids:
                if len(picking.mapped('ddt_ids')) == 0:
                    picking_ids.append(picking)
            if not picking_ids:
                raise UserError(
                    _("There are not picking to create a DdT"))
            ddt = ddt_model.create(ddt_model.preparare_ddt_data(
                picking_ids,
                partner=self.partner_id))
            if order.invoice_status == 'no':
                order.invoice_status = 'to invoice'
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

    @api.multi
    def action_cancel(self):
        for order in self:
            for ddt in order.ddt_ids:
                if ddt.state == 'draft':
                    ddt.unlink()
                else:
                    raise UserError(
                        _("Document %d has invoice linked" % ddt.ddt_number))
        return super(SaleOrder, self).action_cancel()

    @api.multi
    def action_view_ddt(self):
        mod_obj = self.env['ir.model.data']
        act_obj = self.env['ir.actions.act_window']

        result = mod_obj.get_object_reference(
            'stock_picking_package_preparation',
            'action_stock_picking_package_preparation')
        ddt_id = result and result[1] or False
        result = act_obj.browse(ddt_id).read()[0]

        ddt_ids = []
        for so in self:
            ddt_ids += [ddt.id for ddt in so.ddt_ids]

        if len(ddt_ids) > 1:
            result['domain'] = "[('id','in',[" + ','.join(
                map(str, ddt_ids)) + "])]"
        else:
            res = mod_obj.get_object_reference(
                'stock_picking_package_preparation',
                'stock_picking_package_preparation_form')
            result['views'] = [(res and res[1] or False, 'form')]
            result['res_id'] = ddt_ids and ddt_ids[0] or False
        return result

    def get_delivery_values(self, vals):
        '''If write is called from exteranl partner (i.e. e-commerce)
        delivery data will be empty even if ddt_type and/or carrier_id are set
        In ordinary edit by end-user, delivery_data_set is True'''
        if not vals.get('delivery_data_set'):
            if vals.get('partner_id'):
                partner = self.env['res.partner'].browse(
                    vals['partner_id'])
                for field in ('carriage_condition_id',
                              'goods_description_id',
                              'transportation_reason_id',
                              'transportation_method_id',
                              'ddt_invoicing_group',
                              'ddt_invoice_exclude'):
                    if partner[field] and not vals.get(field):
                        if field.endswith('_id'):
                            vals[field] = partner[field].id
                        else:
                            vals[field] = partner[field]
                if not vals.get('ddt_type_id'):
                    vals['ddt_type_id'] = self.env[
                        'sale.order']._default_ddt_type()
            if vals.get('ddt_type_id'):
                ddt_type = self.env['stock.ddt.type'].browse(
                    vals['ddt_type_id'])
                for field in ('carriage_condition_id',
                              'goods_description_id',
                              'transportation_reason_id',
                              'transportation_method_id'):
                    default_field = 'default_%s' % field
                    if ddt_type[default_field] and not vals.get(field):
                        vals[field] = ddt_type[default_field].id
                if self.ddt_type_id.note and not self.note:
                    self.note = self.ddt_type_id.note
            if vals.get('carrier_id'):
                carrier = self.env['delivery.carrier'].browse(
                    vals['carrier_id'])
                for field in ('carriage_condition_id',
                              'goods_description_id',
                              'transportation_reason_id',
                              'transportation_method_id',
                              'ddt_carrier_id'):
                    if carrier[field] and not vals.get(field):
                        vals[field] = carrier[field].id
        vals['delivery_data_set'] = True
        return vals

    @api.multi
    def write(self, vals):
        vals = self.get_delivery_values(vals)
        return super(SaleOrder, self).write(vals)

    @api.model
    def create(self, vals):
        vals = self.get_delivery_values(vals)
        return super(SaleOrder, self).create(vals)
