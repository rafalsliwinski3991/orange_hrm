from repo.orange_hrm.fixture.page_base import PageBase


class SessionHelper(PageBase):

    def login_to_app_as(self, role, login_value='', password_value=''):
        self.navigate_to_page(self.login_page.page_url)
        if role == 'admin':
            self.fill_input('xpath', self.login_page.inputs['login'], self.login_data.logins['correct_value'])
            self.fill_input('xpath', self.login_page.inputs['password'], self.login_data.passwords['correct_value'])
        elif role == 'employee':
            self.fill_input('xpath', self.login_page.inputs['login'], login_value)
            self.fill_input('xpath', self.login_page.inputs['password'], password_value)
        self.click_button('xpath', self.login_page.buttons['login'])

    def login_to_app_as_admin(self):
        self.navigate_to_page(self.login_page.page_url)
        self.fill_input('xpath', self.login_page.inputs['login'], self.login_data.logins['correct_value'])
        self.fill_input('xpath', self.login_page.inputs['password'], self.login_data.passwords['correct_value'])
        self.click_button('xpath', self.login_page.buttons['login'])

    def login_to_app_as_employee(self, login_value, password_value):
        self.navigate_to_page(self.login_page.page_url)
        self.fill_input('xpath', self.login_page.inputs['login'], login_value)
        self.fill_input('xpath', self.login_page.inputs['password'], password_value)
        self.click_button('xpath', self.login_page.buttons['login'])

    def logout_from_app(self):
        self.click_element('xpath', self.header.user_dropdown)
        self.click_element('xpath', self.header.logout_option)

    def find_employee_by(self, search_criteria, value):
        self.navigate_to_page(self.employee_list_page.page_url)
        if search_criteria == 'employee_id':
            self.fill_input('xpath', self.employee_list_page.inputs['employee_id'], value)
        self.click_button('xpath', self.employee_list_page.buttons['search'])

    def delete_employee(self, search_criteria, value):
        self.find_employee_by(search_criteria, value)
        self.wait_for_text_to_be_present('xpath', '//div[text()="{}"]'.format(value), value)
        if self.wd.find_element('xpath', '//span[text()="(1) Record Found"]').get_attribute('innerText') == \
                '(1) Record Found':
            self.click_button('xpath', self.employee_list_page.icons['delete'])
            self.click_button('xpath', self.employee_list_page.buttons['removal_confirmation'])
        else:
            pass

    def cleanup(self):
        self.delete_employee('employee_id', self.add_employee_data.inputs['employee_id'])
        self.logout_from_app()

    def quit_session(self):
        self.wd.quit()
