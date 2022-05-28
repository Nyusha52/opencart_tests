from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderElement(BasePage):
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")

    @property
    def assert_text_card(self):
        m = self._find_element(self.CART_BUTTON).text
        return m
