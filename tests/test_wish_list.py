import logging

from pages.elements.alerts import AlertsMessages
from pages.main_page import MainPage
from pages.wish_list_page import WishListPage

logger = logging.getLogger("test")


class TestWishListPage:

    def test_add_goods_wish_list_not_register(self, browser):
        main_page = MainPage(browser)
        alert_message = AlertsMessages(browser)
        main_page.get_url("/")
        main_page._find_element(locator=MainPage.WISH_LIST).click()
        assert "create an account" in alert_message.message_negative_add_wish_list

    def test_add_goods_wish_list(self, new_user):
        browser = new_user.driver
        main_page = MainPage(browser)
        wish_list_page = WishListPage(browser)
        main_page.get_url("/")
        main_page._find_element(locator=MainPage.WISH_LIST).click()
        main_page._find_element(locator=MainPage.WISH_LIST_TOTAL).click()
        assert wish_list_page._find_element(
            wish_list_page.WISH_LIST).text == "My Wish List"
