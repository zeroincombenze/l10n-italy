# -*- coding: utf-8 -*-

from openerp.osv import orm, fields
from openerp.tools.translate import _


class CausalePagamento(orm.Model):
    _name = 'causale.pagamento'
    _description = 'Causale Pagamento'

    # def _check_code(self):
    #     for causale in self:
    #         domain = [('code', '=', causale.code)]
    #         elements = self.search(domain)
    #         if len(elements) > 1:
    #             raise ValidationError(
    #                 _("The element with code %s already exists")
    #                 % causale.code)

    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['code', 'name'], context=context)
        res = []
        for record in reads:
            name = "%s - %s" % (record['code'], record['name'])
            if len(name) > 50:
                name = name[:50] + '...'
            res.append((record['id'], name))
        return res

    _columns = {
        'code': fields.char(string='Code', size=2, required=True),
        'name': fields.text(string='Description', required=True)
    }
