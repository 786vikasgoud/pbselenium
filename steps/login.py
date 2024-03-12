import time

from behave import *
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Lanching the chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    # context.driver.quit()


@when('I open the Amazon home page')
def step_impl(context):
    context.driver.get("https://www.amazon.in/")
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='nav-hamburger-menu']")))


@when('Enter the username')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']").click()
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("shivaiahgarivikasgoud@gmail.com")


@when('click the continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='continue']").click()


@then('click the continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='continue']").click()


@when('Enter the password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Vikas786@")


@then('user should sucessfully login into the Amazon page')
def step_impl(context):
    WebDriverWait(context.driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='nav-hamburger-menu']")))
    title = context.driver.title
    assert title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"


# @when('Enter the username "{username}"')
# def step_impl(context, username):
#     context.driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']").click()
#     context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(username)


@then('Enter the username "{username}"')
def step_impl(context, username):
    context.driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']").click()
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(username)


@then('The email error message have to display')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'We cannot find an account with that email address')]")))
    assert True


@when('Enter the password "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys(password)


@then('Enter the password "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys(password)


@when('click the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()


@then('click the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()


@then('The password error message have to display')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Your password is incorrect')]")))
    assert True
