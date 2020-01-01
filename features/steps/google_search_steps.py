from behave import *
from features.object import Singleton
from features.pages.google_search_page import GooglePage
from selenium.webdriver.common.keys import Keys


@given(u'I navigate to the Google page')
def navigate_to_the_google(context):
    google_page = Singleton.getInstance(context, GooglePage)
    context.browser.get(google_page.project_url)


@when(u'I search for {query}')
def search_for_lexisnexis(context, query):
    google_page = Singleton.getInstance(context, GooglePage)
    element = google_page.search_field(context.browser)
    element.send_keys(query)
    element.send_keys(Keys.RETURN)


@then(u'I must see {name} on results')
def step_impl(context, name):
    response = context.browser.page_source
    assert name in response
