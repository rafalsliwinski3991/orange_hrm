from selenium.webdriver.common.keys import Keys
from repo.orange_hrm.fixture.session import SessionHelper


class Application(SessionHelper):

    def clear_employee_id_input(self):
        employee_id_len = len(self.wd.find_element(self.types['xpath'],
                                                   self.add_employee_page.inputs['employee_id']).get_attribute('value'))
        for i in range(employee_id_len):
            self.wd.find_element(self.types['xpath'],
                                 self.add_employee_page.inputs['employee_id']).send_keys(Keys.BACKSPACE)

    def add_employee(self, details, first_name='', middle_name='', last_name='', employee_id='',
                     username='', password='', confirm_password=''):
        self.navigate_to_page(self.add_employee_page.page_url)
        if details == 'yes':
            self.fill_input('xpath', self.add_employee_page.inputs['first_name'], first_name)
            self.fill_input('xpath', self.add_employee_page.inputs['middle_name'], middle_name)
            self.fill_input('xpath', self.add_employee_page.inputs['last_name'], last_name)
            self.clear_employee_id_input()
            self.fill_input('xpath', self.add_employee_page.inputs['employee_id'], employee_id)
            self.click_button('xpath', self.add_employee_page.buttons['create_login_details'])
            self.fill_input('xpath', self.add_employee_page.inputs['username'], username)
            self.fill_input('xpath', self.add_employee_page.inputs['password'], password)
            self.fill_input('xpath', self.add_employee_page.inputs['confirm_password'], confirm_password)
        else:
            self.fill_input('xpath', self.add_employee_page.inputs['first_name'], first_name)
            self.fill_input('xpath', self.add_employee_page.inputs['middle_name'], middle_name)
            self.fill_input('xpath', self.add_employee_page.inputs['last_name'], last_name)
            self.clear_employee_id_input()
            self.fill_input('xpath', self.add_employee_page.inputs['employee_id'], employee_id)
        self.click_button('xpath', self.add_employee_page.buttons['save'])
