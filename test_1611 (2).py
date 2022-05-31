from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome(
        "C:/Users/kislc/selenium_course/driver/chromedrive")
    browser.get(link)
    # заполняем обязательные поля
    First_name = browser.find_element(
        By.XPATH, "//input[@placeholder='Input your name' and @required]")
    First_name.click()
    First_name.send_keys("First")
    Email = browser.find_element(
        By.XPATH, "//input[@placeholder='Input your email' and @required]")
    Email.click()
    Email.send_keys("test@test.ru")
    # Нажимаем кнопку "Submit"
    Submit = browser.find_element(By.XPATH, "//button")
    Submit.click()
    # Находим элемент содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # Записываем текст найденного элемента в переменную
    welcome_text = welcome_text_elt.text
    # Проверка ожидаемого текста с тем что получен на странице
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    # browser.quit()
