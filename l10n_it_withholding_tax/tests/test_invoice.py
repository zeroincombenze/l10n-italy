# -*- coding: utf-8 -*-
"""
Tests are based on test environment created by module mk_test_env in repository
https://github.com/zeroincombenze/zerobug-test

Each model is declared by a dictionary which name should be "TEST_model",
where model is the upercase model name with dot replaced by '_'
i.e.: res_partner -> TEST_RES_PARTNER

Every record is declared in the model dictionary by a key which is the external
reference used to retrieve the record.
i.e.:
TEST_RES_PARTNER = {
    'z0bug.partner1': {
        'name': 'Alpha',
        'street': '1, First Avenue',
        ...
    }
}

The magic dictionary TEST_SETUP contains data to load at test setup.
TEST_SETUP = {
    'res.partner': TEST_RES_PARTNER,
    ...
}

In setup() function, the following code
    self.setup_records(lang='it_IT')
creates all record declared by above data; lang is an optional parameter.

Final notes:
* Many2one value must be declared as external identifier
* Written on 2022-04-07 19:28:20.059533 by mk_test_env 10.0.0.7.3
"""
import logging

from odoo.tests import common

_logger = logging.getLogger(__name__)

# Record data for base models
TEST_ACCOUNT_ACCOUNT = {
    "external.3112": {
        "code": "3112",
        "reconcile": False,
        "user_type_id": "account.data_account_type_revenue",
        "name": "Ricavi da merci e servizi",
    },
    "external.1601": {
        "code": "1601",
        "reconcile": False,
        "user_type_id": "account.data_account_type_current_assets",
        "name": "IVA n/credito",
    },
    "external.4101": {
        "code": "4101",
        "reconcile": False,
        "user_type_id": "account.data_account_type_direct_costs",
        "name": "Acq. Merce",
    },
    "external.2601": {
        "code": "2601",
        "reconcile": False,
        "user_type_id": "account.data_account_type_current_liabilities",
        "name": "IVA n/debito",
    },
    "external.4204": {
        "code": "4204",
        "reconcile": False,
        "user_type_id": "account.data_account_type_expenses",
        "name": "Spese legali e notarili",
    },
}
TEST_ACCOUNT_FISCAL_POSITION = {
    "z0bug.fiscalpos_it": {
        "name": "Italia",
    },
}
TEST_ACCOUNT_JOURNAL = {
    "external.BILL": {
        "code": "BILL",
        "name": "Fatture di acquisto",
        "update_posted": True,
        "type": "purchase",
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
TEST_PRODUCT_TEMPLATE = {
    "by": "default_code",
    "z0bug.product_template_0": {
        "property_account_income_id": "external.3112",
        "name": "Varie",
        "type": "consu",
        "conai_category_id": "l10n_it_conai.ca",
        "standard_price": 9.5,
        "supplier_taxes_id": "external.22a",
        "uom_id": "product.product_uom_unit",
        "lst_price": 18,
        "default_code": "MISC",
        "property_account_expense_id": "external.4101",
        "uom_po_id": "product.product_uom_unit",
        "taxes_id": "external.22v",
    },
}
TEST_RES_PARTNER = {
    "z0bug.res_partner_10": {
        "street": "Largo Fasuli Decimomanno, 10",
        "property_payment_term_id": "z0bug.payment_3",
        "city": "Torino",
        "zip": "10121",
        "country_id": "base.it",
        "property_account_position_id": "z0bug.fiscalpos_it",
        "supplier": True,
        "property_supplier_payment_term_id": "z0bug.payment_3",
        "email": "jacksonlibero@pec.notariato.it",
        "vat": "IT10242670015",
        "fiscalcode": "JCKLBR72M24L736R",
        "lang": "it_IT",
        "customer": False,
        "name": "Notaio Decimo Jackson",
        "is_company": True,
        "state_id": "base.state_it_to",
    },
}
TEST_SETUP_LIST = [
    "account.account",
    "account.fiscal.position",
    "account.journal",
    "account.tax",
    "product.template",
    "res.partner",
]
TEST_SETUP = {
    "account.account": TEST_ACCOUNT_ACCOUNT,
    "account.fiscal.position": TEST_ACCOUNT_FISCAL_POSITION,
    "account.journal": TEST_ACCOUNT_JOURNAL,
    "account.tax": TEST_ACCOUNT_TAX,
    "product.template": TEST_PRODUCT_TEMPLATE,
    "res.partner": TEST_RES_PARTNER,
}

# Record data for child models
TEST_ACCOUNT_INVOICE_LINE = {
    "z0bug.invoice_ZI_1_1": {
        "product_id": "z0bug.product_product_0",
        "invoice_id": "z0bug.invoice_ZI_1",
        "price_unit": 1500,
        "account_id": "external.4204",
        "name": "Costituzione società",
        "invoice_line_tax_ids": "external.22a",
        "invoice_line_tax_wt_ids": "z0bug.wt_1040",
        "quantity": 1,
    },
    "z0bug.invoice_ZI_1_1": {
        "product_id": "z0bug.product_product_0",
        "invoice_id": "z0bug.invoice_ZI_1",
        "price_unit": 1500,
        "account_id": "external.4204",
        "name": "Costituzione società",
        "invoice_line_tax_ids": "external.22a",
        "invoice_line_tax_wt_ids": "z0bug.wt_1040",
        "quantity": 1,
    },
}

# Record data for models to test
TEST_ACCOUNT_INVOICE = {
    "z0bug.invoice_ZI_1": {
        "origin": "SAJ/0807",
        "reference": "SAJ/0807",
        "type": "in_invoice",
        "payment_term_id": "z0bug.payment_3",
        "journal_id": "external.BILL",
        "date_invoice": "2020-12-20",
        "date": "2020-12-31",
        "partner_id": "z0bug.res_partner_10",
        "fiscal_position_id": "z0bug.fiscalpos_it",
    },
}

TNL_RECORDS = {
    "product.product": {
        # 'type': ['product', 'consu'],
    },
    "product.template": {
        # 'type': ['product', 'consu'],
    },
}


class AccountInvoice(common.TransactionCase):

    # --------------------------------------- #
    # Common code: may be share among modules #
    # --------------------------------------- #

    def simulate_xref(
        self,
        xref,
        raise_if_not_found=None,
        model=None,
        by=None,
        company=None,
        case=None,
    ):
        """Simulate External Reference
        This function simulates self.env.ref() searching for model record.
        Ordinary xref is formatted as "MODULE.NAME"; when MODULE = "external"
        this function is called.
        Record is searched by <by> parameter, default is 'code' or 'name';
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
        if (
            model
            not in ("product.product", "product.template", "res.partner", "res.users")
            and company
            and "company_id" in _fields
        ):
            domain.append(("company_id", "=", company.id))
        objs = self.env[model].search(domain)
        if len(objs) == 1:
            return objs[0]
        if raise_if_not_found:
            raise ValueError("External ID not found in the system: %s" % xref)
        return False

    def env_ref(
        self,
        xref,
        raise_if_not_found=None,
        model=None,
        by=None,
        company=None,
        case=None,
    ):
        """Get External Reference
        This function is like self.env.ref(); if xref does not exist and
        xref prefix is 'external.', engage simulate_xref

        Args:
            xref (str): external reference, format is "module.name"
            raise_if_not_found (bool): raise exception if xref not found
            model (str): external ref. model; required for "external." prefix
            by (str): field to search for object record (def 'code' or 'name')
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
                return self.simulate_xref(
                    xref, model=model, by=by, company=company, case=case
                )
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
        xrefs = ir_model.search([("module", "=", module), ("name", "=", name)])
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
            elif (
                _fields[item]["type"] == "many2many"
                and "." in values[item]
                and " " not in values[item]
            ):
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
            res = self.env[model].with_context(check_move_validity=False).create(values)
        else:
            res = self.env[model].create(values)
        if xref and " " not in xref:
            self.add_xref(xref, model, res.id)
        return res

    def model_browse(self, model, xid, company=None, by=None, raise_if_not_found=True):
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
        res = self.model_browse(
            model, xref, company=company, by=by, raise_if_not_found=False
        )
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
                raise ValueError("Module %s not found in the system" % locale_name)

    def install_language(self, iso, overwrite=None, force_translation=None):
        iso = iso or "en_US"
        overwrite = overwrite or False
        load = False
        lang_model = self.env["res.lang"]
        languages = lang_model.search([("code", "=", iso)])
        if not languages:
            languages = lang_model.search([("code", "=", iso), ("active", "=", False)])
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

    def setup_records(self, lang=None, locale=None, company=None, save_as_demo=None):
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
                vals = self.get_values(model, model_data[item], company=company)
                res = self.model_make(model, vals, item, company=company, by=by)
                if model == "product.template":
                    model2 = "product.product"
                    vals = self.get_values(model2, model_data[item], company=company)
                    vals["product_tmpl_id"] = res.id
                    self.model_make(
                        model2,
                        vals,
                        item.replace("template", "product"),
                        company=company,
                        by=by,
                    )

        self.save_as_demo = save_as_demo or False
        if locale:
            self.set_locale(locale)
        if lang:
            self.install_language(lang)
        if not self.env["ir.module.module"].search(
            [("name", "=", "stock"), ("state", "=", "installed")]
        ):
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
        super(AccountInvoice, self).setUp()
        self.setup_records(lang="it_IT")

    def tearDown(self):
        super(AccountInvoice, self).tearDown()
        if self.save_as_demo:
            self.env.cr.commit()  # pylint: disable=invalid-commit

    def test_account_invoice(self):
        # Here an example of code you should insert to test
        # Example is based on account.invoice
        model = "account.invoice"
        model_child = "account.invoice.line"
        for xref in TEST_ACCOUNT_INVOICE:
            _logger.info("🎺 Testing %s[%s]" % (model, xref))
            vals = self.get_values(model, TEST_ACCOUNT_INVOICE[xref])
            res = self.model_make(model, vals, xref)

            for xref_child in TEST_ACCOUNT_INVOICE_LINE.values():
                if xref_child["invoice_id"] == xref:
                    vals = self.get_values(model_child, xref_child)
                    vals["invoice_id"] = res.id
                    self.model_make(model_child, vals, False)
            res.compute_taxes()
