This module gives a lot of features usable by reports.

Inside every report it is possible check for some charactes o add some values.
Look at follow table for details:

.. $include usage_detail.rst

`Report Identity`

Report Identity is used to manage standard Odoo reports or customized reports.
If value is 'Odoo' all customizzation is disabled and original Odoo reports are printed.

`Print description`

This parameter manage the printing of description of document lines.
May be one of: 'as_is', 'line1', 'nocode', 'nocode1'

* as_is: is default value; means description is printed as is, without manipulations
* line1: only the 1st line of description is printed
* nocode: product code (printed between [brackets]) is removed
* nocode1: same of line1 + nocode

`Header mode`

This parameter set how header is printed. May be one of 'standard', 'logo', 'no_header'

* standard: standard Odoo header is printed
* logo: only the logo is printed, without text; logo must contain company informations
* no_header: no header is printed

In xml report it is also possible test the existence of a field. The should be as follow:

`
<div t-if="'some_field' in docs[0]">FOUND SOME FIELD</div>
<div t-if="'some_field' not in docs[0]">NOT FOUND SOME FIELD</div>
`
