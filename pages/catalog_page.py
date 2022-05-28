from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CatalogPage(BasePage):
    COUNT = (By.CSS_SELECTOR, ".caption > h4")
    SORT = (By.CSS_SELECTOR, "#input-sort")
    SORT_NAME_DESC = (By.XPATH, "//*[text()='Name (Z - A)']")

    @property
    def count_goods(self):
        return self.browser.find_elements(*self.COUNT)

    def sort_goods_by_name(self):
        self._find_element(self.SORT).click()
        self._find_element(self.SORT_NAME_DESC).click()

    @property
    def sorted_goods(self):
        return self.browser.find_elements(*self.COUNT)
