import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenarios, given, when, then

scenarios('../Tests/features/Login.feature')

@pytest.fixture
def driver():
   browser = webdriver.Chrome()
   yield browser
   browser.quit()

@given('the user is on the login page')
def navigate_to_login(driver):
   driver.get("https://bstackdemo.com/signin")

@when('the user enters valid credentials')
def enter_credentials(driver):
   #select username
   driver.find_element(by=By.ID, value="username").click()
   driver.find_element(by=By.CSS_SELECTOR,value="#react-select-2-option-0-0").click()
   #select password
   driver.find_element(by=By.ID,value="password").click()
   driver.find_element(by=By.CSS_SELECTOR, value="#react-select-3-option-0-0").click()
   #click submit
   driver.find_element(By.ID,"login-btn").click()

@then('the user should be logged in')
def verify_login(driver):
   assert driver.title=="StackDemo"