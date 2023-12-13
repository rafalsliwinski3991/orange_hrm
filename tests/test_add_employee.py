from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import repo.orange_hrm.pages.PIM_tab.add_employee_page as add_employee_page
import repo.orange_hrm.data.PIM_tab.add_employee_page as add_employee_data
import repo.orange_hrm.pages.PIM_tab.employee_tab.personal_details_page as personal_details_page
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
def cleanup(request):
    fixture = Application(wd, 10)
    request.addfinalizer(app.cleanup)
    return fixture


@pytest.fixture()
def quit_session(request):
    fixture = Application(wd, 10)
    request.addfinalizer(app.quit_session)
    return fixture


def test_adding_employee_successfully_without_login_details(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', add_employee_page.buttons['save'])  # Step 5
    app.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['first_name'])
    assert wd.find_element(app.types['xpath'], personal_details_page.inputs['first_name']).get_attribute('value')\
           == add_employee_data.inputs['first_name']  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['middle_name'])
    assert wd.find_element(app.types['xpath'],
                           personal_details_page.inputs['middle_name']).get_attribute('value') == \
           add_employee_data.inputs['middle_name']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['last_name'])
    assert wd.find_element(app.types['xpath'], personal_details_page.inputs['last_name']).get_attribute('value')\
           == add_employee_data.inputs['last_name']  # Assertion 3
    app.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['employee_id'])
    assert wd.find_element(app.types['xpath'],
                           personal_details_page.inputs['employee_id']).get_attribute('value') == \
           add_employee_data.inputs['employee_id']  # Assertion 4
    app.wait_for_text_to_be_present('xpath', personal_details_page.avatar_header, 'Thomas Anderson')
    assert wd.find_element(app.types['xpath'], personal_details_page.avatar_header).text \
           == add_employee_data.inputs['first_name'] + ' ' + add_employee_data.inputs['last_name']  # Assertion 5


def test_adding_employee_successfully_with_login_details(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', add_employee_page.buttons['create_login_details'])  # Step 5
    app.fill_input('xpath', add_employee_page.inputs['username'], add_employee_data.inputs['username'])  # Step 6
    app.fill_input('xpath', add_employee_page.inputs['password'], add_employee_data.inputs['password'])  # Step 7
    app.fill_input('xpath', add_employee_page.inputs['confirm_password'],
                   add_employee_data.inputs['confirm_password'])  # Step 8
    app.click_button('xpath', add_employee_page.buttons['save'])  # Step 9
    app.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['first_name'])
    assert wd.find_element(app.types['xpath'], personal_details_page.inputs['first_name']).get_attribute('value')\
           == add_employee_data.inputs['first_name']  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['middle_name'])
    assert wd.find_element(app.types['xpath'],
                           personal_details_page.inputs['middle_name']).get_attribute('value') == \
           add_employee_data.inputs['middle_name']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['last_name'])
    assert wd.find_element(app.types['xpath'], personal_details_page.inputs['last_name']).get_attribute('value')\
           == add_employee_data.inputs['last_name']  # Assertion 3
    app.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['employee_id'])
    assert wd.find_element(app.types['xpath'],
                           personal_details_page.inputs['employee_id']).get_attribute('value') == \
           add_employee_data.inputs['employee_id']  # Assertion 4
    app.wait_for_text_to_be_present('xpath', personal_details_page.avatar_header, 'Thomas Anderson')
    assert wd.find_element(app.types['xpath'], personal_details_page.avatar_header).text \
           == add_employee_data.inputs['first_name'] + ' ' + add_employee_data.inputs['last_name']  # Assertion 5


def test_adding_employee_with_empty_login_details(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', add_employee_page.buttons['create_login_details'])  # Step 5
    app.click_button('xpath', add_employee_page.buttons['save'])  # Step 6
    assert wd.current_url == add_employee_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_username'])
    assert wd.find_element(app.types['xpath'], add_employee_page.error_messages['missing_username']).text == \
           add_employee_data.error_messages['missing_username']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_password'])
    assert wd.find_element(app.types['xpath'], add_employee_page.error_messages['missing_password']).text == \
           add_employee_data.error_messages['missing_password']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_password_confirmation'])
    assert wd.find_element(app.types['xpath'],
                           add_employee_page.error_messages['missing_password_confirmation']).text == \
           add_employee_data.error_messages['missing_password_confirmation']  # Assertion 2


def test_adding_employee_cancelled_without_login_details_filled(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', add_employee_page.buttons['cancel'])  # Step 5
    assert wd.current_url == personal_details_page.page_url  # Assertion 1


def test_adding_employee_cancelled_with_login_details_filled(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    app.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    app.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    app.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    app.click_button('xpath', add_employee_page.buttons['create_login_details'])  # Step 5
    app.fill_input('xpath', add_employee_page.inputs['username'], add_employee_data.inputs['username'])  # Step 6
    app.fill_input('xpath', add_employee_page.inputs['password'], add_employee_data.inputs['password'])  # Step 7
    app.fill_input('xpath', add_employee_page.inputs['confirm_password'],
                   add_employee_data.inputs['confirm_password'])  # Step 8
    app.click_button('xpath', add_employee_page.buttons['cancel'])  # Step 9
    assert wd.current_url == personal_details_page.page_url  # Assertion 1


def test_adding_employee_without_first_name(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 1
    app.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 2
    app.clear_employee_id_input()
    app.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 3
    app.click_button('xpath', add_employee_page.buttons['save'])  # Step 4
    assert wd.current_url == add_employee_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_first_name'])
    assert wd.find_element(app.types['xpath'], add_employee_page.error_messages['missing_first_name']).text == \
           add_employee_data.error_messages['missing_first_name']  # Assertion 2


def test_adding_employee_without_last_name(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 1
    app.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 2
    app.clear_employee_id_input()
    app.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 3
    app.click_button('xpath', add_employee_page.buttons['save'])  # Step 4
    assert wd.current_url == add_employee_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_first_name'])
    assert wd.find_element(app.types['xpath'], add_employee_page.error_messages['missing_first_name']).text == \
           add_employee_data.error_messages['missing_first_name']  # Assertion 2


def test_adding_employee_without_first_and_last_name(quit_session):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    app.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 1
    app.clear_employee_id_input()
    app.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 2
    app.click_button('xpath', add_employee_page.buttons['save'])  # Step 3
    assert wd.current_url == add_employee_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_first_name'])
    assert wd.find_element(app.types['xpath'], add_employee_page.error_messages['missing_first_name']).text == \
           add_employee_data.error_messages['missing_first_name']  # Assertion 2
    app.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_last_name'])
    assert wd.find_element(app.types['xpath'], add_employee_page.error_messages['missing_last_name']).text == \
           add_employee_data.error_messages['missing_last_name']  # Assertion 2
    app.logout_from_app()
