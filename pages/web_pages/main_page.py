from selenium.webdriver.common.by import By

from extensions.ui_actions import UiActions

main_title = (By.CLASS_NAME, 'css-1aanzv4')


class MainPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_main_title(self):
        title = UiActions.get_text(self.driver, main_title)
        return title



