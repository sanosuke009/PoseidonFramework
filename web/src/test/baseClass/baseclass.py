
from playwright.sync_api import Page
from web.src.test.managers.resultmanager import resultmanager
from web.src.test.managers.visualtestmanager import visualtestmanager
from web.src.test.managers.testdatamanager import testdatamanager


class baseclass:

    def __init__(self, page:Page, assert_snapshot) -> None:
        self.rm = resultmanager(page)
        self.visual = visualtestmanager(page, assert_snapshot)
        self.page = page

    def settestdatamanager(self, testdatafilepath):
        self.tm = testdatamanager(testdatafilepath)

    def setkeyword(self, keyword):
        self.keyword = keyword

    def getkeyword(self) -> str:
        return self.keyword
    
    def gettestdata(self):
        return self.tm.gets(self.keyword)