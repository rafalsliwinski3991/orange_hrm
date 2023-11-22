from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import repo.orange_hrm.pages.PIM_tab.add_employee_page as add_employee_page
import repo.orange_hrm.data.PIM_tab.add_employee_page as add_employee_data
import repo.orange_hrm.pages.PIM_tab.employee_tab.personal_details_page as personal_details_page
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
Test: test_adding_employee_successfully_without_login_details

PRECONDITIONS:
1. User with admin credentials exists and is logged in.
2. 'PIM' page/'Add Employee' subpage is displayed.

STEPS:
1. Fill the 'First Name' field. -> First name is entered.
2. Fill the 'Middle Name' field. -> Middle name is entered.
3. Fill the 'Last Name' field. -> Last name is entered.
4. Fill the 'Employee Id' field. -> Employee Id is entered.
5. Click the 'Save' button. -> Button is clicked, 'Personal Details' subpage is displayed.

ASSERTIONS:
1. Check if displayed 'Employee First Name' matches data entered in Step #1. 
2. Check if displayed 'Employee Middle Name' matches data entered in Step #2.
3. Check if displayed 'Employee Last Name' matches data entered in Step #3.
4. Check if displayed 'Employee Id' matches data entered in Step #4.
5. Check if avatar's header matches data entered in STEP #1 and #3.
"""


def test_adding_employee_successfully_without_login_details():
    app.login_to_app()  # Precondition 1
    page_base.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    page_base.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    page_base.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    page_base.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    page_base.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    page_base.click_button('xpath', add_employee_page.buttons['save'])  # Step 5
    page_base.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['first_name'])
    assert wd.find_element(page_base.types['xpath'], personal_details_page.inputs['first_name']).get_attribute('value')\
           == add_employee_data.inputs['first_name']  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['middle_name'])
    assert wd.find_element(page_base.types['xpath'],
                           personal_details_page.inputs['middle_name']).get_attribute('value') == \
           add_employee_data.inputs['middle_name']  # Assertion 2
    page_base.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['last_name'])
    assert wd.find_element(page_base.types['xpath'], personal_details_page.inputs['last_name']).get_attribute('value')\
           == add_employee_data.inputs['last_name']  # Assertion 3
    page_base.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['employee_id'])
    assert wd.find_element(page_base.types['xpath'],
                           personal_details_page.inputs['employee_id']).get_attribute('value') == \
           add_employee_data.inputs['employee_id']  # Assertion 4
    page_base.wait_for_text_to_be_present('xpath', personal_details_page.avatar_header, 'Thomas Anderson')
    assert wd.find_element(page_base.types['xpath'], personal_details_page.avatar_header).text \
           == add_employee_data.inputs['first_name'] + ' ' + add_employee_data.inputs['last_name']  # Assertion 5
    app.delete_user('employee_id', add_employee_data.inputs['employee_id'])
    app.logout_from_app()
    session.quit_session()


"""
Test: test_adding_employee_successfully_with_login_details

PRECONDITIONS:
1. User with admin credentials exists and is logged in.
2. 'PIM' page/'Add Employee' subpage is displayed.

STEPS:
1. Fill the 'First Name' field. -> First name is entered.
2. Fill the 'Middle Name' field. -> Middle name is entered.
3. Fill the 'Last Name' field. -> Last name is entered.
4. Fill the 'Employee Id' field. -> Employee Id is entered.
5. Click the 'Create Login Details' slider button. -> Login details section is displayed.
6. Fill the 'Username' field. -> Username is entered.
7. Fill the 'Password' field. -> Password is entered.
8. Fill the 'Confirm Password' field. -> Password is entered.
9. Click the 'Save' button. -> Button is clicked, 'Personal Details' subpage is displayed.

