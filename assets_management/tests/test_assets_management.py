# Copyright 2021-24 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
# The tests of this module are based on two cases; all data are in the excel file
# in "test/Test Workflow.xlsx" with follow work-flow:
#
# PLEASE: take care testbed values are based on current year0 -> 2024
# Set # of day for year in Intro of "test/Test Workflow.xlsx" and update below
# TESTBED_VALUES
#
# 1. New assets creation (4 items, #1 #2 #3 and #4) with temporary value 1/10
# 2. Depreciation for 1.st year: fixed rate (#1 #3) or pro-rata-temporis (#2 #4)
# 3. Link assets with purchase invoice: asset values updated
# 4. Depreciation for 1.st year: fixed rate (#1 #3) or pro-rata-temporis (#2 #4)
# 5. For asset #3 down value
# 6. Depreciation for 2.nd year (#1 #2 #4 full year, #3 base on down value)
# 7. Full (asset #1) and partial (asset #2) disposal
#
from datetime import datetime, date
import logging

from odoo.tools.float_utils import float_round
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)


#################################
#      Test values to check     #
#################################
TESTBED_VALUES = {
    "date.eoy[-3]": date(date.today().year - 3, 12, 31),
    "date.eoy[-2]": date(date.today().year - 2, 12, 31),
    "date.eoy[-1]": date(date.today().year - 1, 12, 31),
    "date.eoy[0]": date(date.today().year, 12, 31),
    "date.eoy[0.1]": date(date.today().year, 1, 31),
    "date.eoy[0.2]": date(date.today().year, 1, 15),
    # If leap year set (year - 2)-03-30
    "asset3.date_down[-2]": date(date.today().year - 2, 3, 31),
    # If leap year set (year - 2)-07-30
    "asset4.date_disposal[-2]": date(date.today().year - 2, 7, 31),
    # Disposal rate 20%
    "asset_4.partial_dismis_percentage[-2]": 20,

    "asset_1.initial_amount": 100.0,
    "asset_1.purchase_amount": 1000,
    "asset_1.initial_depreciation_amount": 17.5,
    "asset_1.depreciation_amount[-3]": 175,
    "asset_1.depreciated_amount[-3]": 175,
    "asset_1.residual_amount[-3]": 825,
    "asset_1.depreciation_amount[-2]": 350,
    "asset_1.depreciated_amount[-2]": 525,
    "asset_1.residual_amount[-2]": 475,
    "asset_1.depreciation_amount[-1]": 350,
    "asset_1.depreciated_amount[-1]": 875,
    "asset_1.residual_amount[-1]": 125,
    "asset_1.depreciation_amount[0.1]": 29.64,
    "asset_1.depreciated_amount[0.1]": 904.64,
    "asset_1.residual_amount[0.1]": 95.36,
    "asset_1.depreciation_amount[0.2]": 14.34,
    "asset_1.depreciated_amount[0.2]": 889.34,
    "asset_1.residual_amount[0.2]": 110.66,
    "asset_1.sale_amount[0.2]": 400.00,
    "asset_1.sold_value[0.2]": 110.66,
    "asset_1.gain[0.2]": 289.34,

    "asset_2.initial_amount": 250,
    "asset_2.purchase_amount": 2500,
    "asset_2.initial_depreciation_amount": 15.1,
    "asset_2.depreciation_amount[-3]": 151.23,
    "asset_2.depreciated_amount[-3]": 151.23,
    "asset_2.residual_amount[-3]": 2348.77,
    "asset_2.depreciation_amount[-2]": 600,
    "asset_2.depreciated_amount[-2]": 751.23,
    "asset_2.residual_amount[-2]": 1748.77,
    "asset_2.depreciation_amount[-1]": 600,
    "asset_2.depreciated_amount[-1]": 1351.23,
    "asset_2.residual_amount[-1]": 1148.77,
    "asset_2.depreciation_amount[0.1]": 50.82,
    "asset_2.depreciated_amount[0.1]": 1402.05,
    "asset_2.residual_amount[0.1]": 1697.95,
    "asset_2.sale_amount[0]": 1000.00,
    "asset_2.loss[0]": 97.95,


    "asset_3.initial_amount": 100.0,
    "asset_3.purchase_amount": 1000,
    "asset_3.initial_depreciation_amount": 12.5,
    "asset_3.depreciation_amount[-3]": 125,
    "asset_3.depreciated_amount[-3]": 125,
    "asset_3.residual_amount[-3]": 875,
    "asset_3.depreciation_amount_pre[-2]": 61.64,
    "asset_3.depreciated_amount_pre[-2]": 186.64,
    "asset_3.residual_amount_pre[-2]": 813.36,
    "asset_3.down_value[-2]": 725,
    "asset_3.depreciation_amount[-2]": 51.8,
    "asset_3.purchase_amount_post[-2]": 275,
    "asset_3.depreciated_amount[-2]": 238.44,
    "asset_3.residual_amount[-2]": 36.56,
    "asset_3.depreciation_amount[-1]": 36.56,
    "asset_3.depreciated_amount[-1]": 275,
    "asset_3.residual_amount[-1]": 0.0,
    "asset_3.depreciation_amount[0.1]": 0.0,
    "asset_3.depreciated_amount[0.1]": 275,
    "asset_3.residual_amount[0.1]": 0.0,
    "asset_3.sale_amount[0.2]": 250.00,
    "asset_3.sold_value[0.2]": 250.00,
    "asset_3.gain[0.2]": 250.00,

    "asset_4.initial_amount": 250.0,
    "asset_4.purchase_amount": 2500,
    "asset_4.initial_depreciation_amount": 15.1,
    "asset_4.depreciation_amount[-3]": 151.23,
    "asset_4.depreciated_amount[-3]": 151.23,
    "asset_4.residual_amount[-3]": 2348.77,
    "asset_4.depreciation_amount_pre[-2]": 348.49,
    "asset_4.depreciated_amount_pre[-2]": 499.72,
    "asset_4.residual_amount_pre[-2]": 2000.28,
    "asset_4.disposal_rate": 0.2,
    "asset_4.sale_amount[-2]": 525,
    "asset_4.sold_value[-2]": 400.06,
    "asset_4.gain[-2]": 124.94,
    "asset_4.depreciation_amount[-2]": 211.26,
    "asset_4.depreciated_amount[-2]": 710.98,
    "asset_4.residual_amount[-2]": 1888.68,
    "asset_4.depreciation_amount[-1]": 503.99,
    "asset_4.depreciated_amount[-1]": 1214.97,
    "asset_4.residual_amount[-1]": 1384.69,
    "asset_4.depreciation_amount[0.1]": 42.69,
    "asset_4.depreciated_amount[0.1]": 1257.66,
    "asset_4.residual_amount[0.1]": 1342.0,
}


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

    def get_depreciation_lines(
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

    def check_4_move_depreciated(self, dep):
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

    def check_4_move(self, dep):
        if dep.move_id:
            method = "_check_4_move_%s" % dep.move_type
            if hasattr(self, method):
                return getattr(self, method)(dep)

    def check_4_depreciation_line(
        self, date_dep, dep, asset, amount=None, depreciation_nr=None, final=False
    ):
        """Run sequential tests on single line for amount, asset_id, date, number"""
        if amount:
            self.assertEqual(
                float_round(dep.amount, 2),
                float_round(amount, 2),
                "Invalid depreciation amount for asset %s on %s!" % (asset.name,
                                                                     date_dep),
            )
        self.assertEqual(dep.asset_id, asset, "Invalid dep. asset id!")
        self.assertEqual(dep.date, date_dep, "Invalid dep. date %s!" % dep.date)
        if depreciation_nr:
            self.assertEqual(
                dep.depreciation_nr, depreciation_nr, "Invalid depreciation number!"
            )
        self.assertEqual(dep.final, final, "Invalid dep. final flag!")
        self.check_4_move(dep)

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
        for dep in self.get_depreciation_lines(asset=asset, date_from=date_dep):
            self.check_4_depreciation_line(
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
                ctr,
                len(asset.depreciation_ids),
                "Missed depreciation move for asset %s!" % asset.name
            )

    def initial_test_depreciation(self):
        """Run 1.st year test on all assets"""
        date_dep = TESTBED_VALUES["date.eoy[0]"]
        self.run_wizard_4_depreciation(date_dep=date_dep)
        nr = 0
        for xref in ("z0bug.asset_1", "z0bug.asset_3"):
            asset = self.resource_browse(xref)
            nr += 1
            self.assertEqual(
                asset.state,
                "partially_depreciated",
                "Asset %s initial not 'partially_depreciated' state!" % asset.name,
            )
            for dep in self.get_depreciation_lines(asset=asset, date_from=date_dep):
                self.assertEqual(
                    float_round(dep.amount, 2),
                    float_round(self.get_test_value(
                        xref, "initial_depreciation_amount"), 2),
                    "Invalid initial depreciation amount for asset %s!" % asset.name,
                )
        self.env["asset.depreciation.line"].search([]).unlink()

    def _test_depreciation_all_assets_y3(self, final):
        """Run 1.st year test on all assets"""
        date_dep = TESTBED_VALUES["date.eoy[-3]"]
        self.run_wizard_4_depreciation(date_dep=date_dep, final=final)
        for xref in (
                "z0bug.asset_1", "z0bug.asset_2", "z0bug.asset_3", "z0bug.asset_4"):
            asset = self.resource_browse(xref)
            if not final:
                self.assertEqual(
                    asset.state,
                    "partially_depreciated",
                    "Asset %s not 'partially_depreciated' state [-3]!" % asset.name,
                )
            self._test_all_depreciation_lines(
                date_dep,
                asset,
                amount=self.get_test_value(xref, "depreciation_amount[-3]"),
                depreciation_nr=1,
                final=final,
            )
            for dep in asset.depreciation_ids:
                self.assertEqual(
                    float_round(dep.amount_depreciated, 2),
                    float_round(self.get_test_value(xref, "depreciated_amount[-3]"), 2),
                    "Invalid depreciated amount for asset %s [-3]!" % asset.name,
                )
                self.assertEqual(
                    float_round(dep.amount_residual, 2),
                    float_round(self.get_test_value(xref, "residual_amount[-3]"), 2),
                    "Invalid depreciated amount for asset %s [-3]!" % asset.name,
                )

    def _test_depreciation_all_assets_y2(self, final):
        """Run 2.nd year test on all assets"""
        date_dep = TESTBED_VALUES["date.eoy[-2]"]
        self.run_wizard_4_depreciation(date_dep=date_dep, final=final)
        for xref in (
                "z0bug.asset_1", "z0bug.asset_2", "z0bug.asset_3", "z0bug.asset_4"):
            asset = self.resource_browse(xref)
            self._test_all_depreciation_lines(
                date_dep,
                asset,
                amount=self.get_test_value(xref, "depreciation_amount[-2]"),
                depreciation_nr=3 if xref in ("z0bug.asset_3", "z0bug.asset_4") else 2,
                final=final,
            )
            for dep in asset.depreciation_ids:
                self.assertEqual(
                    float_round(dep.amount_depreciated, 2),
                    float_round(self.get_test_value(xref, "depreciated_amount[-2]"), 2),
                    "Invalid depreciated amount for asset %s [-2]!" % asset.name,
                )

    def _test_depreciation_all_assets_y1(self, final):
        """Run 2.nd year test on all assets"""
        date_dep = TESTBED_VALUES["date.eoy[-1]"]
        self.run_wizard_4_depreciation(date_dep=date_dep, final=final)
        for xref in (
                "z0bug.asset_1", "z0bug.asset_2", "z0bug.asset_3", "z0bug.asset_4"):
            asset = self.resource_browse(xref)
            self._test_all_depreciation_lines(
                date_dep,
                asset,
                amount=self.get_test_value(xref, "depreciation_amount[-1]"),
                depreciation_nr=4 if xref in ("z0bug.asset_3", "z0bug.asset_4") else 3,
                final=final,
            )
            for dep in asset.depreciation_ids:
                self.assertEqual(
                    float_round(dep.amount_depreciated, 2),
                    float_round(self.get_test_value(xref, "depreciated_amount[-1]"), 2),
                    "Invalid depreciated amount for asset %s [-1]!" % asset.name,
                )

    def _test_depreciation_all_assets_y0_1(self, final):
        """Run current year (jan, 31th) test on all assets"""
        date_dep = TESTBED_VALUES["date.eoy[0.1]"]
        self.run_wizard_4_depreciation(date_dep=date_dep, final=final)
        # Asset #3 is full depreciated
        for xref in ("z0bug.asset_1", "z0bug.asset_2", "z0bug.asset_4"):
            asset = self.resource_browse(xref)
            self._test_all_depreciation_lines(
                date_dep,
                asset,
                amount=self.get_test_value(xref, "depreciation_amount[0.1]"),
                depreciation_nr=5 if xref in ("z0bug.asset_3", "z0bug.asset_4") else 4,
                final=final,
            )
            for dep in asset.depreciation_ids:
                self.assertEqual(
                    float_round(dep.amount_depreciated, 2),
                    float_round(self.get_test_value(xref,
                                                    "depreciated_amount[0.1]"), 2),
                    "Invalid depreciated amount for asset %s [0.1]!" % asset.name,
                )

    def run_wizard_4_depreciation(
        self, date_dep=None, asset=None, final=False, windows_break=None
    ):
        date_dep = date_dep or TESTBED_VALUES["date.eoy[-3]"]
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
                             "Invalid response for 'Final depreciation'")
            act_windows = self.wizard(
                act_windows=act_windows,
                button_name="do_generate",
                ctx={},
            )
        else:
            self.assertTrue(self.is_action(act_windows))
        return act_windows

    def down_asset3(self):
        date_dep = TESTBED_VALUES["asset3.date_down[-2]"]
        down_value = TESTBED_VALUES["asset_3.down_value[-2]"]
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
                float_round(TESTBED_VALUES["asset_3.purchase_amount_post[-2]"], 2),
                "Invalid asset %s updated value [-2]!" % asset.name,
            )
        self._test_all_depreciation_lines(
            date_dep,
            asset,
            amount=self.get_test_value(xref, "depreciation_amount_pre[-2]"),
            depreciation_nr=2,
        )

    def run_disposal_asset_1_3(self):
        xref_asset = "z0bug.asset_1"
        asset = self.resource_browse(xref_asset)
        xref_invoice = "z0bug.sale_invoice_13"
        invoice = self.resource_browse(xref_invoice)
        act_windows = self.resource_edit(
            invoice, actions="open_wizard_manage_asset")
        self.assertTrue(self.is_action(act_windows))
        xref_line = "z0bug.sale_invoice_13_1"
        self.wizard(
            act_windows=act_windows,
            records=invoice,
            web_changes=[
                ("management_type", "dismiss"),
                ("asset_id", xref_asset),
                ("invoice_line_ids", xref_line),
            ],
            button_name="link_asset",
            button_ctx={"show_asset": 0},
        )

        for dep in self.get_depreciation_lines(asset=asset,
                                               move_type="loss",
                                               date_from=invoice.date):
            self.assertEqual(
                float_round(dep.amount, 2),
                float_round(self.get_test_value(xref_asset, "loss[0.2]"), 2),
                "Invalid loss amount for asset %s!" % asset.name,
            )

        xref_asset = "z0bug.asset_3"
        asset = self.resource_browse(xref_asset)
        act_windows = self.resource_edit(
            invoice, actions="open_wizard_manage_asset")
        self.assertTrue(self.is_action(act_windows))
        xref_line = "z0bug.sale_invoice_13_2"
        self.wizard(
            act_windows=act_windows,
            records=invoice,
            web_changes=[
                ("management_type", "dismiss"),
                ("asset_id", xref_asset),
                ("invoice_line_ids", xref_line),
            ],
            button_name="link_asset",
            button_ctx={"show_asset": 0},
        )

        for dep in self.get_depreciation_lines(asset=asset,
                                               move_type="gain",
                                               date_from=invoice.date):
            self.assertEqual(
                float_round(dep.amount, 2),
                float_round(self.get_test_value(xref_asset, "gain[0.2]"), 2),
                "Invalid gain amount for asset %s!" % asset.name,
            )

    def run_disposal_asset_2(self):
        # date_dep = TESTBED_VALUES["date.eoy[0.1]"]
        xref_asset = "z0bug.asset_2"
        asset = self.resource_browse(xref_asset)
        xref_invoice = "z0bug.sale_invoice_2"
        invoice = self.resource_browse(xref_invoice)
        act_windows = self.resource_edit(
            invoice, actions="open_wizard_manage_asset")
        self.assertTrue(self.is_action(act_windows))
        xref_line = "z0bug.sale_invoice_2_1"
        self.wizard(
            act_windows=act_windows,
            records=invoice,
            web_changes=[
                ("management_type", "dismiss"),
                ("asset_id", xref_asset),
                ("invoice_line_ids", xref_line),
            ],
            button_name="link_asset",
            button_ctx={"show_asset": 0},
        )

        for dep in self.get_depreciation_lines(asset=asset,
                                               move_type="loss",
                                               date_from=invoice.date):
            self.assertEqual(
                float_round(dep.amount, 2),
                float_round(self.get_test_value(xref_asset, "loss[0]"), 2),
                "Invalid loss amount for asset %s!" % asset.name,
            )

    def run_disposal_asset_4(self):
        xref_asset = "z0bug.asset_4"
        asset = self.resource_browse(xref_asset)
        xref_invoice = "z0bug.sale_invoice_4"
        invoice = self.resource_browse(xref_invoice)
        invoice.action_invoice_open()
        act_windows = self.resource_edit(
            invoice, actions="open_wizard_manage_asset")
        self.assertTrue(self.is_action(act_windows))
        xref_line = "z0bug.sale_invoice_4_1"
        self.wizard(
            act_windows=act_windows,
            records=invoice,
            web_changes=[
                ("management_type", "partial_dismiss"),
                (
                    "partial_dismiss_percentage",
                    TESTBED_VALUES["asset_4.partial_dismis_percentage[-2]"],
                ),
                ("asset_id", xref_asset),
                ("invoice_line_ids", xref_line),
            ],
            button_name="link_asset",
            button_ctx={"show_asset": 0},
        )

        for dep in self.get_depreciation_lines(asset=asset,
                                               move_type="gain",
                                               date_from=invoice.date):
            self.assertEqual(
                float_round(dep.amount, 2),
                float_round(self.get_test_value(xref_asset, "gain[-2]"), 2),
                "Invalid gain amount for asset %s!" % asset.name,
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

    def validate_invoices(self):
        self.resource_browse("z0bug.purchase_invoice_1").action_invoice_open()
        self.resource_browse("z0bug.purchase_invoice_2").action_invoice_open()
        for xref in ("z0bug.purchase_invoice_1", "z0bug.purchase_invoice_2"):
            self.assertEqual(
                self.resource_browse(xref).state,
                "open",
            )

    def prevalidate_assets(self):
        for xref in (
                "z0bug.asset_0", "z0bug.asset_1", "z0bug.asset_2", "z0bug.asset_3",
                "z0bug.asset_4"):
            asset = self.resource_browse(xref)
            self.assertEqual(asset.state, "non_depreciated")
            self.assertFalse(asset.supplier_id)
            self.assertFalse(asset.customer_id)
            if xref == "z0bug.asset_0":
                asset.unlink()
            else:
                self.assertEqual(asset.purchase_amount,
                                 self.get_test_value(xref, "initial_amount"),
                                 "Invalid purchase amount for asset %s" % asset.name)

    def print_journal(self):
        date_print = TESTBED_VALUES["date.eoy[-1]"]
        vals = {}
        web_changes = [("date", datetime.strftime(date_print, "%Y-%m-%d"))]
        act_windows = self.wizard(
            "assets_management",
            "action_wizard_asset_journal_report",
            default=vals,
            button_name="button_export_asset_journal_pdf",
            web_changes=web_changes,

        )
        self.assertTrue(isinstance(act_windows, dict))
        self.assertTrue("report_name" in act_windows)

        date_print = TESTBED_VALUES["date.eoy[0]"]
        vals = {}
        web_changes = [("date", datetime.strftime(date_print, "%Y-%m-%d"))]
        act_windows = self.wizard(
            "assets_management",
            "action_wizard_asset_previsional_report",
            default=vals,
            button_name="button_export_asset_previsional_pdf",
            web_changes=web_changes,

        )
        self.assertTrue(isinstance(act_windows, dict))
        self.assertTrue("report_name" in act_windows)

    def test_asset(self):
        _logger.info(
            "🎺 Testing test_asset"
        )
        self.prevalidate_assets()
        self.initial_test_depreciation()
        self.validate_invoices()

        self.run_buy_asset_1()
        self.run_buy_asset_2()
        self.run_buy_asset_3()
        self.run_buy_asset_4()

        self._test_depreciation_all_assets_y3(final=False)
        self._test_depreciation_all_assets_y3(final=True)
        self.down_asset3()
        self.run_disposal_asset_4()
        self._test_depreciation_all_assets_y2(final=False)
        self._test_depreciation_all_assets_y1(final=False)
        self._test_depreciation_all_assets_y0_1(final=False)

        for xref_invoice in "z0bug.sale_invoice_13", "z0bug.sale_invoice_2":
            invoice = self.resource_browse(xref_invoice)
            invoice.action_invoice_open()

        self.run_disposal_asset_2()
        self.run_disposal_asset_1_3()

        self.print_journal()
