import time

import allure

from utils.base_test import BaseTest
from utils.common_ops import get_data
from workflows.web_flows import WebFlows


class TestWeb(BaseTest):
    driver = None
    coupons = WebFlows.coupon_code
    t: int = get_data('retries')

    @allure.title('Test01: Verify Login my account')
    @allure.description('This test verifies a successful login to my account')
    def test_verify_login(self):
        WebFlows.accept_cookie_msg()
        WebFlows.nav_login_page()
        WebFlows.verify_login_page_title()
        WebFlows.login_to_account(get_data('UserName'), get_data('Password'), 0)
        WebFlows.verify_successful_login()
        time.sleep(30)

    # def teardown_method(self):
    #     WebFlows.grafana_home(self.driver)
