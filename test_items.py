from selenium import webdriver
import pytest
import time
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_goods_has_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_basket, 'кнопка добавления товара отсутвует'
