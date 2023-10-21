from selenium import webdriver
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.pages.login_page as login_page
from repo.orange_hrm.fixture.page_base import PageBase

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

wd = webdriver.Chrome(options=options)
wd.maximize_window()

page_base = PageBase(wd, 10)

"""
1. Navigate to login page. -> Login page is displayed.
2. Fill the 'username' field. -> User name is entered.
3. Fill the 'password' field. -> Password is entered.
4. Click the 'Login' button. -> Button is clicked, dashboard page is displayed.
"""

page_base.navigate_to_page(login_page.page_url)  # 1
page_base.fill_input('xpath', login_page.login_input, login_data.login_value)  # 2
page_base.fill_input('xpath', login_page.password_input, login_data.password_value)  # 3
page_base.click_element('xpath', login_page.login_button)  # 4
wd.quit()
