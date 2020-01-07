from behave import *
from features.object import Singleton
from features.pages.correios_page import CorreiosPage
from selenium.webdriver.common.keys import Keys


@given(u'a web browser is at the Correios search address page')
def navigate_to_the_google(context):
    correios_page = Singleton.getInstance(context, CorreiosPage)
    context.browser.get(correios_page.project_url)


@when(u'the user searches for address {query}')
def search_for_lexisnexis(context, query):
    correios_page = Singleton.getInstance(context, CorreiosPage)
    element = correios_page.search_field(context.browser)
    element.send_keys(query)
    element.send_keys(Keys.RETURN)


@then(u'the user will be redirected to another page and see {message}')
def step_impl(context, message):
    response = context.browser.page_source
    assert message in response
