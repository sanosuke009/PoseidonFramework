"This class controls the allure report or any other report generation"


from allure_commons.types import AttachmentType
import allure
from playwright.sync_api import APIRequestContext


class resultmanager:

    def __init__(self):
        pass

    def addtoreport(self, message):
        allure.attach(name=message, attachment_type=AttachmentType.TEXT)
    