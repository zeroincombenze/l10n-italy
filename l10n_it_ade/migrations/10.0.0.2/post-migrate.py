# -*- coding: utf-8 -*-
#
# Copyright 2016-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import re
from odoo import api, SUPERUSER_ID

NATURE = {
    'N010100': ('[Ee]scl', '15', None, None, None, None, None, None),
    'N020100': ('(FC|F.C|[Ff]uori [Cc]ampo)', '1',
                None, None, None, None, None, None),
    'N020101': ('(FC|F.C|[Ff]uori [Cc]ampo)', '2',
                None, None, None, None, None, None),
    'N020102': ('(FC|F.C|[Ff]uori [Cc]ampo)', '3',
                None, None, None, None, None, None),
    'N020103': ('(FC|F.C|[Ff]uori [Cc]ampo)', '4',
                None, None, None, None, None, None),
    'N020104': ('(FC|F.C|[Ff]uori [Cc]ampo)', '5',
                None, None, None, None, None, None),
    'N020201': (None, '7', 'bis', None, None, None, None, None, None),
    'N020202': (None, '7', 'ter', None, None, None, None, None, None),
    'N020203': (None, '7', 'quater', None, None, None, None, None, None),
    'N020204': (None, '7', 'quinquies', None, None, None, None, None, None),
    'N020206': (None, '7', 'sexies', None, None, None, None, None, None),
    'N020207': (None, '7', 'septies', None, None, None, None, None, None),
    'N020208': (None, '38', None, '5', None, None, None, None,
                'D.?L.? *331'),
    'N020209': ('no.? res', '17', None, '3', None, None, None, None, None),
    'N020210': (None, '7', None, None, None, None, None, None,
                '19[- .,]*c[- .,]*3[- .,/]*l[etr.]*b'),
    'N020212': ('[Nn][on.]+ [Ss]', '50', 'bis', '4', '[cehi .]+',
                None, None, None, 'D.?L.? *331'),
    'N020213': (None, '7', 'octies', None, None,  None, None, None, None),
}


def migrate(cr, version):
    """Set default values"""

    def search_4_tokens(tax_name, number, nature=None, bis=None,
                        comma=None, letter=None, roman=None, law=None):
        if nature:
            regex = '%s.*[Aa]rt[ .]*%s' % (nature, number)
        else:
            regex = '[Aa]rt[ .]*%s' % number
        plus = False
        if bis:
            regex += '[- ]%s' % bis
            plus = True
        if comma:
            regex += '[- .,]*c(omma)?[- .,/]*%s' % comma
            plus = True
        if letter:
            regex += '[- .,/]*l[etr.]*%s' % letter
            plus = True
        if roman:
            regex += '[- .,/]+%s' % roman
            plus = True
        if not plus:
            regex += '[^0-9]'
        if law:
            regex += '%s' % law
        if re.search(regex, tax_name):
            return True
        return False

    if not version:
        return
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        assosoftware_model = env['italy.ade.tax.assosoftware']
        tax_model = env['account.tax']
        for tax in tax_model.search([]):
            found = False
            for assosoftware in NATURE.keys():
                if search_4_tokens(
                        tax.name,
                        NATURE[assosoftware][1],
                        nature=NATURE[assosoftware][0],
                        bis=NATURE[assosoftware][2],
                        comma=NATURE[assosoftware][3],
                        letter=NATURE[assosoftware][4],
                        roman=NATURE[assosoftware][5]):
                    assosoftware_rec = assosoftware_model.search(
                        [('code', '=', assosoftware)])
                    found = True
                    print('Code %s - %s = %s[%s]' % (
                        tax.description, tax.name,
                        assosoftware, assosoftware_rec.nature
                    ))
                    break
            if not found:
                for assosoftware in NATURE.keys():
                    if not NATURE[assosoftware][0]:
                        continue
                    if search_4_tokens(
                            tax.name,
                            NATURE[assosoftware][1],
                            bis=NATURE[assosoftware][2],
                            comma=NATURE[assosoftware][3],
                            letter=NATURE[assosoftware][4],
                            roman=NATURE[assosoftware][5]):
                        assosoftware_rec = assosoftware_model.search(
                            [('code', '=', assosoftware)])
                        found = True
                        print('Code %s - %s = %s[%s]' % (
                            tax.description, tax.name,
                            assosoftware, assosoftware_rec.nature
                        ))
                        break
            if not found:
                print('Code %s - %s w/o classification' % (
                    tax.description, tax.name
                ))
