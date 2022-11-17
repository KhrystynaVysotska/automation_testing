from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def click_button(locator, driver):
    button = driver.find_element(*locator)
    button.click()

def insert_input(locator, value, driver):
    input = driver.find_element(*locator)
    input.send_keys(value)

def get_error_message_for(id, driver):
    error_locator = (By.XPATH, f"//*[@id='{id}']/following-sibling::div")

    try:
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located(error_locator))
        return driver.find_element(*error_locator).text
    except NoSuchElementException:
        return ''