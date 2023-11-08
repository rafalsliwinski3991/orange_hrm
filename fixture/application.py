from repo.orange_hrm.fixture.page_base import PageBase
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.header as header


class Application(PageBase):

    def enter_username(self, locator_value, username_value):
        self.fill_input('xpath', locator_value, username_value)

    def enter_password(self, locator_value, password_value):
        self.fill_input('xpath', locator_value, password_value)

    def login_to_app(self):
        self.navigate_to_page(login_page.page_url)
        self.enter_username(login_page.inputs['login'], login_data.logins['correct_value'])
        self.enter_password(login_page.inputs['password'], login_data.passwords['correct_value'])
        self.click_button('xpath', login_page.buttons['login'])

    def logout_from_app(self):
        self.click_element('xpath', header.user_dropdown)
        self.click_element('xpath', header.logout_option)
