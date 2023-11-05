from repo.orange_hrm.fixture.page_base import PageBase
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.header as header
import repo.orange_hrm.pages.password_reset_page as pwd_reset_page


class Application(PageBase):

    def enter_username(self, locator_value, username_value):
        self.fill_input('xpath', locator_value, username_value)

    def enter_password(self, locator_value, password_value):
        self.fill_input('xpath', locator_value, password_value)

    def click_login_button(self):
        self.click_element('xpath', login_page.login_button)

    def login_to_app(self):
        self.navigate_to_page(login_page.page_url)
        self.enter_username(login_page.login_input, login_data.login_correct_value)
        self.enter_password(login_page.password_input, login_data.password_correct_value)
        self.click_login_button()

    def logout_from_app(self):
        self.click_element('xpath', header.user_dropdown)
        self.click_element('xpath', header.logout_option)

    def click_reset_password_button(self):
        self.click_element('xpath', pwd_reset_page.reset_password_button)  # Step 3

    def click_forgot_your_password_link(self):
        self.click_element('xpath', login_page.forgot_your_password_link)

    def click_cancel_password_reset_button(self):
        self.click_element('xpath', pwd_reset_page.cancel_button)
