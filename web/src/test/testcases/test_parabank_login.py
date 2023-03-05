from playwright.sync_api import Playwright, Page
from web.src.test.config.propConfig import *
import pytest

from web.src.test.managers.resultmanager import resultmanager
from web.src.test.pageObjects.parabank.homepage import homepage
from web.src.test.pageObjects.parabank.launchpage import launchpage


@pytest.fixture(scope="function", autouse=True)
def before_each(page:Page):
    if localExecution:
        LOGIN_URL = parabankurl_local
    else:
        LOGIN_URL = parabankurl_local
    page.goto(LOGIN_URL)
    yield page


def test_web_login(page:Page):
    rm = resultmanager(page)
    launchpageobj = launchpage(page, rm)
    assert launchpageobj.login(parabankusername, parabankpassword) == True
    homepageobj = homepage(page, rm)
    assert homepageobj.ishomepagedisplayed() == True

def test_web_login_again(page:Page):
    rm = resultmanager(page)
    launchpageobj = launchpage(page, rm)
    assert launchpageobj.login(parabankusername, parabankpassword) == True
    homepageobj = homepage(page, rm)
    assert homepageobj.ishomepagedisplayed() == True