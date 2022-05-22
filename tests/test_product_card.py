from pages.product_card_page import ProductCardPage


class TestProductCardPage:
    def test_add_goods(self, browser):
        browser.get(browser.base_url + "/desktops//htc-touch-hd")
        assert browser.find_element(*ProductCardPage.CART_BUTTON).text == "0 item(s) - $0.00"
        browser.find_element(*ProductCardPage.QUANTITY).clear()
        browser.find_element(*ProductCardPage.QUANTITY).send_keys("5")
        browser.find_element(*ProductCardPage.ADD_CART).click()
        summ = float(browser.find_element(*ProductCardPage.PRICE).text[1:]) * 5
        assert browser.find_element(*ProductCardPage.CART_BUTTON).text == f"5 item(s) - ${summ:.2f}"
