import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.user import RegistrData
from pages.admin_panel_page import AdminPanelPage
from pages.main_page import MainPage
from pages.register_account_page import RegisterAccountPage


class TestRegistrPozitive:
    def test_register(self, browser):
        data = RegistrData.random()
        browser.get(browser.base_url)
        browser.find_element(*MainPage.MY_ACCOUNT).click()
        browser.find_element(*MainPage.REGISTER).click()
        browser.find_element(*RegisterAccountPage.FIRSTNAME).send_keys(data.name)
        browser.find_element(*RegisterAccountPage.LASTNAME).send_keys(data.lastname)
        browser.find_element(*RegisterAccountPage.EMAIL).send_keys(data.email)
        browser.find_element(*RegisterAccountPage.TELEPHONE).send_keys(data.telephone)
        browser.find_element(*RegisterAccountPage.PASSWORD).send_keys(data.password)
        browser.find_element(*RegisterAccountPage.PASSWORD_CONFIRM).send_keys(data.password)
        browser.find_element(*RegisterAccountPage.BOX_AGREE).click()
        browser.find_element(*RegisterAccountPage.CONTINUE).click()
        assert browser.find_element(*RegisterAccountPage.GOOD_REGISTER).text == "Your Account Has Been Created!"
        browser.get(browser.base_url + "/admin/")
        browser.find_element(*AdminPanelPage.USER_NAME).send_keys("user")
        browser.find_element(*AdminPanelPage.PASSVORD).send_keys("bitnami")
        browser.find_element(*AdminPanelPage.LOG_IN).click()
        browser.find_element(*AdminPanelPage.CUSTOMERS).click()
        browser.find_element(*AdminPanelPage.CUSTOMERS_1).click()
        browser.find_element(AdminPanelPage.BOX[0],
                             AdminPanelPage.BOX[1].format(f"{data.name} {data.lastname}")).click()
        browser.find_element(*AdminPanelPage.DELETE).click()
        alert = browser.switch_to.alert
        alert.accept()
        wait = WebDriverWait(browser, 10, poll_frequency=1)
        message = wait.until(EC.visibility_of_element_located(AdminPanelPage.DELETE_OK))
        assert message.text == "Success: You have modified customers!\n×"

    @pytest.mark.parametrize('name', [0, 'a', "a" * 32, "lat"], ids=["ноль", "один символ", "32 символов", "латиница"])
    def test_register_name(self, browser, name):
        browser.get(browser.base_url)
        data = RegistrData.random()
        browser.find_element(*MainPage.MY_ACCOUNT).click()
        browser.find_element(*MainPage.REGISTER).click()
        browser.find_element(*RegisterAccountPage.FIRSTNAME).send_keys(name)
        browser.find_element(*RegisterAccountPage.LASTNAME).send_keys(data.lastname)
        browser.find_element(*RegisterAccountPage.EMAIL).send_keys(data.email)
        browser.find_element(*RegisterAccountPage.TELEPHONE).send_keys("телефон")
        browser.find_element(*RegisterAccountPage.PASSWORD).send_keys(data.password)
        browser.find_element(*RegisterAccountPage.PASSWORD_CONFIRM).send_keys(data.password)
        browser.find_element(*RegisterAccountPage.BOX_AGREE).click()
        browser.find_element(*RegisterAccountPage.CONTINUE).click()
        assert browser.find_element(*RegisterAccountPage.GOOD_REGISTER).text == "Your Account Has Been Created!"
        browser.get(browser.base_url + "/admin/")
        browser.find_element(*AdminPanelPage.USER_NAME).send_keys("user")
        browser.find_element(*AdminPanelPage.PASSVORD).send_keys("bitnami")
        browser.find_element(*AdminPanelPage.LOG_IN).click()
        browser.find_element(*AdminPanelPage.CUSTOMERS).click()
        browser.find_element(*AdminPanelPage.CUSTOMERS_1).click()
        browser.find_element(AdminPanelPage.BOX[0], AdminPanelPage.BOX[1].format(f"{name} {data.lastname}")).click()
        browser.find_element(*AdminPanelPage.DELETE).click()
        alert = browser.switch_to.alert
        alert.accept()
        wait = WebDriverWait(browser, 10, poll_frequency=1)
        message = wait.until(EC.visibility_of_element_located(AdminPanelPage.DELETE_OK))
        assert message.text == "Success: You have modified customers!\n×"


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
        browser.get(browser.base_url)
        browser.find_element(*MainPage.MY_ACCOUNT).click()
        browser.find_element(*MainPage.REGISTER).click()
        if "firstName" in data:
            browser.find_element(*RegisterAccountPage.FIRSTNAME).send_keys(data["firstName"])
        if "lastName" in data:
            browser.find_element(*RegisterAccountPage.LASTNAME).send_keys(data["lastName"])
        if "email" in data:
            browser.find_element(*RegisterAccountPage.EMAIL).send_keys(data["email"])
        if "telephone" in data:
            browser.find_element(*RegisterAccountPage.TELEPHONE).send_keys(data["telephone"])
        if "password" in data:
            browser.find_element(*RegisterAccountPage.PASSWORD).send_keys(data["password"])
        if "password_confirm" in data:
            browser.find_element(*RegisterAccountPage.PASSWORD_CONFIRM).send_keys(data["password_confirm"])
        browser.find_element(*RegisterAccountPage.BOX_AGREE).click()
        browser.find_element(*RegisterAccountPage.CONTINUE).click()
        assert browser.find_element(RegisterAccountPage.ASSERT_TEXT[0],
                                    RegisterAccountPage.ASSERT_TEXT[1].format(data["assert"])).is_displayed()

    def test_register_password_not_equals_confirm_password(self, browser):
        browser.get(browser.base_url)
        browser.find_element(*MainPage.MY_ACCOUNT).click()
        browser.find_element(*MainPage.REGISTER).click()
        browser.find_element(*RegisterAccountPage.FIRSTNAME).send_keys("Имя")
        browser.find_element(*RegisterAccountPage.LASTNAME).send_keys("Фамилия")
        browser.find_element(*RegisterAccountPage.EMAIL).send_keys("kgkg@имq1qя.попййцe")
        browser.find_element(*RegisterAccountPage.TELEPHONE).send_keys("телефон")
        browser.find_element(*RegisterAccountPage.PASSWORD).send_keys("пароль123")
        browser.find_element(*RegisterAccountPage.PASSWORD_CONFIRM).send_keys("пароль1235")
        browser.find_element(*RegisterAccountPage.BOX_AGREE).click()
        browser.find_element(*RegisterAccountPage.CONTINUE).click()
        assert browser.find_element(RegisterAccountPage.ASSERT_TEXT[0],
                                    RegisterAccountPage.ASSERT_TEXT[1].format(
                                        'Password confirmation does not match password!')).is_displayed()
