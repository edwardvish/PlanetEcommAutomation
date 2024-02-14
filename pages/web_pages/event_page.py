from selenium.webdriver.common.by import By

from extensions.ui_actions import UiActions

event_title = (By.XPATH, '//li/h1')
event_Details = (By.XPATH, "//div/p[@class='info-descr']")  # both date and running time data - ver against imdb
day_select = (By.CSS_SELECTOR, 'button[data-automation-id="day_4"]')
cinema_selection = (By.CSS_SELECTOR, 'button[data-id="select8"]')
cinema_list = (By.XPATH, "(//ul[@role='listbox'])[3]/li/a/span[@class='text']")
first_screening_button = (By.XPATH, "(//div[@class='qb-movie-info-column']/a[1])[1]")


class MainPage(UiActions):
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
        



