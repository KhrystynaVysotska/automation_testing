import unittest
import helpers as HL
import messages as MSG
from config.browser import Browser
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser().get()
        self.login_page = LoginPage(self.browser)
    
    def tearDown(self):
        self.browser.quit()

    def test_should_succeed_when_user_can_navigate_to_login_form(self):
        self.login_page.open()

        actual_url = self.browser.current_url
        self.assertEqual(actual_url, self.login_page.LOGIN_PAGE_URL)
    
    def test_should_fail_when_email_empty(self):
        self.login_page.open()

        profile = {
            "email": "",
            "password": "123456"
        }

        self.login_page.fill_form(profile)
        HL.click_button(self.login_page.LOGIN_BUTTON, self.browser)

        actual_error_message = HL.get_error_message_for('email', self.browser)
        self.assertEqual(actual_error_message, MSG.REQUIRED_FIELD_ERROR)

    def test_should_fail_when_password_empty(self):
        self.login_page.open()

        profile = {
            "email": "khrystynavysotska@gmail.com",
            "password": ""
        }

        self.login_page.fill_form(profile)
        HL.click_button(self.login_page.LOGIN_BUTTON, self.browser)

        actual_error_message = HL.get_error_message_for('pass', self.browser)        
        self.assertEqual(actual_error_message, MSG.REQUIRED_FIELD_ERROR)

    def test_should_fail_when_password_wrong(self):
        self.login_page.open()

        profile = {
            "email": "khrystynavysotska@gmail.com",
            "password": "wrongpass"
        }

        self.login_page.fill_form(profile)
        HL.click_button(self.login_page.LOGIN_BUTTON, self.browser)

        actual_error_message = self.login_page.search_failed_login_message()        
        self.assertEqual(actual_error_message, MSG.INVALID_CREDENTIALS_ERROR)

    def test_should_fail_when_email_not_exists(self):
        self.login_page.open()

        profile = {
            "email": "notexistingemail@gmail.com",
            "password": "123456"
        }

        self.login_page.fill_form(profile)
        HL.click_button(self.login_page.LOGIN_BUTTON, self.browser)

        actual_error_message = self.login_page.search_failed_login_message()        
        self.assertEqual(actual_error_message, MSG.INVALID_CREDENTIALS_ERROR)

    def test_should_succeed_when_credentials_correct(self):
        self.login_page.open()

        profile = {
            "email": "khrystynavysotska@gmail.com",
            "password": "123456"
        }

        self.login_page.fill_form(profile)
        HL.click_button(self.login_page.LOGIN_BUTTON, self.browser)

        actual_welcome_message = self.login_page.search_welcome_message()
        self.assertEqual(actual_welcome_message, MSG.LOGIN_WELCOME_MSG)
    
    def test_should_succeed_when_password_can_be_restored(self):
        self.login_page.open()

        HL.click_button(self.login_page.FORGOT_PASSWORD_LINK, self.browser)

        email_to_restore = self.login_page.search_email_to_restore_input()
        email_to_restore.send_keys("khrystynavysotska@gmail.com")

        HL.click_button(self.login_page.SUBMIT_EMAIL_TO_RESTORE_BUTTON, self.browser)

        actual_success_message = self.login_page.search_success_message()
        self.assertEqual(actual_success_message, MSG.PASSWORD_RESET_SUCCESS_MSG)

    def test_should_succeed_when_user_can_navigate_to_register_page(self):
        self.login_page.open()

        HL.click_button(self.login_page.CREATE_ACCOUNT_BUTTON, self.browser)

        actual_url = self.browser.current_url
        self.assertEqual(actual_url, RegistrationPage.REGISTRATION_PAGE_URL)