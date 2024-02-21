import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from extensions.ui_actions import UiActions
from utils.common_ops import get_data

event_title = (By.XPATH, '//li/h1')
day = (By.CSS_SELECTOR, 'button[data-automation-id="day_4"]')
screentimes_2d = (By.XPATH, "//a[contains(@data-attrs, '2d')"
                            " and not(contains(@data-attrs, '4dx'))"
                            " and not(contains(""@data-attrs, 'screenx'))"
                            " and not(contains(@data-attrs, 'vip'))"
                            " and not(contains(""@data-attrs,"" 'imax'))]")
cinema_drop_down = (By.CSS_SELECTOR, 'button[data-id="select8"]')
cinema_list = (By.XPATH, "(//ul[@role='listbox'])[3]//li//a//span[@class='text']")
book_now_button = (By.CSS_SELECTOR, "a[aria-label='BOOK NOW']")
selected_location = (By.CSS_SELECTOR, ".qb-cinema-name")
event_date = (By.CSS_SELECTOR, ".col-xs-12.mb-sm h5")
login_button = (By.CSS_SELECTOR, 'button[data-automation-id="login-button"]')
buy_as_guest_button = (By.CSS_SELECTOR, 'button[data-automation-id="guest-button"]')
timeout = get_data('WaitTime')


class EMPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_event_title(self):
        title = UiActions.get_text(self.driver, event_title)
        return title

    # def get_event_details(self):
    #     details = UiActions.find_multiple(self.driver, *event_Details)
    #     release_date = UiActions.get_text(details[0])
    #     duration = UiActions.get_text(details[1])
    #     return release_date, duration

    def select_cinema_location(self):
        loc = get_data('location')
        loc_dd_list = WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(cinema_drop_down))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", loc_dd_list)
        # time.sleep(15)
        self.click(self.driver, cinema_drop_down)
        cinemas = self.find_multiple(self.driver, *cinema_list)
        try:
            for cinema in cinemas:
                if loc == cinema.text:
                    cinema.click()
        except:
            print('Location ' + str(loc) + ' not found in list')

    def get_cinema_location(self):
        return self.get_text(self.driver, selected_location)

    def select_day(self):
        self.click(self.driver, day)

    def select_time(self):
        events = self.get_event_times()
        events[0].click()

    def get_em_title(self):
        return self.get_text(self.driver, event_title)

    def get_event_date(self):
        return self.get_text(self.driver, event_date)

    def get_event_times(self):
        return self.find_multiple(self.driver, *screentimes_2d)

    def click_login_em_page(self):
        self.click(self.driver,login_button)

    def click_continue_as_guest(self):
        self.click(self.driver, buy_as_guest_button)

