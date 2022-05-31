from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    browser.get(link)
    input = browser.find_element_by_css_selector("button.btn")
    input.click()
    confirm = browser.switch_to.alert
    confirm.accept()


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
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
