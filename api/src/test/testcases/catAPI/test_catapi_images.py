import pytest
from api.src.test.baseClass.baseclass import baseclass
from api.src.test.testcases.catAPI.conftest import catapitestdatafile

@pytest.fixture(scope="function", autouse=True)
def before_each(base:baseclass):
    base.settestdatamanager(catapitestdatafile)
    yield base

@pytest.mark.parametrize("keyword", ["getrandomcatimage"])
def test_GET_random_cat_image(base:baseclass, keyword) -> None:
    testdata = base.tm.gets(keyword)
    uri = testdata.get("url_tail")
    new_issue = base.apireqcontext.get(uri)
    issues_response = new_issue.json()
    print("Sending GET request to uri "+uri)
    print("The status of the GET request is "+str(new_issue.status))
    print("The json response of the GET request is "+str(issues_response))
    assert new_issue.ok

@pytest.mark.parametrize("keyword", ["getcatimagebyid"])
def test_GET_cat_image_by_id(base:baseclass, keyword) -> None:
    testdata = base.tm.gets(keyword)
    uri = testdata.get("url_tail")+testdata.get("id")
    new_issue = base.apireqcontext.get(uri)
    issues_response = new_issue.json()
    print("Sending GET request to uri "+uri)
    print("The status of the GET request is "+str(new_issue.status))
    print("The json response of the GET request is "+str(issues_response))
    assert new_issue.ok
    assert issues_response == testdata.get("response")

@pytest.mark.parametrize("keyword", ["postfavoutite"])
def test_POST_set_favorite(base:baseclass, keyword) -> None:
    testdata = base.tm.gets(keyword)
    uri = testdata.get("url_tail")
    payload = testdata.get("payload")
    new_issue = base.apireqcontext.post(uri, data=payload)
    issues_response = new_issue.json()
    print("Sending POST request to uri "+uri)
    print("The status of the POST request is "+str(new_issue.status))
    print("The json response of the POST request is "+str(issues_response))
    assert new_issue.ok
    assert new_issue.status == testdata.get("expectedresponsecode")

@pytest.mark.parametrize("keyword", ["deletefavoutite"])
def test_DELETE_remove_favorite(base:baseclass, keyword) -> None:
    testdata = base.tm.gets(keyword)
    uri = testdata.get("url_tail")
    new_issue = base.apireqcontext.get(uri)
    issues_response = new_issue.json()
    favourite_id = issues_response[0].get("id")
    uri = testdata.get("url_tail")+"/"+str(favourite_id)
    new_issue = base.apireqcontext.delete(uri)
    issues_response = new_issue.json()
    print("Sending DELETE request to uri "+uri)
    print("The status of the DELETE request is "+str(new_issue.status))
    print("The json response of the DELETE request is "+str(issues_response))
    print("The favorite id is "+str(favourite_id))
    assert new_issue.ok
    assert new_issue.status == testdata.get("expectedresponsecode")