# -*- coding: utf-8 -*-
"""
Tests are based on test environment created by module mk_test_env in repository
https://github.com/zeroincombenze/zerobug-test

Each model is declared by a dictionary which name should be "TEST_model",
where model is the uppercase model name with dot replaced by "_".
i.e.: res_partner -> TEST_RES_PARTNER

Every record is declared in the model dictionary by a key which is the external
reference used to retrieve the record.
i.e. the following record is named 'z0bug.partner1':
TEST_RES_PARTNER = {
    "z0bug.partner1": {
        "name": "Alpha",
        "street": "1, First Avenue",
        ...
    }
}

The magic dictionary TEST_SETUP contains data to load at test setup.
TEST_SETUP = {
    "res.partner": TEST_RES_PARTNER,
    ...
}

In setup() function, the following code
    self.setup_records(lang="it_IT")
creates all record declared by above data; lang is an optional parameter.

Final notes:
* Many2one value must be declared as external identifier
* Written on 2022-07-05 18:14:38.278288 by mk_test_env 10.0.0.7.5
"""
# import time
from datetime import datetime
import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)

# Record data for base models
TEST_ACCOUNT_ACCOUNT = {
    "external.3112": {
        "code": "3112",
        "name": "Ricavi da merci e servizi",
        "user_type_id": "account.data_account_type_revenue",
        "reconcile": False,
    },
    "external.4101": {
        "code": "4101",
        "name": "Acq. Merce",
        "user_type_id": "account.data_account_type_direct_costs",
        "reconcile": False,
    },
}
TEST_ACCOUNT_TAX = {
    "by": "description",
    "external.22a": {
        "amount_type": "percent",
        "account_id": "external.1601",
        "name": "IVA 22% da acquisti",
        "refund_account_id": "external.1601",
        "amount": 22,
        "type_tax_use": "purchase",
        "price_include": False,
        "description": "22a",
    },
    "external.22v": {
        "amount_type": "percent",
        "account_id": "external.2601",
        "name": "IVA 22% su vendite",
        "refund_account_id": "external.2601",
        "amount": 22,
        "type_tax_use": "sale",
        "price_include": False,
        "description": "22v",
    },
}
TEST_DELIVERY_CARRIER = {
    "delivery.delivery_carrier": {
        "name": "Consegna",
        "goods_description_id": "l10n_it_ddt.goods_description_CAR",
        "fixed_price": 4.9,
        "free_if_more_than": True,
        "amount": 50.0,
    }
}
TEST_DDT_TYPE = {
    "l10n_it_ddt.ddt_type_ddt": {
        "default_transportation_reason_id": "l10n_it_ddt.transportation_reason_VEN"
    }
}
TEST_PRODUCT_TEMPLATE = {
    "by": "default_code",
    "z0bug.product_template_1": {
        "property_account_income_id": "external.3112",
        "name": "Prodotto Alpha",
        "weight": 0.1,
        "type": "consu",
        "standard_price": 0.42,
        "supplier_taxes_id": "external.22a",
        "uom_id": "product.product_uom_unit",
        "lst_price": 0.84,
        "default_code": "AA",
        "property_account_expense_id": "external.4101",
        "uom_po_id": "product.product_uom_unit",
        "taxes_id": "external.22v",
    },
    "z0bug.product_template_2": {
        "property_account_income_id": "external.3112",
        "name": "Prodotto Beta",
        "weight": 0.2,
        "type": "consu",
        "standard_price": 1.69,
        "supplier_taxes_id": "external.22a",
        "uom_id": "product.product_uom_unit",
        "lst_price": 3.38,
        "default_code": "BB",
        "property_account_expense_id": "external.4101",
        "uom_po_id": "product.product_uom_unit",
        "taxes_id": "external.22v",
    },
    "z0bug.product_template_18": {
        "property_account_income_id": "external.3112",
        "name": "Prodotto Rho",
        "weight": 0.06,
        "type": "product",
        "standard_price": 0.59,
        "supplier_taxes_id": "external.22a",
        "uom_id": "product.product_uom_unit",
        "lst_price": 1.19,
        "default_code": "WW",
        "property_account_expense_id": "external.4101",
        "uom_po_id": "product.product_uom_unit",
        "taxes_id": "external.22v",
    },
}
TEST_RES_PARTNER = {
    "z0bug.res_partner_2": {
        "street": "Via Dueville, 2",
        "property_payment_term_id": "z0bug.payment_2",
        "city": "S. Secondo Pinerolo",
        "zip": "10060",
        "country_id": "base.it",
        "property_account_position_id": "z0bug.fiscalpos_it",
        "supplier": False,
        "email": "agrolait2@libero.it",
        "vat": "IT02345670018",
        "website": "http://www.agrolait2.it/",
        "lang": "it_IT",
        "transportation_method_id": "l10n_it_ddt.transportation_method_COR",
        "phone": "+39 0121555123",
        "customer": True,
        "name": "Latte Beta Due s.n.c.",
        "is_company": True,
        "carriage_condition_id": "l10n_it_ddt.carriage_condition_PAF",
        "state_id": "base.state_it_to",
        "goods_description_id": "l10n_it_ddt.goods_description_SFU",
    },
    "z0bug.res_partner_13": {
        "street": "Christophstraße 13",
        "property_payment_term_id": "z0bug.payment_5",
        "city": "Määnz",
        "zip": "55113",
        "country_id": "base.de",
        "property_account_position_id": "z0bug.fiscalpos_eu",
        "supplier": False,
        "vat": "DE812526315",
        "lang": "en_US",
        "customer": True,
        "name": "Axilor GmbH",
        "is_company": True,
    },
}
TEST_SETUP_LIST = [
    "account.account",
    "account.tax",
    "delivery.carrier",
    "product.template",
    "stock.ddt.type",
    "res.partner",
]
TEST_SETUP = {
    "account.account": TEST_ACCOUNT_ACCOUNT,
    "account.tax": TEST_ACCOUNT_TAX,
    "delivery.carrier": TEST_DELIVERY_CARRIER,
    "product.template": TEST_PRODUCT_TEMPLATE,
    "stock.ddt.type": TEST_DDT_TYPE,
    "res.partner": TEST_RES_PARTNER,
}

# Record data for child models
TEST_SALE_ORDER_LINE = {
    "z0bug.sale_order_Z0_2_1": {
        "product_id": "z0bug.product_product_1",
        "weight": 9.9,
        "order_id": "z0bug.sale_order_Z0_2",
        "price_unit": 0.42,
        "product_uom_qty": 100,
        "tax_id": "external.22v",
        "name": "Prodotto Alpha",
    },
    "z0bug.sale_order_Z0_2_2": {
        "product_id": "z0bug.product_product_2",
        "weight": 2,
        "order_id": "z0bug.sale_order_Z0_2",
        "price_unit": 1.69,
        "product_uom_qty": 10,
        "tax_id": "external.22v",
        "name": "Prodotto Beta",
    },
    "z0bug.sale_order_Z0_4_1": {
        "product_id": "z0bug.product_product_18",
        "order_id": "z0bug.sale_order_Z0_4",
        "price_unit": 1.09,
        "product_uom_qty": 250,
        "tax_id": "external.22v",
        "name": "Prodotto Rho",
    },
}

# Record data for models to test
TEST_SALE_ORDER = {
    # Sale Order with Picking
    "z0bug.sale_order_Z0_2": {
        "origin": "Test2",
        "payment_term_id": "z0bug.payment_2",
        "client_order_ref": "220123",
        "date_order": "2022-06-25",
        "partner_id": "z0bug.res_partner_2",
        "ddt_type_id": "l10n_it_ddt.ddt_type_ddt",
    },
    # Sale Order without Picking
    "z0bug.sale_order_Z0_4": {
        "origin": "Test4",
        "payment_term_id": "z0bug.payment_2",
        "client_order_ref": "IT/22/004",
        "date_order": "2022-06-26",
        "partner_id": "z0bug.res_partner_2",
        "ddt_type_id": "l10n_it_ddt.ddt_type_ddt",
    },
}

