from distutils import filelist
import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(
        executable_path=r'C:/Users/kislc/selenium_course/driver/chromedriver')
    browser.get(link)
    import os
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test1.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    elements = browser.find_elements_by_css_selector('input[type="text"]')
    for element in elements:
        element.send_keys("Настя")
    # input1 = browser.find_element_by_tag_name("firstname")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element_by_name("lastname")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element_by_class_name("form-control")
    # input3.send_keys("petrov@mail.ru")
    input = browser.find_element_by_id("file")
    input.send_keys()

    with open('test1.txt', 'w') as file:
        path = os.getcwd() + '/' + file.name
    file.write('test1 for mls 228')

finally:

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
