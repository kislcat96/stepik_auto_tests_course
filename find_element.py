from selenium import webdriver
import time
import random
try:
    browser = webdriver.Chrome(executable_path=r'C:/Users/kislc/selenium_course/driver/chromedriver')
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector( 'input[type="text"]')
    for element in elements:
        element.send_keys ("Настя")
    # input1 = browser.find_element_by_tag_name("input")
    # input1.send_keys("random")
    # input2 = browser.find_element_by_name("last_name")
    # input2.send_keys("random")
    # input3 = browser.find_element_by_class_name("city")
    # input3.send_keys("random")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("random")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла