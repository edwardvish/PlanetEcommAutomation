import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from extensions.ui_actions import UiActions
from utils.common_ops import get_data

event_title = (By.XPATH, '//li/h1')
event_Details = (By.XPATH, "//div/p[@class='info-descr']")  # both date and running time data - ver against imdb
day_select = (By.CSS_SELECTOR, 'button[data-automation-id="day_4"]')
cinema_drop_down = (By.CSS_SELECTOR, 'button[data-id="select8"]')
cinema_list = (By.XPATH, "(//ul[@role='listbox'])[3]//li//a//span[@class='text']")
first_screening_button = (By.XPATH, "(//div[@class='qb-movie-info-column']/a[1])[1]")
book_now_button = (By.CSS_SELECTOR, "a[aria-label='BOOK NOW']")
selected_location = (By.CSS_SELECTOR, ".qb-cinema-name")

timeout=get_data('WaitTime')

class EMPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_event_title(self):
        title = UiActions.get_text(self.driver, event_title)
        return title

    def get_event_details(self):
        details = UiActions.find_multiple(self.driver, *event_Details)
        release_date = UiActions.get_text(details[0])
        duration = UiActions.get_text(details[1])
        return release_date, duration

    def choose_screening_time(self):
        UiActions.click(self.driver, first_screening_button)

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
