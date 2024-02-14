from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from extensions.ui_actions import UiActions
from utils.common_ops import get_data

favourite_cinema = (By.XPATH, '//span[@class="v-chip__content"]')
dashboard = (By.XPATH, "//div[contains(text(),'Dashboard')]")
bookings = (By.XPATH, "//div[contains(text(),'Tickets')]")
personal_details = (By.XPATH, "//div[contains(text(),'Personal details')]")
account_settings = (By.XPATH, "//div[contains(text(),'Account settings')]")
payments = (By.XPATH, "//div[contains(text(),'Payments')]")


class LoginPage(UiActions):
    def __init__(self, driver):
        self.driver = driver













