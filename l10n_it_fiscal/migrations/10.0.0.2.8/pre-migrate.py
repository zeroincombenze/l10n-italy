from odoo import api, SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)

THIS_MODULE = 'l10n_it_fiscal'


def update_rc_tax_codes(cr):
    """Tax codes for reverse charge are changed from a17v to aa17v.
    This changes wad made to avoid conflict with sale codes.
    Args:
        cr (obj): sql cursor

    Returns:
        None
    """
    def update_tax_records(tax_model):
        chart_template_id = env.ref(
            'l10n_it_fiscal.l10n_chart_it_zeroincombenze')
        action_done = False
        domain = [('chart_template_id', '=', chart_template_id.id)] if hasattr(
            tax_model, 'chart_template_id') else []
        domain.append(('type_tax_use', '=', 'sale'))
        domain.append('|')
        domain.append('|')
        domain.append(('description', '=like', 'a17%'))
        domain.append(('description', '=like', 'a38%'))
        domain.append(('description', '=like', 'a41%'))
        for tax in tax_model.search(domain):
            if (tax.description == 'a17v' or
                    tax_model.search(
                        [('description', '=', 'a%s' % tax.description)])):
                continue
            tax.description = 'a%s' % tax.description
            action_done = True
        if action_done:
            _logger.info("Migration update_tax_records terminated.")

    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        update_tax_records(env['account.tax.template'])
        update_tax_records(env['account.tax'])


def update_ext_ref(cr):
    """Update external reference of above tax codes
    """
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        ir_model_data = env['ir.model.data']
        action_done = False
        for ref in ir_model_data.search(
                [('module', '=', THIS_MODULE),
                 ('model', '=like', 'account.tax%'),
                 '|', '|',
                 ('name', '=like', 'a17%'),
                 ('name', '=like', 'a38%'),
                 ('name', '=like', 'a41%')]):
            tax = env[ref.model].browse(ref.res_id)
            if ref.name != tax.description:
                ref.name = tax.description
            action_done = True
        if action_done:
            _logger.info("Migration update_ext_ref terminated.")


def purge_tax_code(cr):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        ir_model_data = env['ir.model.data']
        tax_model = env['account.tax.template']
        chart_template_id = env.ref(
            'l10n_it_fiscal.l10n_chart_it_zeroincombenze')
        action_done = False
        domain = [('chart_template_id', '=', chart_template_id.id)]
        domain.append('|')
        domain.append(('description', '=like', 'EU-%'))
        domain.append(('description', '=like', '22v%INC'))
        for tax in tax_model.search(domain):
            code = tax.description
            tax.unlink()
            action_done = True
            ref = ir_model_data.search(
                [('module', '=', THIS_MODULE),
                 ('model', '=', 'account.tax.template'),
                 ('name', '=', code)]
            )
            ref.unlink()
            action_done = True
        if action_done:
            _logger.info("Migration purge_tax_code terminated.")


def migrate(cr, version):
    if not version:
        return
    update_rc_tax_codes(cr)
    update_ext_ref(cr)
    purge_tax_code(cr)
