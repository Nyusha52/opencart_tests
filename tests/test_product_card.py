from pages.product_card_page import ProductCardPage


class TestProductCardPage:

    def test_add_goods(self, browser):
        product_card = ProductCardPage(browser)
        product_card.get_url("/desktops/htc-touch-hd")
        assert product_card._find_element(locator=ProductCardPage.CART_BUTTON).text == "0 item(s) - $0.00"
        product_card._send_keys(element=product_card._find_element(locator=ProductCardPage.QUANTITY), text='5')
        product_card._find_element(locator=ProductCardPage.ADD_CART).click()
        summa = product_card._find_element(locator=ProductCardPage.PRICE).text[1:]
        assert product_card._find_element(
            locator=ProductCardPage.CART_BUTTON).text == f"5 item(s) - ${float(summa) * 5:.2f}"

    def test_add_goods_1(self, browser):
        """Для скриншота"""
        product_card = ProductCardPage(browser)
        product_card.get_url("/desktops/htc-touch-hd")
        assert product_card._find_element(locator=ProductCardPage.CART_BUTTON).text == "0 item(s) - $0.00"
        product_card._send_keys(element=product_card._find_element(locator=ProductCardPage.QUANTITY), text='5')
        product_card._find_element(locator=ProductCardPage.ADD_CART).click()
        summa = product_card._find_element(locator=ProductCardPage.PRICE).text[1:]
        assert product_card._find_element(
            locator=ProductCardPage.CART_BUTTON).text == f"5 item(s) - ${float(summa) * 6:.2f}"
