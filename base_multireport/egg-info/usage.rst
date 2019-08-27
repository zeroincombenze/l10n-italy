This module gives a lot of pretty features to print nice reports.

Inside every report it is possible check for some characteristics and/or add some values.
The value of every parameter is evaluate in fallback way.
The fallback path is:
1. Valid value (not null and not space) in report (model ir_action_report_xml)
2. Valid value (not null and not space) in template of report (model multireport.template), if declared
3. Valid value (not null and not space) in specific document style (model multireport.style)
4. Value in default document style (model multireport.style)
5. For some parameters, for historical reason, value may be load from other sources (i.e. custom footer)

In report the fallback function is report.get_report_attrib(PARAM,o,doc_opts), where param is parme to get value.

Report may load specific value if declare field as follow:
* If field name beginning with `doc_opts`, value is from the specific report which is printing.
* If Field name beginning with `doc_style`, value is from the style of the company.

Warning! If report get value directly from report or style, can get a None value and result may be unexpected.

Look at follow table for details:

.. $include usage_detail.rst

`Report Identity`

Report Identity is used to select standard Odoo reports or customized reports.
If value is 'Odoo' all customization is disabled and original Odoo reports are printed.
It is only an attribute of company style.

`Print description`

This parameter manage the printing of description in document lines.
May be one of: 'as_is', 'line1', 'nocode', 'nocode1'

* as_is: that is the default value; it means description is printed as is, without manipulations
* line1: only the 1st line of description is printed
* nocode: product code (text between [brackets]) is removed
* nocode1: same of line1 + nocode

It is an fallback attribute.

`Header mode`

This parameter set how header is printed. May be one of 'standard', 'logo', 'no_header'

* standard: standard Odoo header is printed
* logo: only the logo is printed, without text; logo must contain company informations
* no_header: no header is printed

It is an fallback attribute.

|

In xml report it is also possible test the existence of a field. The should be as follow:

`
<div t-if="'some_field' in docs[0]">FOUND SOME FIELD</div>
<div t-if="'some_field' not in docs[0]">NOT FOUND SOME FIELD</div>
`
