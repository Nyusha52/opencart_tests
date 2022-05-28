from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddProductPage(BasePage):
    ADD_NEW_PRODUCT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PRODUCT_NAME = (By.NAME, "product_description[1][name]")
    META_TAG_TITLE = (By.NAME, "product_description[1][meta_title]")
    MODEL = (By.NAME, "model")
    SAFE = (By.CSS_SELECTOR, '[data-original-title="Save"]')
    DATA_TAB = (By.XPATH, "//a[text()='Data']")

    def required_fields_general_tab(self, data):
        self._send_keys(element=self._find_element(self.PRODUCT_NAME), text=data.name)
        self._send_keys(element=self._find_element(self.META_TAG_TITLE), text=data.meta_tag)

    def required_fields_data_tab(self, data):
        self._find_element(self.DATA_TAB).click()
        self._send_keys(element=self._find_element(self.MODEL), text=data.model)

    def safe(self):
        self._find_element(self.SAFE).click()
