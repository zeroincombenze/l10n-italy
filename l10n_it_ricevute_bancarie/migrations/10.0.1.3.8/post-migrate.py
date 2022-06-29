# -*- coding: utf-8 -*-

from odoo import SUPERUSER_ID, api


def update_riba_flag(cr):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        lines = env["account.move.line"].search(
            [("invoice_id.type", "=", "out_invoice"),
             ("invoice_id.payment_term_id.riba", "=", True),
             ("account_id.internal_type", "=", "receivable"),
             ]
        )
        for line in lines:
            line.riba = True


def migrate(cr, version):
    if not version:
        return
    update_riba_flag(cr)
