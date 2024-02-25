# Automated Event Selection and Verification Tests

This Python project uses Selenium and Allure for automated web testing, specifically for event selection, verification of event details, and ticket prices. It is structured around a base testing framework that integrates utility functions and web workflows to interact with a specified eCommerce platform.

## Features

- Event selection based on location, date, and time
- Verification of event details and special messages
- Validation of ticket names and prices against provided data
- Utilizes Allure for enhanced test reporting

## Prerequisites

Before running these tests, ensure you have the following installed:
- Python 4 or higher
- Selenium WebDriver
- Allure Framework

Additionally, ensure you have access to the required external data files and URLs specified within the utility functions (`utils/common_ops.py`).

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages:

pip install -r requirements.txt


## Running the tests 
pytest -s -v .\tests\test_ticket_purchase.py --alluredir=.\allure-results

## View Allure report 
allure serve .\allure-results\



