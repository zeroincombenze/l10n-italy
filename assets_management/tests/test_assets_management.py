# Copyright 2021-22 librERP enterprise network <https://www.librerp.it>
# Copyright 2021-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
# The tests of this module are based on two cases; all data are in the excel file
# in "test/Test Workflow.xlsx" with follow work-flow:
#
# 1. New assets creation (4 items, #1 #2 #3 and #4) with tempary value 1/10
# 2. Depreciation for 1.st year: fixed rate (#1 #3) or pro-rata-temporis (#2 #4)
# 3. Link assets with purchase invoice: asset values updated
# 4. Depreciation for 1.st year: fixed rate (#1 #3) or pro-rata-temporis (#2 #4)
# 5. For asset #3 down value
# 6. Depreciation for 2.nd year (#1 #2 #4 full year, #3 base on down value)
# 7. Full (asset #1) and partial (asset #2) dismission
#
from datetime import datetime, date
from calendar import isleap
import logging

from odoo.tools.float_utils import float_round
from odoo.exceptions import UserError, ValidationError
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)


#################################
#      Test values to check     #
#################################
TESTBED_VALUES = {
    "cat_1.percentage": 25,
    "cat_2.percentage": 24,

    "date.eoy[-2]": date(date.today().year - 2, 12, 31),
    "date.eoy[-1]": date(date.today().year - 1, 12, 31),
    "date.eoy": date(date.today().year, 12, 31),

    "asset_1.initial_amount": 100.0,
    "asset_1.initial_depreciation_amount": 12.50,
    "asset_1.purchase_amount": 1000.0,
    "asset_1.depreciation_amount[-2]": 125.0,
    "asset_1.depreciated_amount[-2]": 125.00,
    "asset_1.residual_amount[-2]": 875.00,
    "asset_1.depreciation_amount[-1]": 250.0,
    "asset_1.depreciated_amount[-1]": 375.00,
    "asset_1.residual_amount[-1]": 625.00,

    "asset_2.initial_amount": 250.0,
    "asset_2.initial_depreciation_amount": 15.12,
    "asset_2.purchase_amount": 2500.0,
    "asset_2.depreciation_amount[-2]": 151.23,
    "asset_2.depreciated_amount[-2]": 151.23,
    "asset_2.residual_amount[-2]": 2348.77,
    "asset_2.depreciation_amount[-1]": 600.0,
    "asset_2.depreciated_amount[-1]": 751.23,
    "asset_2.residual_amount[-1]": 1748.77,

    "asset_3.initial_amount": 100.0,
    "asset_3.initial_depreciation_amount": 12.50,
    "asset_3.purchase_amount": 1000.0,
    "asset_3.depreciation_amount[-2]": 125.0,
    "asset_3.depreciated_amount[-2]": 125.0,
    "asset_3.residual_amount[-2]": 875.00,
    # For leap year set (year - 1)-03-30
    "asset3.date_down[-1]": date(date.today().year - 1, 3, 31),
    "asset_3.down_value[-1]": 725.0,
    "asset_3.purchase_amount_post[-1]": 275.0,
    "asset_3.depreciation_amount_pre[-1]": 61.64,
    "asset_3.depreciation_amount[-1]": 51.8,
    "asset_3.depreciated_amount[-1]": 238.44,
    "asset_3.residual_amount[-1]": 36.56,

    "asset_4.initial_amount": 250.0,
    "asset_4.initial_depreciation_amount": 15.12,
    "asset_4.purchase_amount": 2500.0,
    "asset_4.depreciation_amount[-2]": 151.23,
    "asset_4.depreciated_amount[-2]": 151.23,
    "asset_4.residual_amount[-2]": 2348.77,
    # For leap year set (year - 1)-07-30
    "asset4.date_disposal[-1]": date(date.today().year - 1, 7, 31),
    # Disposal rate 20%
    "asset_4.partial_dismis_percentage[-1]": 20,
    "asset_4.sale_amount[-1]": 525.0,
    "asset_4.depreciation_amount[-1]": 211.26,
    "asset_4.depreciated_amount[-1]": 710.98,
    "asset_4.residual_amount[-1]": 1888.68,

    "asset_1_2.date.disposal": date(date.today().year, 1, 31),
    "asset_4.date.disposal": date(date.today().year, 7, 31),
    "asset_1_3.date.disposal": date(date.today().year - 2, 12, 1),
    "asset_2_4.date.disposal": date(date.today().year - 2, 10, 1),

    "asset_1.sale_amount": 1400.0,
    "asset_2.sale_amount": 3210.0,

    "asset_3.down_value": 725.0,

}
TESTBED_VALUES.update(
    {
        # Asset #1 + #3 - yearly depreciation amount
        "asset_1.depreciation_amount": float_round(
            TESTBED_VALUES["asset_1.purchase_amount"]
            * TESTBED_VALUES["cat_1.percentage"]
            / 100.0,
            2,
        ),
        # Asset #2 + #4 - yearly depreciation amount
        "asset_2.depreciation_amount": float_round(
            TESTBED_VALUES["asset_2.purchase_amount"]
            * TESTBED_VALUES["cat_2.percentage"]
            / 100.0,
            2,
        ),
        # Asset #3 - asset value after down (out) value
        "asset_3.purchase_amount[-1]": float_round(
            TESTBED_VALUES["asset_3.purchase_amount"]
            - TESTBED_VALUES["asset_3.down_value"],
            2,
        ),
    }
)


TEST_SETUP_LIST = [
    "account.account",
    "account.tax",
    "asset.category",
    "asset.category.depreciation.type",
    "asset.asset",
    "account.fiscal.year",
    "account.invoice",
    "account.invoice.line",
]


class TestAssets(SingleTransactionCase):

    def setUp(self):
        super().setUp()
        self.debug_level = 0
        self.odoo_commit_test = True
        self.setup_env()                                      # Create test environment

    def tearDown(self):
        super().tearDown()

    def get_xref4test(self, xref, item):
        return xref.split(".")[1] + "." + item

    def get_test_value(self, xref, item):
        return TESTBED_VALUES[self.get_xref4test(xref, item)]

    def set_sale_invoice_asset_4(self):
        tax = self.get_sale_tax()
        vals = {
            "partner_id": self.env.ref("base.res_partner_2").id,
            "type": "out_invoice",
            "date_invoice":
                TESTBED_VALUES["asset_4.date.disposal"].strftime("%Y-%m-%d"),
            "invoice_line_ids": [],
        }
        vals["invoice_line_ids"].append(
            (
                0,
                0,
                {
                    "name": "Asset Four",
                    "account_id": self.asset_1.category_id.asset_account_id.id,
                    "price_unit": TESTBED_VALUES["asset_4.sale_amount"],
                    "quantiy": 1.0,
                    "invoice_line_tax_ids": [(6, 0, [tax.id])],
                },
            )
        )
        self.sale_invoice4 = self.env["account.invoice"].create(vals)
        self.sale_invoice4.journal_id.update_posted = True  # Assure invoice cancel
        self.sale_invoice4.action_invoice_open()

    def _day_rate(self, date_from, date_to, is_leap=None):
        return ((date_to - date_from).days + 1) / (365 if not is_leap else 366)

    def _remove_depreciation_lines(self, asset=None, date_from=None):
        date_from = date_from or date(date.today().year, 1, 1)
        self._get_depreciation_lines(asset=asset, date_from=date_from).unlink()

    def _get_depreciation_lines(
        self, asset=None, move_type=None, date_from=None, date_to=None
    ):
        dep_line_model = self.env["asset.depreciation.line"]
        move_type = move_type or "depreciated"
        domain = [("move_type", "=", move_type)]
        if asset:
            domain.append(("asset_id", "=", asset.id))
        if date_from:
            if isinstance(date_from, date):
                date_from = date_from.strftime("%Y-%m-%d")
            domain.append(("date", ">=", date_from))
        if date_to:
            if isinstance(date_to, date):
                date_to = date_to.strftime("%Y-%m-%d")
            domain.append(("date", "<=", date_to))
        return dep_line_model.search(domain)

    def _check_4_move_depreciated(self, dep):
        for line in dep.move_id.line_ids:
            if line.account_id == self.env.ref("z0bug.coa_conf_xfa_fund"):
                self.assertEqual(
                    dep.amount,
                    line.credit,
                    "Invalid credit amount for fund move %s" % dep.move_id.id,
                )
            elif line.account_id == self.env.ref("z0bug.coa_depreciations"):
                self.assertEqual(
                    dep.amount,
                    line.debit,
                    "Invalid debit amount for fund move %s" % dep.move_id.id,
                )
            else:
                raise (
                    TypeError,
                    "Invalid line account for fund move %s" % dep.move_id.id,
                )

    def _check_4_move_gain(self, dep):
        for line in dep.move_id.line_ids:
            if line.account_id == self.account_gain:
                self.assertEqual(
                    dep.amount,
                    line.credit,
                    "Invalid credit amount for gain move %s" % dep.move_id.id,
                )
            elif line.account_id == self.account_fixed_assets:
                self.assertEqual(
                    dep.amount,
                    line.debit,
                    "Invalid debit amount for gain move %s" % dep.move_id.id,
                )
            else:
                raise (
                    TypeError,
                    "Invalid line account for gain move %s" % dep.move_id.id,
                )

    def _check_4_move_out(self, dep):
        for line in dep.move_id.line_ids:
            if line.account_id == self.account_fixed_assets:
                self.assertEqual(
                    dep.amount,
                    line.credit,
                    "Invalid credit amount for out move %s" % dep.move_id.id,
                )
            elif line.account_id == self.account_loss:
                self.assertEqual(
                    dep.amount,
                    line.debit,
                    "Invalid debit amount for out move %s" % dep.move_id.id,
                )
            else:
                raise (
                    TypeError,
                    "Invalid line account for out move %s" % dep.move_id.id,
                )

    def _check_4_move(self, dep):
        if dep.move_id:
            method = "_check_4_move_%s" % dep.move_type
            if hasattr(self, method):
                return getattr(self, method)(dep)

    def _check_4_depreciation_line(
        self, date_dep, dep, asset, amount=None, depreciation_nr=None, final=False
    ):
        """Run sequential tests on single line for amount, asset_id, date, number"""
        if amount:
            self.assertEqual(
                float_round(dep.amount, 2),
                float_round(amount, 2),
                "Invalid depreciation amount!",
            )
        self.assertEqual(dep.asset_id, asset, "Invalid asset id!")
        self.assertEqual(dep.date, date_dep, "Invalid date!")
        if depreciation_nr:
            self.assertEqual(
                dep.depreciation_nr, depreciation_nr, "Invalid depreciation number!"
            )
        self.assertEqual(dep.final, final, "Invalid final flag!")
        self._check_4_move(dep)

    def _test_all_depreciation_lines(
        self,
        date_dep,
        asset,
        amount=None,
        depreciation_nr=None,
        final=False,
        no_test_ctr=None,
    ):
        """Run tests for all depreciation type values + count for moves"""
        ctr = 0
        for dep in self._get_depreciation_lines(asset=asset, date_from=date_dep):
            self._check_4_depreciation_line(
                date_dep,
                dep,
                asset,
                amount=amount,
                depreciation_nr=depreciation_nr,
                final=final,
            )
            ctr += 1
        if not no_test_ctr:
            self.assertEqual(
                ctr, len(asset.depreciation_ids), "Missed depreciation move!"
            )

    def _initial_test_depreciation(self):
        """Run 1.st year test on all assets"""
        date_dep = TESTBED_VALUES["date.eoy"]
        self._run_wizard_4_depreciation(date_dep=date_dep)
        nr = 0
        for xref in ("z0bug.asset_1", "z0bug.asset_3"):
            asset = self.resource_browse(xref)
            nr += 1
            self.assertEqual(
                asset.state,
                "partially_depreciated",
                "Asset is not in 'partially_depreciated' state!",
            )
            for dep in self._get_depreciation_lines(asset=asset, date_from=date_dep):
                self.assertEqual(
                    float_round(dep.amount, 2),
                    float_round(self.get_test_value(xref,
                                                    "initial_depreciation_amount"),
                                2),
                    "Invalid depreciation amount!",
                )
        self.env["asset.depreciation.line"].search([]).unlink()

    def _test_depreciation_all_assets_y2(self, final):
        """Run 1.st year test on all assets"""
        date_dep = TESTBED_VALUES["date.eoy[-2]"]
        self._run_wizard_4_depreciation(date_dep=date_dep, final=final)
        for xref in (
                "z0bug.asset_1", "z0bug.asset_2", "z0bug.asset_3", "z0bug.asset_4"):
            asset = self.resource_browse(xref)
            if not final:
                self.assertEqual(
                    asset.state,
                    "partially_depreciated",
                    "Asset is not in 'partially_depreciated' state!",
                )
            self._test_all_depreciation_lines(
                date_dep,
                asset,
                amount=self.get_test_value(xref, "depreciation_amount[-2]"),
                depreciation_nr=1,
                final=final,
            )
            for dep in asset.depreciation_ids:
                self.assertEqual(
                    float_round(dep.amount_depreciated, 2),
                    float_round(self.get_test_value(xref, "depreciated_amount[-2]"), 2),
                    "Invalid depreciated amount!",
                )
                self.assertEqual(
                    float_round(dep.amount_residual, 2),
                    float_round(self.get_test_value(xref, "residual_amount[-2]"), 2),
                    "Invalid depreciated amount!",
                )

    def _test_depreciation_all_assets_y1(self, final):
        """Run 2.nd year test on all assets"""
        date_dep = TESTBED_VALUES["date.eoy[-1]"]
        self._run_wizard_4_depreciation(date_dep=date_dep, final=final)
        for xref in (
                "z0bug.asset_1", "z0bug.asset_2", "z0bug.asset_3", "z0bug.asset_4"):
            asset = self.resource_browse(xref)
            self._test_all_depreciation_lines(
                date_dep,
                asset,
                amount=self.get_test_value(xref, "depreciation_amount[-1]"),
                depreciation_nr=3 if xref in ("z0bug.asset_3", "z0bug.asset_4") else 2,
                final=final,
            )
            for dep in asset.depreciation_ids:
                self.assertEqual(
                    float_round(dep.amount_depreciated, 2),
                    float_round(self.get_test_value(xref, "depreciated_amount[-1]"), 2),
                    "Invalid depreciated amount!",
                )

    def _run_wizard_4_depreciation(
        self, date_dep=None, asset=None, final=False, windows_break=None
    ):
        date_dep = date_dep or TESTBED_VALUES["date.eoy[-2]"]
        if asset:
            vals = {"asset_ids": [(6, 0, [asset.id])]}
        else:
            vals = {}
        web_changes = [("date_dep", datetime.strftime(date_dep, "%Y-%m-%d"))]
        if final:
            web_changes.append(("final", final))
        act_windows = self.wizard(
            "assets_management",
            "action_wizard_asset_generate_depreciation",
            default=vals,
            button_name="do_warning",
            web_changes=web_changes,
            ctx={} if final else {"reload_window": True},
        )
        if final:
            self.assertEqual(act_windows["res_model"],
                             "asset.generate.warning",
                             "Invalid response for 'Final depreciations'")
            act_windows = self.wizard(
                act_windows=act_windows,
                button_name="do_generate",
                ctx={},
            )
        else:
            self.assertTrue(self.is_action(act_windows))
        return act_windows

    def _down_asset3(self):
        date_dep = TESTBED_VALUES["asset3.date_down[-1]"]
        down_value = TESTBED_VALUES["asset_3.down_value[-1]"]
        dep_line_model = self.env["asset.depreciation.line"]
        xref = "z0bug.asset_3"
        asset = self.resource_browse(xref)
        for dep in asset.depreciation_ids:
            vals = {
                "amount": down_value,
                "asset_id": asset.id,
                "depreciation_line_type_id": self.env.ref(
                    "assets_management.adpl_type_sva"
                ).id,
                "date": date_dep.strftime("%Y-%m-%d"),
                "depreciation_id": dep.id,
                "move_type": "out",
                "type_id": dep.type_id.id,
                "name": "Asset loss",
            }
            dep_line_model.with_context(depreciated_by_line=True).create(vals)
            self.assertEqual(
                float_round(dep.amount_depreciable_updated, 2),
                float_round(TESTBED_VALUES["asset_3.purchase_amount_post[-1]"], 2),
                "Invalid asset updated value!",
            )
        self._test_all_depreciation_lines(
            date_dep,
            asset,
            amount=self.get_test_value(xref, "depreciation_amount_pre[-1]"),
            depreciation_nr=2,
        )

    def run_dismis_asset_4(self):
        # date_dep = TESTBED_VALUES["asset4.date_disposal[-1]"]
        # sale_value = TESTBED_VALUES["asset_4.sale_amount[-1]"]
        # dep_line_model = self.env["asset.depreciation.line"]
        xref_asset = "z0bug.asset_4"
        # asset = self.resource_browse(xref_asset)
        xref_invoice = "z0bug.sale_invoice_4"
        invoice = self.resource_browse(xref_invoice)
        invoice.action_invoice_open()
        xref_line = "z0bug.sale_invoice_4_1"
        act_windows = self.resource_edit(
            invoice, actions="open_wizard_manage_asset")
        self.assertTrue(self.is_action(act_windows))
        self.wizard(
            act_windows=act_windows,
            records=invoice,
            web_changes=[
                ("management_type", "partial_dismiss"),
                (
                    "partial_dismiss_percentage",
                    TESTBED_VALUES["asset_4.partial_dismis_percentage[-1]"],
                ),
                ("asset_id", xref_asset),
                ("invoice_line_ids", xref_line),
            ],
            button_name="link_asset",
            button_ctx={"show_asset": 0},
        )

    def run_buy_asset(self, xref_invoice, xref_line, xref_asset):
        invoice = self.resource_browse(xref_invoice)
        act_windows = self.resource_edit(
            invoice, actions="open_wizard_manage_asset")
        self.assertTrue(self.is_action(act_windows))
        self.wizard(
            act_windows=act_windows,
            records=invoice,
            web_changes=[
                ("management_type", "update"),
                ("asset_id", xref_asset),
                ("invoice_line_ids", xref_line),
            ],
            button_name="link_asset",
            button_ctx={"show_asset": 0},
        )
        asset = self.resource_browse(xref_asset)
        inv_line = self.resource_browse(xref_line)
        self.assertFalse(asset.customer_id)
        self.assertEqual(asset.supplier_id, invoice.partner_id)
        self.assertEqual(asset.purchase_amount, inv_line.price_subtotal)

    def run_buy_asset_1(self):
        self.run_buy_asset(
            "z0bug.purchase_invoice_2",
            "z0bug.purchase_invoice_2_1",
            "z0bug.asset_1")

    def run_buy_asset_2(self):
        self.run_buy_asset(
            "z0bug.purchase_invoice_1",
            "z0bug.purchase_invoice_1_1",
            "z0bug.asset_2")

    def run_buy_asset_3(self):
        self.run_buy_asset(
            "z0bug.purchase_invoice_2",
            "z0bug.purchase_invoice_2_2",
            "z0bug.asset_3")

    def run_buy_asset_4(self):
        self.run_buy_asset(
            "z0bug.purchase_invoice_1",
            "z0bug.purchase_invoice_1_2",
            "z0bug.asset_4")

    def run_dismis_asset_1(self):
        asset = self.asset_1
        act_window = self.sale_invoice.open_wizard_manage_asset()
        act_window = self.envtest_wizard_start(act_window)
        self.envtest_wizard_exec(
            act_window,
            button_name="link_asset",
            button_ctx={"show_asset": 0},
            web_changes=[
                ("management_type", "dismiss"),
                ("invoice_ids", [(6, 0, [self.sale_invoice.id])]),
                ("asset_id", self.asset_1.id),
            ],
        )
        year = date.today().year
        dismis_date = TESTBED_VALUES["asset_1_2.date.disposal"]
        rate = self._day_rate(date(year, 1, 1), dismis_date, is_leap=isleap(year))
        depreciation_amount = float_round(
            TESTBED_VALUES["asset_1.depreciation_amount"] * rate, 2
        )
        depreciated_amount = float_round(
            TESTBED_VALUES["asset_1.amount_depreciated[-1]"] + depreciation_amount, 2
        )
        self._test_all_depreciation_lines(
            dismis_date, asset, amount=depreciation_amount, depreciation_nr=3
        )
        for dep in self._get_depreciation_lines(
            asset=asset,
            move_type="out",
            date_from=dismis_date,
            date_to=dismis_date,
        ):
            down_value = float_round(
                TESTBED_VALUES["asset_1.purchase_amount"] - depreciated_amount, 2
            )
            self.assertEqual(
                float_round(dep.amount, 2), down_value, "Invalid dismiss amount!"
            )
            self._check_4_move(dep)
        for dep in self._get_depreciation_lines(
            asset=asset,
            move_type="gain",
            date_from=dismis_date,
            date_to=dismis_date,
        ):
            down_value = float_round(
                TESTBED_VALUES["asset_1.sale_amount"]
                - (TESTBED_VALUES["asset_1.purchase_amount"] - depreciated_amount),
                2,
            )
            self.assertEqual(
                float_round(dep.amount, 2), down_value, "Invalid gain amount!"
            )
            self._check_4_move(dep)

    def _test_asset_1(self):
        # Basic test #1
        #
        # We test 3 years depreciations of 1000.0€ asset #1:
        # Test (setup)   : Test (A1)          | Test (A2)         | Test (A3)
        # (year-2)-10-01 : (year-2)-12-31     | (year-1)-12-31    | Today
        # start -> 1000€ : depr.50% -> 125.0€ | depr.100% -> 250€ | depr -> 0..250.0€
        #
        asset = self.asset_1
        #
        # (A1) Year #1: Generate 50% depreciation -> 1000.00€ * 25% * 50% = 125.0€
        # Depreciation for year-2 is run before starting this test
        #
        #
        # (A2) Year #2: Depreciation amount is 250€ (1000€ * 25%)
        # Depreciation for year-1 is run before starting this test
        #
        # (A3) Year #3: Current depreciation amount depends on today
        date_dep = date.today()
        year = date_dep.year
        rate = self._day_rate(date(year, 1, 1), date_dep, is_leap=isleap(year))
        self._run_wizard_4_depreciation(date_dep=date_dep, asset=asset)
        depreciation_amount = float_round(
            TESTBED_VALUES["asset_1.depreciation_amount"] * rate, 2
        )
        depreciated_amount = float_round(
            TESTBED_VALUES["asset_1.amount_depreciated[-1]"] + depreciation_amount, 2
        )
        self._test_all_depreciation_lines(
            date_dep,
            asset,
            amount=depreciation_amount,
            depreciation_nr=3,
            final=False,
        )
        for dep in asset.depreciation_ids:
            self.assertEqual(
                float_round(dep.amount_depreciated, 2),
                depreciated_amount,
                "Invalid depreciated amount!",
            )
        #
        # (A3.b) Year #3: Repeat depreciation and prior data will be removed
        date_dep = TESTBED_VALUES["date.eoy"]
        self._run_wizard_4_depreciation(date_dep=date_dep, asset=asset)
        depreciation_amount = TESTBED_VALUES["asset_1.depreciation_amount"]
        depreciated_amount = float_round(
            TESTBED_VALUES["asset_1.amount_depreciated[-1]"] + depreciation_amount, 2
        )
        self._test_all_depreciation_lines(
            date_dep,
            asset,
            amount=depreciation_amount,
            depreciation_nr=3,
            final=False,
        )
        for dep in asset.depreciation_ids:
            self.assertEqual(
                float_round(dep.amount_depreciated, 2),
                depreciated_amount,
                "Invalid depreciated amount!",
            )
        #
        # (A3.c) Year #3: Repeat depreciation
        # One day depreciation -> 1000.00€ * 25% * / 365 = 0,68€
        date_dep = date(year, 1, 1)
        rate = self._day_rate(date(year, 1, 1), date_dep, is_leap=isleap(year))
        self._run_wizard_4_depreciation(date_dep=date_dep, asset=asset)
        depreciation_amount_1day = float_round(
            TESTBED_VALUES["asset_1.depreciation_amount"] * rate, 2
        )
        depreciated_amount = float_round(
            TESTBED_VALUES["asset_1.amount_depreciated[-1]"] + depreciation_amount_1day,
            2,
        )
        self._test_all_depreciation_lines(
            date_dep,
            asset,
            amount=depreciation_amount_1day,
            depreciation_nr=3,
            final=False,
        )
        for dep in asset.depreciation_ids:
            self.assertEqual(
                float_round(dep.amount_depreciated, 2),
                depreciated_amount,
                "Invalid depreciated amount!",
            )
        #
        # (A4) Special test: cannot generate depreciation on (year-2)
        date_dep = TESTBED_VALUES["date.eoy[-2]"]
        with self.assertRaises(ValidationError):
            self._run_wizard_4_depreciation(date_dep=date_dep, asset=asset)
        #
        # (A9) Dismiss
        self.set_sale_invoice_asset_1()
        self.run_dismis_asset_1()

    def _test_asset_2(self):
        # Basic test #2
        #
        # We test 3 years depreciations of 2500.0€ asset #2:
        # Test (setup)   : Test (B1)         | Test (B2)         | Test (B3)
        # (year-2)-10-01 : (year-2)-12-31    | (year-1)-12-31    | Today
        # start -> 2500€ : 92/365 -> 150.82€ | depr.100% -> 600€ | depr -> 0..600.0€
        #
        asset = self.asset_2
        #
        # (B1) Year #1:
        #         Generate 92 days depreciation -> 2500.00€ * 24% * 92 / 365 = 151.23€
        # If year-2 is leap depreciation value is 150.82€
        # Depreciation for year-2 is run before starting this test
        #
        # (B2) Year #2: Depreciation amount is 600€ (2500€ * 24%)
        # Depreciation for year-1 is run before starting this test
        #
        # (B3) Year #3: Current depreciation amount depends on today: value is <= 600€
        date_dep = date.today()
        year = date_dep.year
        rate = self._day_rate(date(year, 1, 1), date_dep, is_leap=isleap(year))
        self._run_wizard_4_depreciation(date_dep=date_dep, asset=asset)
        depreciation_amount = float_round(
            TESTBED_VALUES["asset_2.depreciation_amount"] * rate, 2
        )
        depreciated_amount = float_round(
            TESTBED_VALUES["asset_2.amount_depreciated[-1]"] + depreciation_amount, 2
        )
        self._test_all_depreciation_lines(
            date_dep,
            asset,
            amount=depreciation_amount,
            depreciation_nr=3,
            final=False,
        )
        for dep in asset.depreciation_ids:
            self.assertEqual(
                float_round(dep.amount_depreciated, 2),
                depreciated_amount,
                "Invalid depreciated amount!",
            )
        #
        # (B9) Dismiss
        self.set_sale_invoice_asset_2()
        self.run_dismis_asset_2()
        #
        # In order to run dismission tests on asset #2 we used the same sale invoice
        # We set invoice state to cancel and this action unlinked asset #1 from invoice
        # So now we have to relink line #2 of invoice to asset #1
        # (A9.b) Check for deleted out & ganin lines
        dismis_date = TESTBED_VALUES["asset_1_2.date.disposal"]
        self.assertFalse(
            self._get_depreciation_lines(
                asset=self.asset_1,
                move_type="out",
                date_from=dismis_date,
                date_to=dismis_date,
            ),
            "Found out undelede out moves",
        )
        self.assertFalse(
            self._get_depreciation_lines(
                asset=self.asset_1,
                move_type="gain",
                date_from=dismis_date,
                date_to=dismis_date,
            ),
            "Found out undelede out moves",
        )
        self.run_dismis_asset_1()

    def _test_asset_3(self):
        # Out + Dismiss tests asset #3 (that is #1 copy)
        #
        # Current depreciable amount is 1000.0€ * 25% = 250.0€
        # Prior test (A1) | Test (C3) 90-91 days : Test (C2)      : (C4) 275 days
        # (year-2)-03-31  | (year-1)-03-31       : (year-1)-03-31 : (year-1)-12-31
        #                 | Depr.ble = 250.0€    : Depr.ble amt 275.0€ * 25% = 68.75€
        # depr. 125.0€    | depr -> 61.64€       : 'out' -> -725€ : depr -> 51.80€
        #
        # (C2) Asset #1, year #2: depreciation moves removed, then value will be reduced
        asset = self.asset_3
        #
        # (C1) Year #1: Generate 50% depreciation -> 1000.00€ * 25% * 50% = 125.0€
        # Depreciation for year-2 is run before starting this test
        #
        #
        # (C2) Year #2: we have to repeat test for thi year
        #
        year = date.today().year - 1
        date_dep = date(year, 3, 31)
        self._remove_depreciation_lines(asset=asset, date_from=date(year, 1, 1))
        down_value = TESTBED_VALUES["asset_3.down_value"]
        dep_line_model = self.env["asset.depreciation.line"]
        for dep in asset.depreciation_ids:
            vals = {
                "amount": down_value,
                "asset_id": asset.id,
                "depreciation_line_type_id": self.env.ref(
                    "assets_management.adpl_type_sva"
                ).id,
                "date": date_dep.strftime("%Y-%m-%d"),
                "depreciation_id": dep.id,
                "move_type": "out",
                "type_id": dep.type_id.id,
                "name": "Asset loss",
            }
            dep_line_model.with_context(depreciated_by_line=True).create(vals)
            self.assertEqual(
                float_round(dep.amount_depreciable_updated, 2),
                float_round(TESTBED_VALUES["asset_1.purchase_amount"] - down_value, 2),
                "Invalid asset updated value!",
            )
        # (C3) Now check for depreciation amount, 90 or 91 days (leap year)
        rate = self._day_rate(date(year, 1, 1), date_dep, is_leap=isleap(year))
        depreciation_amount = float_round(
            TESTBED_VALUES["asset_1.depreciation_amount"] * rate, 2
        )
        depreciated_amount = float_round(
            TESTBED_VALUES["asset_1.depreciation_amount[-2]"] + depreciation_amount, 2
        )
        self._test_all_depreciation_lines(
            date_dep,
            asset,
            amount=depreciation_amount,
            depreciation_nr=2,
            final=False,
        )
        for dep in asset.depreciation_ids:
            self.assertEqual(
                float_round(dep.amount_depreciated, 2),
                depreciated_amount,
                "Invalid depreciated amount!",
            )
        for dep in self._get_depreciation_lines(
            asset=asset,
            move_type="out",
            date_from=date_dep,
            date_to=date_dep,
        ):
            self.assertEqual(
                float_round(dep.amount, 2), down_value, "Invalid out amount!"
            )
            self._check_4_move(dep)
        #
        # (C4) Now we do an end of year depreciation
        date_dep = TESTBED_VALUES["date.eoy[-1]"]
        self._run_wizard_4_depreciation(date_dep=date_dep)
        rate = self._day_rate(date(year, 4, 1), date_dep, is_leap=isleap(year))
        depreciation_amount = float_round(
            TESTBED_VALUES["asset_3.depreciation_amount[-1]"] * rate, 2
        )
        depreciated_amount = float_round(depreciated_amount + depreciation_amount, 2)
        self._test_all_depreciation_lines(
            date_dep,
            asset,
            amount=depreciation_amount,
            depreciation_nr=3,
            final=False,
        )
        for dep in asset.depreciation_ids:
            self.assertEqual(
                float_round(dep.amount_depreciated, 2),
                depreciated_amount,
                "Invalid depreciated amount!",
            )
        return

        dep_residual = 0.0
        wiz = None
        #
        # Dismis Asset #1 price 150.0€
        # Current depreciable amount is 275.0€ * 25% = 68.75€
        # Prior test (C4) | Test (C5) 31 days : Test (C6)        : (C7)
        # (year-1)-12-31  | (year-1)-01-31    : (year-1)-01-31   : (year-1)-01-31
        # Residual 36.56€ | depr -> 5.84€     : 'out' -> -30.72€ : gain -> 119.28€
        #
        dismis_date = TESTBED_VALUES["asset_1_2.date.disposal"]
        rate = self._day_rate(date(year, 1, 1), dismis_date, is_leap=isleap(year))
        depreciation_amount = float_round(
            TESTBED_VALUES["asset_1.depreciation_amount"]
            * rate
            * (TESTBED_VALUES["cat_1.percentage"] / 100),
            2,
        )
        vals = {
            "amount": 150.0,
            "asset_id": asset.id,
            "date": dismis_date.strftime("%Y-%m-%d"),
        }
        self.env["asset.depreciation"].generate_dismiss_line(vals)
        # (C5) Dismiss asset on 2022-01-31, depreciation amount, 31 days
        # 68.75€ * 31 / 365 * 25% = 5.84€ or 68.75€ * 31 / 366 * 25% = 5.82€
        self._test_all_depreciation_lines(
            dismis_date,
            asset,
            amount=depreciation_amount,
            depreciation_nr=4,
            no_test_ctr=True,
        )
        self.assertEqual(
            asset.state, "totally_depreciated", "Asset is not in non depreciated state!"
        )
        # (C6)
        dep_amount = float_round(dep_residual - depreciation_amount, 2)
        for dep in self._get_depreciation_lines(
            asset=asset, date_from=dismis_date, move_type="out"
        ):
            self._check_4_depreciation_line(wiz, dep, asset, amount=dep_amount)
        # (C7)
        dep_amount = float_round(150.0 - depreciation_amount, 2)
        for dep in self._get_depreciation_lines(
            asset=asset, date_from=dismis_date, move_type="gain"
        ):
            self._check_4_depreciation_line(wiz, dep, asset, amount=dep_amount)

    def _test_asset_4(self):
        # Partial Dismiss tests asset #4 (that is #2 copy)
        #
        # Current depreciable amount is 2500.0€ * 24% = 600.0€
        # We test 3 years depreciations of 2500.0€
        # Residual 2.500€ (initial) - 150.82€ (1.depr) - 600€ (2.nd depr) = 1749.18€
        # Prior test (B2)     | Test (D3): dismis 20% for 500€
        # (year-1)-12-31      | (year)-07-31
        # depr.100% -> 600€   | Depr.amt 600€ * 24% * 212 / 365 = 348.49€
        # Residual = 1749.18€ | Residual = 1749.18€ - 348.49€ = 1400.69€
        # Rate 20% fo dismis -> 1400.69€ * 20% = 280.14€
        # Sale price: 500€ -> Gain 500€ - 280.14€ = 219.86€
        asset = self.asset_4
        self.set_sale_invoice_asset_4()
        act_window = self.sale_invoice4.open_wizard_manage_asset()
        act_window = self.envtest_wizard_start(act_window)
        self.envtest_wizard_exec(
            act_window,
            button_name="link_asset",
            button_ctx={"show_asset": 0},
            web_changes=[
                ("invoice_ids", [(6, 0, [self.sale_invoice4.id])]),
                (
                    "invoice_line_ids",
                    [(6, 0, [x.id for x in self.sale_invoice4.invoice_line_ids])],
                ),
                ("asset_id", self.asset_4.id),
                ("management_type", "partial_dismiss"),
                (
                    "partial_dismiss_percentage",
                    TESTBED_VALUES["asset_4.disposal_percentage"],
                ),
            ],
        )
        year = date.today().year
        dismis_date = TESTBED_VALUES["asset_4.date.disposal"]
        rate = self._day_rate(date(year, 1, 1), dismis_date, is_leap=isleap(year))
        depreciation_amount = float_round(
            TESTBED_VALUES["asset_2.depreciation_amount"] * rate, 2
        )
        depreciated_amount = float_round(
            TESTBED_VALUES["asset_2.amount_depreciated[-1]"] + depreciation_amount, 2
        )
        # (D3)
        self._test_all_depreciation_lines(
            dismis_date, asset, amount=depreciation_amount, depreciation_nr=3
        )
        for dep in self._get_depreciation_lines(
            asset=asset,
            move_type="out",
            date_from=dismis_date,
            date_to=dismis_date,
        ):
            down_value = float_round(
                (TESTBED_VALUES["asset_2.purchase_amount"] - depreciated_amount)
                * TESTBED_VALUES["asset_4.disposal_percentage"]
                / 100,
                2,
            )
            self.assertEqual(
                float_round(dep.amount, 2), down_value, "Invalid dismiss amount!"
            )
            self._check_4_move(dep)
        for dep in self._get_depreciation_lines(
            asset=asset,
            move_type="gain",
            date_from=dismis_date,
            date_to=dismis_date,
        ):
            down_value = float_round(
                TESTBED_VALUES["asset_4.sale_amount"]
                - (TESTBED_VALUES["asset_2.purchase_amount"] - depreciated_amount)
                * TESTBED_VALUES["asset_4.disposal_percentage"]
                / 100,
                2,
            )
            self.assertEqual(
                float_round(dep.amount, 2), down_value, "Invalid gain amount!"
            )
            self._check_4_move(dep)

    def _test_asset_8(self):
        # Wizard tests
        #
        # Delete all records
        self._remove_depreciation_lines()
        self._test_depreciation_all_assets_y2(True)

        # Now we search for last invoice recorded
        invs = self.env["account.invoice"].search(
            [("type", "=", "out_invoice")], order="number"
        )
        invoice = invs[0]
        invoice.journal_id.update_posted = True  # Assure invoice cancel
        invoice.action_invoice_cancel()
        invoice.action_invoice_draft()
        for line in invoice.invoice_line_ids:
            line.account_id = self.asset_1.category_id.asset_account_id.id
            break
        year = date.today().year - 1
        invoice.date_invoice = date(year, 12, 31)
        invoice.action_invoice_open()
        act_window = invoice.open_wizard_manage_asset()
        act_window = self.envtest_wizard_start(act_window)
        self.envtest_wizard_exec(
            act_window,
            button_name="link_asset",
            button_ctx={"show_asset": 0},
            web_changes=[
                ("management_type", "dismiss"),
                ("invoice_ids", [(6, 0, [invoice.id])]),
                ("asset_id", self.asset_1.id),
            ],
        )

    def _test_asset_9(self):
        # Special final tests
        #
        # Check for journal unlink is impossible when journal use in asset
        with self.assertRaises(UserError):
            self.journal.unlink()
        self.assertEqual(
            self.journal.id,
            self.env.ref("assets_management.asset_account_journal").id,
            "Invalid asset journal",
        )

    def _validate_invoices(self):
        self.resource_browse("z0bug.purchase_invoice_1").action_invoice_open()
        self.resource_browse("z0bug.purchase_invoice_2").action_invoice_open()
        self.resource_browse("z0bug.sale_invoice_1").action_invoice_open()
        for xref in (
                "z0bug.purchase_invoice_1", "z0bug.purchase_invoice_2",
                "z0bug.sale_invoice_1"):
            self.assertEqual(
                self.resource_browse(xref).state,
                "open",
            )

    def _prevalidate_assets(self):
        for xref in (
                "z0bug.asset_1", "z0bug.asset_2", "z0bug.asset_3", "z0bug.asset_4"):
            asset = self.resource_browse(xref)
            self.assertEqual(asset.state, "non_depreciated")
            self.assertFalse(asset.supplier_id)
            self.assertFalse(asset.customer_id)
            self.assertEqual(asset.purchase_amount,
                             self.get_test_value(xref, "initial_amount"))

    def test_asset(self):
        _logger.info(
            "🎺 Testing test_asset"
        )
        self._prevalidate_assets()
        self._initial_test_depreciation()
        self._validate_invoices()

        self.run_buy_asset_1()
        self.run_buy_asset_2()
        self.run_buy_asset_3()
        self.run_buy_asset_4()

        self._test_depreciation_all_assets_y2(final=False)
        self._test_depreciation_all_assets_y2(final=True)
        self._down_asset3()
        self.run_dismis_asset_4()
        self._test_depreciation_all_assets_y1(False)
        # self._test_asset_1()
        # self._test_asset_2()
        # self._test_asset_3()
        # self._test_asset_4()
        # self._test_asset_8()
        # self._test_asset_9()
