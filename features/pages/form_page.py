from features.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class FormPage(BasePage):

    project_url = "https://jessicaschelly.typeform.com/to/sKiyLf"

    def press_enter(browser):
        actions = ActionChains(browser)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def get_active_element(browser):
        return browser.switch_to.active_element

    def write_to_active_element(browser, text):
        actions = ActionChains(browser)
        actions.send_keys(text)
        actions.perform()
