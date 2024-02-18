import time

import allure
import pages.web_pages.login_page
import pages.web_pages.main_page
import utils.manage_pages as page
from extensions.verifications import Verifications
from utils.common_ops import wait_for_element, Oper, get_data, read_csv


# from pages.web_pages.main_page import MainPage

class WebFlows:
    coupon_code = read_csv(get_data('coupon_codes'))
    ticket_info = read_csv(get_data('ticket_info'))

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
            print("Could not navigate to login page after " + str(t) + 'attempts')

    @staticmethod
    @allure.step('Login to account')
    def login_to_account(email: str, password: str, is_fail: int):
        page.web_login_page.login_to_app(email, password, is_fail)
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
        accountURL = page.web_account_page.get_Url()
        Verifications.verify_contains('myaccount', str(accountURL))

    # @staticmethod
    # @allure.step('Verify Displayed menu buttons, using smart assertions')
    #     # Verifications.soft_displayed(elems)
    #
    #
    # @staticmethod
    # @allure.step('Open users list in the "Server admin"')
    #
    # @staticmethod
    # @allure.step('Add a new user')
    #
    #
    #
    # @staticmethod
    # @allure.step('Count the number of users on screen')
    #
    #
    # @staticmethod
    # @allure.step('Delete users by their index in the list')
    #
    # @staticmethod
    # @allure.step('Delete users by the username')
    #
    # @staticmethod
    # @allure.step('Delete user wrapper')
    #
    #
    # @staticmethod
    # @allure.step('search for a user using filtering')
    #
    # @staticmethod
    # @allure.step('Return back to the main grafana screen')
    #
    #
