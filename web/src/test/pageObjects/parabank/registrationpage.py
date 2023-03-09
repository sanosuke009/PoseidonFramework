"This module contains the page object class of the registration page"

from web.src.test.baseClass.baseclass import baseclass
from web.src.test.managers.resultmanager import resultmanager
from playwright.sync_api import Page


class registrationpage:

    def __init__(self, base:baseclass):
        self.page = base.page
        self.rm = base.rm

    # Page object locators
    page_title = 'parabank.parasoft.com/parabank/register.htm' #'Home | playwright-practice'
    xpath_header_signuppage = "//h1[text()='Signing up is easy!']"
    id_input_FirstName = "customer.firstName"
    id_input_LastName = "customer.lastName"
    id_input_Address = "customer.address.street"
    id_input_City = "customer.address.city"
    id_input_State = "customer.address.state"
    id_input_ZipCode = "customer.address.zipCode"
    id_input_Phone = "customer.phoneNumber"
    id_input_SSN = "customer.ssn"
    id_input_Username = "customer.username"
    id_input_Password = "customer.password"
    id_input_ConfirmPassword = "repeatedPassword"
    xpath_button_login = "//input[@value='Register']"

    # Page object methods/functions
    def registernewuser(self, FirstName, LastName, Address, 
                 City, State, ZipCode, Phone, SSN, Username, Password):
        try:
            self.page.wait_for_selector("xpath="+self.xpath_header_signuppage)
            if self.page_title in self.page.url:
                self.rm.addscreenshot("Registration page is launched.")
                self.page.locator("id="+self.id_input_FirstName).fill(FirstName)
                self.page.locator("id="+self.id_input_LastName).fill(LastName)
                self.page.locator("id="+self.id_input_Address).fill(Address)
                self.page.locator("id="+self.id_input_City).fill(City)
                self.page.locator("id="+self.id_input_State).fill(State)
                self.page.locator("id="+self.id_input_ZipCode).fill(ZipCode)
                self.page.locator("id="+self.id_input_Phone).fill(Phone)
                self.page.locator("id="+self.id_input_SSN).fill(SSN)
                self.page.locator("id="+self.id_input_Username).fill(Username)
                self.page.locator("id="+self.id_input_Password).fill(Password)
                self.page.locator("id="+self.id_input_ConfirmPassword).fill(Password)
                self.rm.addscreenshot("All required fields are filled in.")
                self.page.locator("xpath="+self.xpath_button_login).click()
                self.rm.addscreenshot("Register button is clicked.")
            else:
                self.rm.addscreenshot("Registration page is NOT launched.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during Registration page launch and Registration.")
            print(e)
            return False
        else:
            return True
        

