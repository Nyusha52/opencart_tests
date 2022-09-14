import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger("test")


class WishListPage(BasePage):
    WISH_LIST = (By.CSS_SELECTOR, "h2")
