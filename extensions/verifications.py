import allure
from selenium.common import NoSuchElementException
from smart_assertions import *
from extensions.ui_actions import UiActions


class Verifications(UiActions):
    @staticmethod
    @allure.step('Verify if the element is located in the DOM')
    def verify_element_present(locator):
        try:
            UiActions.find(*locator)
            return True
        except NoSuchElementException:
            return print('Element ', str(locator),' not found')

    @staticmethod
    @allure.step('Compare the expected value with the actual')
    def verify_equals(actual, expected):
        assert actual == expected, 'Values not equal, the actual: ' + str(actual) + 'the expected is ' + str(expected)

    @staticmethod
    @allure.step('Soft verification(assert) of elements using smart-assertions')
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step('Custom soft verification of element')
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.append(elems[i].get_attribute('aria-label'))
        if len(failed_elems) > 0:
            for failed in failed_elems:
                print('Soft Display Failed, Elements failed:' + str(failed))
            raise AssertionError('Soft Display Failed')

    @staticmethod
    @allure.step('Verify number of elements')
    def verify_num_of_elements(users, actual):
        assert len(users) == actual, 'The number of elements in list:' + str(len(users)) + 'does not match expected'



