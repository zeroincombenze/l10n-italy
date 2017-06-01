from openerp.osv import fields


class account_account(orm.Model):
    _inherit = "account.account"
    _columns = {
        'parent_consol_ids': fields.many2many('account.account', 'account_account_consol_rel', 'parent_id', 'child_id', 'Consolidated Parents'),
    }


account_account()
