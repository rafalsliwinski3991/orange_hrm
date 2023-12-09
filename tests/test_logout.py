from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.header as header
from repo.orange_hrm.fixture.application import Application

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

wd = webdriver.Chrome(service=service, options=options)
wd.maximize_window()

app = Application(wd, 10)


@pytest.fixture()
def destroy(request):
    fixture = Application(wd, 10)
    request.addfinalizer(app.quit_session)
    return fixture


def test_logout(destroy):
    app.login_to_app_as('admin')  # Precondition 1
    app.click_element('xpath', header.user_dropdown)  # Step 1
    app.click_element('xpath', header.logout_option)  # Step 2
    assert wd.current_url == login_page.page_url  # Assertion 1
