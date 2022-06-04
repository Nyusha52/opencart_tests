from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LogoutPage(BasePage):
    LOGOUT_ASSERT = (By.CSS_SELECTOR, "h1")

    def logout_assert(self):
        logout_assert = self._find_element(self.LOGOUT_ASSERT).text
        return logout_assert
