from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import math
import time
import pytest


@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_browser(url):
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    browser.get(url)

    answer = math.log(int(time.time()))
    browser.implicitly_wait(10)

    input = browser.find_element(
        By.CLASS_NAME, "ember-text-area")
    input.send_keys(answer)
    # time.sleep(30)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(15)

# def test_guest_should_see_login_link(self, browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")
#     # этот тест запустится 2 раза
