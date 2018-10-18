#
# Copyright 2014    Davide Corio
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
import logging

_logger = logging.getLogger(__name__)

# there are multiple statements that should be guarded
# in wizard_export_fatturapa, so we guard the entire file
try:
    from . import wizard_export_fatturapa
except ImportError:
    _logger.debug('Cannot `import pyxb`.')  # Avoid init error if not installed
