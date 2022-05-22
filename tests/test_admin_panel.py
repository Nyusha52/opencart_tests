from pages.admin_panel_page import AdminPanelPage


class TestAdminPage:

    def test_auth_admin(self, browser):
        browser.get(browser.base_url + "/admin/")
        browser.find_element(*AdminPanelPage.USER_NAME).send_keys("user")
        browser.find_element(*AdminPanelPage.PASSVORD).send_keys("bitnami")
        browser.find_element(*AdminPanelPage.LOG_IN).click()
        assert browser.find_element(*AdminPanelPage.LOGIN_OK).text == "Dashboard"
