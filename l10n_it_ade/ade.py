# -*- coding: utf-8 -*-
# Copyright 2017 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                  Associazione Odoo Italia <http://www.odoo-italia.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
"""Many modules use AdE (Agenzia delle Entrate, which is Italian TAX authority)
In order to avoid duplicate definitions and bad coding, most of these
defitions are in this file.

Programs use these constants have to add follow line:
from l10n_it_ade.ade import ADE_LEGALS

There is a class for general purpose named 'res.italy.ade'
"""
from openerp.osv import orm, fields


ADE_LEGALS = {
    'codice_carica': [
        # ('0', 'Azienda PF (Ditta indivisuale/Professionista/eccetera)'),
        ('1', 'Legale rappresentante, socio amministratore'),
        ('2', 'Rappresentante di minore,interdetto,eccetera'),
        ('3', 'Curatore fallimentare'),
        ('4', 'Commissario liquidatore'),
        ('5', 'Custode giudiziario'),
        ('6', 'Rappresentante fiscale di soggetto non residente'),
        ('7', 'Erede'),
        ('8', 'Liquidatore'),
        ('9', 'Obbligato di soggetto estinto'),
        ('10', 'Rappresentante fiscale art. 44c3 DLgs 331/93'),
        ('11', 'Tutore di minore'),
        ('12', 'Liquidatore di DI'),
        ('13', 'Amministratore di condominio'),
        ('14', 'Pubblica Amministrazione'),
        ('15', 'Commissario PA')],
    'ade_natura': [
        ('', 'Imponibili'),
        ('N1', 'Escluse ex art. 15'),
        ('N2', 'Non soggette'),
        ('N3', 'Non imponibili'),
        ('N4', 'Esenti'),
        ('N5', 'Regime del margine / IVA non esposta in fattura'),
        ('N6', 'Reverse charge/autofatturazione'),
        ('N7', 'IVA assolta in altro stato UE'),
        ('FC', 'Fuori campo IVA')],
}


def reduce_selection(main_selection, exclusion_list):
    reduced_list = []
    for i, item in enumerate(main_selection):
        if main_selection[i][0] not in exclusion_list:
            reduced_list.append(item)
    return reduced_list


class AdECodiceCarica(orm.Model):
    _name = 'italy.ade.codice.carica'
    _description = 'Codice Carica'

    _columns = {
        'code': fields.char(string='Code', size=2,
                            help='Code assigned by Tax Authority'),
        'name': fields.char(string='Name'),
        'help': fields.char(string='Help'),
        'scope': fields.char(string='Scope',
                             help='Reserved to specific scope'),
        'active': fields.boolean(string='Active')
    }
    _default = {
        'active': True
    }
