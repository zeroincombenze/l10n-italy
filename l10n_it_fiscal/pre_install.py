# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)


def update_rc_tax_codes(cr):
    """Tax codes for reverse charge are changed from a17v to aa17v.
    This changes wad made to avoid conflict with sale codes.
    Args:
        cr (obj): sql cursor

    Returns:
        None
    """
    def update_tax_records(tax_model):
        for tax in tax_model.search([()]):
            if (tax.type_tax_use == 'sale' and
                    (tax.description.startswith('a17')) or
                    (tax.description.startswith('a38')) or
                    (tax.description.startswith('a41'))):
                if tax_model.search(
                        [('description', '=', 'a%s' % tax.description)]):
                    continue
                tax.description = 'a%s' % tax.description

    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        update_tax_records(env['account.tax.template'])
        update_tax_records(env['account.tax'])


def update_rc_tax_codes_post(cr, registry):

    update_rc_tax_codes(cr)
