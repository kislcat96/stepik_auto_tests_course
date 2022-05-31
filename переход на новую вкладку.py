from msilib.schema import CheckBox
from multiprocessing.connection import answer_challenge
from struct import calcsize
from certifi import where
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(
        executable_path=r'C:/Users/kislc/selenium_course/driver/chromedriver')
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    input = browser.find_element_by_class_name(
        "trollface")
    input.click()
    # confirm = browser.switch_to.alert
    # confirm.accept()
    # time.sleep(10)
    # browser.switch_to.window("new_window")
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    first_window = browser.window_handles[0]
    # first_window = browser.window_handles[0]
    # time.sleep(10)
    # confirm = browser.switch_to_alert
    # confirm.accept()
    # first_window = browser.window_handles[0]
    # time.sleep(10)
    # input1 = browser.find_element_by_id("robotsRule")
    # input1.send_keys("Robots rule")
    # option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    # option1.click()
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

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
    button.click()
    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()
