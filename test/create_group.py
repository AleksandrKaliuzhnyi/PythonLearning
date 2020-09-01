import pytest
from group import Group
from application_group import Application_group

@pytest.fixture
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_group(app):
    app.login( username="admin", password="secret")
    app.group_creation( Group(name="1st group", header="logo", footer="comment"))
    app.logout()
