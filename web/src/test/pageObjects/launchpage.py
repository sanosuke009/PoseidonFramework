"This module contains the page object class of the launch page"

from web.src.test.managers.resultmanager import resultmanager
from playwright.sync_api import Page
from web.src.test.config.propConfig import explicitwait


class launchpage:

    def __init__(self, page : Page, resultmanager : resultmanager):
        self.page = page
        self.rm = resultmanager

    # Page object locators
    page_title = 'symonstorozhenko.wixsite.com' #'Home | playwright-practice'
    xpath_buttonoption_home = "//p[text()='Home']"
    xpath_buttonoption_shopwomen = "//p[text()='Shop Women']"
    xpath_buttonoption_shopwomenwinter = "//p[text()='Shop Women Winter']"
    xpath_buttonoption_lookbook = "//p[text()='Look Book']"
    xpath_buttonoption_contactus = "//p[text()='Contact Us']"
    xpath_buttonoption_faq = "//p[text()='FAQ']"    

    xpath_buttonoption_login = "//span[text()='Log In']"   

    # Page object methods/functions
    def clickonloginbutton(self):
        try:
            self.page.wait_for_load_state(state='networkidle', timeout=explicitwait)
            if self.page_title in self.page.url:
                self.rm.addscreenshot("Launch page is launched.")
                loginoption = self.page.locator(self.xpath_buttonoption_login)
                loginoption.click()
                self.rm.addscreenshot("Login option is clicked.")
            else:
                self.rm.addscreenshot("Launch page is NOT launched.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during launch page launch.")
            print(e)
            return False
        else:
            return True
        

