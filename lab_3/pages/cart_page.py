import common.helpers as HL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage():
    CART_PAGE_URL = f"{BasePage.BASE_URL}/checkout/cart/"

    TABLE_XPATH = "//table[@id='shopping-cart-table']"
    TABLE_BODY_XPATH = f"{TABLE_XPATH}/tbody"

    PRODUCT_CART_IMAGE = (By.XPATH, f"{TABLE_BODY_XPATH}//td[contains(@class, 'product-cart-image')]/a")
    PRODUCT_CART_INFO = {
                            "name": (By.XPATH, f"{TABLE_BODY_XPATH}//h2[contains(@class, 'product-name')]/a"),
                            "sku": (By.XPATH, f"{TABLE_BODY_XPATH}//div[contains(@class, 'product-cart-sku')]"),
                            "color": (By.XPATH, f"{TABLE_BODY_XPATH}//dl[contains(@class, 'item-options')]/dt[contains(text(), 'Color')]/following-sibling::dd"),
                            "size": (By.XPATH, f"{TABLE_BODY_XPATH}//dl[contains(@class, 'item-options')]/dt[contains(text(), 'Size')]/following-sibling::dd"),
                            "price": (By.XPATH, f"{TABLE_BODY_XPATH}//td[contains(@class, 'product-cart-price')]//span[contains(@class, 'price')]"),
                            "qty": (By.XPATH, f"{TABLE_BODY_XPATH}//td[contains(@class, 'product-cart-actions')]/input"),
                            "subtotal": (By.XPATH, f"{TABLE_BODY_XPATH}//td[contains(@class, 'product-cart-total')]//span[contains(@class, 'price')]")
                        }

    TAX_PRICE = (By.XPATH, '//*[@id="shopping-cart-totals-table"]/tbody//td[contains(text(), "Tax")]/following-sibling::td/span[@class="price"]') 
    SUBTOTAL_PRICE = (By.XPATH, '//*[@id="shopping-cart-totals-table"]/tbody//td[contains(text(), "Subtotal")]/following-sibling::td/span[@class="price"]')
    GRAND_TOTAL_PRICE = (By.XPATH, '//*[@id="shopping-cart-totals-table"]/tfoot//span[@class="price"]')

    EMPTY_CART_BUTTON = (By.ID, "empty_cart_button")
    UPDATE_CART_BUTTON = (By.XPATH, '//*[@id="shopping-cart-table"]/tfoot/tr/td/button[3]')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "button[title='Continue Shopping']")

    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[title='Proceed to Checkout']")

    REMOVE_PRODUCT_BUTTON = (By.XPATH, f"{TABLE_BODY_XPATH}//td[contains(@class, 'product-cart-remove')]/a")
    UPDATE_QUANTITY_BUTTON = (By.XPATH, f"{TABLE_BODY_XPATH}//td[contains(@class, 'product-cart-actions')]/button")
    EDIT_QUANTITY_BUTTON = (By.XPATH, f"{TABLE_BODY_XPATH}//td[contains(@class, 'product-cart-actions')]/ul[@class='cart-links']//a[@title='Edit item parameters']")

    SUCCESS_MESSAGE = (By.XPATH, "//li[@class='success-msg']//li")

    def __init__(self, browser):
        self.browser = browser

    def open(self) -> None:
        self.browser.get(self.CART_PAGE_URL)

    def to_checkout(self) -> None:
        HL.click_button(self.PROCEED_TO_CHECKOUT_BUTTON, self.browser)

    def click_continue_shopping_button(self) -> None:
        HL.click_button(self.CONTINUE_SHOPPING_BUTTON, self.browser)
    
    def click_update_cart_button(self) -> None:
        HL.click_button(self.UPDATE_CART_BUTTON, self.browser)

    def click_update_quantity_button(self) -> None:
        HL.click_button(self.UPDATE_QUANTITY_BUTTON, self.browser)

    def click_empty_cart_button(self) -> None:
        HL.click_button(self.EMPTY_CART_BUTTON, self.browser)

    def search_product_info(self, index=0) -> dict:
        return {
            "name": HL.get_elements(self.PRODUCT_CART_INFO["name"], self.browser)[index].text,
            "sku": HL.get_elements(self.PRODUCT_CART_INFO["sku"], self.browser)[index].text.replace("SKU: ", ""),
            "color": HL.get_elements(self.PRODUCT_CART_INFO["color"], self.browser)[index].text,
            "size": HL.get_elements(self.PRODUCT_CART_INFO["size"], self.browser)[index].text,
            "price": HL.get_elements(self.PRODUCT_CART_INFO["price"], self.browser)[index].text,
            "qty": HL.get_elements(self.PRODUCT_CART_INFO["qty"], self.browser)[index].get_attribute("value"),
            "subtotal": HL.get_elements(self.PRODUCT_CART_INFO["subtotal"], self.browser)[index].text
        }
    
    def edit_quantity(self, qty, index=0) -> None:
        qty_input = HL.get_elements(self.PRODUCT_CART_INFO["qty"], self.browser)[index]
        HL.insert_input(qty_input, qty, self.browser)
    
    def search_success_message(self) -> str:
        return HL.get_element(self.SUCCESS_MESSAGE, self.browser).text
    
    def search_tax_price(self) -> str:
        return HL.get_element(self.TAX_PRICE, self.browser).text
    
    def search_subtotal_price(self) -> str:
        return HL.get_element(self.SUBTOTAL_PRICE, self.browser).text
    
    def search_grand_total_price(self) -> str:
        return HL.get_element(self.GRAND_TOTAL_PRICE, self.browser).text