from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class CorreiosPage(BasePage):

    project_url = "http://www.buscacep.correios.com.br/sistemas/buscacep/"

    def search_field(browser):
        return browser.find_element_by_name('relaxation')
