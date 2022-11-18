from typing import List
import common.helpers as HL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    REGISTRATION_PAGE_URL = f"{BasePage.BASE_URL}/customer/account/create/"

    FIRST_NAME_INPUT = (By.ID, "firstname")
    MIDDLE_NAME_INPUT = (By.ID, "middlename")
    LAST_NAME_INPUT = (By.ID, "lastname")
    EMAIL_ADDRESS_INPUT = (By.ID, "email_address")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRMATION_INPUT = (By.ID, "confirmation")

    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[title='Register']")

    FAILED_REGISTRATION_MSG = (By.XPATH, "//*[@class='error-msg']//span")
    SUCCESSFUL_REGISTRATION_MSG = (By.XPATH, "//*[@class='success-msg']//span")

    def open(self) -> None:
        self.browser.get(self.BASE_URL)
        self.select_option(self.REGISTER_OPTION)

    def search_failed_registration_message(self) -> str:
        return HL.get_element(self.FAILED_REGISTRATION_MSG, self.browser).text

    def search_failed_registration_messages(self) -> List[str]:
        messages = HL.get_elements(self.FAILED_REGISTRATION_MSG, self.browser)
        return list(map(lambda msg: msg.text, messages))

    def search_sucessful_registration_message(self) -> str:
        return HL.get_element(self.SUCCESSFUL_REGISTRATION_MSG, self.browser).text

    def fill_form(self, profile) -> None:
        HL.insert_input(self.FIRST_NAME_INPUT, profile["firstname"], self.browser)
        HL.insert_input(self.MIDDLE_NAME_INPUT, profile["middlename"], self.browser)
        HL.insert_input(self.LAST_NAME_INPUT, profile["lastname"], self.browser)
        HL.insert_input(self.EMAIL_ADDRESS_INPUT, profile["email"], self.browser)
        HL.insert_input(self.PASSWORD_INPUT, profile["password"], self.browser)
        HL.insert_input(self.CONFIRMATION_INPUT, profile["confirmation"], self.browser)
    
    def click_register_button(self) -> None:
        HL.click_button(self.REGISTER_BUTTON, self.browser)