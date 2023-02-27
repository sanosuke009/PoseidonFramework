"This module contains the page object class of the login page"

from web.src.test.pageObjects.launchpage import launchpage
from web.src.test.managers.resultmanager import resultmanager
from playwright.sync_api import Page
from web.src.test.config.propConfig import explicitwait

class loginpage(launchpage):

    def __init__(self, page : Page, resultmanager : resultmanager):
        self.page = page
        self.rm = resultmanager

    # Page object locators
    page_title = 'Home | playwright-practice'
    xpath_heading_signin = "//h1[text()='Sign Up']"
    xpath_link_login = "//button[text()='Log In']"
    xpath_button_shopwomenwinter = "//button[@data-testid='xButton']"
    
    xpath_heading_login = "//h1[text()='Log In']"
    xpath_button_loginwithemail = "//button/span[text()='Log in with Email']"

    id_input_username = "input_input_emailInput_SM_ROOT_COMP10"
    id_input_password = "input_input_passwordInput_SM_ROOT_COMP10"
    xpath_button_login = "(//button/span[text()='Log In'])[2]"

    # Page object methods/functions

    def navigatetologinwithemail(self):
        try:
            self.page.wait_for_load_state(state='networkidle', timeout=explicitwait)
            self.rm.addscreenshot("Sign Up page is displayed.")
            header = self.page.wait_for_selector(selector="xpath="+self.xpath_heading_signin) #, state='visible'
            self.rm.addscreenshot("Sign up header is displayed.")
            if self.page.is_visible(selector="xpath="+self.xpath_heading_signin):
                self.rm.addscreenshot("Sign Up page is displayed 2.")
                loginlink = self.page.locator(self.xpath_link_login)
                loginlink.click()
                self.rm.addscreenshot("Clicked on Lon In link.")
                header = self.page.wait_for_selector(selector="xpath="+self.xpath_heading_login) #, state='visible'
                if self.page.is_visible(selector="xpath="+self.xpath_heading_login):
                    self.rm.addscreenshot("Log In page is displayed.")
                else:
                    self.rm.addscreenshot("Log In page is NOT displayed.")
                    return False
            else:
                self.rm.addscreenshot("Sign Up page is NOT displayed.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred while navigating to Login Page.")
            print(e)
            return False
        else:
            return True
        

    def loginwithemail(self, username, password):
        try:
            loginwithemaillink = self.page.wait_for_selector(selector="xpath="+self.xpath_button_loginwithemail, state='visible')
            if self.page.is_visible(selector="xpath="+self.xpath_button_loginwithemail):
                loginwithemaillink.click()
                self.rm.addscreenshot("Clicked on Lon In With Email link.")
                usernamefield = self.page.wait_for_selector(selector="id="+self.id_input_username, state='visible')
                if self.page.is_visible(selector="id="+self.id_input_username):
                    usernamefield.fill(username)
                    passwordfield = self.page.locator("id="+self.id_input_password)
                    passwordfield.fill(password)
                    self.rm.addscreenshot("Crendial fields are filled.")
                    loginbutton = self.page.locator(self.xpath_button_login)
                    loginbutton.click()
                    self.rm.addscreenshot("The login button is clicked.")
                else:
                    self.rm.addscreenshot("Username field is NOT displayed.")
                    return False
            else:
                self.rm.addscreenshot("Log In With Email Link is NOT displayed.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred while logging in with email.")
            print(e)
            return False
        else:
            return True

