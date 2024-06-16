from web.src.test.baseClass.baseclass import baseclass
from web.src.test.config.propConfig import youtubetestdatafilepath
import pytest
from web.src.test.pageObjects.youtube.launchpage import launchpage


@pytest.fixture(scope="function", autouse=True)
def before_each(base:baseclass):
    base.settestdatamanager(youtubetestdatafilepath)
    yield base

@pytest.mark.parametrize(
    "keyword",
    sorted(["AamShol", "Quail", "gulmoharreview", "ordinary_review", "CHAKA", "RedRiverValley"]),
)
def test_web_login(base:baseclass, keyword):
    testdata = base.tm.gets(keyword)
    base.page.goto(testdata.get("url"))
    launchpageobj = launchpage(base)
    assert launchpageobj.verifytitleofthevideo(testdata.get("title")) == True