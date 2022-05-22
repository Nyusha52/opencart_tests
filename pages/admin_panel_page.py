from selenium.webdriver.common.by import By


class AdminPanelPage:
     USER_NAME = (By.CSS_SELECTOR, "#input-username")
     PASSVORD = (By.CSS_SELECTOR, "#input-password")
     LOG_IN = (By.CSS_SELECTOR, ".fa.fa-key")
     CUSTOMERS = (By.XPATH, "//a[text()=' Customers']")
     CUSTOMERS_1 = (By.XPATH, "//a[text()='Customers']")
     BOX = (By.XPATH, "//text()[contains(.,'{}')]/../..//input")
     DELETE = (By.CSS_SELECTOR, ".btn.btn-danger")
     DELETE_OK = (By.CSS_SELECTOR, ".alert")
     LOGIN_OK = (By.CSS_SELECTOR, "h1")


