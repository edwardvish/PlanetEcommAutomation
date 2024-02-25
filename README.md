Event Selection Automation Tests

This project contains automated tests for selecting events and verifying event details on a web platform using Python, Selenium, and Allure for reporting. It automates the process of selecting an event, day, and time, proceeding through an e-commerce page, and verifying ticket details against a CSV file.

Features
Event Selection: Automates the selection of events, cinemas, and times.
Location Verification: Verifies that the selected location matches the expected one.
E-commerce Integration: Checks the transition from selecting an event to the e-commerce page.
Ticket Verification: Validates ticket names and prices against a predefined CSV file.
Reporting: Utilizes Allure for enhanced test reporting.
Prerequisites
Before running the tests, ensure you have the following installed:

Python 3.x
Selenium WebDriver
Allure (for reporting)
Additionally, you'll need to set up your environment with necessary web drivers for Selenium and ensure they are in your PATH.

Installation
Clone this repository to your local machine:

git clone https://github.com/yourgithubusername/event-selection-automation.git
cd event-selection-automation
Install the required Python dependencies:

pip install -r requirements.txt
Running the Tests
To run the automated tests, execute the following command from the root directory of the project:

pytest
For generating an Allure report, run:


pytest --alluredir=/path/to/results/directory
And to view the report, use:


allure serve /path/to/results/directory
Contributing
Contributions to enhance the automation tests are welcome. Please follow the standard fork and pull request workflow.

License
This project is licensed under the MIT License - see the LICENSE file for details.

