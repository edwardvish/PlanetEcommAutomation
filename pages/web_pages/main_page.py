from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from extensions.ui_actions import UiActions


cookies_msg_button = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
main_title = (By.CSS_SELECTOR, 'a[data-automation-id="header-logo-link"]')
acc_login = (By.CSS_SELECTOR, 'a[data-automation-id="account-section-link"][aria-label=" Log in"]')
acc_register = (By.CSS_SELECTOR, 'a[data-automation-id="account-section-link"][aria-label="Register"]')
search = (By.CSS_SELECTOR, 'input[data-automation-id="quicksearch-input"]')
language_change = (By.CSS_SELECTOR, 'div[class="btn-group mt-xs fit-width btn-group dropdown"]')
offers = (By.CSS_SELECTOR, 'a[aria-label="OFFERS"]')
whatson = (By.CSS_SELECTOR, 'a[href*="/whatson"]')
blog = (By.CSS_SELECTOR, 'a[aria-label="BLOG"]')
moviecards = (By.CSS_SELECTOR, 'a[aria-label="GIFTS & MOVIE CARDS"]')
imax = (By.CSS_SELECTOR, 'a[href="/imax"]')
fdx = (By.CSS_SELECTOR, 'a[aria-label="/4dx"]')
screenx = (By.CSS_SELECTOR, 'a[aria-label="/screenx"]')
vip = (By.CSS_SELECTOR, 'a[aria-label="/vip"]')
now_playing_first = (By.CSS_SELECTOR, 'div[aria-label^="2 /"]')
cinema_selection = (By.CSS_SELECTOR, 'button[data-id="select26"]')
cinema_list = (By.XPATH, '((//ul[@role="listbox"])[2]/li[@role="option"]')


class MainPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_main_title(self):
        title = UiActions.get_text(self.driver, main_title)
        return title

    def get_cookies_message(self):
        return self.find(self.driver, *cookies_msg_button)

    def accept_cookies(self):
        self.click(self.driver, cookies_msg_button)

    def get_login_page(self):
        UiActions.click(self.driver, acc_login)

    def select_eventmaster(self):
        # Wait for the element to be present/visible
        em = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(now_playing_first))
        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView();", em)
        # Assuming self.click is a custom method you've defined to click on elements
        self.click(self.driver, now_playing_first)

