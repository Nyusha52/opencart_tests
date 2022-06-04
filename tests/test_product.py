from models.product import ProductData
from pages.admin.add_product_page import AddProductPage
from pages.admin.admin_panel_page import AdminPanelPage
from pages.admin.admin_products_page import AdminProductPage
from pages.elements.alerts import AlertsMessages


class TestAddProduct:

    def test_add_product(self, browser):
        admin_panel = AdminPanelPage(browser)
        add_product = AddProductPage(browser)
        data = ProductData.random()
        product = AdminProductPage(browser)
        admin_panel.get_url_admin()
        admin_panel.log_in()
        admin_panel.open_product_page()
        product.add_new_product()
        add_product.required_fields_general_tab(data)
        add_product.required_fields_data_tab(data)
        add_product.safe()
        product.filter_name(data)
        assert data.name in product.assert_product()

    def test_dell_product(self, add_product):
        browser = add_product[0]
        data = add_product[1]
        alert_delete = AlertsMessages(browser)
        product = AdminProductPage(browser)
        product.delete_product(data.name)
        alert_delete.alert_window()
        assert data.name not in product.assert_product()
