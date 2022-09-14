import pytest

from models.contact_us import ContactUsData
from pages.contact_page import ContactPage
from pages.elements.alerts import AlertsMessages
from pages.elements.footer import FooterElement
from pages.main_page import MainPage


class TestContactPage:

    def test_add_to_card(self, browser):
        main = MainPage(browser)
        footer = FooterElement(browser)
        contact_page = ContactPage(browser)
        alert_message = AlertsMessages(browser)
        message = ContactUsData.random()
        main.get_url("/")
        footer.open_contact_page()
        contact_page.fill_name(message.name)
        contact_page.fill_email(message.email)
        contact_page.fill_enquiry(message.enquiry)
        contact_page.send_submit()
        assert "Your enquiry has been successfully sent to the store owner!" == \
               alert_message.message_send_form

    @pytest.mark.parametrize('name', ['a', "a" * 33],
                             ids=["один символ", "33 символов"])
    def test_add_to_card_negative_name(self, browser, name):
        main = MainPage(browser)
        footer = FooterElement(browser)
        contact_page = ContactPage(browser)
        alert_message = AlertsMessages(browser)
        message = ContactUsData.random()
        main.get_url("/")
        footer.open_contact_page()
        contact_page.fill_name(name)
        contact_page.fill_email(message.email)
        contact_page.fill_enquiry(message.enquiry)
        contact_page.send_submit()
        assert "Name must be between 3 and 32 characters!" == \
               alert_message.message_send_form_negative_name

    @pytest.mark.parametrize('email', ['a', 'ddd@ghgh', 'ghgh@@.gjgj.tut'],
                             ids=["один символ", "без доменной зоны", "Две собаки"])
    def test_add_to_card_negative_email(self, browser, email):
        main = MainPage(browser)
        footer = FooterElement(browser)
        contact_page = ContactPage(browser)
        alert_message = AlertsMessages(browser)
        message = ContactUsData.random()
        main.get_url("/")
        footer.open_contact_page()
        contact_page.fill_name(message.name)
        contact_page.fill_email(email)
        contact_page.fill_enquiry(message.enquiry)
        contact_page.send_submit()
        assert "E-Mail Address does not appear to be valid!" == \
               alert_message.message_send_form_negative_email

    @pytest.mark.parametrize('enquiry', ['auu', 'a'*3001],
                             ids=["один символ", "1000 знаков"])
    def test_add_to_card_negative_enquiry(self, browser, enquiry):
        main = MainPage(browser)
        footer = FooterElement(browser)
        contact_page = ContactPage(browser)
        alert_message = AlertsMessages(browser)
        message = ContactUsData.random()
        main.get_url("/")
        footer.open_contact_page()
        contact_page.fill_name(message.name)
        contact_page.fill_email(message.email)
        contact_page.fill_enquiry(enquiry)
        contact_page.send_submit()
        assert "Enquiry must be between 10 and 3000 characters!" == \
               alert_message.message_send_form_negative_enquiry
