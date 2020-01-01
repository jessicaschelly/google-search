from features.pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class GooglePage(BasePage):

    project_url = "https://forms.gle/wWP9p7o18XFR8BoY6"

    def get_field(browser, field):
        return browser.find_element_by_xpath(f'//input[@aria-label="{field}"]')

    def submit(browser):
        browser.find_element_by_xpath('//div[@role="button"]').click()
