import time

from pytest_bdd import scenario, given, when, then
from selenium import webdriver


@scenario('../features/example.feature', 'Example Scenario')
def test():
    pass


@given("I exist", target_fixture="browser")
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    return browser


@then("I run")
def step_impl(browser):
    browser.get('https://github.com')
    time.sleep(5)
    browser.quit()
