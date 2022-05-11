from msilib.schema import CheckBox
from multiprocessing.connection import answer_challenge
from operator import truediv
from pickle import TRUE
from struct import calcsize
from certifi import where
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(
        executable_path=r'C:/Users/kislc/selenium_course/driver/chromedriver')
    browser.get("http://suninjuly.github.io/execute_script.html")
    # browser.execute_script("alert('Robots at work');")

    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView();", button)
    # button.click()
    input1 = browser.find_element_by_id("robotsRule")
    input1.send_keys("Robots rule")
    option1 = browser.find_element_by_id("robotCheckbox")
    print({'НИКИТА ЛЯЛЯЫ': option1})
    option1.click()


finally:
    import math

    def calck(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print({'НИКИТА': x})
    y = calck(x)
    print({'НАСТЯ': y})
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    print({'button': button})
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 150);")
    button.click()

    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()
