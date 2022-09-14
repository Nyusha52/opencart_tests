import logging

from allure_commons._allure import step
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger("test")


class FooterElement(BasePage):
    CONTACT_US = (By.XPATH, "//a[text()='Contact Us']")

    @step("Open contact us")
    def open_contact_page(self):
        logger.info(f"===> Open contact us")
        self._find_element(self.CONTACT_US).click()
