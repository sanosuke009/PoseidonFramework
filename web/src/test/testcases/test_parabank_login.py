from web.src.test.baseClass.baseclass import baseclass
from web.src.test.config.propConfig import *
import pytest
from web.src.test.pageObjects.parabank.homepage import homepage
from web.src.test.pageObjects.parabank.launchpage import launchpage


@pytest.fixture(scope="function", autouse=True)
def before_each(base:baseclass):
    base.settestdatamanager(parabanktestdatafilepath)
    if localExecution:
        LOGIN_URL = base.tm.gets("parabankurl_local")
    else:
        LOGIN_URL = base.tm.gets("parabankurl_local")
    base.page.goto(LOGIN_URL)
    yield base


def test_web_login(base:baseclass):
    testdata = base.tm.gets("Login")
    launchpageobj = launchpage(base)
    assert launchpageobj.login(testdata.get("parabankusername"), testdata.get("parabankpassword")) == True
    homepageobj = homepage(base)
    assert homepageobj.ishomepagedisplayed() == True

def test_web_login_again(base:baseclass):
    testdata = base.tm.gets("Login")
    launchpageobj = launchpage(base)
    assert launchpageobj.login(testdata.get("parabankusername"), testdata.get("parabankpassword")) == True
    homepageobj = homepage(base)
    assert homepageobj.ishomepagedisplayed() == True