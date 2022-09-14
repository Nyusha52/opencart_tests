from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AlertsMessages(BasePage):
    ADD_CART_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    SEND_FORM_MESSAGE = \
        (By.XPATH, "//*[text()='Your enquiry has been successfully sent to the store owner!']")
    NEGATIVE_NAME = \
        (By.XPATH, "//*[text()='Name must be between 3 and 32 characters!']")
    NEGATIVE_EMAIL = \
        (By.XPATH, "//*[text()='E-Mail Address does not appear to be valid!']")
    NEGATIVE_ENQUIRY = \
        (By.XPATH, "//*[text()='Enquiry must be between 10 and 3000 characters!']")
    NEGATIVE_ADD_WISH_LIST = \
        (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    @property
    def message_add_card(self):
        message = self._find_element(self.ADD_CART_MESSAGE).text
        return message

    @property
    def message_negative_add_wish_list(self):
        message = self._find_element(self.NEGATIVE_ADD_WISH_LIST).text
        return message

    def alert_window(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    @property
    def message_send_form(self):
        message = self._find_element(self.SEND_FORM_MESSAGE).text
        return message

    @property
    def message_send_form_negative_name(self):
        message = self._find_element(self.NEGATIVE_NAME).text
        return message

    @property
    def message_send_form_negative_email(self):
        message = self._find_element(self.NEGATIVE_EMAIL).text
        return message

    @property
    def message_send_form_negative_enquiry(self):
        message = self._find_element(self.NEGATIVE_ENQUIRY).text
        return message


