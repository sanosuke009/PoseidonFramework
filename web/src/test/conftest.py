
from pytest import *
import pytest
from playwright.sync_api import BrowserType, Playwright, BrowserContext
from typing import Dict
from web.src.test.config.propConfig import playwright_traces_dir, browsername, headless, playwright_videos_dir

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True, #For bypassing the http certificate errors
        "no_viewport": True,
        "record_video_dir": playwright_videos_dir
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": headless,
        "traces_dir": playwright_traces_dir
    }

@pytest.fixture(scope="session")
def browser_type(playwright : Playwright):
    if browsername == 'Chrome':
        browser_type = playwright.chromium
    elif browsername == 'Firefox':
        browser_type = playwright.firefox
    else:
        browser_type = playwright.webkit
    yield browser_type

@pytest.fixture(scope="session")
def context(
    browser_type: BrowserType,
    browser_type_launch_args: Dict,
    browser_context_args: Dict
):
    browser = browser_type.launch(**{
        **browser_type_launch_args,
    })
    context = browser.new_context(**{
        **browser_context_args,
    })
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def page(context:BrowserContext):
    page = context.new_page()
    yield page