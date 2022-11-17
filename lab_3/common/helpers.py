from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

def get_element(locator, driver):
    try:
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located(locator))
        return driver.find_element(*locator)
    except NoSuchElementException:
        return None

def get_elements(locator, driver):
    try:
        WebDriverWait(driver, timeout=5).until(EC.presence_of_all_elements_located(locator))
        return driver.find_elements(*locator)
    except TimeoutException:
        return []

def hover_element(locator, driver):
    actions = ActionChains(driver)
    element = driver.find_element(*locator)
    actions.move_to_element(element).perform()

def click_enter(locator, driver):
    element = driver.find_element(*locator)
    element.send_keys(Keys.ENTER)

def is_clickable(locator, driver):
    try:
        WebDriverWait(driver, timeout=2).until(EC.element_to_be_clickable(locator))
        return True
    except TimeoutException:
        return False