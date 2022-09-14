import logging

from pages.product_card_page import ProductCardPage

logger = logging.getLogger("test")


class TestProductCardPage:

    def test_add_goods(self, browser):
        """Для скриншота"""
        product_card = ProductCardPage(browser)
        product_card.get_url("/desktops/htc-touch-hd")
        assert product_card._find_element(
            locator=ProductCardPage.CART_BUTTON).text == "0 item(s) - $0.00"
        product_card._send_keys(
            element=product_card._find_element(locator=ProductCardPage.QUANTITY), text='5')
        product_card._find_element(locator=ProductCardPage.ADD_CART).click()
        summa = product_card._find_element(locator=ProductCardPage.PRICE).text[1:]
        logger.info(f"5 item(s) - ${float(summa) * 6:.2f}")
        assert product_card._find_element(
            locator=ProductCardPage.CART_BUTTON).text == f"5 item(s) - ${float(summa) * 5:.2f}"

    def test_add_goods_1(self, browser):
        product_card = ProductCardPage(browser)
        product_card.get_url("/desktops/htc-touch-hd")
        assert product_card._find_element(
            locator=ProductCardPage.CART_BUTTON).text == "0 item(s) - $0.00"
        product_card._send_keys(
            element=product_card._find_element(locator=ProductCardPage.QUANTITY), text='5')
        product_card._find_element(locator=ProductCardPage.ADD_CART).click()
        summa = product_card._find_element(locator=ProductCardPage.PRICE).text[1:]
        logger.info(f"5 item(s) - ${float(summa) * 5:.2f}")
        assert product_card._find_element(
            locator=ProductCardPage.CART_BUTTON).text == f"5 item(s) - ${float(summa) * 5:.2f}"

    def test_delete_good(self, browser):
        product_card = ProductCardPage(browser)
        product_card.get_url("/desktops/htc-touch-hd")
        assert product_card._find_element(
            locator=ProductCardPage.CART_BUTTON).text == "0 item(s) - $0.00"
        product_card._send_keys(
            element=product_card._find_element(locator=ProductCardPage.QUANTITY), text='1')
        product_card._find_element(locator=ProductCardPage.ADD_CART).click()
        product_card.get_url("/index.php?route=checkout/cart")
        product_card._find_element(locator=ProductCardPage.DELETE_PRODUCT).click()
        assert product_card._find_element(
            locator=ProductCardPage.EMPTY).text == "Your shopping cart is empty!"
