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
* Written on 2022-04-21 18:34:00.000000 by mk_test_env 10.0.0.7.3
"""
import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)

# Record data for base models
TEST_ACCOUNT_ACCOUNT = {
    'external.1601': {
        'code': '1601',
        'reconcile': False,
        'user_type_id': 'account.data_account_type_current_assets',
        'name': 'IVA n/credito',
    },
    'external.2601': {
        'code': '2601',
        'reconcile': False,
        'user_type_id': 'account.data_account_type_current_liabilities',
        'name': 'IVA n/debito',
    },
}
TEST_ACCOUNT_TAX = {
    'by': 'description',
    'external.22a': {
        'amount_type': 'percent',
        'account_id': 'external.1601',
        'name': 'IVA 22% da acquisti',
        'refund_account_id': 'external.1601',
        'amount': 22,
        'type_tax_use': 'purchase',
        'price_include': False,
        'description': '22a',
    },
    'external.22v': {
        'amount_type': 'percent',
        'account_id': 'external.2601',
        'name': 'IVA 22% su vendite',
        'refund_account_id': 'external.2601',
        'amount': 22,
        'type_tax_use': 'sale',
        'price_include': False,
        'description': '22v',
    },
    'external.2280a': {
        'amount_type': 'group',
        'account_id': None,
        'name': 'IVA 22% detraibile 80%',
        'refund_account_id': None,
        'amount': 0.0,
        'type_tax_use': 'purchase',
        'price_include': False,
        'description': '2280a',
    },
    'external.2280a1': {
        'parent_tax_ids': 'external.2280a',
        'amount_type': 'percent',
        'account_id': None,
        'name': 'IVA 22% quota indetraibile',
        'refund_account_id': None,
        'amount': 4.4,
        'type_tax_use': 'purchase',
        'price_include': False,
        'description': '2280a1',
    },
    'external.2280a2': {
        'parent_tax_ids': 'external.2280a',
        'amount_type': 'percent',
        'account_id': 'external.1601',
        'name': 'IVA 22% quota detraibile',
        'refund_account_id': 'external.1601',
        'amount': 17.6,
        'type_tax_use': 'purchase',
        'price_include': False,
        'description': '2280a2',
    },
}
TEST_SETUP_LIST = [
    'account.account',
    'account.tax',
]
TEST_SETUP = {
    'account.account': TEST_ACCOUNT_ACCOUNT,
    'account.tax': TEST_ACCOUNT_TAX,
}


class AccountTax(common.TransactionCase):

    # --------------------------------------- #
    # Common code: may be share among modules #
    # --------------------------------------- #

    def simulate_xref(self, xref, raise_if_not_found=None,
                      model=None, by=None, company=None, case=None):
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
                raise ValueError('Model %s not found in the system' % model)
            return False
        _fields = self.env[model].fields_get()
        if not by:
            if model in self.by:
                by = self.by[model]
            else:
                by = 'code' if 'code' in _fields else 'name'
        module, name = xref.split('.', 1)
        if '=' in name:
            by, name = name.split('=', 1)
        if case == 'upper':
            name = name.upper()
        elif case == 'lower':
            name = name.lower()
        domain = [(by, '=', name)]
        if (model not in ('product.product',
                          'product.template',
                          'res.partner',
                          'res.users') and
                company and 'company_id' in _fields):
            domain.append(('company_id', '=', company.id))
        objs = self.env[model].search(domain)
        if len(objs) == 1:
            return objs[0]
        if raise_if_not_found:
            raise ValueError('External ID not found in the system: %s' % xref)
        return False

    def env_ref(self, xref, raise_if_not_found=None,
                model=None, by=None, company=None, case=None):
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
            module, name = xref.split('.', 1)
            if module == 'external':
                return self.simulate_xref(xref,
                                          model=model,
                                          by=by,
                                          company=company,
                                          case=case)
        return obj

    def add_xref(self, xref, model, xid):
        """Add external reference that will be used in next tests.
        If xref exist, result ID will be upgraded"""
        module, name = xref.split('.', 1)
        if module == 'external':
            return False
        ir_model = self.env['ir.model.data']
        vals = {
            'module': module,
            'name': name,
            'model': model,
            'res_id': xid,
        }
        xrefs = ir_model.search([('module', '=', module),
                                 ('name', '=', name)])
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
        # if model in TNL_RECORDS:
        #     for item in TNL_RECORDS[model].keys():
        #         if item in values:
        #             (old, new) = TNL_RECORDS[model][item]
        #             if values[item] == old:
        #                 values[item] = new
        for item in values.keys():
            if item not in _fields:
                continue
            if item == 'company_id' and not values[item]:
                vals[item] = company.id
            elif _fields[item]['type'] == 'many2one':
                res = self.env_ref(
                    values[item],
                    model=_fields[item]['relation'],
                    by=by,
                    company=company,
                    case=case,
                )
                if res:
                    vals[item] = res.id
            elif (_fields[item]['type'] == 'many2many' and
                  '.' in values[item] and
                  ' ' not in values[item]):
                res = self.env_ref(
                    values[item],
                    model=_fields[item]['relation'],
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
        if model.startswith('account.move'):
            res = self.env[model].with_context(
                check_move_validity=False).create(values)
        else:
            res = self.env[model].create(values)
        if xref and ' ' not in xref:
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
            if model.startswith('account.move'):
                res.with_context(check_move_validity=False).write(values)
            else:
                res.write(values)
            return res
        return self.model_create(model, values, xref=xref)

    def default_company(self):
        return self.env.user.company_id

    def set_locale(self, locale_name, raise_if_not_found=True):
        modules_model = self.env['ir.module.module']
        modules = modules_model.search([('name', '=', locale_name)])
        if modules and modules[0].state != 'uninstalled':
            modules = []
        if modules:
            modules.button_immediate_install()
            self.env['account.chart.template'].try_loading_for_current_company(
                locale_name
            )
        else:
            if raise_if_not_found:
                raise ValueError(
                    'Module %s not found in the system' % locale_name)

    def install_language(self, iso, overwrite=None, force_translation=None):
        iso = iso or 'en_US'
        overwrite = overwrite or False
        load = False
        lang_model = self.env['res.lang']
        languages = lang_model.search([('code', '=', iso)])
        if not languages:
            languages = lang_model.search([('code', '=', iso),
                                           ('active', '=', False)])
            if languages:
                languages.write({'active': True})
                load = True
        if not languages or load:
            vals = {
                'lang': iso,
                'overwrite': overwrite,
            }
            self.env['base.language.install'].create(vals).lang_install()
        if force_translation:
            vals = {'lang': iso}
            self.env['base.update.translations'].create(vals).act_update()

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
            for item in sorted(model_data.keys()):
                if isinstance(model_data[item], str):
                    continue
                vals = self.get_values(
                    model,
                    model_data[item],
                    company=company)
                res = self.model_make(
                    model, vals, item,
                    company=company)
                if model == 'product.template':
                    model2 = 'product.product'
                    vals = self.get_values(
                        model2,
                        model_data[item],
                        company=company)
                    vals['product_tmpl_id'] = res.id
                    self.model_make(
                        model2, vals, item.replace('template', 'product'),
                        company=company)

        self.save_as_demo = save_as_demo or False
        if locale:
            self.set_locale(locale)
        if lang:
            self.install_language(lang)
        # if not self.env['ir.module.module'].search(
        #         [('name', '=', 'stock'), ('state', '=', 'installed')]):
        #     TNL_RECORDS['product.product']['type'] = ['product', 'consu']
        #     TNL_RECORDS['product.template']['type'] = ['product', 'consu']
        company = company or self.default_company()
        self.by = {}
        for model, model_data in TEST_SETUP.items():
            by = model_data.get('by')
            if by:
                self.by[model] = by
        for model in TEST_SETUP_LIST:
            model_data = TEST_SETUP[model]
            iter_data(model, model_data, company)

    # ------------------ #
    # Specific test code #
    # ------------------ #
    def setUp(self):
        super(AccountTax, self).setUp()
        self.setup_records()

    def tearDown(self):
        super(AccountTax, self).tearDown()
        if self.save_as_demo:
            self.env.cr.commit()               # pylint: disable=invalid-commit

    def test_account_tax(self):
        model = 'account.tax'
        tax_model = self.env[model]
        _logger.info("🎺 Testing %s" % model)

        tax = self.model_browse(model, 'external.22v')
        self.assertEqual(
            tax._get_tax_amount(),
            22.0,
            msg='Invalid rate for 22v')
        tax = self.model_browse(model, 'external.22a')
        self.assertEqual(
            tax._get_tax_amount(),
            22.0,
            msg='Invalid rate for 22a')
        tax = self.model_browse(model, 'external.2280a')
        self.assertEqual(
            tax._get_tax_amount(),
            22.0,
            msg='Invalid rate for 2280a')

        ctx = {'from_date': '2022-01-01', 'to_date': '2022-12-31'}
        parent_name = ''
        for (xref, name, test_base, test_vat) in (
                ('external.22v', 'IVA 22% su vendite', 122.0, 22.0),
                ('external.22a', 'IVA 22% da acquisti', 61.0, 11.0),
                ('external.2280a', 'IVA 22% detraibile 80%', 61.0, 11.0),
                ('external.2280a1', 'IVA 22% quota indetraibile', 0.0, 0.0),
                ('external.2280a2', 'IVA 22% quota detraibile', 0.0, 0.0),
        ):
            if xref == 'external.2280a':
                parent_name = name
            tax = self.model_browse(model, xref)
            self.assertEqual(
                tax._get_tax_name(),
                parent_name if '2280a' in xref else name,
                msg='Invalid name for %s' % xref)
            # tax.write({'base_balance': test_base, 'balance': test_vat})
            (tax_name, base, vat, deductible, undeductible) = (
                tax._compute_totals_tax(ctx)
            )
            self.assertEqual(
                tax_name,
                name,
                msg='Invalid name for %s' % xref)
            # self.assertEqual(
            #     base,
            #     test_base,
            #     msg='Invalid name for %s' % xref)

        for (nature, rc) in (
                ('N1', False),
                ('N2', False),
                ('N3.1', True),
                ('N3.2', True),
                ('N3.3', True),
                ('N3.4', True),
                ('N3.5', False),
                ('N3.6', True),
                ('N4', False),
                ('N5', False),
                ('N6.1', True),
                ('N6.2', True),
                ('N6.3', True),
                ('N6.4', True),
                ('N6.5', True),
                ('N6.6', True),
                ('N6.7', True),
                ('N7', False),
        ):
            self.assertEqual(
                tax_model.is_rc(nature=nature),
                rc,
                msg='Invalid flag rc for nature %s' % nature)
