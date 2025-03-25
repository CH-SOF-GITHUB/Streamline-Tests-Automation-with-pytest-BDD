import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# constants
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'
# scenarios
scenarios('../features/web.feature')


# Fixtures
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@given("the DuckDuckGo home page is displayed")
def step_impl(driver):
    driver.get(url=DUCKDUCKGO_HOME)


@when(parsers.parse('the user searches for "{phrase}"'))
def step_impl(driver, phrase):
    search_input = driver.find_element(by=By.ID, value="searchbox_input")
    search_input.send_keys(phrase + Keys.RETURN)


@then(parsers.parse('results are show for "{phrase}"'))
def step_impl(driver, phrase):
    Xpath = "//div[@data-testid='result-title-a']"
    results = driver.find_elements(by=By.XPATH, value=Xpath)
    for result in results:
        assert phrase in result.text
