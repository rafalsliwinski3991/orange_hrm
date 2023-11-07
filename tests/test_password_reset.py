from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.data.password_reset_page as pwd_reset_data
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.password_reset_page as pwd_reset_page
import repo.orange_hrm.pages.password_reset_confirmation_page as pwd_confirmed_reset_page
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

"""
Test: test_password_reset_successful

PRECONDITIONS:
1. User exists and is logged out.
2. Login page is displayed.

STEPS:
1. Click the 'Forgot your password' link. -> 'Reset Password' modal is displayed.
2. Fill the 'Username' field. -> Username is entered.
3. Click the 'Reset Password' button. -> Button is clicked, modal with title 'Reset Password link sent successfully'
is displayed.
4. ASSERTION - check if current URL matches password reset confirmation page URL.
5. ASSERTION - check if modal with proper title is displayed.
"""


def test_password_reset_successful():
    page_base.navigate_to_page(login_page.page_url)  # Precondition 2
    page_base.click_link('xpath', login_page.links['forgot_your_password'])  # Step 1
    app.enter_username(pwd_reset_page.inputs['username'], login_data.logins['correct_value'])  # Step 2
    page_base.click_button('xpath', pwd_reset_page.buttons['reset_password'])  # Step 3
    assert wd.current_url == pwd_confirmed_reset_page.page_url  # Step 4
    page_base.wait_for_element_to_be_visible('xpath', pwd_confirmed_reset_page.modal_header)
    assert wd.find_element(page_base.types['xpath'], pwd_confirmed_reset_page.modal_header).is_displayed()  # Step 5
    session.quit_session()


"""
Test: test_password_reset_cancelled_with_username_not_filled

PRECONDITIONS:
1. User exists and is logged out.
2. Login page is displayed.

STEPS:
1. Click the 'Forgot your password' link. -> 'Reset Password' modal is displayed.
2. Click the 'Cancel' button. -> Login page is displayed.
3. ASSERTION - check if current URL matches login page URL.
"""


def test_password_reset_cancelled_with_username_not_filled():
    page_base.navigate_to_page(login_page.page_url)  # Precondition 2
    page_base.click_link('xpath', login_page.links['forgot_your_password'])  # Step 1
    page_base.click_button('xpath', pwd_reset_page.buttons['cancel'])  # Step 2
    assert wd.current_url == login_page.page_url  # Step 3
    session.quit_session()


"""
Test: test_password_reset_cancelled_with_username_filled

PRECONDITIONS:
1. User exists and is logged out.
2. Login page is displayed.

STEPS:
1. Click the 'Forgot your password' link. -> 'Reset Password' modal is displayed.
2. Fill the 'Username' field. -> Username is entered.
3. Click the 'Cancel' button. -> Login page is displayed.
4. ASSERTION - check if current URL matches login page URL.
"""


def test_password_reset_cancelled_with_username_filled():
    page_base.navigate_to_page(login_page.page_url)  # Precondition 2
    page_base.click_link('xpath', login_page.links['forgot_your_password'])  # Step 1
    app.enter_username(pwd_reset_page.inputs['username'], login_data.logins['correct_value'])  # Step 2
    page_base.click_button('xpath', pwd_reset_page.buttons['cancel'])  # Step 3
    assert wd.current_url == login_page.page_url  # Step 4
    session.quit_session()


"""
Test: test_password_reset_empty_username

PRECONDITIONS:
1. User exists and is logged out.
2. Login page is displayed.

STEPS:
1. Click the 'Forgot your password' link. -> 'Reset Password' modal is displayed.
2. Click the 'Reset Password' button. -> Button is clicked, error message beneath 'Username' input is displayed.
3. ASSERTION - check if current URL matches password reset page URL.
4. ASSERTION - check if displayed error message text is what it should be.
"""


def test_password_reset_empty_username():
    page_base.navigate_to_page(login_page.page_url)  # Precondition 2
    page_base.click_link('xpath', login_page.links['forgot_your_password'])  # Step 1
    page_base.click_button('xpath', pwd_reset_page.buttons['reset_password'])  # Step 2
    assert wd.current_url == pwd_reset_page.page_url  # Step 3
    page_base.wait_for_element_to_be_visible('xpath', pwd_reset_page.error_messages['missing_username'])
    assert wd.find_element(page_base.types['xpath'], pwd_reset_page.error_messages['missing_username']).text == \
           pwd_reset_data.error_message_value  # Step 4
    session.quit_session()
