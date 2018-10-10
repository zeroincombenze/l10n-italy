# -*- coding: utf-8 -*-
#
# Copyright 2015-16 Lorenzo Battistini - Agile Business Group
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
import logging

_logger = logging.getLogger(__name__)

# pyxb is referenced in several in top-level statements in
# fatturapa_v_1_1, so we guard the import of the entire file
try:
    from . import fatturapa_v_1_1
except ImportError:
    _logger.debug('Cannot `import pyxb`.')  # Avoid init error if not installed
