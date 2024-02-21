import random
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from extensions.ui_actions import UiActions
from utils.common_ops import get_data

title = (By.XPATH, "//h1[text()='Login to My Planet']")
email = (By.CSS_SELECTOR, 'input[id="email"]')
password_field = (By.CSS_SELECTOR, 'input[id="password"]')
login_button = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')
signup_button = (By.CSS_SELECTOR, 'button[data-qa="signup-link"]')
failed_login_msg = (By.CSS_SELECTOR, 'div["class=v-alert__content"]')


class LoginPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.get_text(self.driver, title)

    def set_username(self, user):
        self.set_text(self.driver, email, user)

    def set_password(self, password):
        self.set_text(self.driver, password_field, password)

    def click_login_button(self):
        self.click(self.driver, login_button)

    # def login_to_app(self, user, password, is_fail):
    #     self.set_username(user)
    #     time.sleep(random.uniform(0.1,0.3))
    #     self.set_password(password)
    #     time.sleep(random.uniform(0.1,0.3))
    #     self.click_login_button()
    #     if is_fail:
    #         message = self.get_login_message()
    #         return message

    def get_login_message(self):
        try:
            msg_elem = self.get_text(self.driver, failed_login_msg)
            return str(msg_elem)
        except NoSuchElementException:
            return "Login message not found"
