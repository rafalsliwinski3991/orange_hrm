from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import repo.orange_hrm.pages.header as header
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.dashboard_page as dashboard_page
import repo.orange_hrm.pages.password_reset_page as pwd_reset_page
import repo.orange_hrm.pages.PIM_tab.add_employee_page as add_employee_page
import repo.orange_hrm.pages.password_reset_confirmation_page as pwd_confirmed_reset_page
import repo.orange_hrm.pages.PIM_tab.employee_list_page as employee_list_page
import repo.orange_hrm.pages.PIM_tab.employee_tab.personal_details_page as personal_details_page
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.data.password_reset_page as pwd_reset_data
import repo.orange_hrm.data.PIM_tab.add_employee_page as add_employee_data


class PageBase:

    types = {
        'name': By.NAME,
        'id': By.ID,
        'xpath': By.XPATH
    }

    def __init__(self, wait):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wait = wait
        self.header = header
        self.login_page = login_page
        self.dashboard_page = dashboard_page
        self.pwd_reset_page = pwd_reset_page
        self.pwd_confirmed_reset_page = pwd_confirmed_reset_page
        self.add_employee_page = add_employee_page
        self.employee_list_page = employee_list_page
        self.personal_details_page = personal_details_page
        self.login_data = login_data
        self.pwd_reset_data = pwd_reset_data
        self.add_employee_data = add_employee_data

    def navigate_to_page(self, page_url):
        self.wd.get(page_url)

    def wait_for_element_to_be_visible(self, locator_type, locator_value):
        wait = WebDriverWait(self.wd, 10)
        wait.until(EC.visibility_of_element_located((self.types[locator_type], locator_value)))

    def wait_for_text_to_be_present(self, locator_type, locator_value, desired_text):
        wait = WebDriverWait(self.wd, 10)
        wait.until(EC.text_to_be_present_in_element((self.types[locator_type], locator_value), desired_text))

    def click_element(self, locator_type, locator_value):
        wait = WebDriverWait(self.wd, 10)
        wait.until(EC.element_to_be_clickable((self.types[locator_type], locator_value)))
        self.wd.find_element(self.types[locator_type], locator_value).click()

    def fill_input(self, locator_type, locator_value, data_value):
        self.click_element(self.types[locator_type], locator_value)
        self.wd.find_element(self.types[locator_type], locator_value).clear()
        self.wd.find_element(self.types[locator_type], locator_value).send_keys(data_value)

    def click_button(self, locator_type, locator_value):
        self.click_element(self.types[locator_type], locator_value)

    def click_link(self, locator_type, locator_value):
        self.click_element(self.types[locator_type], locator_value)
