# -*- coding: utf-8 -*-
#
# Copyright 2018-24 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    if not version:
        return
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        tax_model = env["account.tax"]
        for tax in tax_model.search([]):
            tax._onchange_nature()

        fiscalposition = env["account.fiscal.position"]
        transient_account_id = False
        for fpos in fiscalposition.search([]):
            if fpos.rc_type_id:
                vals = {
                    "rc_type": "self",
                    "partner_type": fpos.rc_type_id.partner_type,
                    "self_journal_id": fpos.rc_type_id.self_journal_id.id,
                    "payment_journal_id": fpos.rc_type_id.payment_journal_id.id,
                    "transient_account_id": fpos.rc_type_id.transient_account_id.id,
                }
                fpos.write(vals)
                if not transient_account_id and fpos.rc_type_id.transient_account_id:
                    transient_account_id = fpos.rc_type_id.transient_account_id
                # Warning: following field are declared l10n_it_ade which is
                # a depending on module. Here because fiscal position
                for taxes in fpos.rc_type_id.tax_ids:
                    taxes.purchase_tax_id.rc_sale_tax_id = taxes.sale_tax_id.id
        if transient_account_id:
            for fpos in fiscalposition.search([("rc_type_id", "!=", False),
                                               ("transient_account_id", "=", False)]):
                fpos.transient_account_id = transient_account_id.id
