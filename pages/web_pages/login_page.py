from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from extensions.ui_actions import UiActions
from utils.common_ops import get_data

user_name = (By.CSS_SELECTOR, 'input[name="user"]')
password_field = (By.CSS_SELECTOR, '#current-password')
login_button = (By.CSS_SELECTOR, 'button[aria-label="Login button"]')
skip_button = (By.CLASS_NAME, 'css-2vac51-button')
success_login_msg = (By.XPATH, '//div[contains(text(),"Logged in")]')
failed_login_msg = (By.XPATH, '//div[contains(text(),"Invalid username or password")]')


class LoginPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, user):
        self.set_text(self.driver, user_name, user)

    def set_password(self, password):
        self.set_text(self.driver, password_field, password)

    def click_login_button(self):
        self.click(self.driver, login_button)

    def login_to_app(self, user, password):
        self.set_username(user)
        self.set_password(password)
        self.click_login_button()
        message = self.get_login_message()
        return message

    def click_skip(self):
        WebDriverWait(self.driver, get_data('WaitTime')).until(EC.visibility_of_element_located(skip_button)).click()
        # return MainPage

    def get_login_message(self):
        try:
            msg_elem = self.get_text(self.driver, success_login_msg)
            return str(msg_elem)
        except NoSuchElementException:
            try:
                msg_elem = self.get_text(self.driver, failed_login_msg)
                return str(msg_elem)
            except NoSuchElementException:
                return "Login message not found"



















