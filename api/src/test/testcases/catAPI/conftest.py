
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext
from api.src.test.baseClass.baseclass import baseclass

#==================Global Variables For Cat API================================================
CAT_API_BASE_URL = "https://api.thecatapi.com"
CAT_API_TOKEN_KEY = "x-api-key"
CAT_API_TOKEN_VALUE = "live_CLiPEgDaZzLbzU4YXWXmjA7cVypNVrElt3g7nV1FNQ3cc1xQsL8AmqD3GMx0slt2"
catapitestdatafile = "./api/src/test/testData/catApi/testdata.json"
#=============================================================================================

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/json",
        CAT_API_TOKEN_KEY: CAT_API_TOKEN_VALUE
    }
    request_context = playwright.request.new_context(
        base_url=CAT_API_BASE_URL, extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="function")
def base(api_request_context: APIRequestContext):
    basec = baseclass(api_request_context)
    yield basec