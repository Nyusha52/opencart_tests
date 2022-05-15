from selenium.webdriver.common.by import By


class RegisterAccountPage:
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    BOX_AGREE = (By.CSS_SELECTOR, "[name ='agree']")
    CONTINUE = (By.CSS_SELECTOR, ".btn.btn-primary")
    GOOD_REGISTER = (By.CSS_SELECTOR, "h1")
    ASSERT_TEXT = (By.XPATH, '//*[text()="{}"]')
