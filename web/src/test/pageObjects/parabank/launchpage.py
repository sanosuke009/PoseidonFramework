"This module contains the page object class of the launch page"

from web.src.test.baseClass.baseclass import baseclass
from web.src.test.managers.resultmanager import resultmanager
from playwright.sync_api import Page


class launchpage:

    def __init__(self, base:baseclass):
        self.page = base.page
        self.rm = base.rm

    # Page object locators
    page_title = 'parabank.parasoft.com/parabank/index.htm' #'Home | playwright-practice'
    xpath_header_customerlogin = "//h2[text()='Customer Login']"
    xpath_input_username = "//input[@name='username']"
    xpath_input_password = "//input[@name='password']"
    xpath_button_login = "//input[@value='Log In']"
    xpath_link_register = "//a[text()='Register']"

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
        

    def clickonregister(self):
        try:
            self.page.wait_for_selector("xpath="+self.xpath_header_customerlogin)
            if self.page_title in self.page.url:
                self.rm.addscreenshot("Launch page is launched.")
                self.page.locator("xpath="+self.xpath_link_register).click()
                self.rm.addscreenshot("Register link is clicked on Launch.")
            else:
                self.rm.addscreenshot("Launch page is NOT launched.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during clicking the Registration link from launch page.")
            print(e)
            return False
        else:
            return True
        

