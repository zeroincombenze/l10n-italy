from odoo import api, SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)


def rm_old_account(cr):
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
        action_done = False
        for tmpl in tmpl_model.search([()]):
            if len(tmpl.code) < 6:
                tmpl.unlink()
                action_done = True
        if action_done:
            _logger.info("Migration remove_old_account terminated.")


def migrate(cr, version):
    if not version:
        return
    rm_old_account(cr)
