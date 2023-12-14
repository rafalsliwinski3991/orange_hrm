import pytest
from repo.orange_hrm.fixture.application import Application

app = Application(10)


@pytest.fixture()
def quit_session(request):
    fixture = Application(10)
    request.addfinalizer(app.quit_session)
    return fixture


def test_password_reset_successful():
    app.navigate_to_page(app.login_page.page_url)  # Precondition 2
    app.click_link('xpath', app.login_page.links['forgot_your_password'])  # Step 1
    app.fill_input('xpath', app.pwd_reset_page.inputs['username'], app.login_data.logins['correct_value'])  # Step 2
    app.click_button('xpath', app.pwd_reset_page.buttons['reset_password'])  # Step 3
    assert app.wd.current_url == app.pwd_confirmed_reset_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.pwd_confirmed_reset_page.modal_header)
    assert app.wd.find_element(app.types['xpath'], app.pwd_confirmed_reset_page.modal_header).is_displayed()
    # Assertion 2


def test_password_reset_cancelled_with_username_not_filled():
    app.navigate_to_page(app.login_page.page_url)  # Precondition 2
    app.click_link('xpath', app.login_page.links['forgot_your_password'])  # Step 1
    app.click_button('xpath', app.pwd_reset_page.buttons['cancel'])  # Step 2
    assert app.wd.current_url == app.login_page.page_url  # Assertion 1


def test_password_reset_cancelled_with_username_filled():
    app.navigate_to_page(app.login_page.page_url)  # Precondition 2
    app.click_link('xpath', app.login_page.links['forgot_your_password'])  # Step 1
    app.fill_input('xpath', app.pwd_reset_page.inputs['username'], app.login_data.logins['correct_value'])  # Step 2
    app.click_button('xpath', app.pwd_reset_page.buttons['cancel'])  # Step 3
    assert app.wd.current_url == app.login_page.page_url  # Assertion 1


def test_password_reset_empty_username(quit_session):
    app.navigate_to_page(app.login_page.page_url)  # Precondition 2
    app.click_link('xpath', app.login_page.links['forgot_your_password'])  # Step 1
    app.click_button('xpath', app.pwd_reset_page.buttons['reset_password'])  # Step 2
    assert app.wd.current_url == app.pwd_reset_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.pwd_reset_page.error_messages['missing_username'])
    assert app.wd.find_element(app.types['xpath'], app.pwd_reset_page.error_messages['missing_username']).text == \
           app.pwd_reset_data.error_messages['missing_username']  # Assertion 2
