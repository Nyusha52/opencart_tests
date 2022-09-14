import logging

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger("test")


class ContactPage(BasePage):
    LOGOUT_ASSERT = (By.CSS_SELECTOR, "h1")
    YOUR_NAME = (By.XPATH, "//*[@name='name']")
    EMAIL_ADDRESS = (By.XPATH, "//*[@name='email']")
    ENQUIRY = (By.XPATH, "//*[@name='enquiry']")
    SUBMIT = (By.XPATH, "//*[@value='Submit']")

    def fill_name(self, name):
        logger.info(f"===> fill name")
        with allure.step(f"fill {name}"):
            self._send_keys(element=self._find_element(self.YOUR_NAME), text=name)

    def fill_email(self, email):
        with allure.step(f"login {email}"):
            self._send_keys(element=self._find_element(self.EMAIL_ADDRESS), text=email)

    def fill_enquiry(self, enquiry):
        with allure.step(f"fill {enquiry}"):
            self._send_keys(element=self._find_element(self.ENQUIRY), text=enquiry)

    def send_submit(self):
        with allure.step(f"send submit"):
            self._find_element(self.SUBMIT).click()
