import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger("test")

class LogoutPage(BasePage):
    LOGOUT_ASSERT = (By.CSS_SELECTOR, "h1")

    def logout_assert(self):
        logger.info(f"===> logout assert")
        logout_assert = self._find_element(self.LOGOUT_ASSERT).text
        return logout_assert
