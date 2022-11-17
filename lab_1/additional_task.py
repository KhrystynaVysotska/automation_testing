from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://demo-store.seleniumacademy.com/customer/account/create/")

fake = Faker()
email = fake.email()
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()

# Написати скрипт реєстрації на сторінці селекторами, за XPath-селекторами

first_name_input = driver.find_element(By.XPATH, "//*[@id='firstname']")
first_name_input.send_keys(first_name)

last_name_input = driver.find_element(By.XPATH, "//*[@id='lastname']")
last_name_input.send_keys(last_name)

email_input = driver.find_element(By.XPATH, "//*[@id='email_address']")
email_input.send_keys(email)

password_input = driver.find_element(By.XPATH, "//*[@id='password']")
password_input.send_keys(password)

confirmation_input = driver.find_element(By.XPATH, "//*[@id='confirmation']")
confirmation_input.send_keys(password)

register_button = driver.find_element(By.XPATH, "//*[@id='form-validate']/div[2]/button")
register_button.click()

driver.quit()