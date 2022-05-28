from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AlertsMessages(BasePage):
    ADD_CART_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    @property
    def message_add_card(self):
        message = self._find_element(self.ADD_CART_MESSAGE).text
        return message

    def alert_window(self):
        alert = self.browser.switch_to.alert
        alert.accept()
