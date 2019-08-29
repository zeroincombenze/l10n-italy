# -*- coding: utf-8 -*-

from openerp import api, SUPERUSER_ID


def migrate(cr, version):
    """Set default values"""
    if not version:
        return
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        mr_t_odoo = env.ref('base_multireport.mr_t_odoo').id
        mr_style_model = env['multireport.style']
        vals = {
            'template_sale_order': mr_t_odoo,
            'template_stock_picking_package_preparation': mr_t_odoo,
            'template_account_invoice': mr_t_odoo,
            'template_purchase_order': mr_t_odoo,
        }
        where = [('origin', '!=', 'odoo')]
        for mr_style in mr_style_model.search(where):
            mr_style.write(vals)

        ir_report_model = env['ir.actions.report.xml']
        vals = {'template': mr_t_odoo,}
        where = [('model', 'in', ('sale.order',
                                  'stock.picking.package.preparation',
                                  'account.invoice',
                                  'purchase.order'))]
        for ir_report in ir_report_model.search(where):
            ir_report.write(vals)

        vals = {}
        ir_view_model = env['ir.ui.view']
        where = [('key', '=', 'base_multireport.external_layout_header')]
        ids = ir_view_model.search(where)
        if len(ids) == 1:
            vals['header_id'] = ids[0].id
        where = [('key', '=', 'base_multireport.external_layout_footer')]
        ids = ir_view_model.search(where)
        if len(ids) == 1:
            vals['footer_id'] = ids[0].id
        if vals:
            mr_template_model = env['multireport.template']
            for mr_template in mr_template_model.search([]):
                mr_template.write(vals)

        mr_style_odoo = env.ref('base_multireport.mr_style_odoo').id
        company_model = env['res.company']
        vals = {'report_model_style': mr_style_odoo}
        for company in company_model.search([]):
            try:
                company.write(vals)
            except IOError:
                pass
