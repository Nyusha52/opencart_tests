from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.main_page import MainPage


class TestAuth:

    def test_auth(self, new_user):
        browser = new_user.driver
        browser.get(browser.base_url)
        browser.find_element(*MainPage.MY_ACCOUNT).click()
        browser.find_element(*MainPage.LOGOUT).click()
        assert browser.find_element(*LogoutPage.LOGOUT).text == "Account Logout"
        browser.find_element(*MainPage.MY_ACCOUNT).click()
        browser.find_element(*MainPage.LOGIN).click()
        browser.find_element(*LoginPage.EMAIL).send_keys(new_user.email)
        browser.find_element(*LoginPage.PASSWORD).send_keys(new_user.password)
        browser.find_element(*LoginPage.LOGIN).click()
