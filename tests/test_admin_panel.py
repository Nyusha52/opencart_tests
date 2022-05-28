from pages.admin.admin_panel_page import AdminPanelPage
from pages.admin.admin_products_page import AdminProductPage


class TestAdminPage:

    def test_auth_admin(self, browser):
        admin_panel = AdminPanelPage(browser)
        admin_panel.get_url_admin()
        admin_panel.log_in()
        assert admin_panel._find_element(admin_panel.LOGIN_OK).text == "Dashboard"