ASSERTIONS:
1. Check if displayed 'Employee First Name' matches data entered in Step #1. 
2. Check if displayed 'Employee Middle Name' matches data entered in Step #2.
3. Check if displayed 'Employee Last Name' matches data entered in Step #3.
4. Check if displayed 'Employee Id' matches data entered in Step #4.
5. Check if avatar's header matches data entered in STEP #1 and #3.
"""


def test_adding_employee_successfully_with_login_details():
    app.login_to_app()  # Precondition 1
    page_base.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    page_base.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    page_base.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    page_base.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    page_base.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    page_base.click_button('xpath', add_employee_page.buttons['create_login_details'])  # Step 5
    page_base.fill_input('xpath', add_employee_page.inputs['username'], add_employee_data.inputs['username'])  # Step 6
    page_base.fill_input('xpath', add_employee_page.inputs['password'], add_employee_data.inputs['password'])  # Step 7
    page_base.fill_input('xpath', add_employee_page.inputs['confirm_password'],
                         add_employee_data.inputs['confirm_password'])  # Step 8
    page_base.click_button('xpath', add_employee_page.buttons['save'])  # Step 9
    page_base.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['first_name'])
    assert wd.find_element(page_base.types['xpath'], personal_details_page.inputs['first_name']).get_attribute('value')\
           == add_employee_data.inputs['first_name']  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['middle_name'])
    assert wd.find_element(page_base.types['xpath'],
                           personal_details_page.inputs['middle_name']).get_attribute('value') == \
           add_employee_data.inputs['middle_name']  # Assertion 2
    page_base.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['last_name'])
    assert wd.find_element(page_base.types['xpath'], personal_details_page.inputs['last_name']).get_attribute('value')\
           == add_employee_data.inputs['last_name']  # Assertion 3
    page_base.wait_for_element_to_be_visible('xpath', personal_details_page.inputs['employee_id'])
    assert wd.find_element(page_base.types['xpath'],
                           personal_details_page.inputs['employee_id']).get_attribute('value') == \
           add_employee_data.inputs['employee_id']  # Assertion 4
    page_base.wait_for_text_to_be_present('xpath', personal_details_page.avatar_header, 'Thomas Anderson')
    assert wd.find_element(page_base.types['xpath'], personal_details_page.avatar_header).text \
           == add_employee_data.inputs['first_name'] + ' ' + add_employee_data.inputs['last_name']  # Assertion 5
    app.delete_user('employee_id', add_employee_data.inputs['employee_id'])
    app.logout_from_app()
    session.quit_session()


"""
Test: test_adding_employee_with_empty_login_details

PRECONDITIONS:
1. User with admin credentials exists and is logged in.
2. 'PIM' page/'Add Employee' subpage is displayed.

STEPS:
1. Fill the 'First Name' field. -> First name is entered.
2. Fill the 'Middle Name' field. -> Middle name is entered.
3. Fill the 'Last Name' field. -> Last name is entered.
4. Fill the 'Employee Id' field. -> Employee Id is entered.
5. Click the 'Create Login Details' slider button. -> Login details section is displayed.
6. Click the 'Save' button. -> Button is clicked, error messages are displayed beneath 'Username', 'Password' and 
'Confirm Password' inputs.

ASSERTIONS:
1. Check if current URL matches 'PIM' page/'Add Employee' subpage URL.
2. Check if displayed error messages texts are what they should be.
"""


def test_adding_employee_with_empty_login_details():
    app.login_to_app()  # Precondition 1
    page_base.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    page_base.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    page_base.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    page_base.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    page_base.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    page_base.click_button('xpath', add_employee_page.buttons['create_login_details'])  # Step 5
    page_base.click_button('xpath', add_employee_page.buttons['save'])  # Step 6
    assert wd.current_url == add_employee_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_username'])
    assert wd.find_element(page_base.types['xpath'], add_employee_page.error_messages['missing_username']).text == \
           add_employee_data.error_messages['missing_username']  # Assertion 2
    page_base.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_password'])
    assert wd.find_element(page_base.types['xpath'], add_employee_page.error_messages['missing_password']).text == \
           add_employee_data.error_messages['missing_password']  # Assertion 2
    page_base.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_password_confirmation'])
    assert wd.find_element(page_base.types['xpath'],
                           add_employee_page.error_messages['missing_password_confirmation']).text == \
           add_employee_data.error_messages['missing_password_confirmation']  # Assertion 2
    app.logout_from_app()
    session.quit_session()


"""
Test: test_adding_employee_cancelled_without_login_details_filled

