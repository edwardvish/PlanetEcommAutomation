from time import sleep

import allure

import pages.web_pages.main_page as main_page
import pages.web_pages.server_admin_users
import pages.web_pages.server_admin_users as server_admin_users
import pages.web_pages.server_admin_new_user as server_admin_new_user
import utils.manage_pages as page
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications

from utils.common_ops import wait_for_element, Oper, get_data, read_csv, search_user, By, SearchBy


# from pages.web_pages.main_page import MainPage

class WebFlows:
    user_data = read_csv(get_data('user_data_dir'))

    @staticmethod
    @allure.step('Login to grafana')
    def login_flow(user: str, password: str):
        # page.web_login_page.set_username(user)
        # page.web_login_page.set_password(password)
        # page.web_login_page.click_login_button()
        # login_msg = page.web_login_page.get_login_message()
        login_msg = page.web_login_page.login_to_app(user, password)
        page.web_login_page.click_skip()
        return login_msg

    @staticmethod
    @allure.step('Verify grafana title')
    def verify_grafana_title(expected: str):
        wait_for_element(Oper.Element_Displayed, main_page.main_title)
        actual = page.web_main_page.get_main_title()
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step('Verify Displayed menu buttons, using smart assertions')
    def verify_upper_menu_buttons():
        elems = [page.web_upper_menu_page.get_general(),
                 page.web_upper_menu_page.get_home(),
                 page.web_upper_menu_page.get_save_dash(),
                 page.web_upper_menu_page.get_dash_settings(),
                 page.web_upper_menu_page.get_view_mode(),
                 ]
        # Verifications.soft_displayed(elems)
        Verifications.soft_assert(elems)

    @staticmethod
    @allure.step('Open users list in the "Server admin"')
    def open_users_page(expected: str):
        # ui_actions = UiActions(driver)
        # locate the server admin element in the left menu page
        elem1 = page.web_left_menu_page.get_server_admin_menu()
        elem2 = page.ws_admin_menu_page.get_users()
        # mouse hover the icon and click on the users
        UiActions.mouse_hover(elem1, elem2)
        # wait for page to load, extract the title.
        wait_for_element(Oper.Element_Displayed, server_admin_users.title)
        actual = page.ws_admin_users.get_page_title()
        # verify server admin users page is loaded.
        Verifications.verify_equals(actual.lower(), expected.lower())

    @staticmethod
    @allure.step('Add a new user')
    def create_new_user(expected: str, name: str, user: str, email: str, password: str):
        # locate and click the new user form
        wait_for_element(Oper.Element_Displayed, server_admin_users.new_user)
        page.ws_admin_users.open_new_user_from()
        # wait for the form to load and get the form title
        wait_for_element(Oper.Element_Displayed, server_admin_new_user.form_title)
        # store and compare the title is as expected
        actual = page.ws_admin_new_user.get_form_title().text
        Verifications.verify_equals(actual, expected)
        # set all form fields
        page.ws_admin_new_user.set_name(name)
        sleep(0.5)
        page.ws_admin_new_user.set_email(email)
        sleep(0.5)
        page.ws_admin_new_user.set_username(user)
        sleep(0.5)
        page.ws_admin_new_user.set_password(password)
        sleep(0.5)
        page.ws_admin_new_user.click_create_button()

    @staticmethod
    @allure.step('Count the number of users on screen')
    def verify_user_num(number):
        if number > 0:
            wait_for_element(Oper.Element_Displayed, server_admin_users.users_list)
            actual = page.ws_admin_users.get_users_list()
            Verifications.verify_num_of_elements(actual, number)

    @staticmethod
    @allure.step('Delete users by their index in the list')
    def delete_user_by_index(driver, index):
        user = page.ws_admin_users.get_user_by_index(index)
        user.click()
        UiActions.click(driver, server_admin_users.delete_user)
        wait_for_element(Oper.Element_Displayed, server_admin_users.delete_dialog)
        UiActions.click(driver, server_admin_users.dialog_confirm_delete)
        wait_for_element(Oper.Element_Displayed, server_admin_users.title)

    @staticmethod
    @allure.step('Delete users by the username')
    def delete_user_by_username(driver, name):
        user = page.ws_admin_users.get_user_by_name(name)
        user.click()
        UiActions.click(driver, server_admin_users.delete_user)
        wait_for_element(Oper.Element_Displayed, server_admin_users.delete_dialog)
        UiActions.click(driver, server_admin_users.dialog_confirm_delete)
        wait_for_element(Oper.Element_Displayed, server_admin_users.title)

    @staticmethod
    @allure.step('Delete user wrapper')
    def delete_user(driver, by, value):
        if by == 'index':
            WebFlows.delete_user_by_index(driver, int(value))

        elif by == 'name':
            WebFlows.delete_user_by_username(driver, value)


    @staticmethod
    @allure.step('search for a user using filtering')
    def search_user(driver, value, i):
        users = search_user(value)
        UiActions.set_text(driver, pages.web_pages.server_admin_users.search, str(users[i]))

    @staticmethod
    @allure.step('Return back to the main grafana screen')
    def grafana_home(driver):
        driver.get(get_data('URL'))





 









