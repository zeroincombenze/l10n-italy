# -*- coding: utf-8 -*-
#
# Copyright 2018-22 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#

from z0bug_odoo import test_common

NATURA_CODE = "N9.9"
NATURA_NAME = "Please, do not use this record!"
NATURA_NAME2 = "Please, delete this record!"


class TestNatura(test_common.SingleTransactionCase):
    def setUp(self):
        super(TestNatura, self).setUp()

    def test_natura(self):
        model_name = "italy.ade.tax.nature"
        self.natura_id = self.create_id(
            model_name, {"code": NATURA_CODE, "name": NATURA_NAME}
        )
        rec = self.browse_rec(model_name, self.natura_id)
        self.assertEqual(rec.name, NATURA_NAME)
        self.write_rec(model_name, self.natura_id, {"name": NATURA_NAME2})
        rec = self.browse_rec(model_name, self.natura_id)
        self.assertEqual(rec.name, NATURA_NAME2)
        names = rec.name_get()
        self.assertEqual(names[0], '[%s] %s' % (NATURA_CODE, NATURA_NAME2))
