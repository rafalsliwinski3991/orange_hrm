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


def test_password_reset_successful():
    page_base.navigate_to_page(login_page.page_url)  # Precondition 2
    page_base.click_link('xpath', login_page.links['forgot_your_password'])  # Step 1
    page_base.fill_input('xpath', pwd_reset_page.inputs['username'], login_data.logins['correct_value'])  # Step 2
    page_base.click_button('xpath', pwd_reset_page.buttons['reset_password'])  # Step 3
    assert wd.current_url == pwd_confirmed_reset_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', pwd_confirmed_reset_page.modal_header)
    assert wd.find_element(page_base.types['xpath'], pwd_confirmed_reset_page.modal_header).is_displayed()
    # Assertion 2
    session.quit_session()


def test_password_reset_cancelled_with_username_not_filled():
    page_base.navigate_to_page(login_page.page_url)  # Precondition 2
    page_base.click_link('xpath', login_page.links['forgot_your_password'])  # Step 1
    page_base.click_button('xpath', pwd_reset_page.buttons['cancel'])  # Step 2
    assert wd.current_url == login_page.page_url  # Assertion 1
    session.quit_session()


def test_password_reset_cancelled_with_username_filled():
    page_base.navigate_to_page(login_page.page_url)  # Precondition 2
    page_base.click_link('xpath', login_page.links['forgot_your_password'])  # Step 1
    page_base.fill_input('xpath', pwd_reset_page.inputs['username'], login_data.logins['correct_value'])  # Step 2
    page_base.click_button('xpath', pwd_reset_page.buttons['cancel'])  # Step 3
    assert wd.current_url == login_page.page_url  # Assertion 1
    session.quit_session()


def test_password_reset_empty_username():
    page_base.navigate_to_page(login_page.page_url)  # Precondition 2
    page_base.click_link('xpath', login_page.links['forgot_your_password'])  # Step 1
    page_base.click_button('xpath', pwd_reset_page.buttons['reset_password'])  # Step 2
    assert wd.current_url == pwd_reset_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', pwd_reset_page.error_messages['missing_username'])
    assert wd.find_element(page_base.types['xpath'], pwd_reset_page.error_messages['missing_username']).text == \
           pwd_reset_data.error_messages['missing_username']  # Assertion 2
    session.quit_session()
