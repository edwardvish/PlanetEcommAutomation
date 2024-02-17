import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.common_ops import get_data
from utils.event_listeners import EventListener
from utils.manage_pages import ManagePages
import allure

driver = None
action = None


@pytest.fixture(scope='class')
def init_web_driver(request):
    edriver = get_web_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    timeout = int(get_data('WaitTime'))
    driver.implicitly_wait(timeout)
    driver.get(get_data('URL'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_web_pages()
    yield
    driver.close()


def get_web_driver():
    browser = get_data('Browser').lower()
    if browser == 'chrome':
        return get_chrome()
    elif browser == 'firefox':
        return get_firefox()
    elif browser == 'edge':
        return get_edge()
    else:
        raise Exception('Unrecognised browser type')


def get_chrome():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def get_firefox():
    return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


def get_edge():
    srv = Service(EdgeChromiumDriverManager().install())
    return webdriver.Edge(service=srv)


@pytest.mark.usefixtures('init_web_driver')
def pytest_exception_interact(node, call, report):
    if isinstance(node, (pytest.Function, pytest.Class)):
        driver = node.funcargs['request'].cls.driver
        if report.failed and driver is not None:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_path = os.path.join(get_data('ScreenshotPath'), f'screenshot_{now}.png')
            driver.get_screenshot_as_file(screenshot_path)
            print(f"Screenshot taken and saved to {screenshot_path}")
            allure.attach.file(screenshot_path, name="Screenshot on Failure",
                               attachment_type=allure.attachment_type.PNG)
