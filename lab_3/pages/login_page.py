import helpers as HL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    LOGIN_PAGE_URL = f"{BasePage.BASE_URL}/customer/account/login/"

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "pass")
    EMAIL_TO_RESTORE_INPUT = (By.ID, "email_address")

    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[title='Login']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[title='Create an Account']")
    SUBMIT_EMAIL_TO_RESTORE_BUTTON = (By.CSS_SELECTOR, "button[title='Submit']")

    WELCOME_MSG = (By.XPATH, "//*[@class='welcome-msg']//strong")
    SUCCESS_MSG = (By.XPATH, "//*[@class='success-msg']//span")
    FAILED_LOGIN_MSG = (By.XPATH, "//*[@class='error-msg']//span")

    FORGOT_PASSWORD_LINK = (By.XPATH, "//*[@class='form-list']//a")

    def open(self):
        self.browser.get(self.BASE_URL)
        self.select_option(self.LOGIN_OPTION)

    def search_email_to_restore_input(self):
        return self.browser.find_element(*self.EMAIL_TO_RESTORE_INPUT)

    def search_failed_login_message(self):
        return self.browser.find_element(*self.FAILED_LOGIN_MSG).text

    def search_success_message(self):
        return self.browser.find_element(*self.SUCCESS_MSG).text

    def search_welcome_message(self):
        return self.browser.find_element(*self.WELCOME_MSG).text

    def fill_form(self, profile):
        HL.insert_input(self.EMAIL_INPUT, profile["email"], self.browser)
        HL.insert_input(self.PASSWORD_INPUT, profile["password"], self.browser)