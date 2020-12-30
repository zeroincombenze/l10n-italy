# -*- coding: utf-8 -*-
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
from datetime import datetime

import odoo.addons.decimal_precision as dp
from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, float_is_zero
from odoo.tools.misc import formatLang


class StockPickingCarriageCondition(models.Model):

    _name = "stock.picking.carriage_condition"
    _description = "Carriage Condition"

    name = fields.Char(string='Carriage Condition',
                       required=True, translate=True)
    note = fields.Text(string='Note', translate=True)


class StockPickingGoodsDescription(models.Model):

    _name = 'stock.picking.goods_description'
    _description = "Description of Goods"

    name = fields.Char(string='Description of Goods',
                       required=True, translate=True)
    note = fields.Text(string='Note', translate=True)


class StockPickingTransportationReason(models.Model):

    _name = 'stock.picking.transportation_reason'
    _description = 'Reason for Transportation'

    name = fields.Char(string='Reason For Transportation',
                       required=True, translate=True)
    note = fields.Text(string='Note', translate=True)
    to_be_invoiced = fields.Boolean(string='To be Invoiced')


class StockPickingTransportationMethod(models.Model):

    _name = 'stock.picking.transportation_method'
    _description = 'Method of Transportation'

    name = fields.Char(string='Method of Transportation',
                       required=True, translate=True)
    note = fields.Text(string='Note', translate=True)


class StockDdtType(models.Model):

    _name = 'stock.ddt.type'
    _description = 'Stock DdT Type'

    name = fields.Char(required=True)
    sequence_id = fields.Many2one('ir.sequence', required=True)
    note = fields.Text(string='Note')
    default_carriage_condition_id = fields.Many2one(
        'stock.picking.carriage_condition',
        string='Default Carriage Condition')
    default_goods_description_id = fields.Many2one(
        'stock.picking.goods_description',
        string='Default Description of Goods')
    default_transportation_reason_id = fields.Many2one(
        'stock.picking.transportation_reason',
        string='Default Reason for Transportation')
    default_transportation_method_id = fields.Many2one(
        'stock.picking.transportation_method',
        string='Default Method of Transportation')
    company_id = fields.Many2one(
        comodel_name='res.company', string='Company',
        default=lambda self: self.env.user.company_id.id)


