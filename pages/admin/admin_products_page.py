from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdminProductPage(BasePage):
    ADD_NEW_PRODUCT = (By.CSS_SELECTOR, ".pull-right .btn.btn-primary")
    FILTER_NAME = (By.NAME, "filter_name")
    FILTER = (By.ID, "button-filter")
    ASSERT_PRODUCT = (By.CSS_SELECTOR, ".table.table-bordered.table-hover")
    BOX = (By.XPATH, "//text()[contains(.,'{}')]/../..//input")
    DELETE = (By.CSS_SELECTOR, ".btn.btn-danger")

    def add_new_product(self):
        self._find_element(self.ADD_NEW_PRODUCT).click()

    def filter_name(self, data):
        self._send_keys(element=self._find_element(self.FILTER_NAME), text=data.name)
        self._find_element(self.FILTER).click()

    def assert_product(self):
        result = self._find_element(self.ASSERT_PRODUCT).text
        return result

    def delete_product(self, name):
        self._find_element((self.BOX[0], self.BOX[1].format(f"{name}"))).click()
        self._find_element(self.DELETE).click()
