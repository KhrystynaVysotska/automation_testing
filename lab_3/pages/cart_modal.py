import time
from typing import List
import common.helpers as HL
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CartModal:
    CART_ICON = (By.XPATH, '//div[@class="account-cart-wrapper"]/div[@class="header-minicart"]/a')
    CART_ICON_COUNT = (By.XPATH, '//div[@class="account-cart-wrapper"]/div[@class="header-minicart"]//span[@class="count"]')
    
    CART_MODAL_PRODUCT_LIST = (By.ID, "cart-sidebar")
    CART_MODAL_PRODUCT_LIST_ITEM = (By.XPATH, "//ul[@id='cart-sidebar']/li")

    PRODUCT_INFO = {
                        "name": (By.XPATH, "//ul[@id='cart-sidebar']//p[contains(@class, 'product-name')]/a"),
                        "price": (By.XPATH, "//ul[@id='cart-sidebar']//table[contains(@class, 'info-wrapper')]//span[contains(@class, 'price')]"),
                        "qty": (By.XPATH, "//ul[@id='cart-sidebar']//table[contains(@class, 'info-wrapper')]//tr[contains(@class, 'qty-wrapper')]//input")
                    }
    REMOVE_PRODUCT_BUTTON = (By.XPATH, "//ul[@id='cart-sidebar']//div[contains(@class, 'product-details')]/a[@title='Remove This Item']")
    EDIT_PRODUCT_BUTTON = (By.XPATH, "//ul[@id='cart-sidebar']//div[contains(@class, 'product-details')]/a[@title='Edit item']")
    
    PRODUCT_DETAILS_BUTTON = (By.XPATH, "//ul[@id='cart-sidebar']//div[contains(@class, 'product-details')]//a[@class='details']")
    PRODUCT_DETAILS_COLOR = (By.XPATH, "//ul[@id='cart-sidebar']//div[contains(@class, 'product-details')]//dl[@class='item-options']/dt[contains(text(), 'Color')]/following-sibling::dd")
    PRODUCT_DETAILS_SIZE = (By.XPATH, "//ul[@id='cart-sidebar']//div[contains(@class, 'product-details')]//dl[@class='item-options']/dt[contains(text(), 'Size')]/following-sibling::dd")

    CART_SUBTOTAL = (By.XPATH, '//*[@id="header-cart"]//p[@class="subtotal"]/span[@class="price"]')

    ERROR_MESSAGE = (By.ID, "minicart-error-message")
    SUCCESS_MESSAGE = (By.ID, "minicart-success-message")

    EMPTY_CART_MESSAGE = (By.CLASS_NAME, "empty")

    VIEW_SHOPPING_CART_BUTTON = (By.CLASS_NAME, "cart-link")
    CHECKOUT_BUTTON = (By.XPATH, '//*[@id="header-cart"]//a[@title="Checkout"]')

    def __init__(self, browser):
        self.browser = browser
    
    def open(self) -> None:
        HL.click_button(CartModal.CART_ICON, self.browser)
    
    def to_cart_page(self) -> None:
        HL.click_button(CartModal.VIEW_SHOPPING_CART_BUTTON, self.browser)

    def to_checkout(self) -> None:
        HL.click_button(CartModal.CHECKOUT_BUTTON, self.browser)

    def search_products_count(self) -> int:
        count = HL.get_element(CartModal.CART_ICON_COUNT, self.browser).text
        return int(count)

    def search_products(self) -> List[WebElement]:
        return HL.get_elements(CartModal.CART_MODAL_PRODUCT_LIST_ITEM, self.browser)
    
    def search_product_info(self, index = 0) -> dict:
        return {
            "name": HL.get_elements(CartModal.PRODUCT_INFO["name"], self.browser)[index].text,
            "price": HL.get_elements(CartModal.PRODUCT_INFO["price"], self.browser)[index].text,
            "qty": HL.get_elements(CartModal.PRODUCT_INFO["qty"], self.browser)[index].get_attribute("value")
        }

    def search_empty_cart_message(self) -> str:
        element = HL.get_element(CartModal.EMPTY_CART_MESSAGE, self.browser)

        if not element:
            return ''

        return element.text

    def remove_product(self, index=0) -> str:
        remove_product_button = HL.get_elements(CartModal.REMOVE_PRODUCT_BUTTON, self.browser)[index]
        remove_product_button.click()
        
        self.browser.switch_to.alert.accept()

        time.sleep(2)

        success_message = HL.get_element(CartModal.SUCCESS_MESSAGE, self.browser, visible=True)
        error_messsage = HL.get_element(CartModal.ERROR_MESSAGE, self.browser, visible=True)

        if not success_message:
            return error_messsage.text
        
        return success_message.text
    
    def click_edit_product_button(self, index=0) -> None:
        edit_button = HL.get_elements(CartModal.EDIT_PRODUCT_BUTTON, self.browser)[index]
        edit_button.click()
    
    def hover_over_product_details(self, index=0) -> None:
        details_button = HL.get_elements(CartModal.PRODUCT_DETAILS_BUTTON, self.browser)[index]
        HL.hover_element(details_button, self.browser)

    def search_product_details_color(self, index=0) -> str:
        return HL.get_elements(CartModal.PRODUCT_DETAILS_COLOR, self.browser, visible=True)[index].text

    def search_product_details_size(self, index=0) -> str:
        return HL.get_elements(CartModal.PRODUCT_DETAILS_SIZE, self.browser, visible=True)[index].text

    def search_subtotal(self) -> str:
        return HL.get_element(CartModal.CART_SUBTOTAL, self.browser).text
