from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

from pages.main_page import MainPage


class TestAuth:

    def test_auth(self, new_user):
        browser = new_user.driver
        browser.get(browser.base_url)
        main = MainPage(browser)
        login = LoginPage(browser)
        logout = LogoutPage(browser)
        main.logout_user()
        assert logout.logout_assert() == "Account Logout"
        main.start_login_user()
        login.login(new_user)
        assert login._find_element(login.ASSERT_LOGIN).text == "My Account"
