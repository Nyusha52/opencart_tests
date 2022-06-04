import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    MY_ACCOUNT = (By.CSS_SELECTOR, "a[title='My Account']")
    REGISTER = (By.XPATH, "//a[text()='Register']")
    LOGIN = (By.XPATH, "//a[text()='Login']")
    LOGOUT = (By.XPATH, "//a[text()='Logout']")
    ADD_CART = (By.CSS_SELECTOR, ".button-group")
    LOGOUT_ASSERT = (By.CSS_SELECTOR, "h1")
    CURRENCY = (By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle")
    POUND_STERLING = (By.CSS_SELECTOR, '[name="GBP"]')
    PRICE_TAX = (By.CSS_SELECTOR, '.price-tax')

    def find_user(self):
        self._find_element(self.MY_ACCOUNT).click()
        self._find_element(self.REGISTER).click()

    def logout_user(self):
        self._find_element(self.MY_ACCOUNT).click()
        self._find_element(self.LOGOUT).click()

    def start_login_user(self):
        self._find_element(self.MY_ACCOUNT).click()
        self._find_element(self.LOGIN).click()

    def click_good(self):
        goods = self.list_elements(self.ADD_CART)
        assert len(goods) == 4
        goods[random.randint(0, 1)].click()

    def change_currency(self):
        self._find_element(self.CURRENCY).click()
        self._find_clickable_element(self.POUND_STERLING).click()

    def assert_change_currency(self):
        currency = self.list_elements(self.PRICE_TAX)
        return currency
