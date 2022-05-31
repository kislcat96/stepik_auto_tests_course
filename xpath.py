from selenium import webdriver
import time
import random
try:
    browser = webdriver.Chrome(executable_path=r'C:/Users/kislc/selenium_course/driver/chromedriver')
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_css_selector( 'input[type="text"]')
    for element in elements:
        element.send_keys ("Настя")
    elementByXpath = browser.find_element_by_xpath ("/html/body/div/form/div[6]/button[3]")
    elementByXpath.click()
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла