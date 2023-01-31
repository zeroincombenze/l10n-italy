# -*- coding: utf-8 -*-
import os
from datetime import datetime
from time import sleep
import logging
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)


# Record data for base models
TEST_ACCOUNT_ACCOUNT = {
    "external.1601": {
        "code": "1601",
        "reconcile": False,
        "user_type_id": "account.data_account_type_current_assets",
        "name": "IVA n/credito",
    },
    "external.2601": {
        "code": "2601",
        "reconcile": False,
        "user_type_id": "account.data_account_type_current_liabilities",
        "name": "IVA n/debito",
    },
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
TEST_PRODUCT_TEMPLATE = {
    "z0bug.product_template_1": {
        "property_account_income_id": "external.3112",
        "name": "Prodotto Alpha",
        "weight": 0.1,
        "type": "consu",
        "standard_price": 0.42,
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
        "city": "S. Secondo Pinerolo",
        "zip": "10060",
        "country_id": "base.it",
        "supplier": False,
        "email": "agrolait2@libero.it",
        "vat": "IT02345670018",
        "website": "http://www.agrolait2.it/",
        # "lang": "it_IT",
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
        "city": "Määnz",
        "zip": "55113",
        "country_id": "base.de",
        "supplier": False,
        "vat": "DE812526315",
        "lang": "en_US",
        "customer": True,
        "name": "Axilor GmbH",
        "is_company": True,
    },
}
TEST_STOCK_DDT_TYPE = {
    "l10n_it_ddt.ddt_type_ddt": {
        "default_transportation_reason_id": "l10n_it_ddt.transportation_reason_VEN"
    }
}
TEST_SETUP_LIST = [
    "account.account",
    "account.tax",
    "delivery.carrier",
    "product.template",
    "stock.ddt.type",
    "res.partner",
]


# Record data for child models
TEST_SALE_ORDER_LINE = {
    "z0bug.sale_order_Z0_2_1": {
        "sequence": 1,
        "product_id": "z0bug.product_product_1",
        "weight": 9.9,
        "order_id": "z0bug.sale_order_Z0_2",
        "price_unit": 0.42,
        "product_uom_qty": 100,
        "product_uom": "product.product_uom_unit",
        "tax_id": "external.22v",
        "name": "Prodotto Alpha",
    },
    "z0bug.sale_order_Z0_2_2": {
        "sequence": 2,
        "product_id": "z0bug.product_product_2",
        "weight": 2,
        "order_id": "z0bug.sale_order_Z0_2",
        "price_unit": 1.69,
        "product_uom_qty": 10,
        "product_uom": "product.product_uom_unit",
        "tax_id": "external.22v",
        "name": "Prodotto Beta",
    },
    "z0bug.sale_order_Z0_4_1": {
        "sequence": 1,
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
        "client_order_ref": "220123",
        "date_order": "####-##-<#",
        "partner_id": "z0bug.res_partner_2",
        "ddt_type_id": "l10n_it_ddt.ddt_type_ddt",
        "carrier_id": "delivery.delivery_carrier",
    },
    # Sale Order without Picking
    "z0bug.sale_order_Z0_4": {
        "origin": "Test4",
        "client_order_ref": "IT/22/004",
        "date_order": "####-##-##",
        "partner_id": "z0bug.res_partner_2",
        "ddt_type_id": "l10n_it_ddt.ddt_type_ddt",
        "carrier_id": "delivery.normal_delivery_carrier",
    },
}

TEST_STOCK_INVENTORY = {
    "z0bug.inventory_1": {
        "date": "####-##-<#",
        "name": "Test Inventory",
        "filter": "none",
        "location_id": "stock.stock_location_stock",
    }
}
TEST_STOCK_INVENTORY_LINE = {
    "z0bug.inventory_1_WW": {
        "inventory_id": "z0bug.inventory_18",
        "location_id": "stock.stock_location_stock",
        "product_id": "z0bug.product_product_18",
        "product_qty": 250.0,
        "product_uom_id": "product.product_uom_unit",
    }
}


class TestDdt(SingleTransactionCase):
    def setUp(self):
        super(TestDdt, self).setUp()
        self.debug_level = 3
        data = {"TEST_SETUP_LIST": TEST_SETUP_LIST}
        for resource in TEST_SETUP_LIST:
            item = "TEST_%s" % resource.upper().replace(".", "_")
            data[item] = globals()[item]
        self.declare_all_data(data)
        data = {
            "TEST_SETUP_LIST": ["sale.order", "sale.order.line"],
            "TEST_SALE_ORDER": TEST_SALE_ORDER,
            "TEST_SALE_ORDER_LINE": TEST_SALE_ORDER_LINE,
        }
        self.declare_all_data(data, group="order")
        self.setup_env()
        self.resource_make("product.template",
                           "delivery.delivery_carrier_product_template",
                           {
                               "property_account_income_id": "external.3112",
                               "taxes_id": "external.22v",
                           })
        self.setup_inventory()

    def tearDown(self):
        super(TestDdt, self).tearDown()
        if os.environ.get("ODOO_COMMIT_TEST", ""):
            # Save test environment, so it is available to use
            self.env.cr.commit()  # pylint: disable=invalid-commit
            _logger.info("✨ Test data committed")

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
        # data = {
        #     "TEST_SETUP_LIST": ["stock.inventory", "stock.inventory.line"],
        #     "TEST_STOCK_INVENTORY": TEST_STOCK_INVENTORY,
        #     "TEST_STOCK_INVENTORY_LINE": TEST_STOCK_INVENTORY_LINE,
        # }
        # self.declare_all_data(data, group="inventory")
        # inventory = self.resource_make(
        #     "stock.inventory", "z0bug.inventory_1", group="inventory")
        inventory.action_done()

    def _create_sale_order(self, xref):
        model = "sale.order"
        _logger.info(
            u"🎺 Testing %s[%s]" % (model, xref)
        )
        order = self.resource_make(model, xref, group="order")
        saved_partner = order.partner_id
        if order.origin == "Test2":
            self.assertEqual(
                order.carrier_id,
                self.env.ref("delivery.delivery_carrier"),
                msg="Invalid order delivery carrier %s!" %
                    order.carrier_id)
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
            # Good description from Carrier Delivery
            self.assertEqual(
                order.goods_description_id,
                self.env.ref("l10n_it_ddt.goods_description_CAR"),
                msg="Invalid order goods description %s!" %
                    order.goods_description_id)
        else:
            self.assertEqual(
                order.carrier_id,
                self.env.ref("delivery.normal_delivery_carrier"),
                msg="Invalid order delivery carrier %s!" %
                    order.carrier_id)
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
            # Good description from Customer
            self.assertEqual(
                order.goods_description_id,
                self.env.ref("l10n_it_ddt.goods_description_SFU"),
                msg="Invalid order goods description %s!" %
                    order.goods_description_id)
        # Now we set the same carrier for both sale orders
        # order.carrier_id = self.env.ref("delivery.normal_delivery_carrier").id
        # order.action_confirm()
        self.resource_edit(
            order,
            web_changes=[
                ("partner_id", self.resource_bind("z0bug.res_partner_13").id),
                ("partner_id", saved_partner.id),
                ("carrier_id", self.env.ref("delivery.normal_delivery_carrier").id),
            ],
            actions="action_confirm"
        )
        self.assertEqual(
            order.state, "sale",
            msg="Invalid order state %s!" % order.state)
        return order

    def _remove_invoice(self, invoice, ddts, orders):
        invoice.action_invoice_cancel()
        invoice.unlink()
        sleep(0.5)
        ddts = ddts if isinstance(ddts, (list, tuple)) else [ddts]
        for ddt in ddts:
            self.assertFalse(
                ddt.invoice_id,
                msg="DdT still set to invoiced!")
            self.assertFalse(
                ddt.invoice_ids,
                msg="DdT still set to invoiced!")
        for order in orders:
            self.assertEqual(
                order.invoice_status, "to invoice",
                msg="Sale order %s still set to invoiced!" % order.name)

    def _remove_ddt(self, ddts, orders):
        ddts = ddts if isinstance(ddts, (list, tuple)) else [ddts]
        ddt_ids = []
        for ddt in ddts:
            ddt.set_draft()
            ddt.action_cancel()
            ddt_ids.append(ddt.id)
        for order in orders:
            order.action_cancel()
        sleep(0.5)
        self.assertFalse(
            self.env["stock.picking.package.preparation"].search(
                [("id", "in", ddt_ids)]))
        for order in orders:
            self.assertFalse(
                order.ddt_ids,
                msg="Delivery Note still linked to Sale Order %s!" % order.name)
            order.action_draft()
            order.action_confirm()

    def _set_ddt_done(self, ddts):
        ddts = ddts if isinstance(ddts, (list, tuple)) else [ddts]
        for ddt in ddts:
            ddt.set_done()
            self.assertEqual(
                ddt.state, "done",
                msg="Invalid DdT state %s!" % ddt.state)
            for picking in ddt.picking_ids:
                self.assertEqual(
                    picking.state, "done",
                    msg="Invalid picking state %s!" % picking.state)

    def _create_ddt_from_1_order(self, order, goods_description=None):
        _logger.info(
            u"🎺 Creating DdT from order %s" % (order.name)
        )
        # ## act_windows = self.resource_edit(
        # ##     resource=[order],
        # ##     actions="l10n_it_ddt.action_create_ddt",
        # ## )
        # ## self.wizard(
        # ##     act_windows=act_windows,
        # ##     records=order,
        # ##     button_name="create_ddt",
        # ## )
        order.action_create_ddt()
        self.assertTrue(
            order.ddt_ids,
            msg="No Delivery Note found!")
        ddt = order.ddt_ids[0]
        self.assertEqual(
            ddt.state, "draft",
            msg="Invalid DdT state %s!" % ddt.state)
        self.assertEqual(
            order.picking_ids, ddt.picking_ids,
            msg="Order picking different from DdT picking")
        # Goods description from Sale Order
        goods_description = goods_description or self.env.ref(
            "l10n_it_ddt.goods_description_CAR")
        self.assertEqual(
            ddt.goods_description_id,
            goods_description,
            msg="Invalid order goods description %s!" %
                ddt.goods_description_id)
        self.assertEqual(
            order.carrier_id, ddt.carrier_id,
            msg="Order delivery method different from DdT picking")
        self.assertEqual(
            order.ddt_type_id, ddt.ddt_type_id,
            msg="Order DdT type different from DdT picking")
        self.resource_edit(order, actions="action_view_ddt")
        return ddt

    def _add_picking_to_ddt(self, ddt, order):
        _logger.info(
            u"🎺 Adding picking to DdT"
        )
        picking = order.picking_ids[0]
        picking.add_to_ddt(ddt)
        self.assertEqual(
            len(ddt.picking_ids), 2,
            msg="Ddt %s is not linked to 2 picking!" % ddt.name)

    def _create_ddt_from_more_orders(self, orders, old_ddt_number):
        _logger.info(
            u"🎺 Creating ddt from more orders"
        )
        orders.action_create_ddt()
        for order in orders:
            self.assertTrue(
                order.ddt_ids,
                msg="No Delivery Note found!")
        ddt = orders[0].ddt_ids[0]
        self.assertEqual(
            ddt.transportation_reason_id.id,
            self.env.ref("l10n_it_ddt.transportation_reason_VEN").id,
            msg="Invalid DdT transportation reason %s!" %
                ddt.transportation_reason_id)
        self._set_ddt_done(ddt)
        # Check for DdT number reused
        self.assertEqual(
            ddt.ddt_number, old_ddt_number,
            msg="Invalid DdT number change!")
        return ddt

    def _create_invoice_from_1_ddt(self, ddt, orders):
        invoice_ids = ddt.action_invoice_create()
        self.assertTrue(
            invoice_ids,
            msg="Cannot create invoice!")
        self.assertTrue(
            ddt.invoice_id,
            msg="DdT not set to invoiced!")
        for order in orders:
            self.assertEqual(
                order.invoice_status, "invoiced",
                msg="Sale order %s not set to invoiced!" % order.name)
        # Check for delivery cost line
        invoice = self.env["account.invoice"].browse(invoice_ids[0])
        delivery_line = False
        for line in invoice.invoice_line_ids:
            if line.is_delivery:
                delivery_line = line
                break
        self.assertTrue(
            delivery_line,
            msg="Invoice w/o delivery line!")
        return invoice

    def _create_invoice_from_ddts(self, ddts, orders):
        invoice_ids = ddts.action_invoice_create()
        self.assertTrue(
            invoice_ids,
            msg="Cannot create invoice!")
        for ddt in ddts:
            self.assertTrue(
                ddt.invoice_id,
                msg="DdT not set to invoiced!")
        for order in orders:
            self.assertEqual(
                order.invoice_status, "invoiced",
                msg="Sale order %s not set to invoiced!" % order.name)
        invoice = self.env["account.invoice"].browse(invoice_ids[0])
        return invoice

    def _edit_ddt(self, ddt, actions=None):
        ddt.set_draft()
        saved_partner = ddt.partner_id
        self.resource_edit(
            ddt,
            web_changes=[
                ("partner_id", self.resource_bind("z0bug.res_partner_13").id),
                ("partner_id", saved_partner.id),
            ],
            actions=actions,
        )
        self._set_ddt_done(ddt)

    def _test_1_ddt_then_picking(self, orders, purge=None):
        _logger.info(
            u"🎺 Creating DdT and then add picking to it"
        )
        ddt = old_ddt_number = None
        for order in orders:
            if not ddt:
                ddt = self._create_ddt_from_1_order(order)
            else:
                # Add picking of sale order to DdT
                self._add_picking_to_ddt(ddt, order)
                self._set_ddt_done(ddt)
                old_ddt_number = ddt.ddt_number
        # Create invoice
        invoice = self._create_invoice_from_1_ddt(ddt, orders)
        if purge:
            self._remove_invoice(invoice, ddt, orders)
            self._remove_ddt(ddt, orders)
            invoice = None
        return invoice, old_ddt_number

    def _test_1_ddt_from_2_orders(self, orders, old_ddt_number, purge=None):
        _logger.info(
            u"🎺 Creating DdT from 2 orders"
        )
        ddt = self._create_ddt_from_more_orders(orders, old_ddt_number)
        invoice = self._create_invoice_from_1_ddt(ddt, orders)
        if purge:
            self._remove_invoice(invoice, ddt, orders)
            self._remove_ddt(ddt, orders)
            invoice = None
        return invoice

    def _test_2_ddts_1_invoice(self, orders, purge=None):
        _logger.info(
            u"🎺 Creating invoice from 2 DdTs"
        )
        # Create a new DdT form 2 sale orders
        ddt1 = self._create_ddt_from_1_order(orders[0])
        ddt2 = self._create_ddt_from_1_order(orders[1], goods_description=self.env.ref(
            "l10n_it_ddt.goods_description_SFU"))
        self._edit_ddt(ddt1, actions="delivery_set")
        self._set_ddt_done([ddt1, ddt2])
        ddts = self.env["stock.picking.package.preparation"]
        ddts += ddt1
        ddts += ddt2
        # Create invoice again
        invoice = self._create_invoice_from_ddts(ddts, orders)
        self.assertTrue(
            invoice,
            msg="Cannot create invoice!")
        self.assertTrue(
            ddt1.invoice_id,
            msg="DdT not set to invoiced!")
        self.assertTrue(
            ddt2.invoice_id,
            msg="DdT not set to invoiced!")
        for order in orders:
            self.assertEqual(
                order.invoice_status, "invoiced",
                msg="Sale order %s not set to invoiced!" % order.name)
        # Check for delivery cost line
        delivery_line_1 = delivery_line_2 = False
        for line in invoice.invoice_line_ids:
            if line.is_delivery:
                if not delivery_line_1:
                    delivery_line_1 = line
                elif not delivery_line_2:
                    delivery_line_2 = line
                else:
                    self.assertTrue(
                        False,
                        msg="Too many delivery lines"
                    )
        self.assertTrue(
            delivery_line_1,
            msg="Invoice w/o delivery line!")
        self.assertTrue(
            delivery_line_2,
            msg="Invoice w/o delivery line!")
        if purge:
            self._remove_invoice(invoice, [ddt1, ddt2], orders)
            self._remove_ddt([ddt1, ddt2], orders)
            invoice = None
        return invoice

    def _test_wizard_1_ddt_from_2_orders(self, orders, purge=None):
        _logger.info(
            u"🎺 Wizard: creating DdT from 2 orders"
        )
        act_windows = self.wizard(
            module="l10n_it_ddt",
            action_name="action_create_ddt",
            ctx={
                'active_ids': [x.id for x in orders],
            },
            button_name="create_ddt",
        )
        self.assertTrue("domain" in act_windows)
        ddts = self.env["stock.picking.package.preparation"].search(
            act_windows["domain"])
        ddt_ids = [x.id for x in ddts]
        self._set_ddt_done(ddts)
        act_windows = self.wizard(
            module="l10n_it_ddt",
            action_name="action_ddt_create_invoice",
            ctx={
                "active_ids": ddt_ids,
            },
            button_name="create_invoice",
        )
        self.assertTrue("domain" in act_windows)
        invoice = self.env["account.invoice"].search(act_windows["domain"])[0]
        if purge:
            self._remove_invoice(invoice, ddts, orders)
            self._remove_ddt(ddts, orders)

    def _test_wizard_1_ddt_from_pickings(self, orders, purge=None):
        _logger.info(
            u"🎺 Wizard: creating DdT from pickings"
        )
        picking_ids = []
        for order in orders:
            for picking in order.picking_ids:
                picking_ids.append(picking.id)
        act_windows = self.wizard(
            module="l10n_it_ddt",
            action_name="action_ddt_from_pickings",
            ctx={
                'active_ids': picking_ids,
            },
            button_name="create_ddt",
        )
        self.assertTrue("res_id" in act_windows)
        ddt = self.env["stock.picking.package.preparation"].browse(
            act_windows["res_id"])
        self._set_ddt_done(ddt)
        act_windows = self.wizard(
            module="l10n_it_ddt",
            action_name="action_ddt_create_invoice",
            ctx={
                "active_ids": [ddt.id],
            },
            button_name="create_invoice",
        )
        self.assertTrue("domain" in act_windows)
        invoice = self.env["account.invoice"].search(act_windows["domain"])[0]
        if purge:
            self._remove_invoice(invoice, ddt.id, orders)
            self._remove_ddt(ddt.id, orders)

    def test_ddt(self):
        orders = self.env["sale.order"]
        for xref in TEST_SALE_ORDER.keys():
            order = self._create_sale_order(xref)
            orders += order

        invoice, old_ddt_number = self._test_1_ddt_then_picking(orders, purge=True)
        self._test_1_ddt_from_2_orders(orders, old_ddt_number, purge=True)
        self._test_2_ddts_1_invoice(orders, purge=True)
        self._test_wizard_1_ddt_from_2_orders(orders, purge=True)
        self._test_wizard_1_ddt_from_pickings(orders, purge=None)
