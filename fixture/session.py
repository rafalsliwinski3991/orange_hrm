from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

wd = webdriver.Chrome(options=options)


class SessionHelper:

    def quit_session(self):
        wd.quit()
