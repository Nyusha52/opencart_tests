import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage


class TestMainPage:
    def test_add_to_card(self, browser):
        browser.get(browser.base_url)
        assert browser.find_element(*MainPage.CART_BUTTON).text == "0 item(s) - $0.00"
        goods = browser.find_elements(*MainPage.ADD_CART)
        assert len(goods) == 4
        goods[random.randint(0, 1)].click()
        wait = WebDriverWait(browser, 10, poll_frequency=1)
        message = wait.until(EC.visibility_of_element_located(MainPage.ADD_CART_MESSAGE))
        assert "Success: You have added" in message.text
        assert "1 item(s)" in browser.find_element(*MainPage.CART_BUTTON).text
