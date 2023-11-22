from selenium.webdriver.common.keys import Keys
from repo.orange_hrm.fixture.page_base import PageBase
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.header as header
import repo.orange_hrm.pages.PIM_tab.add_employee_page as add_employee_page
import repo.orange_hrm.pages.PIM_tab.employee_list_page as employee_list_page


class Application(PageBase):

    def login_to_app(self):
        self.navigate_to_page(login_page.page_url)
        self.fill_input('xpath', login_page.inputs['login'], login_data.logins['correct_value'])
        self.fill_input('xpath', login_page.inputs['password'], login_data.passwords['correct_value'])
        self.click_button('xpath', login_page.buttons['login'])

    def logout_from_app(self):
        self.click_element('xpath', header.user_dropdown)
        self.click_element('xpath', header.logout_option)

    def clear_employee_id_input(self):
        employee_id_len = len(self.wd.find_element(self.types['xpath'],
                                                   add_employee_page.inputs['employee_id']).get_attribute('value'))
        for i in range(employee_id_len):
            self.wd.find_element(self.types['xpath'],
                                 add_employee_page.inputs['employee_id']).send_keys(Keys.BACKSPACE)

    def find_user_by(self, search_criteria, value):
        self.navigate_to_page(employee_list_page.page_url)
        if search_criteria == 'employee_id':
            self.fill_input('xpath', employee_list_page.inputs['employee_id'], value)
        self.click_button('xpath', employee_list_page.buttons['search'])

    def delete_user(self, search_criteria, value):
        self.find_user_by(search_criteria, value)
        self.wait_for_text_to_be_present('xpath', '//div[text()="{}"]'.format(value), value)
        if self.wd.find_element('xpath', '//span[text()="(1) Record Found"]').get_attribute('innerText') == \
                '(1) Record Found':
            self.click_button('xpath', employee_list_page.icons['delete'])
            self.click_button('xpath', employee_list_page.buttons['removal_confirmation'])
        else:
            pass
