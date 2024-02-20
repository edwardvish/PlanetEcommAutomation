import tests.conftest as conft
from pages.web_pages.em_page import EMPage
from pages.web_pages.main_page import MainPage
from pages.web_pages.login_page import LoginPage
from pages.web_pages.my_account_page import MyAccountPage

#Web Objects
web_login_page = None
web_main_page = None
web_account_page = None
web_em_page = None
web_flows = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login_page'] = LoginPage(conft.driver)
        globals()['web_main_page'] = MainPage(conft.driver)
        globals()['web_account_page'] = MyAccountPage(conft.driver)
        globals()['web_em_page'] = EMPage(conft.driver)