TNL_RECORDS = {
    "product.product": {
        # "type": ["product", "consu"],
    },
    "product.template": {
        # "type": ["product", "consu"],
    },
}


class SaleOrder(common.TransactionCase):

    # --------------------------------------- #
    # Common code: may be share among modules #
    # --------------------------------------- #

    def simulate_xref(self, xref, raise_if_not_found=None,
                      model=None, by=None, company=None, case=None):
        """Simulate External Reference
        This function simulates self.env.ref() searching for model record.
        Ordinary xref is formatted as "MODULE.NAME"; when MODULE = "external"
        this function is called.
        Record is searched by <by> parameter, default is "code" or "name";
        id NAME is formatted as "FIELD=VALUE", FIELD value is assigned to <by>
        If company is supplied, it is added in search domain;

        Args:
            xref (str): external reference
            raise_if_not_found (bool): raise exception if xref not found or
                                       if more records found
            model (str): external reference model
            by (str): default field to search object record,
            company (obj): default company
            case: apply for uppercase or lowercase

        Returns:
            obj: the model record
        """
        if model not in self.env:
            if raise_if_not_found:
                raise ValueError("Model %s not found in the system" % model)
            return False
        _fields = self.env[model].fields_get()
        if not by:
            if model in self.by:
                by = self.by[model]
            else:
                by = "code" if "code" in _fields else "name"
        module, name = xref.split(".", 1)
        if "=" in name:
            by, name = name.split("=", 1)
        if case == "upper":
            name = name.upper()
        elif case == "lower":
            name = name.lower()
        domain = [(by, "=", name)]
        if (model not in ("product.product",
                          "product.template",
                          "res.partner",
                          "res.users") and
                company and "company_id" in _fields):
            domain.append(("company_id", "=", company.id))
        objs = self.env[model].search(domain)
        if len(objs) == 1:
            return objs[0]
        if raise_if_not_found:
            raise ValueError("External ID not found in the system: %s" % xref)
        return False

    def env_ref(self, xref, raise_if_not_found=None,
                model=None, by=None, company=None, case=None):
        """Get External Reference
        This function is like self.env.ref(); if xref does not exist and
        xref prefix is "external.", engage simulate_xref

        Args:
            xref (str): external reference, format is "module.name"
            raise_if_not_found (bool): raise exception if xref not found
            model (str): external ref. model; required for "external." prefix
            by (str): field to search for object record (def "code" or "name")
            company (obj): default company

        Returns:
            obj: the model record
        """
        if xref is False or xref is None:
            return xref
        obj = self.env.ref(xref, raise_if_not_found=raise_if_not_found)
        if not obj:
            module, name = xref.split(".", 1)
            if module == "external":
                return self.simulate_xref(xref,
                                          model=model,
                                          by=by,
                                          company=company,
                                          case=case)
        return obj

    def add_xref(self, xref, model, xid):
        """Add external reference that will be used in next tests.
        If xref exist, result ID will be upgraded"""
        module, name = xref.split(".", 1)
        if module == "external":
            return False
        ir_model = self.env["ir.model.data"]
        vals = {
            "module": module,
            "name": name,
            "model": model,
            "res_id": xid,
        }
        xrefs = ir_model.search([("module", "=", module),
                                 ("name", "=", name)])
        if not xrefs:
            return ir_model.create(vals)
        xrefs[0].write(vals)
        return xrefs[0]

    def get_values(self, model, values, by=None, company=None, case=None):
        """Load data values and set them in a dictionary for create function
        * Not existent fields are ignored
        * Many2one field are filled with current record ID
        """
        _fields = self.env[model].fields_get()
        vals = {}
        if model in TNL_RECORDS:
            for item in TNL_RECORDS[model].keys():
                if item in values:
                    (old, new) = TNL_RECORDS[model][item]
                    if values[item] == old:
                        values[item] = new
        for item in values.keys():
            if item not in _fields:
                continue
            if item == "company_id" and not values[item]:
                vals[item] = company.id
            elif _fields[item]["type"] == "many2one":
                res = self.env_ref(
                    values[item],
                    model=_fields[item]["relation"],
                    by=by,
                    company=company,
                    case=case,
                )
                if res:
                    vals[item] = res.id
            elif (_fields[item]["type"] == "many2many" and
                  "." in values[item] and
                  " " not in values[item]):
                res = self.env_ref(
                    values[item],
                    model=_fields[item]["relation"],
                    by=by,
                    company=company,
                    case=case,
                )
                if res:
                    vals[item] = [(6, 0, [res.id])]
            elif values[item] is not None:
                vals[item] = values[item]
        return vals

    def model_create(self, model, values, xref=None):
        """Create a test record and set external ID to next tests"""
        if model.startswith("account.move"):
            res = self.env[model].with_context(
                check_move_validity=False).create(values)
        else:
            res = self.env[model].create(values)
        if xref and " " not in xref:
            self.add_xref(xref, model, res.id)
        return res

    def model_browse(self, model, xid, company=None, by=None,
                     raise_if_not_found=True):
        """Browse a record by external ID"""
        res = self.env_ref(
            xid,
            model=model,
            company=company,
            by=by,
        )
        if res:
            return res
        return self.env[model]

    def model_make(self, model, values, xref, company=None, by=None):
        """Create or write a test record and set external ID to next tests"""
        res = self.model_browse(model,
                                xref,
                                company=company,
                                by=by,
                                raise_if_not_found=False)
        if res:
            if model.startswith("account.move"):
                res.with_context(check_move_validity=False).write(values)
            else:
                res.write(values)
            return res
        return self.model_create(model, values, xref=xref)

    def default_company(self):
        return self.env.user.company_id

    def set_locale(self, locale_name, raise_if_not_found=True):
        modules_model = self.env["ir.module.module"]
        modules = modules_model.search([("name", "=", locale_name)])
        if modules and modules[0].state != "uninstalled":
            modules = []
        if modules:
            modules.button_immediate_install()
            self.env["account.chart.template"].try_loading_for_current_company(
                locale_name
            )
        else:
            if raise_if_not_found:
                raise ValueError(
                    "Module %s not found in the system" % locale_name)

    def install_language(self, iso, overwrite=None, force_translation=None):
        iso = iso or "en_US"
        overwrite = overwrite or False
        load = False
        lang_model = self.env["res.lang"]
        languages = lang_model.search([("code", "=", iso)])
        if not languages:
            languages = lang_model.search([("code", "=", iso),
                                           ("active", "=", False)])
            if languages:
                languages.write({"active": True})
                load = True
        if not languages or load:
            vals = {
                "lang": iso,
                "overwrite": overwrite,
            }
            self.env["base.language.install"].create(vals).lang_install()
        if force_translation:
            vals = {"lang": iso}
            self.env["base.update.translations"].create(vals).act_update()

    def setup_records(
        self, lang=None, locale=None, company=None, save_as_demo=None
    ):
        """Create all record from declared data. See above doc

        Args:
            lang (str): install & load specific language
            locale (str): install locale module with CoA; i.e l10n_it
            company (obj): declare default company for tests
            save_as_demo (bool): commit all test data as they are demo data
            Warning: usa save_as_demo carefully; is used in multiple tests,
            like in travis this option can be cause to failue of tests
            This option can be used in local tests with "run_odoo_debug -T"

        Returns:
            None
        """

        def iter_data(model, model_data, company):
            for item in model_data.keys():
                if isinstance(model_data[item], str):
                    continue
                vals = self.get_values(
                    model,
                    model_data[item],
                    company=company)
                res = self.model_make(
                    model, vals, item,
                    company=company)
                if model == "product.template":
                    model2 = "product.product"
                    vals = self.get_values(
                        model2,
                        model_data[item],
                        company=company)
                    vals["product_tmpl_id"] = res.id
                    self.model_make(
                        model2, vals, item.replace("template", "product"),
                        company=company)

        self.save_as_demo = save_as_demo or False
        if locale:
            self.set_locale(locale)
        if lang:
            self.install_language(lang)
        if not self.env["ir.module.module"].search(
                [("name", "=", "stock"), ("state", "=", "installed")]):
            TNL_RECORDS["product.product"]["type"] = ["product", "consu"]
            TNL_RECORDS["product.template"]["type"] = ["product", "consu"]
        company = company or self.default_company()
        self.by = {}
        for model, model_data in TEST_SETUP.items():
            by = model_data.get("by")
            if by:
                self.by[model] = by
        for model in TEST_SETUP_LIST:
            model_data = TEST_SETUP[model]
            iter_data(model, model_data, company)

    # ------------------ #
    # Specific test code #
    # ------------------ #
    def setUp(self):
        super(SaleOrder, self).setUp()
        self.setup_records(lang="it_IT", save_as_demo=True)
        self.setup_inventory()

    def tearDown(self):
        super(SaleOrder, self).tearDown()
        if self.save_as_demo:
            self.env.cr.commit()               # pylint: disable=invalid-commit

    def setup_inventory(self):
        inventory_model = self.env["stock.inventory"]
        inventory_line_model = self.env["stock.inventory.line"]
        location = self.env.ref("stock.stock_location_stock")
        vals = {
            "date": datetime.today().strftime("%Y-%m-%d"),
            "name": "Test Inventory",
            "filter": "none",
            "location_id": location.id,
        }
        inventory = inventory_model.create(vals)
        for xref in TEST_PRODUCT_TEMPLATE:
            if xref == "by":
                continue
            xref = xref.replace("template", "product")
            product = self.env.ref(xref)
            if product.type != "product":
                continue
            vals = {
                "inventory_id": inventory.id,
                "location_id": location.id,
                "product_id": product.id,
                "product_qty": 250.0,
                "product_uom_id": product.uom_id.id,
            }
            inventory_line_model.create(vals)
        inventory.action_done()

    def test_ddt(self):
        model = "sale.order"
        model_child = "sale.order.line"
        self.ddt = False
        self.ddt_number = False
        self.sales = []
        for xref in TEST_SALE_ORDER:
            _logger.info(
                "🎺 Testing %s[%s]" % (model, xref)
            )
            vals = self.get_values(
                model,
                TEST_SALE_ORDER[xref])
            order = self.model_make(model, vals, xref)
            order.onchange_partner_id()
            if order.partner_id == self.env.ref("z0bug.res_partner_2"):
                self.assertEqual(
                    order.transportation_method_id,
                    self.env.ref("l10n_it_ddt.transportation_method_COR"),
                    msg="Invalid order transportation method %s!" %
                        order.transportation_method_id)
                self.assertEqual(
                    order.carriage_condition_id,
                    self.env.ref("l10n_it_ddt.carriage_condition_PAF"),
                    msg="Invalid order carriage condition %s!" %
                        order.carriage_condition_id)
                self.assertEqual(
                    order.goods_description_id,
                    self.env.ref("l10n_it_ddt.goods_description_SFU"),
                    msg="Invalid order goods description %s!" %
                        order.goods_description_id)
            order.carrier_id = self.env.ref("delivery.delivery_carrier").id

            for xref_child in TEST_SALE_ORDER_LINE.values():
                if xref_child["order_id"] == xref:
                    vals = self.get_values(model_child, xref_child)
                    vals["order_id"] = order.id
                    self.model_make(model_child, vals, False)
            order.action_confirm()
            self.assertEqual(
                order.state, "sale",
                msg="Invalid order state %s!" % order.state)
            self.sales.append(order)

            if not self.ddt:
                # 1. Create a DdT from sale order
                order.action_create_ddt()
                self.assertTrue(
                    order.ddt_ids,
                    msg="No Delivery Note found!")
                self.ddt = order.ddt_ids[0]
                self.assertEqual(
                    self.ddt.state, "draft",
                    msg="Invalid DdT state %s!" % self.ddt.state)
                self.assertEqual(
                    order.picking_ids, self.ddt.picking_ids,
                    msg="Order picking different from DdT picking")
                self.assertEqual(
                    self.ddt.goods_description_id,
                    self.env.ref("l10n_it_ddt.goods_description_CAR"),
                    msg="Invalid order goods description %s!" %
                        self.ddt.goods_description_id)
                self.assertEqual(
                    order.carrier_id, self.ddt.carrier_id,
                    msg="Order delivery method different from DdT picking")
                self.assertEqual(
                    order.ddt_type_id, self.ddt.ddt_type_id,
                    msg="Order DdT type different from DdT picking")
            else:
                # 2. Add picking of sale order to DdT
                picking = order.picking_ids[0]
                picking.add_to_ddt(self.ddt)
                self.assertEqual(
                    len(self.ddt.picking_ids), 2,
                    msg="Ddt %s is not linked to 2 picking!" % self.ddt.name)

                self.ddt.set_done()
                self.assertEqual(
                    self.ddt.state, "done",
                    msg="Invalid DdT state %s!" % self.ddt.state)
                for picking in self.ddt.picking_ids:
                    self.assertEqual(
                        picking.state, "done",
                        msg="Invalid picking state %s!" % picking.state)
                self.ddt_number = self.ddt.ddt_number

        # 3. Create invoice
        invoice_ids = self.ddt.action_invoice_create()
        self.assertTrue(
            invoice_ids,
            msg="Cannot create invoice!")
        self.assertTrue(
            self.ddt.invoice_id,
            msg="DdT not set to invoiced!")
        for order in self.sales:
            self.assertEqual(
                order.invoice_status, "invoiced",
                msg="Sale order %s not set to invoiced!" % order.name)
        # 4. Remove invoice just created
        invoice = self.env["account.invoice"].browse(invoice_ids[0])
        # invoice.action_invoice_cancel()
        # invoice.action_invoice_draft()
        # for ddt_line in self.ddt.line_ids:
        #     if ddt_line.invoice_line_id:
        #         break
        # for inv_line in invoice.invoice_line_ids:
        #     if inv_line == ddt_line.invoice_line_id:
        #         inv_line.unlink()
        # self.assertFalse(ddt_line.invoice_line_id)
        invoice.action_invoice_cancel()
        invoice.unlink()
        self.assertFalse(
            self.ddt.invoice_id,
            msg="DdT still set to invoiced!")
        for order in self.sales:
            self.assertEqual(
                order.invoice_status, "to invoice",
                msg="Sale order %s still set to invoiced!" % order.name)
        # 5. Now remove DdT
        self.ddt.set_draft()
        self.ddt.action_cancel()
        self.ddt.unlink()
        for order in self.sales:
            self.assertFalse(
                order.ddt_ids,
                msg="Delivery Note still linked to Sale Order %s!" % order.name)
        # 6. Create a new DdT form 2 sale orders
        orders = self.env["sale.order"]
        for order in self.sales:
            orders += order
        orders.action_create_ddt()
        for order in self.sales:
            self.assertTrue(
                order.ddt_ids,
                msg="No Delivery Note found!")
            self.assertNotEqual(
                order.ddt_ids[0], self.ddt,
                msg="No new Delivery Note found!")
        self.ddt = self.sales[0].ddt_ids[0]
        # self.ddt.transportation_reason_id = self.env.ref(
        #     "l10n_it_ddt.transportation_reason_VEN")
        self.assertEqual(
            self.ddt.transportation_reason_id.id,
            self.env.ref("l10n_it_ddt.transportation_reason_VEN").id,
            msg="Invalid DdT transportation reason %s!" %
                self.ddt.transportation_reason_id)
        self.ddt.set_done()
        self.assertEqual(
            self.ddt.state, "done",
            msg="Invalid DdT state %s!" % self.ddt.state)
        for picking in self.ddt.picking_ids:
            self.assertEqual(
                picking.state, "done",
                msg="Invalid picking state %s!" % picking.state)
        self.assertEqual(
            self.ddt.ddt_number, self.ddt_number,
            msg="Invalid DdT number change!")
        # 7. Edit DdT
        self.ddt.set_draft()
        saved_partner = self.ddt.partner_id
        self.ddt.partner_id = self.env_ref("z0bug.res_partner_13")
        self.ddt.on_change_partner()
        self.ddt.partner_id = saved_partner
        self.ddt.on_change_partner()
