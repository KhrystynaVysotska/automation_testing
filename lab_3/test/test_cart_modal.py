import unittest
from common.browser import Browser
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.cart_modal import CartModal
from pages.product_page import ProductPage

class CartModalTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser().get()

        self.cart_modal = CartModal(self.browser)
        self.cart_page = CartPage(self.browser)
        self.product_page = ProductPage(self.browser)

        self.first_product_url = "http://demo-store.seleniumacademy.com/elizabeth-knit-top-593.html"
        self.second_product_url = "http://demo-store.seleniumacademy.com/lafayette-convertible-dress.html"

    def tearDown(self):
        self.browser.quit()

    def test_cart_modal_should_succeed_when_able_to_navigate_to_cart_page(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)

        self.cart_modal.open()
        self.cart_modal.to_cart_page()

        self.assertEqual(self.browser.current_url, CartPage.CART_PAGE_URL)

    def test_cart_modal_should_succeed_when_products_displayed_properly(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)
        self.product_page.add_to_cart(self.second_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_8)

        self.cart_modal.open()

        products = self.cart_modal.search_products()
        self.assertEqual(len(products), 2)

        expected_first_product_info = {"name": "ELIZABETH KNIT TOP", "price": "$210.00", "qty": "1"}
        expected_second_product_info = {"name": "LAFAYETTE CONVERTIBLE DRESS", "price": "$340.00", "qty": "1"}
        
        actual_first_product_info = self.cart_modal.search_product_info(index=1)
        actual_second_product_info = self.cart_modal.search_product_info(index=0)

        self.assertEqual(actual_first_product_info, expected_first_product_info)
        self.assertEqual(actual_second_product_info, expected_second_product_info)

    def test_cart_modal_should_succeed_when_product_can_be_removed(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)
        self.product_page.add_to_cart(self.second_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_8)

        self.cart_modal.open()

        products = self.cart_modal.search_products()
        self.assertEqual(len(products), 2)
        
        expected_first_product_info = {"name": "ELIZABETH KNIT TOP", "price": "$210.00", "qty": "1"}
        expected_second_product_info = {"name": "LAFAYETTE CONVERTIBLE DRESS", "price": "$340.00", "qty": "1"}
        
        actual_first_product_info = self.cart_modal.search_product_info(index=1)
        actual_second_product_info = self.cart_modal.search_product_info(index=0)

        self.assertEqual(actual_first_product_info, expected_first_product_info)
        self.assertEqual(actual_second_product_info, expected_second_product_info)

        actual_message = self.cart_modal.remove_product()
        self.assertEqual(actual_message, "Item was removed successfully.")

        updated_products = self.cart_modal.search_products()
        self.assertEqual(len(updated_products), 1)

        actual_product_info = self.cart_modal.search_product_info(index=0)
        self.assertEqual(actual_product_info, expected_first_product_info)

        actual_message = self.cart_modal.remove_product()
        self.assertEqual(actual_message, "Item was removed successfully.")

        actual_empty_cart_message = self.cart_modal.search_empty_cart_message()
        self.assertEqual(actual_empty_cart_message, "You have no items in your shopping cart.")

    def test_cart_modal_should_succeed_when_product_count_is_incremented_properly(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M, "5")

        cart_count = self.cart_modal.search_products_count()
        self.assertEqual(cart_count, 5)

        self.product_page.add_to_cart(self.second_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_8, "5")

        cart_count = self.cart_modal.search_products_count()
        self.assertEqual(cart_count, 10)

    def test_cart_modal_should_succeed_when_product_details_visible_on_hover(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)

        self.cart_modal.open()
        self.cart_modal.hover_over_product_details()

        actual_size = self.cart_modal.search_product_details_size()
        actual_color = self.cart_modal.search_product_details_color()

        expected_size = "M"
        expected_color = "Royal Blue"

        self.assertEqual(actual_size, expected_size)
        self.assertEqual(actual_color, expected_color)

    def test_cart_modal_should_succeed_when_product_can_be_edited(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)

        self.cart_modal.open()
        self.cart_modal.click_edit_product_button()

        expected_url_prefix = f"{CartPage.CART_PAGE_URL}configure/id/"
        self.assertTrue(self.browser.current_url.startswith(expected_url_prefix))

        self.product_page.add_to_cart(self.browser.current_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M, "5")
        self.assertEqual(self.browser.current_url, CartPage.CART_PAGE_URL)

        actual_message = self.cart_page.search_success_message()
        expected_message = "Elizabeth Knit Top was updated in your shopping cart."
        self.assertEqual(actual_message, expected_message)

    def test_cart_modal_should_succeed_when_subtotal_price_displayed(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M, "5")
        self.product_page.add_to_cart(self.second_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_8, "5")

        self.cart_modal.open()

        actual_subtotal = self.cart_modal.search_subtotal()

        # 5 * 210 + 5 * 340 = 2750
        self.assertEqual(actual_subtotal, '$2,750.00')

    def test_cart_modal_should_succeed_when_able_to_navigate_to_checkout(self):
        self.product_page.add_to_cart(self.first_product_url, ProductPage.COLOR_BLUE, ProductPage.SIZE_M)

        self.cart_modal.open()
        self.cart_modal.to_checkout()

        expected_current_url = f"{BasePage.BASE_URL}/checkout/onepage/"
        self.assertEqual(self.browser.current_url, expected_current_url)