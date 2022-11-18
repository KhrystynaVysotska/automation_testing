import unittest
import common.helpers as HL
import common.messages as MSG
from common.browser import Browser
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage

class CartPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser().get()

        self.base_page = BasePage(self.browser)
        self.cart_page = CartPage(self.browser)
        self.product_page = ProductPage(self.browser)

        self.first_product_url = "http://demo-store.seleniumacademy.com/elizabeth-knit-top-593.html"
        self.second_product_url = "http://demo-store.seleniumacademy.com/lafayette-convertible-dress.html"

    def tearDown(self):
        self.browser.quit()

    def test_add_to_cart_should_fail_when_product_color_not_selected(self):
        self.browser.get(self.first_product_url)
        HL.click_button(ProductPage.SIZE_M, self.browser)
        HL.click_button(ProductPage.ADD_TO_CART_BUTTON, self.browser)

        actual_error_message = HL.get_error_message_for('attribute92', self.browser)
        self.assertEqual(actual_error_message, MSG.REQUIRED_FIELD_ERROR)

    def test_add_to_cart_should_fail_when_product_size_not_selected(self):
        self.browser.get(self.first_product_url)
        HL.click_button(ProductPage.COLOR_BLUE, self.browser)
        HL.click_button(ProductPage.ADD_TO_CART_BUTTON, self.browser)

        actual_error_message = HL.get_error_message_for('attribute180', self.browser)
        self.assertEqual(actual_error_message, MSG.REQUIRED_FIELD_ERROR)

    def test_add_to_cart_should_suceed_when_all_required_fields_selected(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)

        self.assertEqual(self.browser.current_url, CartPage.CART_PAGE_URL)

        actual_success_message = self.cart_page.search_success_message()
        expected_success_message = f"Elizabeth Knit Top was added to your shopping cart."
        self.assertEqual(actual_success_message, expected_success_message)

    def test_add_to_cart_should_fail_when_requested_product_quantity_is_not_available(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M, "1000")
        
        actual_error_message = self.product_page.search_error_message()
        expected_error_message = 'The requested quantity for "Elizabeth Knit Top" is not available.'

        self.assertEqual(actual_error_message, expected_error_message)

    def test_cart_page_should_succeed_when_proper_page_title_if_cart_empty(self):
        self.cart_page.open()

        page_title = self.base_page.search_page_title()

        self.assertEqual(page_title, "SHOPPING CART IS EMPTY")
        
    def test_cart_page_should_succeed_when_product_info_is_displayed_properly(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)
        
        expected_product_info = {
            "name": "ELIZABETH KNIT TOP",
            "sku": "wbk012c-Royal Blue-M",
            "color": "Royal Blue",
            "size": "M",
            "price": "$210.00",
            "qty": "1",
            "subtotal": "$210.00"
        }

        actual_product_info = self.cart_page.search_product_info()
        self.assertEqual(actual_product_info, expected_product_info)

    def test_cart_page_should_succeed_when_product_quantity_can_be_edited(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)
        
        actual_product_qty = self.cart_page.search_product_info()["qty"]
        self.assertEqual(actual_product_qty, "1")

        self.cart_page.edit_quantity("3")
        self.cart_page.click_update_quantity_button()

        actual_product_qty = self.cart_page.search_product_info()["qty"]
        self.assertEqual(actual_product_qty, "3")
    
    def test_cart_page_should_succeed_when_product_can_be_removed(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)
        
        actual_page_title = self.base_page.search_page_title()
        self.assertEqual(actual_page_title, "SHOPPING CART")

        actual_product_name = self.cart_page.search_product_info()["name"]
        self.assertEqual(actual_product_name, "ELIZABETH KNIT TOP")

        HL.click_button(CartPage.REMOVE_PRODUCT_BUTTON, self.browser)

        actual_page_title = self.base_page.search_page_title()
        self.assertEqual(actual_page_title, "SHOPPING CART IS EMPTY")

    def test_cart_page_should_succeed_when_cart_can_be_cleared(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)

        self.cart_page.click_empty_cart_button()

        actual_page_title = self.base_page.search_page_title()
        self.assertEqual(actual_page_title, "SHOPPING CART IS EMPTY")

    def test_cart_page_should_succeed_when_can_be_updated(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)
        
        actual_product_qty = self.cart_page.search_product_info()["qty"]
        self.assertEqual(actual_product_qty, "1")

        self.cart_page.edit_quantity("3")
        self.cart_page.click_update_cart_button()

        actual_product_qty = self.cart_page.search_product_info()["qty"]
        self.assertEqual(actual_product_qty, "3")

    def test_cart_page_should_succeed_when_continue_shopping_button_leads_to_previous_page(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)
        self.product_page.add_to_cart(self.second_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_8)

        self.cart_page.click_continue_shopping_button()

        self.assertEqual(self.browser.current_url, self.second_product_url)

    def test_cart_page_should_succeed_when_grand_total_price_displayed(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)
        self.product_page.add_to_cart(self.second_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_8)

        actual_tax_price = self.cart_page.search_tax_price()
        actual_subtotal_price = self.cart_page.search_subtotal_price()
        actual_grand_total_price = self.cart_page.search_grand_total_price()

        self.assertEqual(actual_tax_price, "$45.38")
        self.assertEqual(actual_subtotal_price, "$550.00")
        self.assertEqual(actual_grand_total_price, "$595.38")

    def test_cart_page_should_succeed_when_able_to_navigate_to_checkout(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)
        self.product_page.add_to_cart(self.second_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_8)

        self.cart_page.to_checkout()

        expected_current_url = f"{BasePage.BASE_URL}/checkout/onepage/"
        self.assertEqual(self.browser.current_url, expected_current_url)