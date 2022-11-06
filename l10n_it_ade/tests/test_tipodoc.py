# -*- coding: utf-8 -*-
#
# Copyright 2018-22 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#

from z0bug_odoo import test_common

TIPODOC_CODE = u"TD99"
TIPODOC_NAME = u"Please, do not use this record!"
TIPODOC_NAME2 = u"Please, delete this record!"


class TestTipoDoc(test_common.SingleTransactionCase):
    def setUp(self):
        super(TestTipoDoc, self).setUp()

    def test_invoice_type(self):
        model_name = "italy.ade.invoice.type"
        self.tipo_fattura_id = self.create_id(
            model_name, {"code": TIPODOC_CODE, "name": TIPODOC_NAME}
        )
        rec = self.browse_rec(model_name, self.tipo_fattura_id)
        self.assertEqual(rec.name, TIPODOC_NAME)
        names = rec.name_get()
        self.assertEqual(names[0][1], '[%s] %s' % (TIPODOC_CODE, TIPODOC_NAME))
        self.write_rec(model_name, self.tipo_fattura_id, {"name": TIPODOC_NAME2})
        rec = self.browse_rec(model_name, self.tipo_fattura_id)
        self.assertEqual(rec.name, TIPODOC_NAME2)
