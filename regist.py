from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome(
        executable_path=r'C:/Users/kislc/selenium_course/driver/chromedriver')
    browser.get(link)

    elements = browser.find_element_by_xpath(
        "/html/body/div/form/div[1]/div[1]/input")
    elements.send_keys("Котик")

    elements = browser.find_element_by_xpath(
        "/html/body/div/form/div[1]/div[2]/input")
    elements.send_keys("Котик")

    elements = browser.find_element_by_xpath(
        "/html/body/div/form/div[1]/div[3]/input")
    elements.send_keys("Котик")

    elements = browser.find_element_by_xpath(
        "/html/body/div/form/div[2]/div[1]/input")
    elements.send_keys("Котик")

    elements = browser.find_element_by_xpath(
        "/html/body/div/form/div[2]/div[2]/input")
    elements.send_keys("Котик")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_css_selector("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
