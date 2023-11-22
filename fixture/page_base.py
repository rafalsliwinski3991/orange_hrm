from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PageBase:

    types = {
        'name': By.NAME,
        'id': By.ID,
        'xpath': By.XPATH
    }

    def __init__(self, wd, wait):
        self.wd = wd
        self.wait = wait

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
