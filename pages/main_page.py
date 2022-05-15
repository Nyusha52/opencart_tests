from selenium.webdriver.common.by import By


class MainPage:
    MY_ACCOUNT = (By.CSS_SELECTOR, "a[title='My Account']")
    REGISTER = (By.XPATH, "//a[text()='Register']")
    LOGIN = (By.XPATH, "//a[text()='Login']")
    LOGOUT = (By.XPATH, "//a[text()='Logout']")
    ADD_CART = (By.CSS_SELECTOR, ".button-group")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")
    ADD_CART_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
