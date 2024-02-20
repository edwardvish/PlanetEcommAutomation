from selenium.webdriver.common.by import By
from extensions.ui_actions import UiActions

favourite_cinema = (By.XPATH, '//span[@class="v-chip__content"]')
dashboard = (By.XPATH, "//div[contains(text(),'Dashboard')]")
bookings = (By.XPATH, "//div[contains(text(),'Tickets')]")
personal_details = (By.XPATH, "//div[contains(text(),'Personal details')]")
account_settings = (By.XPATH, "//div[contains(text(),'Account settings')]")
payments = (By.XPATH, "//div[contains(text(),'Payments')]")
now_playing = (By.XPATH, "//h4[contains(text(),'Now Playing in')]")
location_dd = (By.CSS_SELECTOR, "div[class='v-select__selections']")
locations_list = (By.CSS_SELECTOR, "div[id='list-61'] div[class='v-list-item__title']")


class MyAccountPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_Url(self):
        return self.driver.current_url

    def get_dashboard_screen(self):
        return self.find(self.driver, *dashboard)

    def get_now_playing(self):
        return self.find(self.driver, *now_playing)

    def click_cinemas_dropdown(self):
        self.click(self.driver, location_dd)

    def choose_site(self, location:str):
        locations = self.find_multiple(self.driver, *locations_list)
        for cinema in locations:
            if location == cinema.get_text():
                cinema.click()

    def get_location_list(self):
        sites = []
        locations = self.find_multiple(self.driver, *locations_list)
        for location in locations:
            sites.append(location.get_text())
        return sites
