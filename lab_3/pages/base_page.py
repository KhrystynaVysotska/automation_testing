import helpers as HL
from selenium.webdriver.common.by import By

class BasePage:
    BASE_URL = "http://demo-store.seleniumacademy.com"
    
    ACCOUNT_MENU = (By.CSS_SELECTOR, f"a[href='{BASE_URL}/customer/account/']")

    LOGIN_OPTION = (By.CSS_SELECTOR, "a[title='Log In']")
    LOGOUT_OPTION = (By.CSS_SELECTOR, "a[title='Log Out']")
    REGISTER_OPTION = (By.CSS_SELECTOR, "a[title='Register']")

    def __init__(self, browser):
        self.browser = browser

    def select_option(self, option_locator):
        HL.click_button(self.ACCOUNT_MENU, self.browser)
        HL.click_button(option_locator, self.browser)