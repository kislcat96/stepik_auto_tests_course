import math
from selenium import webdriver
import time 


link = "http://suninjuly.github.io/find_link_text"

def new_func(browser):
    link = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    return link

try:
    browser = webdriver.Chrome(executable_path=r'C:/Users/kislc/selenium_course/driver/chromedriver')
    browser.get(link)
    link = new_func(browser)
    link.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()