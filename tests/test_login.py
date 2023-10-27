from selenium import webdriver
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.dashboard_page as dashboard_page
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
1. User exists and is logged out.

STEPS:
1. Navigate to login page. -> Login page is displayed.
2. Fill the 'username' field. -> User name is entered.
3. Fill the 'password' field. -> Password is entered.
4. Click the 'Login' button. -> Button is clicked, dashboard page is displayed.
5. ASSERTION - check if current URL matches dashboard page URL.
6. Log out from the application. -> Login page is displayed.
"""


def test_login():
    page_base.navigate_to_page(login_page.page_url)  # Step 1
    page_base.fill_input('xpath', login_page.login_input, login_data.login_value)  # Step 2
    page_base.fill_input('xpath', login_page.password_input, login_data.password_value)  # Step 3
    page_base.click_element('xpath', login_page.login_button)  # Step 4
    assert wd.current_url == dashboard_page.page_url  # Step 5
    app.logout_from_app()  # Step 6
    session.quit_session()
