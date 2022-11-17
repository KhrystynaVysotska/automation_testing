from math import sin, log

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Відкрити сторінку http://suninjuly.github.io/math.html
driver.get("http://suninjuly.github.io/math.html")

# Прочитати значення змінної х
x_element = driver.find_element(By.ID, "input_value")
x = int(x_element.text)

print(f"x = {x}")

# Обчислити математичну функцию від x: f(x) = ln(abs(12*sin(x))). Використовувати модуль math
y = log(abs(12 * sin(x)))

# Ввести відповідь в текстове поле
answer_input = driver.find_element(By.ID, "answer")
answer_input.send_keys(y)

# Вибрати checkbox "I'm the robot"
robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
robot_checkbox.click()

# Вибрати radiobutton "Robots rule!"
robots_radio = driver.find_element(By.ID, "robotsRule")
robots_radio.click()

# Натиснути кнопку Submit
submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']") 
submit.click()

driver.quit()