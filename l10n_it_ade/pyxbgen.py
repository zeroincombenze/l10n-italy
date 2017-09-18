#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pyxbgen
# Agenzia delle Entrate pyxb generator
#
# This free software is released under GNU Affero GPL3
# author: Antonio M. Vigliotti - antoniomaria.vigliotti@gmail.com
# (C) 2017-2017 by SHS-AV s.r.l. - http://www.shs-av.com - info@shs-av.com
#
import sys


__version__ = '0.1.0.24'


def main(args):
    try:
        fd = open(args[0], 'r')
        source = fd.read()
        fd.close()
        lines = source.split('\n')
        saved_lines = []
        state = 0
        lineno = 0
        lines.insert(lineno,
                     '# flake8: noqa')
        lineno += 1
        lines.insert(lineno,
                     '# -*- coding: utf-8 -*-')
        lineno += 1
        while lineno < len(lines):
            if not lines[lineno]:
                pass
            elif lines[lineno] == '# -*- coding: utf-8 -*-':
                del lines[lineno]
                lineno -= 1
            elif lines[lineno][0:6] == 'import':
                if lines[lineno][0:11] == 'import pyxb':
                    if state == 0:
                        lines.insert(lineno,
                                     'import logging')
                        lineno += 1
                        state = 1
                    if state == 1:
                        saved_lines.append(lines[lineno])
                        del lines[lineno]
                        lineno -= 1
                elif lines[lineno][0:10] == 'import _cm' or \
                        lines[lineno][0:10] == 'import _ds':
                    lines[lineno] = 'from . %s' % lines[lineno]
            elif state == 1:
                lines.insert(lineno,
                             '# from openerp import addons')
                lineno += 1
                lines.insert(lineno,
                             '_logger = logging.getLogger(__name__)')
                lineno += 1
                lines.insert(lineno,
                             'try:')
                lineno += 1
                for saved_line in saved_lines:
                    lines.insert(lineno,
                                 '    %s' % saved_line)
                    lineno += 1
                lines.insert(lineno,
                             'except ImportError as err:')
                lineno += 1
                lines.insert(lineno,
                             '    _logger.debug(err)')
                lineno += 1
                lines.insert(lineno,
                             '')
                lineno += 1
                state = 2
            lineno += 1
        fd = open(args[0], 'w')
        fd.write(''.join('%s\n' % l for l in lines))
        fd.close() 
    except:
        pass


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
