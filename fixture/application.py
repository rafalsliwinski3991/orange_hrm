from repo.orange_hrm.fixture.page_base import PageBase
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.header as header


class Application(PageBase):
    def login_to_app(self):
        self.navigate_to_page(login_page.page_url)
        self.fill_input('xpath', login_page.login_input, login_data.login_correct_value)
        self.fill_input('xpath', login_page.password_input, login_data.password_correct_value)
        self.click_element('xpath', login_page.login_button)

    def logout_from_app(self):
        self.click_element('xpath', header.user_dropdown)
        self.click_element('xpath', header.logout_option)

    def click_login_button(self):
        self.click_element('xpath', login_page.login_button)
