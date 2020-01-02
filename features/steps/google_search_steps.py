from behave import *
from features.object import Singleton
from features.pages.google_search_page import GooglePage
from selenium.webdriver.common.keys import Keys


@given(u'a web browser is at the Google home page')
def navigate_to_the_google(context):
    google_page = Singleton.getInstance(context, GooglePage)
    context.browser.get(google_page.project_url)


@when(u'the user enters {query} into the search bar')
def search_for_lexisnexis(context, query):
    google_page = Singleton.getInstance(context, GooglePage)
    element = google_page.search_field(context.browser)
    element.send_keys(query)
    element.send_keys(Keys.RETURN)


@then(u'links related to {name} are shown on the results page')
def step_impl(context, name):
    response = context.browser.page_source
    assert name in response
