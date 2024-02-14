from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from extensions.ui_actions import UiActions
from utils.common_ops import get_data

title = (By.CSS_SELECTOR, 'h3[data-qa="bookingHeader.past.title"')
booking_info = (By.XPATH, "//tbody//tr")

class LoginPage(UiActions):
    def __init__(self, driver):
        self.driver = driver



















