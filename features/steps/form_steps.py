from behave import *
from features.object import Singleton
from features.pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@given(u'a web browser is at the Form page')
def navigate_to_the_form(context):
    form_page = Singleton.getInstance(context, FormPage)
    context.browser.get(form_page.project_url)
    element_present = EC.presence_of_element_located(
        (By.XPATH, '//div[@data-qa="has-loaded"]'))

    WebDriverWait(context.browser, 10).until(element_present)
    time.sleep(2)


@when(u'the user starts the form')
def user_starts_the_form(context):
    form_page = Singleton.getInstance(context, FormPage)

    form_page.press_enter(context.browser)
    time.sleep(1)


@step(u'the user types {name} as {field}')
def user_types(context, name, field):
    form_page = Singleton.getInstance(context, FormPage)

    form_page.write_to_active_element(context.browser, name)
    form_page.press_enter(context.browser)
    time.sleep(1)


@step(u'the user submits the form')
def submits(context):
    form_page = Singleton.getInstance(context, FormPage)
    form_page.press_enter(context.browser)
    time.sleep(1)


@then(u'the user should see {value}')
def assert_submit(context, value):
    response = context.browser.page_source
    assert value in response


@then(u'the user must see error {message}')
def assert_error_message(context, message):
    response = context.browser.page_source
    assert message in response
