import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from models.product import ProductData
from models.user import RegistrData
from pages.admin.add_product_page import AddProductPage
from pages.admin.admin_panel_page import AdminPanelPage
from pages.admin.admin_products_page import AdminProductPage
from pages.application import Application
from pages.elements.alerts import AlertsMessages
from pages.main_page import MainPage
from pages.register_account_page import RegisterAccountPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers/"))
    parser.addoption("--url", default="http://192.168.1.43:8081")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    base_url = request.config.getoption("--url")

    if browser == "chrome":
        service = Service(executable_path=os.path.join(drivers, "chromedriver"))
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=os.path.join(drivers, "geckodriver"))
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=os.path.join(drivers, "operadriver"))
    elif browser == "ya":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path=os.path.join(drivers, "yandexdriver"), options=options)
    else:
        raise Exception("Driver not supported")
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.get(base_url)
    driver.base_url = base_url

    return driver


@pytest.fixture
def new_user(browser):
    register_account = RegisterAccountPage(browser)
    main_page = MainPage(browser)
    admin_panel = AdminPanelPage(browser)
    alert_delete = AlertsMessages(browser)
    main_page.get_url("/")
    main_page.find_user()
    new_person = RegistrData.random()
    register_account.fill_fields(new_person)
    fixture = Application(
        driver=browser,
        data=new_person
    )
    yield fixture
    main_page.get_url("/admin/")
    admin_panel.log_in()
    admin_panel.delete_user(new_person)
    alert_delete.alert_window()
    admin_panel.assert_delete_user()


@pytest.fixture
def add_product(browser):
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
    return browser, data
