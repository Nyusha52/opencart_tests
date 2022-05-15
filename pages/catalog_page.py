from selenium.webdriver.common.by import By


class CatalogPage:
    COUNT = (By.CSS_SELECTOR, ".caption > h4")
    SORT = (By.CSS_SELECTOR, "#input-sort")
    SORT_NAME_DESC = (By.XPATH, "//*[text()='Name (Z - A)']")
