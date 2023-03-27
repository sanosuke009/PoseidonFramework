from web.src.test.baseClass.baseclass import baseclass
from web.src.test.visualtest.demoblaze.conftest import demoblazetestdatafilepath
import pytest
from web.src.test.pageObjects.demoblaze.launchpage import launchpage


@pytest.fixture(scope="function", autouse=True)
def before_each(base:baseclass):
    base.settestdatamanager(demoblazetestdatafilepath)
    base.page.goto(base.tm.gets("url"))
    yield base

@pytest.mark.parametrize(
    "keyword",
    ["demoblazelogin"],
)
def test_web_login(base:baseclass, keyword):
    base.setkeyword(keyword)
    testdata = base.gettestdata()
    launchpageobj = launchpage(base)
    assert launchpageobj.login(testdata.get("username"), testdata.get("password")) == True
    #base.visual.visualtest()