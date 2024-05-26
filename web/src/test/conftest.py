
from pytest import *
import pytest
from playwright.sync_api import Browser, BrowserType, Playwright, BrowserContext, Page
from typing import Dict
from web.src.test.baseClass.baseclass import baseclass
from web.src.test.config.propConfig import *

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True, #For bypassing the http certificate errors
        "no_viewport": True
        #"record_video_dir": playwright_videos_dir
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": headless,
        "traces_dir": playwright_traces_dir,
        "args": browserargs,
        "channel": browsername
    }

@pytest.fixture(scope="session")
def browser_type(playwright : Playwright):
    if 'chrome' in browsername:
        browser_type = playwright.chromium
    elif 'edge' in browsername:
        browser_type = playwright.chromium
    elif 'firefox' in browsername:
        browser_type = playwright.firefox
    else:
        browser_type = playwright.webkit
    yield browser_type

@pytest.fixture(scope="session")
def browser(
    browser_type: BrowserType,
    browser_type_launch_args: Dict
):
    browser = browser_type.launch(**{
        **browser_type_launch_args,
    })
    yield browser
    browser.close() 

@pytest.fixture(scope="function")
def context(
    browser: Browser,
    browser_context_args: Dict
):
    context = browser.new_context(**{
        **browser_context_args,
    })
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context:BrowserContext):
    context.set_default_timeout(120000)
    page = context.new_page()
    yield page

@pytest.fixture(scope="function")
def base(page:Page):
    basec = baseclass(page)
    yield basec