class StockPickingPackagePreparation(models.Model):

    _inherit = 'stock.picking.package.preparation'
    _rec_name = 'display_name'
    _order = 'ddt_number, date desc'

    _sql_constraints = [('ddt_number',
                         'unique(ddt_number)',
                         'DdT number already exists!')]

    @api.multi
    @api.depends('transportation_reason_id.to_be_invoiced')
    @api.depends('transportation_reason_id.to_be_invoiced')
    def _compute_to_be_invoiced(self):
        for ddt in self:
            ddt.to_be_invoiced = ddt.transportation_reason_id and \
                ddt.transportation_reason_id.to_be_invoiced or False

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
                return res.id
        ids = self.env['stock.ddt.type'].search([], limit=1)
        if not ids:
            return False
        return ids[0].id

    def _set_parcel_qty(self):
        if self.parcels == 0:
            return 1
        return self.parcels

    @api.depends('line_ids.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for ddt in self:
            amount_untaxed = amount_tax = 0.0
            for line in ddt.line_ids:
                amount_untaxed += line.price_subtotal
                # FORWARDPORT UP TO 10.0
                if (ddt.company_id.tax_calculation_rounding_method ==
                        'round_globally'):
                    price = line.price_unit * (
                        1 - (line.discount or 0.0) / 100.0)
                    taxes = line.tax_ids.compute_all(
                        price, line.currency_id,
                        line.product_uom_qty,
                        product=line.product_id,
                        partner=ddt.partner_shipping_id)
                    amount_tax += sum(
                        t.get('amount', 0.0) for t in taxes.get('taxes', []))
                else:
                    amount_tax += line.price_tax
            ddt.update({
                'amount_untaxed': ddt.currency_id.round(amount_untaxed),
                'amount_tax': ddt.currency_id.round(amount_tax),
                'amount_total': amount_untaxed + amount_tax,
            })

    ddt_type_id = fields.Many2one(
        'stock.ddt.type', string='DdT Type', default=_default_ddt_type)
    ddt_number = fields.Char(string='DdT Number', copy=False)
    partner_shipping_id = fields.Many2one(
        'res.partner', string="Shipping Address")
    carriage_condition_id = fields.Many2one(
        'stock.picking.carriage_condition',
        string='Carriage Condition')
    goods_description_id = fields.Many2one(
        'stock.picking.goods_description',
        string='Description of Goods')
    transportation_reason_id = fields.Many2one(
        'stock.picking.transportation_reason',
        string='Reason for Transportation')
    transportation_method_id = fields.Many2one(
        'stock.picking.transportation_method',
        string='Method of Transportation')
    carrier_id = fields.Many2one(
        'res.partner', string='Carrier')
    parcels = fields.Integer('Parcels', default=_set_parcel_qty)
    display_name = fields.Char(
        string='Name', compute='_compute_clean_display_name')
    volume = fields.Float('Volume')
    invoice_id = fields.Many2one(
        'account.invoice', string='Invoice',
        readonly=True, copy=False)
    invoice_ids = fields.Many2many(
        'account.invoice', string='Invoices',
        readonly=True, copy=False)
    to_be_invoiced = fields.Boolean(
        string='To be Invoiced', store=True,
        compute="_compute_to_be_invoiced",
        help="This depends on 'To be Invoiced' field of the Reason for "
             "Transportation of this DDT")
    show_price = fields.Boolean(string='Show prices on report')
    weight_manual = fields.Float(
        string="Force Net Weight",
        help="Fill this field with the value you want to be used as weight. "
             "Leave empty to let the system to compute it")
    gross_weight = fields.Float(string="Gross Weight")
    check_if_picking_done = fields.Boolean(
        compute='_compute_check_if_picking_done',
    )
    currency_id = fields.Many2one(
        related='company_id.currency_id',
        string='Currency',
        store=True, readonly=True)
    amount_untaxed = fields.Monetary(
        string='Untaxed Amount', store=True, readonly=True,
        compute='_amount_all', track_visibility='always')
    amount_tax = fields.Monetary(
        string='Taxes', store=True, readonly=True,
        compute='_amount_all', track_visibility='always')
    amount_total = fields.Monetary(
        string='Total', store=True, readonly=True,
        compute='_amount_all', track_visibility='always')

    @api.multi
    def button_dummy(self):
        self._amount_all()
        return True

    @api.multi
    @api.depends('picking_ids',
                 'picking_ids.state')
    def _compute_check_if_picking_done(self):
        for record in self:
            record.check_if_picking_done = False
            for package in record.picking_ids:
                if package.state == 'done':
                    record.check_if_picking_done = True

    @api.onchange('partner_id', 'ddt_type_id')
    def on_change_partner(self):
        if self.ddt_type_id:
            addr = self.partner_id.address_get(['delivery', 'invoice'])
            self.partner_shipping_id = addr['delivery']
            self.carriage_condition_id = (
                self.partner_id.carriage_condition_id.id
                if self.partner_id.carriage_condition_id
                else self.ddt_type_id.default_carriage_condition_id)
            self.goods_description_id = (
                self.partner_id.goods_description_id.id
                if self.partner_id.goods_description_id
                else self.ddt_type_id.default_goods_description_id)
            self.transportation_reason_id = (
                self.partner_id.transportation_reason_id.id
                if self.partner_id.transportation_reason_id
                else self.ddt_type_id.default_transportation_reason_id)
            self.transportation_method_id = (
                self.partner_id.transportation_method_id.id
                if self.partner_id.transportation_method_id
                else self.ddt_type_id.default_transportation_method_id)
            self.show_price = self.partner_id.ddt_show_price

    @api.model
    def check_linked_picking(self, picking):
        ddt = self.search([('picking_ids', '=', picking.id)])
        if ddt:
            raise UserError(
                _("Selected Picking is already linked to DDT: %s")
                % ddt.display_name
            )

    @api.model
    def get_delivery_value(self, vals, picking, fieldname, condition_help):
        """Set specific condition of delivey. Inherit condition from
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
        """
        ddt_model = self.env['stock.picking.package.preparation']
        pp_fieldname = ddt_model.fieldname_of_model(
            'stock.picking.package.preparation', fieldname)
        if not pp_fieldname:
            return vals
        sp_fieldname = ''
        so_fieldname = ''
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
            delivery_carrier = False
            if dc_fieldname:
                if (picking.sale_id and picking.sale_id.carrier_id):
                    delivery_carrier = picking.sale_id.carrier_id
                # Warning: carrier_id in DdT has different meaning od the same
                # field in sale.order and picking
                # TODO: change name from carrier_id to ddt_carrier_id
                # elif vals.get('carrier_id'):
                #     delivery_carrier = self.env[
                #         'delivery.carrier'].browse(vals['carrier_id'])
            ddt_type = False
            if dt_fieldname:
                if picking.ddt_type:
                    ddt_type = picking.ddt_type
                elif vals.get('ddt_type_id'):
                    ddt_type = self.env[
                        'stock.ddt.type'].browse(vals['ddt_type_id'])
            if (picking.sale_id and picking.sale_id.partner_id):
                inv_partner_id = picking.sale_id.partner_id
            elif picking.partner_id and picking.partner_id.parent_id:
                inv_partner_id = picking.partner_id.parent_id
            else:
                inv_partner_id = False
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
                    delivery_carrier and
                    delivery_carrier[dc_fieldname]):
                if fieldname.endswith('_id'):
                    vals[pp_fieldname] = delivery_carrier[dc_fieldname].id
                else:
                    vals[pp_fieldname] = delivery_carrier[dc_fieldname]
            # field from stock.ddt.type ?
            elif (dt_fieldname and
                    ddt_type and
                    ddt_type[dt_fieldname]):
                if fieldname.endswith('_id'):
                    vals[pp_fieldname] = ddt_type[dt_fieldname].id
                else:
                    vals[pp_fieldname] = ddt_type[dt_fieldname]
            # field from partner ?
            elif (rp_fieldname and
                  inv_partner_id and
                  inv_partner_id[rp_fieldname]):
                if fieldname.endswith('_id'):
                    vals[pp_fieldname] = inv_partner_id[rp_fieldname].id
                else:
                    vals[pp_fieldname] = inv_partner_id[rp_fieldname]
        elif fieldname != 'note':
            # check on picking, if field is valid
            if sp_fieldname and picking[sp_fieldname]:
                if picking[sp_fieldname].id != vals[pp_fieldname]:
                    raise UserError(
                        _('Selected Pickings have different %s' %
                          condition_help))
            # otherwise check in sale order of picking (if exists)
            elif (picking.sale_id and so_fieldname and
                  picking.sale_id[so_fieldname] and
                  picking.sale_id[so_fieldname].id != vals[pp_fieldname]):
                raise UserError(
                    _('Selected Pickings have different %s' %
                      condition_help))
        return vals

    @api.model
    def sum_delivery_value(self, vals, picking, fieldname):
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

    @api.model
    def preparare_ddt_data(self, picking_ids, partner=None):
        vals = {'partner_id': False}
        for picking in picking_ids:
            # check if picking is already linked to a DDT
            self.check_linked_picking(picking)
            current_ddt_shipping_partner = picking.get_ddt_shipping_partner()
            if not partner:
                partner = current_ddt_shipping_partner
            elif partner != current_ddt_shipping_partner:
                raise UserError(
                    _("Selected Pickings have different Partner"))
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
        if len(picking_ids[0].mapped('location_dest_id')) > 1:
            raise UserError(_("Selected pickings have different destinations"))
        for picking in picking_ids:
            vals = self.get_delivery_value(
                vals, picking, 'ddt_type_id', _('ddt type'))
        if not vals.get('ddt_type_id'):
            ddt_type = self.env['stock.ddt.type'].search([], limit=1)
            if ddt_type:
                vals['ddt_type_id'] = ddt_type[0].id
        for picking in picking_ids:
            for field, field_help in (('ddt_carrier_id', _('carrier')),
                                      ('show_price', _('show price')),
                                      ('note', _('note')),
                                      ('carriage_condition_id',
                                       _('carriage condition')),
                                      ('goods_description_id',
                                       _('goods description')),
                                      ('transportation_reason_id',
                                       _('transportation reason')),
                                      ('transportation_method_id',
                                       _('transportation method'))):
                vals = self.get_delivery_value(
                    vals, picking, field, field_help)
            vals = self.sum_delivery_value(vals, picking, 'parcels')
            vals = self.sum_delivery_value(vals, picking, 'weight')
            vals = self.sum_delivery_value(vals, picking, 'gross_weight')
            vals = self.sum_delivery_value(vals, picking, 'volume')
        if not vals.get('parcels'):
            vals['parcels'] = 1
        vals.update({'picking_ids': [(6, 0, [p.id for p in picking_ids])]})
        return vals

    @api.multi
    def action_put_in_pack(self):
        # ----- Check if exist a stock picking whose state is 'done'
        for record_picking in self.picking_ids:
            if record_picking.state == 'done':
                raise UserError(_(
                    "Impossible to put in pack a picking whose state is 'done'"
                ))
        for package in self:
            # ----- Check if package has details
            if not package.line_ids:
                raise UserError(
                    _("Impossible to put in pack a package without details"))
            # ----- Assign ddt number if ddt type is set
            if package.ddt_type_id and not package.ddt_number:
                package.ddt_number = (
                    package.ddt_type_id.sequence_id.next_by_id())
        return super(StockPickingPackagePreparation, self).action_put_in_pack()

    @api.multi
    def set_draft(self):
        invoiced = bool(self.invoice_id)
        picking_ids = []
        for line in self.line_ids:
            if line.invoice_line_id:
                invoiced = True
                break
            if line.move_id.picking_id not in picking_ids:
                picking_ids.append(line.move_id.picking_id)
        if invoiced:
            raise UserError(
                _("Impossible to set draft document when invoiced!"))
        # for picking in picking_ids:
        #     picking.write({'state': 'draft'})
        self.write({'state': 'draft', 'date_done': False})
        return True

    @api.multi
    def set_done(self):
        for ddt in self:
            for field in ('carriage_condition_id',
                          'goods_description_id',
                          'transportation_reason_id',
                          'transportation_method_id'):
                if not ddt[field]:
                    raise UserError(
                        _('Required value for %s' % field))
            do_put_in_pack = False
            for picking in ddt.picking_ids:
                if picking.state == 'assigned':
                    do_put_in_pack = True
                else:
                    do_put_in_pack = False
            if do_put_in_pack:
                return ddt.action_put_in_pack()
            for picking in ddt.picking_ids:
                if picking.state != 'done':
                    raise UserError(
                        _("Not every picking is in done status"))
            for package in ddt:
                if not package.ddt_number:
                    package.ddt_number = (
                        package.ddt_type_id.sequence_id.next_by_id())
            ddt.write({'state': 'done', 'date_done': fields.Datetime.now()})
        return True

    @api.multi
    @api.depends(
        'name', 'ddt_number', 'partner_id.name', 'date'
    )
    def _compute_clean_display_name(self):
        for prep in self:
            name = u''
            if prep.ddt_number:
                if prep.name:
                    name = u'[%s] %s' % (prep.name, prep.ddt_number)
                else:
                    name = prep.ddt_number
            elif prep.partner_id:
                if prep.name:
                    name = u'%s - %s' % (prep.partner_id.name, prep.name)
                else:
                    name = u'%s' % prep.partner_id.name
            elif prep.name:
                name = prep.name
            else:
                name = u'%d' % prep.id
            prep.display_name = name

    @api.multi
    @api.depends('package_id',
                 'package_id.children_ids',
                 'package_id.quant_ids',
                 'picking_ids',
                 'picking_ids.move_lines',
                 'picking_ids.move_lines.quant_ids',
                 'weight_manual')
    def _compute_weight(self):
        super(StockPickingPackagePreparation, self)._compute_weight()
        for prep in self:
            if prep.weight_manual:
                prep.weight = prep.weight_manual
            elif not prep.package_id:
                quants = self.env['stock.quant']
                for picking in prep.picking_ids:
                    for line in picking.move_lines:
                        for quant in line.quant_ids:
                            if quant.qty >= 0:
                                quants |= quant
                weight = sum(l.product_id.weight * l.qty for l in quants)
                prep.net_weight = weight
                prep.weight = weight

    def _get_sale_order_ref(self):
        """
        It returns the first sale order of the ddt.
        """
        sale_order = False
        # for picking in self.picking_ids:
        #     for sm in picking.move_lines:
        #         if sm.procurement_id and sm.procurement_id.sale_line_id:
        #             sale_order = sm.procurement_id.sale_line_id.order_id
        #             return sale_order
        for line in self.line_ids:
            if line.sale_line_id:
                sale_order = line.sale_line_id.order_id
                break
        return sale_order

    @api.multi
    def _prepare_invoice_description(self):
        invoice_description = ''
        lang = self.env['res.lang']._lang_get(self.env.lang)
        date_format = lang.date_format
        ddt_date_from = self._context.get('ddt_date_from', False)
        ddt_date_to = self._context.get('ddt_date_to', False)
        if ddt_date_from and ddt_date_to:
            invoice_description = '{} {} - {}'.format(
                _('Competenza:'),
                datetime.strptime(
                    ddt_date_from,
                    DEFAULT_SERVER_DATE_FORMAT).strftime(date_format),
                datetime.strptime(
                    ddt_date_to,
                    DEFAULT_SERVER_DATE_FORMAT).strftime(date_format)
            )
        return invoice_description

    @api.multi
    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order.
        This method may be
        overridden to implement custom invoice generation (making sure to call
        super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        order = self._get_sale_order_ref()
        if order:
            # Most of the values will be overwritten below,
            # but this preserves inheritance chain
            invoice_vals = order._prepare_invoice()
        else:
            # Initialise res with the fields in sale._prepare_invoice
            # that won't be overwritten below
            invoice_vals = {
                'type': 'out_invoice',
                'partner_shipping_id':
                    self.partner_id.address_get(['delivery'])['delivery'],
                'company_id': self.company_id.id
            }
        journal_id = self._context.get('invoice_journal_id', False)
        if not journal_id:
            journal_id = self.env['account.invoice'].default_get(
                ['journal_id'])['journal_id']
        if not journal_id:
            raise UserError(
                _('Please define an accounting sale journal for this company.')
            )
        journal = self.env['account.journal'].browse(journal_id)
        invoice_partner_id = (
            order and order.partner_invoice_id.id or
            self.partner_id.address_get(['invoice'])['invoice'])
        invoice_partner = self.env['res.partner'].browse(invoice_partner_id)
        invoice_description = self._prepare_invoice_description()
        currency_id = (
            order and order.pricelist_id.currency_id.id or
            journal.currency_id.id or journal.company_id.currency_id.id)
        payment_term_id = (
            order and order.payment_term_id.id or
            self.partner_id.property_payment_term_id.id)
        fiscal_position_id = (
            order and order.fiscal_position_id.id or
            invoice_partner.property_account_position_id.id)
        invoice_vals.update({
            'name': invoice_description or '',
            'date_invoice': self._context.get('invoice_date', False),
            'origin': self.ddt_number,
            'type': 'out_invoice',
            'account_id': (
                invoice_partner.property_account_receivable_id.id),
            'partner_id': invoice_partner_id,
            'partner_shipping_id': self.partner_id.id,
            'journal_id': journal_id,
            'currency_id': currency_id,
            # TO DO 'comment': self.note,
            'payment_term_id': payment_term_id,
            'fiscal_position_id': fiscal_position_id,
            'carriage_condition_id': self.carriage_condition_id.id,
            'goods_description_id': self.goods_description_id.id,
            'transportation_reason_id': self.transportation_reason_id.id,
            'transportation_method_id': self.transportation_method_id.id,
            'carrier_id': self.carrier_id.id,
            'parcels': self.parcels,
            'weight': self.weight,
            'gross_weight': self.gross_weight,
            'volume': self.volume,
        })
        return invoice_vals

    @api.multi
    def action_invoice_create(self):
        """
        Create the invoice associated to the DDT.
        :returns: list of created invoices
        """
        inv_model = self.env['account.invoice']
        invoices = {}
        references = {}
        seq_offset = 0
        for ddt in self:
            if not ddt.to_be_invoiced or ddt.invoice_id:
                continue
            order = ddt._get_sale_order_ref()
            invoiced_order_lines = []
            orders = []

            if order:
                group_method = (
                    order and order.ddt_invoicing_group or 'shipping_partner')
                group_partner_invoice_id = order.partner_invoice_id.id
                group_currency_id = order.currency_id.id
            else:
                if ddt.partner_shipping_id:
                    group_method = (
                        ddt.partner_shipping_id.commercial_partner_id.
                        ddt_invoicing_group)
                else:
                    group_method = (
                        ddt.partner_id.commercial_partner_id.
                        ddt_invoicing_group)
                group_partner_invoice_id = ddt.partner_id.id
                group_currency_id = ddt.partner_id.currency_id.id
            if group_method == 'billing_partner':
                group_key = (group_partner_invoice_id,
                             group_currency_id)
            elif group_method == 'shipping_partner':
                group_key = (ddt.partner_shipping_id.id,
                             ddt.company_id.currency_id.id)
            elif group_method == 'code_group':
                group_key = (ddt.partner_shipping_id.ddt_code_group,
                             group_partner_invoice_id)
            else:
                group_key = ddt.id

            ddt_invoiced = True
            prior_group_key = order
            max_ddt_seq = 0
            invoice = False
            for line in ddt.line_ids:
                if not line.allow_invoice_line():
                    ddt_invoiced = False
                    continue

                if group_method == 'sale_order':
                    if line.sale_line_id:
                        group_key = line.sale_line_id.order_id
                        prior_group_key = group_key
                    else:
                        group_key = prior_group_key
                if line.sale_line_id:
                    if line.sale_line_id.order_id not in orders:
                        orders.append(line.sale_line_id.order_id)
                    if line.sale_line_id not in invoiced_order_lines:
                        invoiced_order_lines.append(line.sale_line_id)

                if group_key not in invoices:
                    inv_data = ddt._prepare_invoice()
                    invoice = inv_model.create(inv_data)
                    references[invoice] = ddt
                    invoices[group_key] = invoice
                    ddt.invoice_ids = [(4, invoice.id)]
                    # ddt.invoice_id = invoice.id
                elif group_key in invoices:
                    vals = {}
                    origin = invoices[group_key].origin
                    if (origin and ddt.ddt_number and
                            ddt.ddt_number not in origin.split(', ')):
                        vals['origin'] = invoices[
                            group_key].origin + ', ' + ddt.ddt_number
                    invoices[group_key].write(vals)
                    ddt.invoice_id = invoices[group_key].id
                    invoice = invoices[group_key]

                line.invoice_line_create(
                    invoices[group_key].id, line.product_uom_qty,
                    offset=seq_offset)
                max_ddt_seq = max(max_ddt_seq, line.sequence)

            seq_offset += max_ddt_seq
            if ddt_invoiced and invoice:
                ddt.invoice_id = invoice.id
            if references.get(invoices.get(group_key)):
                if ddt not in references[invoices[group_key]]:
                    references[invoice] = references[invoice] | ddt

            # Get order lines to invoice because not in ddt
            for order in orders:
                for line in order.order_line:
                    if (line not in invoiced_order_lines and
                            (not line.product_id or
                             line.product_id.invoice_policy == 'order')):
                        line.invoice_line_create(invoices[group_key].id,
                                                 line.qty_to_invoice)
            # Allow additional operations from ddt
            # ddt.other_operations_on_ddt(invoice)

        if not invoices:
            raise UserError(_('There is no invoicable line.'))

        for invoice in invoices.values():
            if not invoice.name:
                invoice.write({
                    'name': invoice.origin
                })
            if not invoice.invoice_line_ids:
                raise UserError(_('There is no invoicable line.'))
            # If invoice is negative, do a refund invoice instead
            if invoice.amount_untaxed < 0:
                invoice.type = 'out_refund'
                for line in invoice.invoice_line_ids:
                    line.quantity = -line.quantity
            # Use additional field helper function (for account extensions)
            for line in invoice.invoice_line_ids:
                line._set_additional_fields(invoice)
            # Necessary to force computation of taxes. In account_invoice,
            # they are triggered
            # by onchanges, which are not triggered when doing a create.
            invoice.compute_taxes()
            invoice.message_post_with_view(
                'mail.message_origin_link',
                values={
                    'self': invoice, 'origin': references[invoice]},
                subtype_id=self.env.ref('mail.mt_note').id)
        return [inv.id for inv in invoices.values()]

    @api.multi
    def action_send_ddt_mail(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.\
                get_object_reference('l10n_it_ddt',
                                     'email_template_edi_ddt')[1]
        except ValueError:
            template_id = False

        try:
            compose_form_id = ir_model_data.\
                get_object_reference('mail',
                                     'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False

        ctx = {
            'default_model': 'stock.picking.package.preparation',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'mark_so_as_sent': True,
            'custom_layout':
                "l10n_it_ddt.mail_template_data_notification_email_ddt"
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

    @api.multi
    def unlink(self):
        for ddt in self:
            if ddt.invoice_id:
                raise UserError(
                    _("Document %s has invoice linked" % ddt.ddt_number))
            if ddt.state != 'cancel':
                raise UserError(
                    _('You can not delete document %s! '
                      'Try to cancel it before.' % ddt.ddt_number))
            # Decrement ddt number if last DdT
            if ddt.ddt_number:
                ddt.ddt_type_id.sequence_id.unnext_by_id(ddt.ddt_number)
        return super(StockPickingPackagePreparation, self).unlink()


class StockPickingPackagePreparationLine(models.Model):
    _inherit = 'stock.picking.package.preparation.line'
    _order = 'partner_id, package_preparation_id, sequence, id'

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_ids')
    def _compute_amount(self):
        """
        Compute the amounts of the line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_ids.compute_all(
                price, line.currency_id,
                line.product_uom_qty,
                product=line.product_id,
                partner=line.sale_id.partner_shipping_id)
            # line.price_subtotal = taxes['total_excluded']
            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })

    sale_id = fields.Many2one(
        related='move_id.procurement_id.sale_line_id.order_id',
        string='Sale order',
        store=True, readonly=True)
    sale_line_id = fields.Many2one(
        related='move_id.procurement_id.sale_line_id',
        string='Sale order line',
        store=True, readonly=True)
    price_unit = fields.Float('Unit Price', digits=dp.get_precision(
        'Product Price'), default=0.0)
    tax_ids = fields.Many2many('account.tax', string='Taxes')
    discount = fields.Float(
        string='Discount (%)', digits=dp.get_precision('Discount'),
        default=0.0)
    ddt_id = fields.Many2one(
        'stock.picking.package.preparation',
        string='Deprecated')
    ddt_number = fields.Char(
        related='package_preparation_id.ddt_number',
        string='Ddt number',
        store=True, readonly=True)
    currency_id = fields.Many2one(
        related='move_id.procurement_id.sale_line_id.order_id.currency_id',
        string='Currency',
        store=True, readonly=True)
    price_subtotal = fields.Monetary(compute='_compute_amount',
                                     string='Subtotal',
                                     readonly=True, store=True)
    price_tax = fields.Monetary(compute='_compute_amount',
                                string='Taxes', readonly=True, store=True)
    price_total = fields.Monetary(compute='_compute_amount',
                                  string='Total', readonly=True, store=True)
    weight = fields.Float(
        string="Line Weight")
    invoice_line_id = fields.Many2one(
        'account.invoice.line', string='Invoice line',
        readonly=True, copy=False)
    invoice_number = fields.Char(
        related='invoice_line_id.invoice_id.number',
        string='Invoice',
        readonly=True, copy=False)
    partner_id = fields.Many2one(
        'res.partner', string='Partner',
        related='package_preparation_id.partner_id',
        store=True, readonly=True, related_sudo=False)
    date = fields.Datetime(
        related='package_preparation_id.date',
        string='Date',
        store=True, readonly=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        super(StockPickingPackagePreparationLine, self)._onchange_product_id()
        if self.product_id:
            order = self.package_preparation_id._get_sale_order_ref()
            partner = order and order.partner_id \
                or self.package_preparation_id.partner_id
            product = self.product_id.with_context(
                lang=self.package_preparation_id.partner_id.lang,
                partner=partner.id,
                quantity=self.product_uom_qty,
                date=self.package_preparation_id.date,
                pricelist=order and order.pricelist_id.id or False,
                uom=self.product_uom_id.id
            )
            # Tax
            taxes = product.taxes_id
            fpos = order and order.fiscal_position_id or \
                self.package_preparation_id.partner_id.\
                property_account_position_id
            self.tax_ids = fpos.map_tax(
                taxes, product, partner) if fpos else taxes
            # Price and discount
            self.price_unit = product.price
            if order:
                context_partner = dict(
                    self.env.context, partner_id=partner.id)
                pricelist_context = dict(
                    context_partner, uom=self.product_uom_id.id,
                    date=order.date_order)
                price, rule_id = order.pricelist_id.with_context(
                    pricelist_context).get_product_price_rule(
                    product, self.product_uom_qty or 1.0, partner)
                new_list_price, currency_id = self.env['sale.order.line']\
                    .with_context(context_partner)._get_real_price_currency(
                    self.product_id, rule_id, self.product_uom_qty,
                    self.product_uom_id, order.pricelist_id.id)
                datas = self._prepare_price_discount(new_list_price, rule_id)
                for key in datas.keys():
                    setattr(self, key, datas[key])

    @api.model
    def _prepare_price_discount(self, price, rule_id):
        """
        Use this method for other fields added in the line.
        Use key of dict to specify the field that will be updated
        """
        res = {
            'price_unit': price
        }
        # Discount
        if rule_id:
            rule = self.env['product.pricelist.item'].browse(rule_id)
            if rule.pricelist_id.discount_policy == \
                    'without_discount':
                res['discount'] = rule.price_discount
        return res

    @api.model
    def _prepare_lines_from_pickings(self, picking_ids):
        """
        Add values used for invoice creation
        """
        lines = super(StockPickingPackagePreparationLine,
                      self)._prepare_lines_from_pickings(picking_ids)
        for line in lines:
            sale_line = False
            if line['move_id']:
                move = self.env['stock.move'].browse(line['move_id'])
                line['weight'] = move.weight
                sale_line = move.procurement_id.sale_line_id or False
            if sale_line:
                line['price_unit'] = sale_line.price_unit or 0
                line['discount'] = sale_line.discount or 0
                line['tax_ids'] = [(6, 0, [x.id]) for x in sale_line.tax_id]
        return lines

    @api.multi
    def _prepare_invoice_line(self, qty, invoice_id=None, offset=None):
        """
        Prepare the dict of values to create the new invoice line for a
        ddt line.

        :param qty: float quantity to invoice
        :param invoice_id: possible existing invoice
        """
        self.ensure_one()
        offset = offset or 0.0
        res = {}
        if (
            self.sale_line_id.product_id.property_account_income_id or
            self.sale_line_id.product_id.categ_id.
            property_account_income_categ_id
        ):
            # Without property_account_income_id or
            # property_account_income_categ_id
            # _prepare_invoice_line would fail
            res = self.sale_line_id._prepare_invoice_line(qty)
        else:
            account = (
                self.product_id.property_account_income_id or
                self.product_id.categ_id.property_account_income_categ_id)
            if not account:
                if invoice_id:
                    invoice = self.env['account.invoice'].browse(invoice_id)
                    account = invoice.journal_id.default_credit_account_id
            if not account:
                raise UserError(
                    _(
                        'Please define income account for this product: "%s" '
                        '(id:%d) - or for its category: "%s".'
                    ) % (
                        self.product_id.name, self.product_id.id,
                        self.product_id.categ_id.name
                    )
                )
            fpos = None
            if self.sale_line_id:
                fpos = (
                    self.sale_line_id.order_id.fiscal_position_id or
                    self.sale_line_id.order_id.partner_id.
                    property_account_position_id
                )
            if fpos:
                account = fpos.map_account(account)
            res['account_id'] = account.id

            if self.sale_line_id.order_id.project_id:
                res[
                    'account_analytic_id'
                ] = self.sale_line_id.order_id.project_id.id
            if self.sale_line_id.analytic_tag_ids:
                res['analytic_tag_ids'] = [
                    (6, 0, self.sale_line_id.analytic_tag_ids.ids)
                ]

        res.update({
            'ddt_line_id': self.id,
            'name': self.name,
            'sequence': self.sequence + offset,
            'origin': self.package_preparation_id.name or '',
            'price_unit': self.price_unit,
            'quantity': qty,
            'discount': self.discount,
            'uom_id': self.product_uom_id.id,
            'product_id': self.product_id.id or False,
            'invoice_line_tax_ids': [(6, 0, self.tax_ids.ids)],
            'weight': self.weight,
        })
        return res

    @api.multi
    def invoice_line_create(self, invoice_id, qty, offset=None):
        """
        :param invoice_id: integer
        :param qty: float quantity to invoice
        """
        precision = self.env['decimal.precision'].precision_get(
            'Product Unit of Measure')
        offset = offset or 0
        for line in self:
            # vals = line._prepare_invoice_line(
            #     qty=qty, invoice_id=invoice_id, offset=offset)
            vals = line._prepare_invoice_line(
                qty=qty, invoice_id=invoice_id)
            vals.update({'invoice_id': invoice_id})
            if line.sale_line_id:
                vals.update(
                    {'sale_line_ids': [
                        (6, 0, [line.sale_line_id.id])
                    ]})
            line_inv = self.env['account.invoice.line'].with_context(
                skip_update_line_ids=True).create(vals)
            line.invoice_line_id = line_inv.id

    def quantity_by_lot(self):
        res = {}
        for quant in self.move_id.quant_ids:
            if quant.lot_id:
                if quant.location_id.id == self.move_id.location_dest_id.id:
                    if quant.lot_id not in res:
                        res[quant.lot_id] = quant.qty
                    else:
                        res[quant.lot_id] += quant.qty
        for lot in res:
            if lot.product_id.tracking == 'lot':
                res[lot] = formatLang(self.env, res[lot])
            else:
                # If not tracking by lots, quantity is not relevant
                res[lot] = False
        return res

    @api.multi
    def allow_invoice_line(self):
        """This method allows or not the invoicing of a specific DDT line.
        It can be inherited for different purposes, e.g. for proper invoicing
        of kit."""
        self.ensure_one()
        # return self.product_uom_qty > 0
        return not self.invoice_line_id

    @api.multi
    def action_line_invoice_create(self):
        """
        Create the invoice selected by end-user.
        :returns: list of created invoices
        """
        inv_model = self.env['account.invoice']
        # ddt_model = self.env['stock.picking.package.preparation']
        invoice = False

        ddt_line_list = []
        ddt_list = []
        partner_id = False
        reference = False
        for line in self:
            if not line.allow_invoice_line():
                continue
            if not partner_id:
                partner_id = line.package_preparation_id.partner_id
            if line.package_preparation_id.partner_id != partner_id:
                raise UserError(_('Too many partners.'))
            if not invoice:
                inv_data = line.package_preparation_id._prepare_invoice()
                invoice = inv_model.create(inv_data)
            line.invoice_line_create(
                invoice.id, line.product_uom_qty)
            if line.package_preparation_id not in ddt_list:
                ddt_list.append(line.package_preparation_id)
            ddt_line_list.append(line.id)

        for ddt in ddt_list:
            ddt_invoiced = True
            reference = ddt
            for line in ddt.line_ids:
                if line.id not in ddt_line_list and not line.invoice_line_id:
                    ddt_invoiced = False
                    break
            if ddt_invoiced:
                ddt.invoice_id = invoice.id

        if not invoice:
            raise UserError(_('There is no invoicable line.'))

        if not invoice.name:
            invoice.write({
                'name': invoice.origin
            })
        if not invoice.invoice_line_ids:
            raise UserError(_('There is no invoicable line.'))
        # If invoice is negative, do a refund invoice instead
        if invoice.amount_untaxed < 0:
            invoice.type = 'out_refund'
            for line in invoice.invoice_line_ids:
                line.quantity = -line.quantity
        # Use additional field helper function (for account extensions)
        for line in invoice.invoice_line_ids:
            line._set_additional_fields(invoice)
        # Necessary to force computation of taxes. In account_invoice,
        # they are triggered
        # by onchanges, which are not triggered when doing a create.
        invoice.compute_taxes()
        invoice.message_post_with_view(
            'mail.message_origin_link',
            values={'self': invoice, 'origin': reference},
            subtype_id=self.env.ref('mail.mt_note').id)
        return [invoice.id]
