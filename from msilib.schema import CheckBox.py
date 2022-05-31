import imghdr
from msilib.schema import CheckBox
from multiprocessing.connection import answer_challenge
from struct import calcsize
from certifi import where
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(
        executable_path=r'C:/Users/kislc/selenium_course/driver/chromedriver')
    browser.get("http://suninjuly.github.io/get_attribute.html")

    input1 = browser.find_element_by_id("robotsRule")
    input1.send_keys("Robots rule")
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    import math

    def calck(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    print({'НИКИТА': x})
    y = calck(x)
    print({'НАСТЯ': y})
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()
