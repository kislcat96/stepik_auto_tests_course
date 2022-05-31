import pytest
# from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

    def pytest_addoption(parser):
        parser.addoption('--browser_name',
                         action='store',
                         default="chrome",
                         help="Choose browser: chrome or firefox")
        parser.addoption('--user_language',
                         action='store',
                         default=None,
                         help="Choose language: ru, en, ... (etc.)")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': "user_language"})
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", "user_language")

    @pytest.fixture(scope="function")
    def browser(request):
        browser_name = request.config.getoption("browser_name")
        if (browser_name == "chrome"):
            print("\n\nStart chrome browser for test ...")
            browser = webdriver.Chrome(options=options)
        elif (browser_name == "firefox"):
            print("\n\nStart firefox  browser for test ...")
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            print("Browser <browser_name> still is not implemented")
        user_language = request.config.getoption("user_language")

        yield browser
        print("\nQuit browser...")
        browser.quit()
