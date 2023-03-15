from playwright.sync_api import APIRequestContext
import pytest
from api.src.test.config.propConfig import catapitestdatafile
from api.src.test.baseClass.baseclass import baseclass

@pytest.fixture(scope="function", autouse=True)
def before_each(base:baseclass):
    base.settestdatamanager(catapitestdatafile)
    yield base

@pytest.mark.parametrize(
    "keyword",
    ["getrandomcatimage"],
)
def test_should_create_bug_report(base:baseclass, keyword) -> None:
    testdata = base.tm.gets(keyword)
    new_issue = base.apireqcontext.get(testdata.get("url_tail"))
    issues_response = new_issue.json()
    print(new_issue.status)
    print(issues_response)
    assert new_issue.ok