import pytest
from repo.orange_hrm.fixture.application import Application

app = Application(10)


@pytest.fixture()
def logout(request):
    fixture = Application(10)
    request.addfinalizer(app.logout_from_app)
    return fixture


@pytest.fixture()
def cleanup(request):
    fixture = Application(10)
    request.addfinalizer(app.cleanup)
    return fixture


@pytest.fixture()
def quit_session(request):
    fixture = Application(10)
    request.addfinalizer(app.quit_session)
    return fixture


def test_adding_employee_successfully_without_login_details(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', app.add_employee_page.inputs['first_name'], app.add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', app.add_employee_page.inputs['middle_name'], app.add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', app.add_employee_page.inputs['last_name'], app.add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', app.add_employee_page.inputs['employee_id'], app.add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', app.add_employee_page.buttons['save'])  # Step 5
    app.wait_for_element_to_be_visible('xpath', app.personal_details_page.inputs['first_name'])
    assert app.wd.find_element(app.types['xpath'],
                               app.personal_details_page.inputs['first_name']).get_attribute('value')\
           == app.add_employee_data.inputs['first_name']  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.personal_details_page.inputs['middle_name'])
    assert app.wd.find_element(app.types['xpath'],
                               app.personal_details_page.inputs['middle_name']).get_attribute('value') == \
           app.add_employee_data.inputs['middle_name']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', app.personal_details_page.inputs['last_name'])
    assert app.wd.find_element(app.types['xpath'],
                               app.personal_details_page.inputs['last_name']).get_attribute('value') == \
           app.add_employee_data.inputs['last_name']  # Assertion 3
    app.wait_for_element_to_be_visible('xpath', app.personal_details_page.inputs['employee_id'])
    assert app.wd.find_element(app.types['xpath'],
                               app.personal_details_page.inputs['employee_id']).get_attribute('value') == \
           app.add_employee_data.inputs['employee_id']  # Assertion 4
    app.wait_for_text_to_be_present('xpath', app.personal_details_page.avatar_header, 'Thomas Anderson')
    assert app.wd.find_element(app.types['xpath'], app.personal_details_page.avatar_header).text == \
           app.add_employee_data.inputs['first_name'] + ' ' + app.add_employee_data.inputs['last_name']  # Assertion 5


def test_adding_employee_successfully_with_login_details(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', app.add_employee_page.inputs['first_name'], app.add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', app.add_employee_page.inputs['middle_name'], app.add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', app.add_employee_page.inputs['last_name'], app.add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', app.add_employee_page.inputs['employee_id'], app.add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', app.add_employee_page.buttons['create_login_details'])  # Step 5
    app.fill_input('xpath', app.add_employee_page.inputs['username'],
                   app.add_employee_data.inputs['username'])  # Step 6
    app.fill_input('xpath', app.add_employee_page.inputs['password'],
                   app.add_employee_data.inputs['password'])  # Step 7
    app.fill_input('xpath', app.add_employee_page.inputs['confirm_password'],
                   app.add_employee_data.inputs['confirm_password'])  # Step 8
    app.click_button('xpath', app.add_employee_page.buttons['save'])  # Step 9
    app.wait_for_element_to_be_visible('xpath', app.personal_details_page.inputs['first_name'])
    assert app.wd.find_element(app.types['xpath'],
                               app.personal_details_page.inputs['first_name']).get_attribute('value') == \
           app.add_employee_data.inputs['first_name']  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.personal_details_page.inputs['middle_name'])
    assert app.wd.find_element(app.types['xpath'],
                               app.personal_details_page.inputs['middle_name']).get_attribute('value') == \
           app.add_employee_data.inputs['middle_name']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', app.personal_details_page.inputs['last_name'])
    assert app.wd.find_element(app.types['xpath'],
                               app.personal_details_page.inputs['last_name']).get_attribute('value') == \
           app.add_employee_data.inputs['last_name']  # Assertion 3
    app.wait_for_element_to_be_visible('xpath', app.personal_details_page.inputs['employee_id'])
    assert app.wd.find_element(app.types['xpath'],
                               app.personal_details_page.inputs['employee_id']).get_attribute('value') == \
           app.add_employee_data.inputs['employee_id']  # Assertion 4
    app.wait_for_text_to_be_present('xpath', app.personal_details_page.avatar_header, 'Thomas Anderson')
    assert app.wd.find_element(app.types['xpath'], app.personal_details_page.avatar_header).text == \
           app.add_employee_data.inputs['first_name'] + ' ' + app.add_employee_data.inputs['last_name']  # Assertion 5


