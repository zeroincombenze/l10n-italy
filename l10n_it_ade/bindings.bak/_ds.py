# flake8: noqa
# -*- coding: utf-8 -*-
# Copyright 2017-2022 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import pyxb
if pyxb.__version__ == '1.2.4':
    from odoo.addons..._ds__1_2_4 import *
elif pyxb.__version__ == '1.2.5':
    from odoo.addons..._ds__1_2_5 import *
elif pyxb.__version__ == '1.2.6':
    from odoo.addons..._ds__1_2_6 import *
else:
    raise pyxb.PyXBVersionError('1.2.4 to 1.2.6')
