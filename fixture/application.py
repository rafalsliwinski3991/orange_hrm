from repo.orange_hrm.fixture.page_base import PageBase
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.pages.login_page as login_page


class Application(PageBase):
    def login_to_web_app(self):
        self.navigate_to_page(login_page.page_url)
        self.fill_input('xpath', login_page.login_input, login_data.login_value)
        self.fill_input('xpath', login_page.password_input, login_data.password_value)
        self.click_element('xpath', login_page.login_button)
