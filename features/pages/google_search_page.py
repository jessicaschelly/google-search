from features.pages.base_page import BasePage


class GooglePage(BasePage):

    project_url = "https://www.google.com/"

    locators = {
        "username": "login",
        "password": "password",
    }

    def search_field(browser):
            return browser.find_element_by_name('q')
