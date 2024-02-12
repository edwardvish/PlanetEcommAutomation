import allure
import pytest
from tests.conftest import eyes
from utils.base_test import BaseTest
from utils.common_ops import get_data, By, read_csv, SearchBy
from workflows.web_flows import WebFlows


class TestWeb(BaseTest):
    driver = None
    user_data = WebFlows.user_data

    @allure.title('Test01: Verify Login Grafana')
    @allure.description('This test verifies a successful login to Grafana')
    def test_verify_login(self):
        msg = WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        assert msg.lower() == 'logged in'
        WebFlows.verify_grafana_title('Welcome to Grafana')

    @allure.title('Test01: Verify Upper Menu Buttons')
    @allure.description('This test verifies a upper menu buttons are displayed')
    def test_verify_upper_menu(self):
        WebFlows.verify_upper_menu_buttons()

    #
    # # def test_add_new_user(self):
    # #     WebFlows.open_users_page('Server Admin')
    # #     WebFlows.create_new_user('Add new user', 'john', 'john', 'test@test.com', 'abc123456')
    # #     WebFlows.create_new_user('Add new user', 'edward', 'edward', 'test2@test.com', '2abc123456')
    # #     WebFlows.verify_user_num(3)
    #
    # # def test_delete_user_by_index(self):
    # #     WebFlows.delete_user_by_index(self.driver, 0)
    # #     WebFlows.verify_user_num(2)

    @allure.title('Test03: Test Adding new users')
    @allure.description('This test adds and verifies adding new users')
    def test_add_new_users(self):
        WebFlows.open_users_page('Server Admin')
        for i in range(3):  # Assuming you want to add 3 users
            user = self.user_data[i]  # Get the user data
            WebFlows.create_new_user('Add new user', user['Name'], user['Username'], user['Email'], user['Password'])
        WebFlows.verify_user_num(4)

    @allure.title('Test04: Test filtering the users list by different criteria')
    @allure.description('This test verifies a upper menu buttons are displayed')
    def test_user_filtering(self):
        WebFlows.open_users_page('Server Admin')
        for item in range(3):
            # Use the search_user method and pass the driver, the desired search criteria (Name, Username or Email) and
            # add the number of items/entries/users
            WebFlows.search_user(self.driver, SearchBy.UNAME, item)
            WebFlows.verify_user_num(1)

    @allure.title('Test05: Delete users')
    @allure.description('This test deletes and verifies users by different types')
    def test_delete_user(self):
        WebFlows.open_users_page('Server Admin')
        WebFlows.delete_user(self.driver, By.USER, 'Daniel Hernandez')
        # WebFlows.delete_user(self.driver, By.INDEX, 1)
        WebFlows.verify_user_num(3)

    @pytest.mark.skipif(get_data('Applitools')).lower() == 'false'
    @allure.title('Test06: Visual Testing')
    @allure.description('This test visually verifies grafana main screen')
    def test_visual_verification_users(self):
        eyes.open(self.driver, 'Grafana', 'User Table Test', )
        WebFlows.open_users_page('Server Admin')
        eyes.check_window('Users Table')


    def teardown_method(self):
        WebFlows.grafana_home(self.driver)
