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

    def click_element(self, locator_type, locator_value):
        wait = WebDriverWait(self.wd, 10)
        wait.until(EC.element_to_be_clickable((self.types[locator_type], locator_value)))
        self.wd.find_element(self.types[locator_type], locator_value).click()

    def fill_input(self, locator_type, locator_value, data_value):
        self.click_element(self.types[locator_type], locator_value)
        self.wd.find_element(self.types[locator_type], locator_value).clear()
        self.wd.find_element(self.types[locator_type], locator_value).send_keys(data_value)