PRECONDITIONS:
1. User with admin credentials exists and is logged in.
2. 'PIM' page/'Add Employee' subpage is displayed.

STEPS:
1. Fill the 'First Name' field. -> First name is entered.
2. Fill the 'Middle Name' field. -> Middle name is entered.
3. Fill the 'Last Name' field. -> Last name is entered.
4. Fill the 'Employee Id' field. -> Employee Id is entered.
5. Click the 'Cancel' button. -> Button is clicked, 'Employee List' subpage is displayed.

ASSERTIONS:
1. Check if current URL matches 'Employee List' subpage URL.
"""


def test_adding_employee_cancelled_without_login_details_filled():
    app.login_to_app()  # Precondition 1
    page_base.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    page_base.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    page_base.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    page_base.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    page_base.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    page_base.click_button('xpath', add_employee_page.buttons['cancel'])  # Step 5
    assert wd.current_url == personal_details_page.page_url  # Assertion 1
    app.logout_from_app()
    session.quit_session()


"""
Test: test_adding_employee_cancelled_with_login_details_filled

PRECONDITIONS:
1. User with admin credentials exists and is logged in.
2. 'PIM' page/'Add Employee' subpage is displayed.

STEPS:
1. Fill the 'First Name' field. -> First name is entered.
2. Fill the 'Middle Name' field. -> Middle name is entered.
3. Fill the 'Last Name' field. -> Last name is entered.
4. Fill the 'Employee Id' field. -> Employee Id is entered.
5. Click the 'Create Login Details' slider button. -> Login details section is displayed.
6. Fill the 'Username' field. -> Username is entered.
7. Fill the 'Password' field. -> Password is entered.
8. Fill the 'Confirm Password' field. -> Password is entered.
9. Click the 'Cancel' button. -> Button is clicked, 'Employee List' subpage is displayed.

ASSERTIONS:
1. Check if current URL matches 'Employee List' subpage URL.
"""


def test_adding_employee_cancelled_with_login_details_filled():
    app.login_to_app()  # Precondition 1
    page_base.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    page_base.fill_input('xpath', add_employee_page.inputs['first_name'], add_employee_data.inputs['first_name'])
    # Step 1
    page_base.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 2
    page_base.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 3
    app.clear_employee_id_input()
    page_base.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 4
    page_base.click_button('xpath', add_employee_page.buttons['create_login_details'])  # Step 5
    page_base.fill_input('xpath', add_employee_page.inputs['username'], add_employee_data.inputs['username'])  # Step 6
    page_base.fill_input('xpath', add_employee_page.inputs['password'], add_employee_data.inputs['password'])  # Step 7
    page_base.fill_input('xpath', add_employee_page.inputs['confirm_password'],
                         add_employee_data.inputs['confirm_password'])  # Step 8
    page_base.click_button('xpath', add_employee_page.buttons['cancel'])  # Step 9
    assert wd.current_url == personal_details_page.page_url  # Assertion 1
    app.logout_from_app()
    session.quit_session()


"""
Test: test_adding_employee_without_first_name

PRECONDITIONS:
1. User with admin credentials exists and is logged in.
2. 'PIM' page/'Add Employee' subpage is displayed.

STEPS:
1. Fill the 'Middle Name' field. -> Middle name is entered.
2. Fill the 'Last Name' field. -> Last name is entered.
3. Fill the 'Employee Id' field. -> Employee Id is entered.
4. Click the 'Save' button. -> Button is clicked, error message beneath 'First Name' input is displayed.

