from selenium import webdriver
import unittest
import time


import pytest


class TestAbs(unittest.TestCase):

    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"

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
        assert(
            "Congratulations! You have successfully registered!", welcome_text, "Daaaaaaaaa!")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"

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
        assert(
            "Congratulations! You have successfully registered!", welcome_text, "Daaaaaaaaa!")


if __name__ == "__main__":
    unittest.main()
