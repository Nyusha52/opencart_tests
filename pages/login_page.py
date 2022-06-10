import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger("test")


class LoginPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN = (By.CSS_SELECTOR, "[value='Login']")
    ASSERT_LOGIN = (By.XPATH, "//h2 [text()='My Account']")

    def login(self, new_user):
        logger.info(f"===> login {new_user}")
        self._send_keys(element=self._find_element(self.EMAIL), text=new_user.email)
        self._send_keys(element=self._find_element(self.PASSWORD), text=new_user.password)
        self._find_element(self.LOGIN).click()
