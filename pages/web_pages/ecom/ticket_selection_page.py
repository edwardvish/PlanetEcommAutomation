from selenium.webdriver.common.by import By

from extensions.ui_actions import UiActions

event_title = (By.XPATH, "//div[@class='event-preview--title']")
tg_message = (By.XPATH, "//div[@class='tickets--group-message']")
ticket_info = (By.XPATH, "//div[@class='form-actions']")#multiple
ticket_summary = (By.XPATH, "//div[@class='tickets--total d-flex justify-content-between']")
continue_button = (By.CSS_SELECTOR, ".btn-text")
first_screening_button = (By.XPATH, "(//div[@class='qb-movie-info-column']/a[1])[1]")


class MainPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_event_title(self):
        title = UiActions.get_text(self.driver, event_title)
        return title

    def get_tg_message(self):
        message = UiActions.get_text(self.driver, tg_message)
        return message

    def get_ticket_info(self):
        driver = self.driver
        ticket = UiActions.find_multiple(driver, *ticket_info)
        ticketinfo = ticket.find_element(By.XPATH, ".//span")
        ticket_data = []
        for i in range(0, len(ticketinfo), 2):
            tkt_name = UiActions.get_text(ticketinfo[i])
            ticket_price = UiActions.get_text(ticketinfo[i + 1])
            ticket_data.append((tkt_name, ticket_price))
        return ticket_data

    def add_tickets(self, ticket_type, count):
        ticket = UiActions.find_multiple(self.driver, *ticket_info)
        if ticket_type.lower() == 'regular':
            add_regular = ticket.find_element(By.XPATH, '/div/i[@class="fas fa-plus"]')
            for i in range(count-1):
                add_regular[0].click()

    def get_total_amount(self): #need to use verify class to verify amount agains CSV file
        summary = UiActions.find(self.driver, *ticket_summary)
        amount = summary.find_element(By.XPATH, '/div/p/strong').text
        return amount














