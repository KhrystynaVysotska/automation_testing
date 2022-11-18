import common.helpers as HL
import common.messages as MSG
from common.browser import Browser
from pages.registration_page import RegistrationPage

import unittest
from faker import Faker

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser().get()
        self.registration_page = RegistrationPage(self.browser)

        fake = Faker()

        password = fake.password(10)
        self.profile = {
            "email": fake.email(),
            "password": password,
            "confirmation": password,
            "firstname": fake.first_name(),
            "middlename": fake.first_name(),
            "lastname": fake.last_name()
        }
    
    def tearDown(self):
        self.browser.quit()

    def test_register_should_succeed_when_user_can_navigate_to_register_form(self):
        self.registration_page.open()

        actual_url = self.browser.current_url
        self.assertEqual(actual_url, RegistrationPage.REGISTRATION_PAGE_URL)
    
    def test_register_should_fail_when_first_name_empty(self):
        self.registration_page.open()

        self.profile["firstname"] = ''
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()
        
        actual_error_message = HL.get_error_message_for('firstname', self.browser)
        self.assertEqual(actual_error_message, MSG.REQUIRED_FIELD_ERROR)
    
    def test_register_should_fail_when_last_name_empty(self):
        self.registration_page.open()

        self.profile["lastname"] = ''
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()
        
        actual_error_message = HL.get_error_message_for('lastname', self.browser)
        self.assertEqual(actual_error_message, MSG.REQUIRED_FIELD_ERROR)
    
    def test_register_should_succeed_when_middle_name_empty(self):
        self.registration_page.open()

        self.profile["middlename"] = ''
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()

        actual_message = self.registration_page.search_sucessful_registration_message()
        self.assertEqual(actual_message, MSG.REGISTERED_SUCCESSFULLY_MSG)

    def test_register_should_fail_when_email_empty(self):
        self.registration_page.open()

        self.profile["email"] = ''
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()
        
        actual_error_message = HL.get_error_message_for('email_address', self.browser)
        self.assertEqual(actual_error_message, MSG.REQUIRED_FIELD_ERROR)
    
    def test_register_should_fail_when_invalid_email_format(self):
        self.registration_page.open()

        self.profile["email"] = 'invalid.email.@domain'
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()
        
        actual_error_message = HL.get_error_message_for('email_address', self.browser)
        self.assertEqual(actual_error_message, MSG.INVALID_EMAIL_FORMAT_ERROR)
    
    def test_register_should_fail_when_invalid_email_hostname(self):
        self.registration_page.open()

        self.profile["email"] = 'invalid.email@domain.dom'
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()

        actual_error_messages = self.registration_page.search_failed_registration_messages()
        self.assertEqual(actual_error_messages, MSG.INVALID_EMAIL_DOMAIN_ERRORS)

    def test_register_should_fail_when_password_empty(self):
        self.registration_page.open()

        self.profile["password"] = ''
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()
        
        actual_password_error_message = HL.get_error_message_for('password', self.browser)
        actual_confirmation_error_message = HL.get_error_message_for('confirmation', self.browser)
        
        self.assertEqual(actual_password_error_message, MSG.REQUIRED_FIELD_ERROR)
        self.assertEqual(actual_confirmation_error_message, MSG.PASSWORD_MISMATCH_ERROR)

    def test_register_should_fail_when_confirmation_empty(self):
        self.registration_page.open()

        self.profile["confirmation"] = ''
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()
        
        actual_error_message = HL.get_error_message_for('confirmation', self.browser)
        self.assertEqual(actual_error_message, MSG.REQUIRED_FIELD_ERROR)

    def test_register_should_fail_when_password_and_confirmation_mismatch(self):
        self.registration_page.open()

        self.profile["confirmation"] = f"{self.profile['password']}wrongpassword"
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()
        
        actual_error_message = HL.get_error_message_for('confirmation', self.browser)
        self.assertEqual(actual_error_message, MSG.PASSWORD_MISMATCH_ERROR)

    def test_register_should_fail_when_password_shorter_than_six_symbols(self):
        self.registration_page.open()

        short_password = "short"
        self.profile["password"] = short_password
        self.profile["confirmation"] = short_password
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()
        
        actual_error_message = HL.get_error_message_for('password', self.browser)
        self.assertEqual(actual_error_message, MSG.PASSWORD_TOO_SHORT_ERROR)

    def test_register_should_succeed_when_inputs_correct_and_user_not_exists(self):
        self.registration_page.open()

        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()

        actual_message = self.registration_page.search_sucessful_registration_message()
        self.assertEqual(actual_message, MSG.REGISTERED_SUCCESSFULLY_MSG)

    def test_register_should_fail_when_inputs_correct_but_user_already_exists(self):
        self.registration_page.open()
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()

        self.registration_page.select_option(self.registration_page.LOGOUT_OPTION)

        self.registration_page.open()
        self.registration_page.fill_form(self.profile)
        self.registration_page.click_register_button()
        
        actual_error_message = self.registration_page.search_failed_registration_message()
        self.assertEqual(actual_error_message, MSG.USER_ALREADY_EXISTS_ERROR)