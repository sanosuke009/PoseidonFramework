"This module contains the page object class of the launch page"

from web.src.test.managers.resultmanager import resultmanager
from playwright.sync_api import Page
from web.src.test.config.propConfig import explicitwait


class launchpage:

    def __init__(self, page : Page, resultmanager : resultmanager):
        self.page = page
        self.rm = resultmanager

    # Page object locators
    page_title = 'parabank.parasoft.com/parabank/index.htm' #'Home | playwright-practice'
    xpath_header_customerlogin = "//h2[text()='Customer Login']"
    xpath_input_username = "//input[@name='username']"
    xpath_input_password = "//input[@name='password']"
    xpath_button_login = "//input[@value='Log In']"

    # Page object methods/functions
    def login(self, username, password):
        try:
            self.page.wait_for_selector("xpath="+self.xpath_header_customerlogin)
            if self.page_title in self.page.url:
                self.rm.addscreenshot("Launch page is launched.")
                usernamefield = self.page.locator("xpath="+self.xpath_input_username)
                passwordfield = self.page.locator("xpath="+self.xpath_input_password)
                loginbutton = self.page.locator("xpath="+self.xpath_button_login)
                usernamefield.fill(username)
                passwordfield.fill(password)
                self.rm.addscreenshot("Credential fields are filled in.")
                loginbutton.click()
                self.rm.addscreenshot("Login button is clicked.")
            else:
                self.rm.addscreenshot("Launch page is NOT launched.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during launch page launch and login.")
            print(e)
            return False
        else:
            return True
        

