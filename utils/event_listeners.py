from selenium.webdriver.support.events import AbstractEventListener


class EventListener(AbstractEventListener):
    button_text = None

    def before_navigate_to(self, url, driver):
        print(f"Before navigating to {url}")
        print(f"Current url before navigating to {url} is '{driver.current_url}'")
        print(f"Page title before navigating to {url} is '{driver.title}'\n")

    def after_navigate_to(self, url, driver):
        print(f"After navigating to {url}")
        print(f"Current url after navigating to {url} is '{driver.current_url}'")
        print(f"Page title after navigating to {url} is '{driver.title}'\n")

    def before_navigate_back(self, driver):
        print(f"Before navigating back, '{driver.current_url}'")

    def after_navigate_back(self, driver):
        print(f"After navigating back, '{driver.current_url}'")

    def before_navigate_forward(self, driver):
        print(f"Before navigating forward, '{driver.current_url}'")

    def after_navigate_forward(self, driver):
        print(f"After navigating forward, '{driver.current_url}'")

    def before_find(self, by, value, driver):
        print(f"Searching for element with '{by}={value}' on {driver.current_url}\n")

    def after_find(self, by, value, driver):
        print(f"Found element with '{by}={value}' on {driver.current_url}\n")

    def before_change_value_of(self, element, driver):
        if element.tag_name == 'input':
            print(f"Before Change Value,{element.get_attribute('value')}")

        else:
            print(f"Before Change Value,{element.get_text}")

    def after_change_value_of(self, element, driver):
        if element.tag_name == 'input':
            print(f"After Change Value,{element.get_attribute('value')}")

        else:
            print(f"After Change Value,{element.get_text}")

    def before_click(self, element, driver):
        EventListener.button_text = element.get_attribute('value')
        if element.tag_name == 'input':
            print(f"Before clicking,{EventListener.button_text}")
        else:
            print(f"Before clicking,{EventListener.button_text}")

    def after_click(self, element, driver):
        print(f"After clicking,{EventListener.button_text}")

    def before_execute_script(self, script, driver):
        print(f"Before executing script,{script}")

    def after_execute_script(self, script, driver):
        print(f"After executing script,{script}")

    def before_close(self, driver):
        print(f"Before closing tab {driver.title}")

    def after_close(self, driver):
        print(f"After closing tab")

    def before_quit(self, driver):
        print(f"Quitting the browser with url: {driver.current_url}")
        print("Bye ...\n")

    def after_quit(self, driver):
        print("Quit the browser. Have a nice day :)")

    def on_exception(self, exception, driver):
        print(f"On Exception: {exception}")
