from behave import *
from features.object import Singleton
from features.pages.google_form_page import GooglePage
from selenium.webdriver.common.keys import Keys


@given(u'I am at the Form page')
def navigate_to_the_google(context):
    google_page = Singleton.getInstance(context, GooglePage)
    context.browser.get(google_page.project_url)


@when(u'I fill in {field} with {value}')
def search_for_lexisnexis(context, field, value):
    google_page = Singleton.getInstance(context, GooglePage)
    element = google_page.get_field(context.browser, field)
    element.send_keys(value)


@when(u'I submit the form')
def submit_form(context):
    google_page = Singleton.getInstance(context, GooglePage)
    google_page.submit(context.browser)


@then(u'I should see {text}')
def step_impl(context, text):
    response = context.browser.page_source
    assert text in response
