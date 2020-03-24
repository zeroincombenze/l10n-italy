# -*- coding: utf-8 -*-
#
# Copyright 2016-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp import api, SUPERUSER_ID


def update_template_ref(cr, registry):
    """Set default values"""
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        mr_style_model = env['multireport.style']
        vals = {
            'template_sale_order':
                env.ref('base_multireport.mr_t_saleorder').id,
            'template_stock_picking_package_preparation':
                env.ref('base_multireport.mr_t_deliverydocument').id,
            'template_account_invoice':
                env.ref('base_multireport.mr_t_invoice').id,
            'template_purchase_order':
                env.ref('base_multireport.mr_t_purchaseorder').id,
        }
        domain = [('origin', '!=', 'odoo')]
        for mr_style in mr_style_model.search(domain):
            mr_style.write(vals)

        ir_report_model = env['ir.actions.report.xml']
        vals = {'template': False,}
        domain = [('model', 'in', ('sale.order',
                                   'stock.picking.package.preparation',
                                   'account.invoice',
                                   'purchase.order'))]
        for ir_report in ir_report_model.search(domain):
            ir_report.write(vals)

        vals = {}
        ir_view_model = env['ir.ui.view']
        domain = [('key', '=', 'base_multireport.external_layout_header')]
        ids = ir_view_model.search(domain)
        if len(ids) == 1:
            vals['header_id'] = ids[0].id
        domain = [('key', '=', 'base_multireport.external_layout_footer')]
        ids = ir_view_model.search(domain)
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
