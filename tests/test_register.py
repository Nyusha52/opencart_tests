import logging

import pytest

from models.user import RegistrData
from pages.admin.admin_panel_page import AdminPanelPage
from pages.elements.alerts import AlertsMessages
from pages.main_page import MainPage
from pages.register_account_page import RegisterAccountPage
logger = logging.getLogger("test")


class TestRegistrPozitive:

    def test_register(self, browser):
        register_account = RegisterAccountPage(browser)
        main_page = MainPage(browser)
        admin_panel = AdminPanelPage(browser)
        allert_delete = AlertsMessages(browser)
        logger.info("===> open main page")
        main_page.get_url("/")
        main_page.find_user()
        new_person = RegistrData.random()
        register_account.fill_fields(new_person)
        main_page.get_url("/admin/")
        admin_panel.log_in()
        admin_panel.delete_user(new_person)
        allert_delete.alert_window()
        admin_panel.assert_delete_user()

    @pytest.mark.parametrize('name', ['a', "a" * 32, "lat"], ids=["один символ", "32 символов", "латиница"])
    def test_register_name(self, browser, name):
        main_page = MainPage(browser)
        admin_panel = AdminPanelPage(browser)
        allert_delete = AlertsMessages(browser)
        register_account = RegisterAccountPage(browser)
        main_page.get_url("/")
        data = RegistrData.random()
        data.name = name
        main_page.find_user()
        register_account._send_keys(element=register_account._find_element(register_account.FIRSTNAME), text=name)

        register_account._send_keys(element=register_account._find_element(register_account.LASTNAME),
                                    text=data.lastname)
        register_account._send_keys(element=register_account._find_element(register_account.EMAIL), text=data.email)
        register_account._send_keys(element=register_account._find_element(register_account.TELEPHONE),
                                    text=data.telephone)
        register_account._send_keys(element=register_account._find_element(register_account.PASSWORD),
                                    text=data.password)
        register_account._send_keys(element=register_account._find_element(register_account.PASSWORD_CONFIRM),
                                    text=data.password)
        register_account._find_element(register_account.BOX_AGREE).click()
        register_account._find_element(register_account.CONTINUE).click()
        assert register_account._find_element(
            register_account.GOOD_REGISTER).text == "Your Account Has Been Created!"
        main_page.get_url("/admin/")
        admin_panel.log_in()
        admin_panel.delete_user(data)
        allert_delete.alert_window()
        admin_panel.assert_delete_user()


class TestRegistrNegative:
    data_with_one_empty_param = [
        ({'firstName': 'Имя', 'lastName': 'Фамилия', 'email': 'test@test.com', "telephone": "555555555",
          'password_confirm': '12345678', 'assert': 'Password must be between 4 and 20 characters!'}),
        ({'password': '12345678', 'firstName': 'Имя', 'lastName': 'Фамилия', 'email': 'test@test.com',
          'password_confirm': '12345678', 'assert': 'Telephone must be between 3 and 32 characters!'}),
        ({'password': '12345678', 'lastName': 'Имя', 'email': 'test@test.com', "telephone": "555555555",
          'password_confirm': '12345678', 'assert': 'First Name must be between 1 and 32 characters!'}),
        ({'password': '12345678', 'firstName': 'Имя', 'email': 'test@test.com', "telephone": "555555555",
          'password_confirm': '12345678', 'assert': 'Last Name must be between 1 and 32 characters!'}),
        ({'password': '12345678', 'firstName': 'Имя', 'lastName': 'Фамилия', "telephone": "555555555",
          'password_confirm': '12345678', 'assert': 'E-Mail Address does not appear to be valid!'}),
        ({'password': '12345678', 'firstName': 'Имя', 'lastName': 'Фамилия', "telephone": "555555555",
          'email': 'test@test.com', 'assert': 'Password confirmation does not match password!'}),
    ]

    @pytest.mark.parametrize("data", data_with_one_empty_param)
    def test_register_one_empty_param(self, browser, data):
        main_page = MainPage(browser)
        register_account = RegisterAccountPage(browser)
        main_page.get_url("/")
        main_page.find_user()
        if "firstName" in data:
            register_account._send_keys(element=register_account._find_element(register_account.FIRSTNAME),
                                        text=data["firstName"])
        if "lastName" in data:
            register_account._send_keys(element=register_account._find_element(register_account.LASTNAME),
                                        text=data["lastName"])
        if "email" in data:
            register_account._send_keys(element=register_account._find_element(register_account.EMAIL),
                                        text=data["email"])
        if "telephone" in data:
            register_account._send_keys(element=register_account._find_element(register_account.TELEPHONE),
                                        text=data["telephone"])
        if "password" in data:
            register_account._send_keys(element=register_account._find_element(register_account.PASSWORD),
                                        text=data["password"])
        if "password_confirm" in data:
            register_account._send_keys(element=register_account._find_element(register_account.PASSWORD_CONFIRM),
                                        text=data["password_confirm"])
        register_account._find_element(register_account.BOX_AGREE).click()
        register_account._find_element(register_account.CONTINUE).click()
        assert register_account._find_element((register_account.ASSERT_TEXT[0],
                                               register_account.ASSERT_TEXT[1].format(data["assert"]))).is_displayed()

    def test_register_password_not_equals_confirm_password(self, browser):
        main_page = MainPage(browser)
        register_account = RegisterAccountPage(browser)
        data = RegistrData.random()
        main_page.get_url("/")
        main_page.find_user()
        register_account._send_keys(element=register_account._find_element(register_account.FIRSTNAME), text=data.name)
        register_account._send_keys(element=register_account._find_element(register_account.LASTNAME),
                                    text=data.lastname)
        register_account._send_keys(element=register_account._find_element(register_account.EMAIL), text=data.email)
        register_account._send_keys(element=register_account._find_element(register_account.TELEPHONE),
                                    text=data.telephone)
        register_account._send_keys(element=register_account._find_element(register_account.PASSWORD),
                                    text=data.password)
        register_account._send_keys(element=register_account._find_element(register_account.PASSWORD_CONFIRM),
                                    text="пароль1235")
        register_account._find_element(register_account.BOX_AGREE).click()
        register_account._find_element(register_account.CONTINUE).click()
        assert register_account._find_element((register_account.ASSERT_TEXT[0],
                                               register_account.ASSERT_TEXT[1].format(
                                                   'Password confirmation does not match password!'))).is_displayed()
