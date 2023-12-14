import pytest
from repo.orange_hrm.fixture.application import Application

app = Application(10)


@pytest.fixture()
def quit_session(request):
    fixture = Application(10)
    request.addfinalizer(app.quit_session)
    return fixture


def test_logout(quit_session):
    app.login_to_app_as_admin()  # Precondition 1
    app.click_element('xpath', app.header.user_dropdown)  # Step 1
    app.click_element('xpath', app.header.logout_option)  # Step 2
    assert app.wd.current_url == app.login_page.page_url  # Assertion 1
