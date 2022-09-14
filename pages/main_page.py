import logging
import random

from allure_commons._allure import step
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger("test")


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
    WISH_LIST = (By.XPATH, "//*[@data-original-title='Add to Wish List']")
    WISH_LIST_TOTAL = (By.XPATH, "//*[@id='wishlist-total']")


    @step("find user")
    def find_user(self):
        logger.info(f"===> find user")
        self._find_element(self.MY_ACCOUNT).click()
        self._find_element(self.REGISTER).click()

    @step("logout user")
    def logout_user(self):
        logger.info(f"===> ogout user")
        self._find_element(self.MY_ACCOUNT).click()
        self._find_element(self.LOGOUT).click()

    @step("start login user")
    def start_login_user(self):
        logger.info(f"===> start login user")
        self._find_element(self.MY_ACCOUNT).click()
        self._find_element(self.LOGIN).click()

    @step("click good")
    def click_good(self):
        logger.info(f"===> click good")
        goods = self.list_elements(self.ADD_CART)
        assert len(goods) == 4
        goods[random.randint(0, 1)].click()

    @step("change currency")
    def change_currency(self):
        logger.info(f"===> change currency")
        self._find_element(self.CURRENCY).click()
        self._find_clickable_element(self.POUND_STERLING).click()

    @step("assert change currency")
    def assert_change_currency(self):
        logger.info(f"===> assert change currency")
        currency = self.list_elements(self.PRICE_TAX)
        return currency

    @step("click good")
    def click_good_wish_list(self):
        logger.info(f"===> click good")
        goods = self.list_elements(self.ADD_CART)
        assert len(goods) == 4
        goods[random.randint(0, 1)].click()