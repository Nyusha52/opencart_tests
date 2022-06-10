import logging

from allure_commons._allure import step
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
logger = logging.getLogger("test")


class CatalogPage(BasePage):
    COUNT = (By.CSS_SELECTOR, ".caption > h4")
    SORT = (By.CSS_SELECTOR, "#input-sort")
    SORT_NAME_DESC = (By.XPATH, "//*[text()='Name (Z - A)']")

    @property
    @step("count_goods")
    def count_goods(self):
        logger.info(f"===> count goods")
        return self.browser.find_elements(*self.COUNT)

    @step("sort_goods_by_name")
    def sort_goods_by_name(self):
        logger.info(f"===> sort goods by name")
        self._find_element(self.SORT).click()
        self._find_element(self.SORT_NAME_DESC).click()


    @property
    @step("count_goods")
    def sorted_goods(self):
        logger.info(f"===> sorted goods")
        return self.browser.find_elements(*self.COUNT)
