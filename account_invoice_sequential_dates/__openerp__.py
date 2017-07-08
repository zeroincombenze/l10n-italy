# -*- coding: utf-8 -*-
#    Copyright (C) 2010-17 Associazione Odoo Italia
#                          <http://www.odoo-italia.org>
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2010: odoo-italia] First version
# [2017: SHS-AV, odoo-italia] Totally rewritten
#
{
    'name': 'Check invoice date consistency',
    'version': '7.0.0.1.1',
    'category': 'Tools',
    'description': """This module customizes Odoo in order to make invoices
with consistent dates.

Functionalities:

- Check invoice date sequence

""",
    'author': "Zeroincombenze®, "
              "Odoo Italian Community, Odoo Community Association (OCA)",
    'website': 'http://www.odoo-italia.org',
    'license': 'AGPL-3',
    "depends": ['account', 'account_invoice_entry_date'],
    "data": [],
    "demo_xml": [],
    "active": False,
    "installable": True
}
