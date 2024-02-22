import time
import allure
from utils.base_test import BaseTest
from utils.common_ops import get_data, read_csv
from workflows.web_flows import WebFlows

class TestWeb(BaseTest):
    driver = None
    coupons = WebFlows.coupon_code
    sites = WebFlows.sites
    location = get_data('location')
    event_details = []
    message = WebFlows.special_message
    tickets = WebFlows.ticket_info

    @allure.title('Test01: Test selecting and event')
    @allure.description('This test select an event, day and time and proceeds to the ecom page')
    def test_select_event(self):
        WebFlows.accept_cookie_msg()
        WebFlows.select_em()
        WebFlows.select_cinema()
        time.sleep(0.5)
        WebFlows.verify_selected_location()
        WebFlows.select_date()
        self.event_details = WebFlows.get_event_details()
        WebFlows.select_time()
        WebFlows.continue_as_guest()
        WebFlows.verify_ecom_page()
        print("This is a debug output" + str(self.event_details))

    @allure.title('Test02: Test event details')
    @allure.description('This test verifies the ticket group message, and the event details')
    def test_event_details(self):
        WebFlows.verify_special_message(self.message)
        WebFlows.verify_event_details(self.event_details)

    @allure.title('Test03:Verify ticket names and prices')
    @allure.description('This test verifies ticket names and prices against a csv file')
    def test_verify_tickets(self):
        data = self.tickets
        WebFlows.verify_ticket_details(data)

    # @classmethod
    # def teardown_class(cls):
    #     """Teardown method to run after all tests in the class."""
    #     WebFlows.cinema_home(cls.driver)
