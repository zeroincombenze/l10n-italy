# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)


def remove_old_account(cr):
    """Remove account with code len < 6; these records were old parent records
    in old Odoo version. From now, account.group are used.
    Args:
        cr (obj): sql cursor

    Returns:
        None
    """
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        tmpl_model = env['account.account.template']
        for tmpl in tmpl_model.search([()]):
            if len(tmpl.code) < 6:
                tmpl.unlink()
        _logger.info("Migration remove_old_account terminated.")


def remove_old_account_post(cr, registry):
    remove_old_account(cr)
