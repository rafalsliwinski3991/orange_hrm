from selenium import webdriver
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.header as header
from repo.orange_hrm.fixture.page_base import PageBase
from repo.orange_hrm.fixture.application import Application
from repo.orange_hrm.fixture.session import SessionHelper

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

wd = webdriver.Chrome(options=options)
wd.maximize_window()

page_base = PageBase(wd, 10)
app = Application(wd, 10)
session = SessionHelper()

"""
PRECONDITIONS:
1. User exists and is logged in.

STEPS:
1. Click the icon next to the user avatar. -> Dropdown list is expanded.
2. Click the 'Logout' option. -> Login page is displayed.
3. ASSERTION - check if current URL matches login page URL.
"""


def test_logout():
    app.login_to_app()  # Precondition 1
    page_base.click_element('xpath', header.user_dropdown)  # Step 1
    page_base.click_element('xpath', header.logout_option)  # Step 2
    assert wd.current_url == login_page.page_url  # Step 3
    session.quit_session()
