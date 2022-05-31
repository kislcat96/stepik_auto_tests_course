import imghdr
from msilib.schema import CheckBox
from multiprocessing.connection import answer_challenge
from re import X
from struct import calcsize
from tkinter import Y
from certifi import where
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(
        executable_path=r'C:/Users/kislc/selenium_course/driver/chromedriver')
    browser.get("http://suninjuly.github.io/selects1.html")


finally:
    import math

    def sum(x, y):
        return str(x+y)
    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    print({'НИКИТА': x})
    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)
    print({'НАСТЯ': y})
    input = browser.find_element_by_id("dropdown")
    input.send_keys(sum(x, y))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()
