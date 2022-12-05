# -*- coding: utf-8 -*-
import os
from datetime import datetime
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
TEST_PRODUCT_TEMPLATE = {
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
        # "property_payment_term_id": "z0bug.payment_2",
        "city": "S. Secondo Pinerolo",
        "zip": "10060",
        "country_id": "base.it",
        # "property_account_position_id": "z0bug.fiscalpos_it",
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
        # "property_payment_term_id": "z0bug.payment_5",
        "city": "Määnz",
        "zip": "55113",
        "country_id": "base.de",
        # "property_account_position_id": "z0bug.fiscalpos_eu",
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
        # "payment_term_id": "z0bug.payment_2",
        "client_order_ref": "220123",
        "date_order": "2022-06-25",
        "partner_id": "z0bug.res_partner_2",
        "ddt_type_id": "l10n_it_ddt.ddt_type_ddt",
        "carrier_id": "delivery.delivery_carrier",
    },
    # Sale Order without Picking
    "z0bug.sale_order_Z0_4": {
        "origin": "Test4",
        # "payment_term_id": "z0bug.payment_2",
        "client_order_ref": "IT/22/004",
        "date_order": "2022-06-26",
        "partner_id": "z0bug.res_partner_2",
        "ddt_type_id": "l10n_it_ddt.ddt_type_ddt",
        "carrier_id": "delivery.normal_delivery_carrier",
    },
}

TEST_STOCK_INVENTORY = {
    "z0bug.inventory_1": {
        "date": "####-##-##",
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


class SaleOrder(SingleTransactionCase):
    def setUp(self):
        super(SaleOrder, self).setUp()
        self.debug_level = 2
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
        # self.setup_env(lang="it_IT")  # Create test environment
        self.setup_env()
        self.resource_make("product.template",
                           "delivery.delivery_carrier_product_template",
                           {
                               "property_account_income_id": "external.3112",
                               "taxes_id": "external.22v",
                           })
        self.setup_inventory()

    def tearDown(self):
        super(SaleOrder, self).tearDown()
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
        order.onchange_partner_id()
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
        order.carrier_id = self.env.ref("delivery.normal_delivery_carrier").id
        order.action_confirm()
        self.assertEqual(
            order.state, "sale",
            msg="Invalid order state %s!" % order.state)
        return order

    def _create_ddt_from_1_order(self, order, goods_description=None):
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
        return ddt

    def _add_picking_to_ddt(self, ddt, order):
        picking = order.picking_ids[0]
        picking.add_to_ddt(ddt)
        self.assertEqual(
            len(ddt.picking_ids), 2,
            msg="Ddt %s is not linked to 2 picking!" % ddt.name)
        ddt.set_done()
        self.assertEqual(
            ddt.state, "done",
            msg="Invalid DdT state %s!" % ddt.state)
        for picking in ddt.picking_ids:
            self.assertEqual(
                picking.state, "done",
                msg="Invalid picking state %s!" % picking.state)
        return ddt.ddt_number

    def _create_ddt_from_more_orders(self, orders, old_ddt_number):
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
        ddt.set_done()
        self.assertEqual(
            ddt.state, "done",
            msg="Invalid DdT state %s!" % ddt.state)
        for picking in ddt.picking_ids:
            self.assertEqual(
                picking.state, "done",
                msg="Invalid picking state %s!" % picking.state)
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

    def _remove_invoice(self, invoice, ddt, orders):
        invoice.action_invoice_cancel()
        invoice.unlink()
        self.assertFalse(
            ddt.invoice_id,
            msg="DdT still set to invoiced!")
        for order in orders:
            self.assertEqual(
                order.invoice_status, "to invoice",
                msg="Sale order %s still set to invoiced!" % order.name)

    def _remove_ddt(self, ddt, orders):
        ddt.set_draft()
        ddt.action_cancel()
        ddt.unlink()
        for order in orders:
            self.assertFalse(
                order.ddt_ids,
                msg="Delivery Note still linked to Sale Order %s!" % order.name)

    def _edit_ddt(self, ddt):
        ddt.set_draft()
        saved_partner = ddt.partner_id
        ddt.partner_id = self.resource_bind("z0bug.res_partner_13")
        ddt.on_change_partner()
        ddt.partner_id = saved_partner
        ddt.on_change_partner()
        ddt.set_done()

    def _test_1_ddt_more_picking(self, ddt, orders):
        # Create invoice
        invoice = self._create_invoice_from_1_ddt(ddt, orders)
        # Remove invoice just created
        self._remove_invoice(invoice, ddt, orders)
        #  Now remove DdT
        self._remove_ddt(ddt, orders)

    def _test_1_ddt_from_2_orders(self, orders, old_ddt_number):
        # Create a new DdT form 2 sale orders
        ddt = self._create_ddt_from_more_orders(orders, old_ddt_number)
        # Edit DdT
        self._edit_ddt(ddt)
        # Create invoice again
        invoice = self._create_invoice_from_1_ddt(ddt, orders)
        # Remove invoice again
        self._remove_invoice(invoice, ddt, orders)
        # Now remove DdT again
        self._remove_ddt(ddt, orders)

    def _test_2_ddts_1_invoice(self, orders, old_ddt_number):
        # Create a new DdT form 2 sale orders
        ddt1 = self._create_ddt_from_1_order(orders[0])
        ddt1.set_done()
        ddt2 = self._create_ddt_from_1_order(orders[1], goods_description=self.env.ref(
            "l10n_it_ddt.goods_description_SFU"))
        ddt2.set_done()
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
        return invoice

    def test_ddt(self):
        ddt = old_ddt_number = False
        orders = self.env["sale.order"]
        for xref in TEST_SALE_ORDER.keys():
            order = self._create_sale_order(xref)
            orders += order
            if not ddt:
                # Create a DdT from sale order
                ddt = self._create_ddt_from_1_order(order)
            else:
                # Add picking of sale order to DdT
                old_ddt_number = self._add_picking_to_ddt(ddt, order)

        self._test_1_ddt_more_picking(ddt, orders)
        self._test_1_ddt_from_2_orders(orders, old_ddt_number)
        self._test_2_ddts_1_invoice(orders, old_ddt_number)
