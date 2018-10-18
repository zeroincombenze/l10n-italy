#
# Copyright 2014    Davide Corio <davide.corio@abstract.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    fatturapa_fiscal_position_id = fields.Many2one(
        'fatturapa.fiscal_position', 'Fiscal Position',
        help="Fiscal position used by FatturaPA",
    )
    fatturapa_sequence_id = fields.Many2one(
        'ir.sequence', 'Sequence',
        help="il progressivo univoco del file è rappresentato da una "
             "stringa alfanumerica di lunghezza massima di 5 caratteri "
             "e con valori ammessi da “A” a “Z” e da “0” a “9”.",
    )
    fatturapa_art73 = fields.Boolean('Art73')
    fatturapa_pub_administration_ref = fields.Char(
        'Public Administration Reference Code', size=20,
    )
    fatturapa_rea_office = fields.Many2one(
        related="partner_id.rea_office", string='REA office')
    fatturapa_rea_number = fields.Char(
        related="partner_id.rea_code", string='Rea Number')
    fatturapa_rea_capital = fields.Float(
        related='partner_id.rea_capital',
        string='Rea Capital')
    fatturapa_rea_partner = fields.Selection(
        related='partner_id.rea_member_type',
        string='Member Type')
    fatturapa_rea_liquidation = fields.Selection(
        related='partner_id.rea_liquidation_state',
        string='Liquidation State')
    fatturapa_tax_representative = fields.Many2one(
        'res.partner', 'Legal Tax Representative'
    )
    fatturapa_sender_partner = fields.Many2one(
        'res.partner', 'Third Party/Sender'
    )
