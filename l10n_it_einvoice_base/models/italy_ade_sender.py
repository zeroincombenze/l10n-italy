# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp.osv import fields, orm

class ItalyEinvoiceSender(orm.Model):
    _name = 'italy.ade.sender'
    _description = "E-Invoice Sender Channel"

    _columns = {
        'name': fields.char(
            'Sender Channel Name',
            required=True,
            help="Give a unique name for Sender Channel"),
        'method': fields.selection(
            [('NO', 'Nessun Invio'),
             ('PEC', 'Tramite PEC'),
             ('FTP', 'Tramite FTP'),
             ('JSON', 'Tramite JSON'),
            ],
            'SDI channel',
            help="Sending Method"),
        'company_id': fields.many2one(
            'res.company', 'Company',
            help="Set company, if specific company channel",
            ),
        'client_id': fields.char(
            'Client ID',
            help="Client ID assigned by 3th Party Sender"),
        'client_key': fields.char(
            'Client key',
            help="Client key assigned by 3th Party Sender"),
        'sender_url': fields.char(
            'Sender url',
            help="3th Party Sender URL to connect"),
        'sender_company_id': fields.char(
            'Company ID',
            help="Company Identification assigned by 3th Party Sender"),
        'hub_ip_addr': fields.char(
            'Hub IP Address',
            help="IP Address to connect"),
        'email_from_for_fatturaPA': fields.char(
            string='Sender Email Address',
            help="PEC of sender"),
        'email_exchange_system': fields.char(
            string='Exchange System Email Address',
            help="E-mail to use when method is PEC"),
        'pec_server_id': fields.many2one(
            'ir.mail_server', string='Pec mail server',
            required=False,
            domain=[('is_fatturapa_pec', '=', True),]),
        'active': fields.boolean(string='Active',
                                default=True),
        }
