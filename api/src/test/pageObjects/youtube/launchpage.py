"This module contains the page object class of the youtube video launch page"

from api.src.test.baseClass.baseclass import baseclass


class launchpage:

    def __init__(self, base:baseclass):
        self.page = base.page
        self.rm = base.rm

    # Page object locators
    xpath_header_videotitle = lambda self, title: "(//h1/*[contains(text(),'"+title+"')])[1]"
    xpath_span_noofviews = "//yt-formatted-string[@id='info']/span[contains(text(), 'views')]"

    # Page object methods/functions
    
    def verifytitleofthevideo(self, title):
        try:
            self.page.wait_for_selector("xpath="+self.xpath_header_videotitle(title))
            if self.page.is_visible(selector="xpath="+self.xpath_header_videotitle(title)):
                views = self.page.text_content(selector="xpath="+self.xpath_span_noofviews)
                self.rm.addscreenshot("The video title "+title+" is displayed as expected. The no. of views is "+views)
            else:
                self.rm.addscreenshot("The video title "+title+" is NOT displayed as expected.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during verification of youtube video title "+title)
            print(e)
            return False
        else:
            return True
        

