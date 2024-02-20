import time

import allure
import pages.web_pages.login_page
import pages.web_pages.main_page
import pages.web_pages.em_page as em_page
import pages.web_pages.my_account_page as my_account_page
import utils.manage_pages as page
from extensions.verifications import Verifications
from utils.common_ops import wait_for_element, Oper, get_data, read_csv


# from pages.web_pages.main_page import MainPage

class WebFlows:
    coupon_code = read_csv(get_data('coupon_codes'))
    ticket_info = read_csv(get_data('ticket_info'))
    sites = read_csv(get_data('sites'))

    @staticmethod
    @allure.step('Wait for cookies button to appear and accept all cookies')
    def accept_cookie_msg():
        for i in range(2):
            try:
                time.sleep(0.5)
                wait_for_element(Oper.Element_Displayed, pages.web_pages.main_page.cookies_msg_button)
                page.web_main_page.accept_cookies()
            except:
                print("Cookie acceptance button not found.")

    @staticmethod
    @allure.step('Navigate to a the login page from the main page')
    def nav_login_page():
        try:
            page.web_main_page.get_login_page()
            wait_for_element(Oper.Element_Displayed, pages.web_pages.login_page.title)
        except:
            print("Could not navigate to login page")

    @staticmethod
    @allure.step('Login to account')
    def login_to_account(email: str, password: str, is_fail: int):
        page.web_login_page.login_to_app(email, password, is_fail)
        if is_fail:
            actual = page.web_login_page.get_login_message()
            Verifications.verify_equals(str(actual), 'Something went wrong')
        wait_for_element(Oper.Element_Clickable, pages.web_pages.login_page.login_button)

    @staticmethod
    @allure.step('Verify my login page title')
    def verify_login_page_title():
        actual = page.web_login_page.get_page_title()
        Verifications.verify_contains('Login', actual)

    @staticmethod
    @allure.step('Verify my account page')
    def verify_successful_login():
        wait_for_element(Oper.Element_Displayed, pages.web_pages.my_account_page.dashboard)
        Verifications.verify_element_present(my_account_page.now_playing)

    @staticmethod
    @allure.step('verify locations list')
    def verify_locations_list(site):
        locations = page.web_account_page.get_location_list()
        missing_locations = [location for location in locations if not Verifications.verify_contains(location, site)]

        if missing_locations:
            print(f"The following locations are missing: {', '.join(missing_locations)}")
        else:
            print("All locations are present.")

    @staticmethod
    @allure.step('Select a favourite cinema location')
    def choose_favourite_cinema(location):
        page.web_account_page.click_cinemas_dropdown()
        page.web_account_page.choose_site(location)


    @staticmethod
    @allure.step('select a cinema location after selecting a movie')
    def select_cinema():
        page.web_em_page.select_cinema_location()


    @staticmethod
    @allure.step('Verify the selected location after choosing')
    def verify_selected_location():
        actual = page.web_em_page.get_cinema_location()
        expected = get_data('location')
        Verifications.verify_equals(actual.lower(), expected.lower())



    @staticmethod
    @allure.step('Scroll to the first movie and select it ')
    def select_movie():
        page.web_main_page.select_eventmaster()
        wait_for_element(Oper.Element_Displayed, em_page.book_now_button)

    @staticmethod
    @allure.step('Return back to the main grafana screen')
    def grafana_home(driver):
        driver.get(get_data('URL'))