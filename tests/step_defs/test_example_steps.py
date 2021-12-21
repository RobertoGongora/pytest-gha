import time

from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@scenario('../features/example.feature', 'Example Scenario')
def test():
    pass


@given("I exist", target_fixture="browser")
def browser():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(10)
    return browser


@then("I run")
def step_impl(browser):
    browser.get('https://github.com')
    browser.quit()
