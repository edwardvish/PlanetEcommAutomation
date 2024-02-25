import json

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import tests.conftest as conft
import xml.etree.ElementTree as ET
import csv


# import re

@allure.step('Parse the content of the XML file')
def get_data(node_name):
    tree = ET.parse('./configuration/data.xml')
    root = tree.getroot()
    return root.find('.//' + node_name).text


@allure.step('Parse the content of a text file')
def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()


@allure.step('Save data to JSON file')
def save_to_json(data, path):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Event data successfully saved to {path}")


@allure.step('Read data from JSON file')
def read_from_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data


@allure.step('Waiting for element to appear in the webpage')
def wait_for_element(oper, locator):
    timeout = int(get_data('WaitTime'))
    try:
        if oper == 'exists':
            WebDriverWait(conft.driver, timeout).until(ec.presence_of_element_located(locator))
        elif oper == 'displayed':
            WebDriverWait(conft.driver, timeout).until(ec.visibility_of_element_located(locator))
        elif oper == 'clickable':
            WebDriverWait(conft.driver, timeout).until(ec.element_to_be_clickable(locator))
    except NoSuchElementException:
        print("Element not found on the page.")


@allure.step('Read the contents of the CSV file and storing it into a dictionary')
def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
        print(data[0])
        return data


def search_user(param):
    # domain = []
    data = read_csv(get_data("user_data_dir"))
    if param == 'Name':
        names = [row[param].strip() for row in data]
        return names
    elif param == 'Email':
        emails = [row[param].strip() for row in data]
        return emails
    elif param == 'Username':
        usernames = [row[param].strip() for row in data]
        return usernames


# Enum for selecting either displayed or existing element on page
class Oper:
    Element_Exists = 'exists'
    Element_Displayed = 'displayed'
    Element_Clickable = 'clickable'


# Enum for selecting a user by name or index

class Type:
    REGULAR = 'regular'
    # USER = 'name'


class SearchBy:
    NAME = 'Name'
    EMAIL = 'Email'
    UNAME = 'Username'
