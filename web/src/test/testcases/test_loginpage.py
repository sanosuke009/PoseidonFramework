from playwright.sync_api import Playwright, Page
from web.src.test.config.propConfig import localExecution, localUrl, vmUrl, browsername, headless, username, password
import pytest

from web.src.test.managers.resultmanager import resultmanager
from web.src.test.pageObjects.homepage import homepage
from web.src.test.pageObjects.launchpage import launchpage
from web.src.test.pageObjects.loginpage import loginpage


""" pytest.fixture(scope="function", autouse=True)
def before_each(playwright: Playwright):
    if localExecution:
        LOGIN_URL = localUrl
    else:
        LOGIN_URL = vmUrl
    if browsername == 'Chrome':
        browser = playwright.chromium.launch(headless=headless)
    elif browsername == 'Firefox':
        browser = playwright.firefox.launch(headless=headless)
    else:
        browser = playwright.webkit.launch(headless=headless)
    context = browser.new_context()
    page = context.new_page()
    page.goto(LOGIN_URL)
    yield
    context.close()
    browser.close() """

@pytest.fixture(scope="function", autouse=True)
def before_each(page:Page):
    if localExecution:
        LOGIN_URL = localUrl
    else:
        LOGIN_URL = vmUrl
    page.goto(LOGIN_URL)
    yield


def test_web_login(page:Page):
    rm = resultmanager(page)
    launchpageobj = launchpage(page, rm)
    assert launchpageobj.clickonloginbutton() == True
    signuppageobj = loginpage(page, rm)
    assert signuppageobj.navigatetologinwithemail() == True
    assert signuppageobj.loginwithemail(username, password) == True
    homepageobj = homepage(page, rm)
    assert homepageobj.ishomepagedisplayed() == True

def test_web_login_again(page:Page):
    rm = resultmanager(page)
    launchpageobj = launchpage(page, rm)
    assert launchpageobj.clickonloginbutton() == True
    signuppageobj = loginpage(page, rm)
    assert signuppageobj.navigatetologinwithemail() == True
    assert signuppageobj.loginwithemail(username, password) == True
    homepageobj = homepage(page, rm)
    assert homepageobj.ishomepagedisplayed() == True