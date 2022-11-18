import common.helpers as HL
from selenium.webdriver.common.by import By

class ProductPage:
    SIZE_S = (By.CLASS_NAME, "option-s")
    SIZE_M = (By.CLASS_NAME, "option-m")
    SIZE_L = (By.CLASS_NAME, "option-l")
    SIZE_XS = (By.CLASS_NAME, "option-xs")
    SIZE_XL = (By.CLASS_NAME, "option-xl")

    SIZE_2 = (By.CLASS_NAME, "option-2")
    SIZE_8 = (By.CLASS_NAME, "option-8")
    SIZE_10 = (By.CLASS_NAME, "option-10")

    COLOR_WHITE = (By.XPATH, "//ul[@id='configurable_swatch_color']/li[contains(@class, 'white')]")
    COLOR_PINK = (By.XPATH, "//ul[@id='configurable_swatch_color']/li[contains(@class, 'pink')]")
    COLOR_RED = (By.XPATH, "//ul[@id='configurable_swatch_color']/li[contains(@class, 'red')]")
    COLOR_BLUE = (By.XPATH, "//ul[@id='configurable_swatch_color']/li[contains(@class, 'blue')]")

    QTY_INPUT = (By.ID, "qty")

    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='add-to-cart-buttons']/button")

    ERROR_MESSAGE = (By.XPATH, "//li[@class='error-msg']//li")

    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self, url, color, size, qty=None):
        self.browser.get(url)

        HL.click_button(color, self.browser)
        HL.click_button(size, self.browser)

        if qty:
            HL.insert_input(ProductPage.QTY_INPUT, qty, self.browser)

        HL.click_button(ProductPage.ADD_TO_CART_BUTTON, self.browser)
    
    def search_error_message(self) -> str:
        element = HL.get_element(ProductPage.ERROR_MESSAGE, self.browser)

        if not element:
            return ''

        return element.text
