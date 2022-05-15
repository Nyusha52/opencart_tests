from selenium.webdriver.common.by import By


class ProductCardPage:
     QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
     ADD_CART = (By.CSS_SELECTOR, "#button-cart")
     CART_BUTTON = (By.CSS_SELECTOR, "#cart")
     ADD_CART_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
     PRICE = (By.CSS_SELECTOR, ".list-unstyled h2")
