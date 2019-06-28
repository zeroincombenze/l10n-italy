This module gives a lot of pretty features to print nice reports.

Inside every report it is possible check for some characteristics and/or add some values.
Field name beginning with `doc_opts` are values from the specific report which is printing.
Field name beginning with `doc_style` are values from the style of the company.
Values in `doc_opts` are more priority than value in `doc_style`.

Look at follow table for details:

.. $include usage_detail.rst

`Report Identity`

Report Identity is used to select standard Odoo reports or customized reports.
If value is 'Odoo' all customization is disabled and original Odoo reports are printed.
It is an attribute of company style.

`Print description`

This parameter manage the printing of description in document lines.
May be one of: 'as_is', 'line1', 'nocode', 'nocode1'

* as_is: that is the default value; it means description is printed as is, without manipulations
* line1: only the 1st line of description is printed
* nocode: product code (text between [brackets]) is removed
* nocode1: same of line1 + nocode

It is an attribute of specific report which is printing.

`Header mode`

This parameter set how header is printed. May be one of 'standard', 'logo', 'no_header'

* standard: standard Odoo header is printed
* logo: only the logo is printed, without text; logo must contain company informations
* no_header: no header is printed

It is an attribute of company style.

|

In xml report it is also possible test the existence of a field. The should be as follow:

`
<div t-if="'some_field' in docs[0]">FOUND SOME FIELD</div>
<div t-if="'some_field' not in docs[0]">NOT FOUND SOME FIELD</div>
`
