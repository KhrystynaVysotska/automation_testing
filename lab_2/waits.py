from selenium import webdriver
from math import sin, log
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Відкрити сторінку http://suninjuly.github.io/explicit_wait2.html 
driver.get("http://suninjuly.github.io/explicit_wait2.html")

# Дочекатись, коли ціна зменшиться до $100
text_found = WebDriverWait(driver, timeout=15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

if text_found:
    # Натиснути кнопку "Book" 
    book_button = driver.find_element(By.ID, "book")
    book_button.click()

    # Розв’язати математичну капчу та відправити розв’язок
    x_element = driver.find_element(By.ID, "input_value")
    x = int(x_element.text)

    y = log(abs(12 * sin(x)))

    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']") 
    submit.click()

driver.quit()