from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.dashboard_page as dashboard_page
from repo.orange_hrm.fixture.application import Application

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

wd = webdriver.Chrome(service=service, options=options)
wd.maximize_window()

app = Application(wd, 10)


@pytest.fixture()
def logout(request):
    fixture = Application(wd, 10)
    request.addfinalizer(app.logout_from_app)
    return fixture


@pytest.fixture()
def quit_session(request):
    fixture = Application(wd, 10)
    request.addfinalizer(app.quit_session)
    return fixture


def test_login_successful(logout):
    app.navigate_to_page(login_page.page_url)  # Step 1
    app.fill_input('xpath', login_page.inputs['login'], login_data.logins['correct_value'])  # Step 2
    app.fill_input('xpath', login_page.inputs['password'], login_data.passwords['correct_value'])  # Step 3
    app.click_button('xpath', login_page.buttons['login'])  # Step 4
    assert wd.current_url == dashboard_page.page_url  # Assertion 1


def test_login_incorrect_username():
    app.navigate_to_page(login_page.page_url)  # Step 1
    app.fill_input('xpath', login_page.inputs['login'], login_data.logins['incorrect_value'])  # Step 2
    app.fill_input('xpath', login_page.inputs['password'], login_data.passwords['correct_value'])  # Step 3
    app.click_button('xpath', login_page.buttons['login'])  # Step 4
    assert wd.current_url == login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', login_page.error_messages['invalid_credentials'])
    assert wd.find_element(app.types['xpath'], login_page.error_messages['invalid_credentials']).text == \
           login_data.error_message_value['invalid_credentials']  # Assertion 2


def test_login_incorrect_password():
    app.navigate_to_page(login_page.page_url)  # Step 1
    app.fill_input('xpath', login_page.inputs['login'], login_data.logins['correct_value'])  # Step 2
    app.fill_input('xpath', login_page.inputs['password'], login_data.passwords['incorrect_value'])  # Step 3
    app.click_button('xpath', login_page.buttons['login'])  # Step 4
    assert wd.current_url == login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', login_page.error_messages['invalid_credentials'])
    assert wd.find_element(app.types['xpath'], login_page.error_messages['invalid_credentials']).text == \
           login_data.error_message_value['invalid_credentials']  # Assertion 2


def test_login_no_username():
    app.navigate_to_page(login_page.page_url)  # Step 1
    app.fill_input('xpath', login_page.inputs['password'], login_data.passwords['correct_value'])  # Step 2
    app.click_button('xpath', login_page.buttons['login'])  # Step 3
    assert wd.current_url == login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', login_page.error_messages['missing_username'])
    assert wd.find_element(app.types['xpath'], login_page.error_messages['missing_username']).text == \
           login_data.error_message_value['missing_username']  # Assertion 2


def test_login_no_password():
    app.navigate_to_page(login_page.page_url)  # Step 1
    app.fill_input('xpath', login_page.inputs['login'], login_data.logins['correct_value'])  # Step 2
    app.click_button('xpath', login_page.buttons['login'])  # Step 3
    assert wd.current_url == login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', login_page.error_messages['missing_password'])
    assert wd.find_element(app.types['xpath'], login_page.error_messages['missing_password']).text == \
           login_data.error_message_value['missing_password']  # Assertion 2


def test_login_no_username_and_password(quit_session):
    app.navigate_to_page(login_page.page_url)  # Step 1
    app.click_button('xpath', login_page.buttons['login'])  # Step 2
    assert wd.current_url == login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', login_page.error_messages['missing_username'])
    app.wait_for_element_to_be_visible('xpath', login_page.error_messages['missing_password'])
    assert wd.find_element(app.types['xpath'], login_page.error_messages['missing_username']).text == \
           login_data.error_message_value['missing_username']  # Assertion 2
    assert wd.find_element(app.types['xpath'], login_page.error_messages['missing_password']).text == \
           login_data.error_message_value['missing_password']  # Assertion 2
