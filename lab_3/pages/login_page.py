import common.helpers as HL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

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

    def open(self) -> None:
        self.browser.get(self.BASE_URL)
        self.select_option(self.LOGIN_OPTION)

    def search_email_to_restore_input(self) -> WebElement:
        return HL.get_element(self.EMAIL_TO_RESTORE_INPUT, self.browser)

    def search_failed_login_message(self) -> str:
        return HL.get_element(self.FAILED_LOGIN_MSG, self.browser).text

    def search_success_message(self) -> str:
        return HL.get_element(self.SUCCESS_MSG, self.browser).text

    def search_welcome_message(self) -> str:
        return HL.get_element(self.WELCOME_MSG, self.browser).text

    def fill_form(self, profile) -> None:
        HL.insert_input(self.EMAIL_INPUT, profile["email"], self.browser)
        HL.insert_input(self.PASSWORD_INPUT, profile["password"], self.browser)

    def click_login_button(self) -> None:
        HL.click_button(self.LOGIN_BUTTON, self.browser)
    
    def click_forgot_password_button(self) -> None:
        HL.click_button(self.FORGOT_PASSWORD_LINK, self.browser)
    
    def click_submit_email_to_restore_button(self) -> None:
        HL.click_button(self.SUBMIT_EMAIL_TO_RESTORE_BUTTON, self.browser)
    
    def click_create_account_button(self) -> None:
        HL.click_button(self.CREATE_ACCOUNT_BUTTON, self.browser)