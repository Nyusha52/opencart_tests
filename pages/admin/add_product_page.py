import logging

from allure_commons._allure import step
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
logger = logging.getLogger("test")


class AddProductPage(BasePage):
    ADD_NEW_PRODUCT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PRODUCT_NAME = (By.NAME, "product_description[1][name]")
    META_TAG_TITLE = (By.NAME, "product_description[1][meta_title]")
    MODEL = (By.NAME, "model")
    SAFE = (By.CSS_SELECTOR, '[data-original-title="Save"]')
    DATA_TAB = (By.XPATH, "//a[text()='Data']")

    @step("required fields general tab")
    def required_fields_general_tab(self, data):
        logger.info(f"===> login {data.name} {data.meta_tag}")
        self._send_keys(element=self._find_element(self.PRODUCT_NAME), text=data.name)
        self._send_keys(element=self._find_element(self.META_TAG_TITLE), text=data.meta_tag)

    @step("required fields data tab")
    def required_fields_data_tab(self, data):
        self._find_element(self.DATA_TAB).click()
        logger.info(f"===> login {data.model}")
        self._send_keys(element=self._find_element(self.MODEL), text=data.model)

    @step("safe")
    def safe(self):
        logger.info(f"===> safe")
        self._find_element(self.SAFE).click()
