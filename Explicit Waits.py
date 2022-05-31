from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import math

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
# button.click()
input = browser.find_element(By.ID, "book")
input.click()
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
# first_window = browser.window_handles[0]
# message = browser.find_element(By.ID, "book")
# time.sleep(12)


def calck(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id("input_value")
x = x_element.text
print({'НИКИТА': x})
y = calck(x)
print({'НАСТЯ': y})
input = browser.find_element_by_id("answer")
input.send_keys(y)
button = browser.find_element_by_id("solve")
button.click()
# успеваем скопировать код за 30 секунд
time.sleep(60)
# закрываем браузер после всех манипуляций
browser.quit()
