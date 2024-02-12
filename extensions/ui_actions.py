import allure

import tests.conftest as conf


class UiActions:
    @staticmethod
    @allure.step('locate a single element and return the webdriver phrase')
    def find(driver, *locator):
        return driver.find_element(*locator)

    @staticmethod
    @allure.step('locate multiple elements and return the webdriver phrases')
    def find_multiple(driver, *locator):
        return driver.find_elements(*locator)

    @staticmethod
    @allure.step('Click a web object')
    def click(driver, locator):
        elem = UiActions.find(driver, *locator)
        elem.click()

    @staticmethod
    @allure.step('Select an option from a dropdown list')
    def select_dropdown(driver, locator1, locator2):
        UiActions.click(driver, locator1)
        UiActions.click(driver, locator2)

    @staticmethod
    @allure.step('Enter text into a filed')
    def set_text(driver, locator, value: str):
        element = UiActions.find(driver, *locator)
        element.clear()
        element.send_keys(value)

    @staticmethod
    @allure.step('Extract the text value of an object')
    def get_text(driver, locator):
        return UiActions.find(driver, *locator).text

    @staticmethod
    @allure.step('Get the title of the browser tab')
    def get_title(driver):
        return driver.title()

    @staticmethod
    @allure.step('Perform the action of a drag and drop ')
    def drag_n_drop(src, target):
        conf.action.drag_and_drop(src, target).perform()

    @staticmethod
    @allure.step('Right click on a web element')
    def right_click(elem):
        conf.action.context_click(elem).perform()

    @staticmethod
    @allure.step('Hover with the mouse over a web element')
    def mouse_hover(elem1, elem2):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()
