import pytest
from repo.orange_hrm.fixture.application import Application

app = Application(10)


@pytest.fixture()
def logout(request):
    fixture = Application(10)
    request.addfinalizer(app.logout_from_app)
    return fixture


@pytest.fixture()
def quit_session(request):
    fixture = Application(10)
    request.addfinalizer(app.quit_session)
    return fixture


def test_login_successful(logout):
    app.navigate_to_page(app.login_page.page_url)  # Step 1
    app.fill_input('xpath', app.login_page.inputs['login'], app.login_data.logins['correct_value'])  # Step 2
    app.fill_input('xpath', app.login_page.inputs['password'], app.login_data.passwords['correct_value'])  # Step 3
    app.click_button('xpath', app.login_page.buttons['login'])  # Step 4
    assert app.wd.current_url == app.dashboard_page.page_url  # Assertion 1


def test_login_incorrect_username():
    app.navigate_to_page(app.login_page.page_url)  # Step 1
    app.fill_input('xpath', app.login_page.inputs['login'], app.login_data.logins['incorrect_value'])  # Step 2
    app.fill_input('xpath', app.login_page.inputs['password'], app.login_data.passwords['correct_value'])  # Step 3
    app.click_button('xpath', app.login_page.buttons['login'])  # Step 4
    assert app.wd.current_url == app.login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.login_page.error_messages['invalid_credentials'])
    assert app.wd.find_element(app.types['xpath'], app.login_page.error_messages['invalid_credentials']).text == \
           app.login_data.error_message_value['invalid_credentials']  # Assertion 2


def test_login_incorrect_password():
    app.navigate_to_page(app.login_page.page_url)  # Step 1
    app.fill_input('xpath', app.login_page.inputs['login'], app.login_data.logins['correct_value'])  # Step 2
    app.fill_input('xpath', app.login_page.inputs['password'], app.login_data.passwords['incorrect_value'])  # Step 3
    app.click_button('xpath', app.login_page.buttons['login'])  # Step 4
    assert app.wd.current_url == app.login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.login_page.error_messages['invalid_credentials'])
    assert app.wd.find_element(app.types['xpath'], app.login_page.error_messages['invalid_credentials']).text == \
           app.login_data.error_message_value['invalid_credentials']  # Assertion 2


def test_login_no_username():
    app.navigate_to_page(app.login_page.page_url)  # Step 1
    app.fill_input('xpath', app.login_page.inputs['password'], app.login_data.passwords['correct_value'])  # Step 2
    app.click_button('xpath', app.login_page.buttons['login'])  # Step 3
    assert app.wd.current_url == app.login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.login_page.error_messages['missing_username'])
    assert app.wd.find_element(app.types['xpath'], app.login_page.error_messages['missing_username']).text == \
           app.login_data.error_message_value['missing_username']  # Assertion 2


def test_login_no_password():
    app.navigate_to_page(app.login_page.page_url)  # Step 1
    app.fill_input('xpath', app.login_page.inputs['login'], app.login_data.logins['correct_value'])  # Step 2
    app.click_button('xpath', app.login_page.buttons['login'])  # Step 3
    assert app.wd.current_url == app.login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.login_page.error_messages['missing_password'])
    assert app.wd.find_element(app.types['xpath'], app.login_page.error_messages['missing_password']).text == \
           app.login_data.error_message_value['missing_password']  # Assertion 2


def test_login_no_username_and_password(quit_session):
    app.navigate_to_page(app.login_page.page_url)  # Step 1
    app.click_button('xpath', app.login_page.buttons['login'])  # Step 2
    assert app.wd.current_url == app.login_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.login_page.error_messages['missing_username'])
    app.wait_for_element_to_be_visible('xpath', app.login_page.error_messages['missing_password'])
    assert app.wd.find_element(app.types['xpath'], app.login_page.error_messages['missing_username']).text == \
           app.login_data.error_message_value['missing_username']  # Assertion 2
    assert app.wd.find_element(app.types['xpath'], app.login_page.error_messages['missing_password']).text == \
           app.login_data.error_message_value['missing_password']  # Assertion 2
