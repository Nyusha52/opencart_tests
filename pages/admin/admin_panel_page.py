from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdminPanelPage(BasePage):
    USER_NAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOG_IN = (By.CSS_SELECTOR, ".fa.fa-key")
    CUSTOMERS = (By.XPATH, "//a[text()=' Customers']")
    CUSTOMERS_1 = (By.XPATH, "//a[text()='Customers']")
    BOX = (By.XPATH, "//text()[contains(.,'{}')]/../..//input")
    DELETE = (By.CSS_SELECTOR, ".btn.btn-danger")
    DELETE_OK = (By.CSS_SELECTOR, ".alert")
    LOGIN_OK = (By.CSS_SELECTOR, "h1")
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCT = (By.XPATH, "//a[text()='Products']")

    def log_in(self):
        self._send_keys(element=self._find_element(self.USER_NAME), text="user")
        self._send_keys(element=self._find_element(self.PASSWORD), text="bitnami")
        self._find_element(self.LOG_IN).click()

    def delete_user(self, new_person):
        self._find_element(self.CUSTOMERS).click()
        self._find_clickable_element(self.CUSTOMERS_1).click()
        self._find_element((self.BOX[0], self.BOX[1].format(f"{new_person.name} {new_person.lastname}"))).click()
        self._find_element(self.DELETE).click()

    def assert_delete_user(self):
        assert self._find_element(self.DELETE_OK).text == "Success: You have modified customers!\n×"

    def open_product_page(self):
        self._find_element(self.CATALOG).click()
        self._find_clickable_element(self.PRODUCT).click()

    def get_url_admin(self):
        self.get_url("/admin")
