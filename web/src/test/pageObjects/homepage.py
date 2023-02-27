"This module contains the page object class of the home page"

from web.src.test.pageObjects.loginpage import loginpage
from web.src.test.managers.resultmanager import resultmanager
from playwright.sync_api import Page

class homepage(loginpage):

    def __init__(self, page : Page, resultmanager : resultmanager):
        self.page = page
        self.rm = resultmanager

    # Page object locators

    # Page object methods/functions

    def ishomepagedisplayed(self):
        try:
            header = self.page.wait_for_selector(selector="xpath="+self.xpath_buttonoption_login, state='hidden')
            if self.page.is_visible(selector="xpath="+self.xpath_buttonoption_login):
                self.rm.addscreenshot("Home page is NOT displayed.")
                return False
            else:
                self.rm.addscreenshot("Home page is displayed.")
        except Exception as e:
            self.rm.addscreenshot("Error occurred while navigating to Home Page.")
            print(e)
            return False
        else:
            return True
        

