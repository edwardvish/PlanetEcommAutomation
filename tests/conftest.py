import os
from datetime import datetime
import pytest
import selenium
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
from applitools.selenium import *
from applitools.selenium.runner import EyesRunner

driver = None
action = None
eyes = Eyes()# Applitools

@pytest.fixture(scope='class')
def init_web_driver(request):
    if get_data('Applitools').lower() == 'true':
        globals()['driver'] = get_web_driver()
        eyes.api_key = get_data('ApplitoolsAPI')
    else:
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
    # time.sleep(5)
    driver.close()
    eyes.close()
    eyes.abort()


def get_web_driver():
    browser = get_data('Browser')
    if browser.lower() == 'chrome':
        driver = get_chrome()

    elif browser.lower() == 'firefox':
        driver = get_firefox()

    elif browser.lower() == 'edge':
        driver = get_edge()

    else:
        driver = None
        raise Exception('Unrecognised browser type')

    return driver


def get_chrome():
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Selenium 4.x
    # chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver


def get_firefox():
    gecko_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return gecko_driver


def get_edge():
    srv = Service(EdgeChromiumDriverManager().install())
    edge_driver = selenium.webdriver.Edge(service=srv)
    return edge_driver


@pytest.mark.usefixtures('init_web_driver')
def pytest_exception_interact(node, call, report):
    driver = node.funcargs['request'].cls.driver
    if report.failed:
        if driver is not None:  # incase we dont invoke the webdriver, i.e. API Testing
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_path = os.path.join(get_data('ScreenshotPath'), f'screenshot_{now}.png')
            driver.get_screenshot_as_file(screenshot_path)
            print(f"Screenshot taken and saved to {screenshot_path}")
            allure.attach.file(screenshot_path, name="Screenshot on Failure",
                               attachment_type=allure.attachment_type.PNG)
