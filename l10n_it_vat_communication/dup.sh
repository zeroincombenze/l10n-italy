echo "\$ rm -fR /opt/odoo/8.0/__to_remove/l10n_it_vat_communication/"
rm -fR /opt/odoo/8.0/__to_remove/l10n_it_vat_communication/
echo "\$ mv /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/ /opt/odoo/8.0/__to_remove/"
mv /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/ /opt/odoo/8.0/__to_remove/
echo "\$ cp -R /opt/odoo/7.0/l10n-italy/l10n_it_vat_communication/ /opt/odoo/8.0/l10n-italy/"
cp -R /opt/odoo/7.0/l10n-italy/l10n_it_vat_communication/ /opt/odoo/8.0/l10n-italy/
# echo "\$ sed 's/import decimal_precision as dp/import openerp.addons.decimal_precision as dp/' -i /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/models/account.py"
# sed 's/import decimal_precision as dp/import openerp.addons.decimal_precision as dp/' -i /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/models/account.py
# echo "sed 's/from l10n_it_vat_communication.ade import ADE_LEGALS/from openerp.addons.l10n_it_vat_communication.ade import ADE_LEGALS/' -i /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/models/account.py"
# sed 's/from l10n_it_vat_communication.ade import ADE_LEGALS/from openerp.addons.l10n_it_vat_communication.ade import ADE_LEGALS/' -i /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/models/account.py
# echo "sed 's/from l10n_it_ade import ade/from openerp.addons.l10n_it_ade import ade/' -i /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/models/account.py"
# sed 's/from l10n_it_ade import ade/from openerp.addons.l10n_it_ade import ade/' -i /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/models/account.py
echo "\$ sed 's/7\.0/8.0/' -i /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/__openerp__.py"
sed 's/7\.0/8.0/' -i /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/__openerp__.py
echo "mv /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/static/src/img /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/static/description"
mv /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/static/src/img /opt/odoo/8.0/l10n-italy/l10n_it_vat_communication/static/description
echo "rm -fR /opt/odoo/8.0//l10n-italy/l10n_it_vat_communication/static/src/"
rm -fR /opt/odoo/8.0//l10n-italy/l10n_it_vat_communication/static/src/

