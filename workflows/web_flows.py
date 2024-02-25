import time
import re

import allure
import pages.web_pages.login_page
import pages.web_pages.main_page
import pages.web_pages.ecom.ticket_selection_page as ticket_selection
import pages.web_pages.em_page as em_page
import pages.web_pages.my_account_page as my_account_page
import utils.manage_pages as page
from extensions.verifications import Verifications
from utils.common_ops import wait_for_element, Oper, get_data, read_csv, read_txt, save_to_json, read_from_json


# from pages.web_pages.main_page import MainPage

class WebFlows:
    coupon_code = read_csv(get_data('coupon_codes'))
    ticket_info = read_csv(get_data('ticket_info'))
    sites = read_csv(get_data('sites'))
    special_message = read_txt(get_data('special_message_dir'))
    event_details_path = get_data('event_details_dir')
    ecom_url_path = get_data('ecommerce_URL')

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
        wait_for_element(Oper.Element_Clickable, pages.web_pages.em_page.login_button)
        page.web_em_page.click_login_em_page()
        page.web_login_page.set_username(email)
        time.sleep(5)
        page.web_login_page.set_password(password)
        page.web_login_page.click_login_button()
        if is_fail:
            actual = page.web_login_page.get_login_message()
            Verifications.verify_equals(str(actual), 'Something went wrong')

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
    def select_em():
        page.web_main_page.select_eventmaster()
        wait_for_element(Oper.Element_Displayed, em_page.book_now_button)

    @staticmethod
    @allure.step('Save Event Details to file')
    def save_event_details():
        event_name = page.web_em_page.get_em_title()
        event_date = page.web_em_page.get_event_date()
        date_only = re.search(r'\d{2}/\d{2}/\d{4}', event_date).group()
        t = page.web_em_page.get_event_times()
        event_time = t[0].text
        path = get_data('event_details_dir')
        event_data = {
            "event_name": event_name.lower(),
            "event_date": date_only,
            "event_time": event_time,
        }
        save_to_json(event_data, path)

    @staticmethod
    @allure.step('Read Event details from JSON')
    def read_event_details():
        event_details = read_from_json(WebFlows.event_details_path)
        em_name = event_details['event_name']
        em_date = event_details['event_date']
        em_time = event_details['event_time']
        em_data = [em_name, em_date, em_time]
        return em_data

    @staticmethod
    @allure.step('Select a screening day')
    def select_date():
        page.web_em_page.select_day()

    @staticmethod
    @allure.step('Select a screening time')
    def select_time():
        page.web_em_page.select_time()

    @staticmethod
    @allure.step('Wait until ecom loads and verify')
    def verify_ecom_page():
        wait_for_element(Oper.Element_Displayed, ticket_selection.tickets_form)

    @staticmethod
    @allure.step('Save the ecom URL')
    def save_ecom_url(driver):
        ecom_url = driver.current_url
        path = get_data('ecommerce_URL')
        Ecommerce_URL = {
            "URL": ecom_url
        }
        save_to_json(Ecommerce_URL, path)

    @staticmethod
    @allure.step('Navigating to the ecom site')
    def navigate_to_url(driver, path):
        data = read_from_json(path)
        url = data['URL']
        driver.get(str(url))

    @staticmethod
    @allure.step('Proceed to ticket selection as guest')
    def continue_as_guest():
        wait_for_element(Oper.Element_Clickable, em_page.buy_as_guest_button)
        page.web_em_page.click_continue_as_guest()

    @staticmethod
    @allure.step('Verify the event details based on the choices')
    def verify_event_details():
        event_details = WebFlows.read_event_details()
        print(str(event_details))
        event_title = page.web_ecom_ticket.get_event_title()
        event_date = page.web_ecom_ticket.get_event_date()
        event_time = page.web_ecom_ticket.get_event_time()
        details = [event_title.lower(), event_date, event_time]
        Verifications.verify_equals(details, event_details)

    @staticmethod
    @allure.step('Verify ticket names and prices')
    def verify_ticket_details(details):
        names = page.web_ecom_ticket.get_ticket_names()
        prices = page.web_ecom_ticket.get_ticket_prices()
        page_data = dict(zip(names, prices))
        for row in details:
            ticket_name = row['Name']
            ticket_price = row['Price'].replace(" NIS", "")
            if ticket_name in page_data:
                webpage_price = re.sub(r'[\u202a\u202c]', '', page_data[ticket_name].replace(" NIS", ""))
                Verifications.verify_equals(webpage_price, ticket_price)

            else:
                print(f"Warning: Ticket name '{ticket_name}' not found on webpage.")

    @staticmethod
    @allure.step('Special message verification')
    def verify_special_message(message: str):
        actual = page.web_ecom_ticket.get_tg_message()
        Verifications.verify_equals(actual, message)

    @staticmethod
    @allure.step('Back to Homepage')
    def cinema_home(driver):
        driver.get(get_data('URL'))
