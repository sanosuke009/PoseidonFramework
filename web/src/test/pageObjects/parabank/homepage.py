"This module contains the page object class of the home page"

from web.src.test.pageObjects.parabank.launchpage import launchpage
from web.src.test.managers.resultmanager import resultmanager
from playwright.sync_api import Page
from web.src.test.config.propConfig import explicitwait

class homepage(launchpage):

    def __init__(self, page : Page, resultmanager : resultmanager):
        self.page = page
        self.rm = resultmanager

    # Page object locators
    xpath_header_accountoverview = "//h1[text()='Accounts Overview']"

    # Page object methods/functions

    def ishomepagedisplayed(self):
        try:
            self.page.wait_for_selector(selector="xpath="+self.xpath_header_accountoverview, state='visible', timeout=explicitwait)
            if self.page.is_visible(selector="xpath="+self.xpath_header_accountoverview):
                self.rm.addscreenshot("Home page is displayed.")
            else:
                self.rm.addscreenshot("Home page is NOT displayed.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred while navigating to Home Page.")
            print(e)
            return False
        else:
            return True
        

