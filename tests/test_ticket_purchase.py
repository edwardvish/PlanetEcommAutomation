import time

import allure

from utils.base_test import BaseTest
from utils.common_ops import get_data
from workflows.web_flows import WebFlows


class TestWeb(BaseTest):
    driver = None
    coupons = WebFlows.coupon_code
    sites = WebFlows.sites
    location = get_data('location')
    event_details = []

    @allure.title('Test01: Verify Login my account')
    @allure.description('This test verifies a successful login to my account')
    # def test_verify_login(self):
    #     WebFlows.accept_cookie_msg()
    #     WebFlows.nav_login_page()
    #     WebFlows.verify_login_page_title()
    #     WebFlows.login_to_account(get_data('UserName'), get_data('Password'), 0)
    #     WebFlows.verify_successful_login()

    # def test_verify_cinema_sites(self):
    #     WebFlows.verify_locations_list(self.sites)
    #     WebFlows.choose_favourite_cinema(self.location)

    # This test selects the newest event master, select a day and time for a 2D screening
    # The output is a navigation to and e-comm page
    def test_select_event(self):
        WebFlows.accept_cookie_msg()
        WebFlows.select_em()
        # time.sleep(15)
        WebFlows.select_cinema()
        time.sleep(0.5)
        WebFlows.verify_selected_location()
        WebFlows.select_date()
        self.event_details = WebFlows.get_event_details()
        WebFlows.select_time()
        # WebFlows.login_to_account(get_data('UserName'), get_data('Password'), 0)
        WebFlows.continue_as_guest()
        WebFlows.verify_ecom_page()
        time.sleep(30)

    def test_choose_tickets(self):
        pass

    # This test will verify the event details after the order was completed in the e-commerce
    # def test_verify_event_details(self):
    #     details = self.event_details

    def teardown_method(self):
        WebFlows.cinema_home(self.driver)