ASSERTIONS:
1. Check if current URL matches 'PIM' page/'Add Employee' subpage URL.
2. Check if displayed error message text is what it should be.
"""


def test_adding_employee_without_first_name():
    app.login_to_app()  # Precondition 1
    page_base.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    page_base.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 1
    page_base.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 2
    app.clear_employee_id_input()
    page_base.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 3
    page_base.click_button('xpath', add_employee_page.buttons['save'])  # Step 4
    assert wd.current_url == add_employee_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_first_name'])
    assert wd.find_element(page_base.types['xpath'], add_employee_page.error_messages['missing_first_name']).text == \
           add_employee_data.error_messages['missing_first_name']  # Assertion 2
    app.logout_from_app()
    session.quit_session()


"""
Test: test_adding_employee_without_last_name

PRECONDITIONS:
1. User with admin credentials exists and is logged in.
2. 'PIM' page/'Add Employee' subpage is displayed.

STEPS:
1. Fill the 'First Name' field. -> First name is entered.
2. Fill the 'Middle Name' field. -> Middle name is entered.
3. Fill the 'Employee Id' field. -> Employee Id is entered.
4. Click the 'Save' button. -> Button is clicked, error message beneath 'Last Name' input is displayed.

ASSERTIONS:
1. Check if current URL matches 'PIM' page/'Add Employee' subpage URL.
2. Check if displayed error message text is what it should be.
"""


def test_adding_employee_without_last_name():
    app.login_to_app()  # Precondition 1
    page_base.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    page_base.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 1
    page_base.fill_input('xpath', add_employee_page.inputs['last_name'], add_employee_data.inputs['last_name'])
    # Step 2
    app.clear_employee_id_input()
    page_base.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 3
    page_base.click_button('xpath', add_employee_page.buttons['save'])  # Step 4
    assert wd.current_url == add_employee_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_first_name'])
    assert wd.find_element(page_base.types['xpath'], add_employee_page.error_messages['missing_first_name']).text == \
           add_employee_data.error_messages['missing_first_name']  # Assertion 2
    app.logout_from_app()
    session.quit_session()


"""
Test: test_adding_employee_without_first_and_last_name

PRECONDITIONS:
1. User with admin credentials exists and is logged in.
2. 'PIM' page/'Add Employee' subpage is displayed.

STEPS:
1. Fill the 'Middle Name' field. -> Middle name is entered.
2. Fill the 'Employee Id' field. -> Employee Id is entered.
3. Click the 'Save' button. -> Button is clicked, error messages beneath 'First Name' and 'Last Name' inputs are 
displayed.

ASSERTIONS:
1. Check if current URL matches 'PIM' page/'Add Employee' subpage URL.
2. Check if displayed error messages texts are what they should be. 
"""


def test_adding_employee_without_first_and_last_name():
    app.login_to_app()  # Precondition 1
    page_base.navigate_to_page(add_employee_page.page_url)  # Precondition 2
    page_base.fill_input('xpath', add_employee_page.inputs['middle_name'], add_employee_data.inputs['middle_name'])
    # Step 1
    app.clear_employee_id_input()
    page_base.fill_input('xpath', add_employee_page.inputs['employee_id'], add_employee_data.inputs['employee_id'])
    # Step 2
    page_base.click_button('xpath', add_employee_page.buttons['save'])  # Step 3
    assert wd.current_url == add_employee_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_first_name'])
    assert wd.find_element(page_base.types['xpath'], add_employee_page.error_messages['missing_first_name']).text == \
           add_employee_data.error_messages['missing_first_name']  # Assertion 2
    page_base.wait_for_element_to_be_visible('xpath', add_employee_page.error_messages['missing_last_name'])
    assert wd.find_element(page_base.types['xpath'], add_employee_page.error_messages['missing_last_name']).text == \
           add_employee_data.error_messages['missing_last_name']  # Assertion 2
    app.logout_from_app()
    session.quit_session()
