from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.header as header
from repo.orange_hrm.fixture.page_base import PageBase
from repo.orange_hrm.fixture.application import Application
from repo.orange_hrm.fixture.session import SessionHelper

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

wd = webdriver.Chrome(service=service, options=options)
wd.maximize_window()

page_base = PageBase(wd, 10)
app = Application(wd, 10)
session = SessionHelper()


def test_logout():
    app.login_to_app_as('admin')  # Precondition 1
    page_base.click_element('xpath', header.user_dropdown)  # Step 1
    page_base.click_element('xpath', header.logout_option)  # Step 2
    assert wd.current_url == login_page.page_url  # Assertion 1
    session.quit_session()
