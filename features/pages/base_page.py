from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
#--------------------------------------------------------------------------------------------------------#
# BasePage is a common class where the developer can write the necessary methods in python and re-use on #
# entire test, make sure the methods that you will write here are flexible, without constants or hardcode#
# data.                                                                                                  #
# Verify method names are readable to facilitate future maintenance and make it easier for other         #
# developers to use the method.                                                                          #
#--------------------------------------------------------------------------------------------------------#
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 5
        self.implicit_wait = 5
