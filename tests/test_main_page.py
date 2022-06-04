from pages.elements.alerts import AlertsMessages
from pages.elements.header import HeaderElement
from pages.main_page import MainPage


class TestMainPage:

    def test_add_to_card(self, browser):
        main = MainPage(browser)
        alert_message = AlertsMessages(browser)
        header = HeaderElement(browser)
        main.get_url("/")
        assert header.assert_text_card == "0 item(s) - $0.00"
        main.click_good()
        assert "Success: You have added" in alert_message.message_add_card
        assert "1 item(s)" in header.assert_text_card

    def test_change_currency(self, browser):
        main = MainPage(browser)
        main.get_url("/")
        main.change_currency()
        texts = main.assert_change_currency()
        for i in texts:
            assert "£" in i.text