def test_adding_employee_with_empty_login_details(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', app.add_employee_page.inputs['first_name'], app.add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', app.add_employee_page.inputs['middle_name'], app.add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', app.add_employee_page.inputs['last_name'], app.add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', app.add_employee_page.inputs['employee_id'], app.add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', app.add_employee_page.buttons['create_login_details'])  # Step 5
    app.click_button('xpath', app.add_employee_page.buttons['save'])  # Step 6
    assert app.wd.current_url == app.add_employee_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.add_employee_page.error_messages['missing_username'])
    assert app.wd.find_element(app.types['xpath'], app.add_employee_page.error_messages['missing_username']).text == \
           app.add_employee_data.error_messages['missing_username']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', app.add_employee_page.error_messages['missing_password'])
    assert app.wd.find_element(app.types['xpath'], app.add_employee_page.error_messages['missing_password']).text == \
           app.add_employee_data.error_messages['missing_password']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', app.add_employee_page.error_messages['missing_password_confirmation'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_employee_page.error_messages['missing_password_confirmation']).text == \
           app.add_employee_data.error_messages['missing_password_confirmation']  # Assertion 2


def test_adding_employee_cancelled_without_login_details_filled(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', app.add_employee_page.inputs['first_name'], app.add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', app.add_employee_page.inputs['middle_name'], app.add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', app.add_employee_page.inputs['last_name'], app.add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', app.add_employee_page.inputs['employee_id'], app.add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', app.add_employee_page.buttons['cancel'])  # Step 5
    assert app.wd.current_url == app.personal_details_page.page_url  # Assertion 1


def test_adding_employee_cancelled_with_login_details_filled(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', app.add_employee_page.inputs['first_name'], app.add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', app.add_employee_page.inputs['middle_name'], app.add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', app.add_employee_page.inputs['last_name'], app.add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', app.add_employee_page.inputs['employee_id'], app.add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', app.add_employee_page.buttons['create_login_details'])  # Step 5
    app.fill_input('xpath', app.add_employee_page.inputs['username'],
                   app.add_employee_data.inputs['username'])  # Step 6
    app.fill_input('xpath', app.add_employee_page.inputs['password'],
                   app.add_employee_data.inputs['password'])  # Step 7
    app.fill_input('xpath', app.add_employee_page.inputs['confirm_password'],
                   app.add_employee_data.inputs['confirm_password'])  # Step 8
    app.click_button('xpath', app.add_employee_page.buttons['cancel'])  # Step 9
    assert app.wd.current_url == app.personal_details_page.page_url  # Assertion 1


def test_adding_employee_without_first_name(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', app.add_employee_page.inputs['middle_name'], app.add_employee_data.inputs['middle_name'])
    # Step 1
    app.fill_input('xpath', app.add_employee_page.inputs['last_name'], app.add_employee_data.inputs['last_name'])
    # Step 2
    app.clear_employee_id_input()
    app.fill_input('xpath', app.add_employee_page.inputs['employee_id'], app.add_employee_data.inputs['employee_id'])
    # Step 3
    app.click_button('xpath', app.add_employee_page.buttons['save'])  # Step 4
    assert app.wd.current_url == app.add_employee_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.add_employee_page.error_messages['missing_first_name'])
    assert app.wd.find_element(app.types['xpath'], app.add_employee_page.error_messages['missing_first_name']).text == \
           app.add_employee_data.error_messages['missing_first_name']  # Assertion 2


def test_adding_employee_without_last_name(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', app.add_employee_page.inputs['middle_name'], app.add_employee_data.inputs['middle_name'])
    # Step 1
    app.fill_input('xpath', app.add_employee_page.inputs['last_name'], app.add_employee_data.inputs['last_name'])
    # Step 2
    app.clear_employee_id_input()
    app.fill_input('xpath', app.add_employee_page.inputs['employee_id'], app.add_employee_data.inputs['employee_id'])
    # Step 3
    app.click_button('xpath', app.add_employee_page.buttons['save'])  # Step 4
    assert app.wd.current_url == app.add_employee_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.add_employee_page.error_messages['missing_first_name'])
    assert app.wd.find_element(app.types['xpath'], app.add_employee_page.error_messages['missing_first_name']).text == \
           app.add_employee_data.error_messages['missing_first_name']  # Assertion 2


def test_adding_employee_without_first_and_last_name(quit_session):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', app.add_employee_page.inputs['middle_name'], app.add_employee_data.inputs['middle_name'])
    # Step 1
    app.clear_employee_id_input()
    app.fill_input('xpath', app.add_employee_page.inputs['employee_id'], app.add_employee_data.inputs['employee_id'])
    # Step 2
    app.click_button('xpath', app.add_employee_page.buttons['save'])  # Step 3
    assert app.wd.current_url == app.add_employee_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.add_employee_page.error_messages['missing_first_name'])
    assert app.wd.find_element(app.types['xpath'], app.add_employee_page.error_messages['missing_first_name']).text == \
           app.add_employee_data.error_messages['missing_first_name']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', app.add_employee_page.error_messages['missing_last_name'])
    assert app.wd.find_element(app.types['xpath'], app.add_employee_page.error_messages['missing_last_name']).text == \
           app.add_employee_data.error_messages['missing_last_name']  # Assertion 2
    app.logout_from_app()
