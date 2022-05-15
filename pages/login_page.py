from selenium.webdriver.common.by import By


class LoginPage:
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN = (By.CSS_SELECTOR, "[value='Login']")
