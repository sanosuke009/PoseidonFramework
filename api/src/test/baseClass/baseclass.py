
from playwright.sync_api import APIRequestContext
from api.src.test.managers.resultmanager import resultmanager
from api.src.test.managers.testdatamanager import testdatamanager


class baseclass:

    def __init__(self, api_request_context: APIRequestContext) -> None:
        self.rm = resultmanager()
        self.apireqcontext = api_request_context

    def settestdatamanager(self, testdatafilepath):
        self.tm = testdatamanager(testdatafilepath)