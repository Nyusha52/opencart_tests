import logging
import datetime

import pytest
import requests
import allure
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.opera.options import Options

from models.product import ProductData
from models.user import RegistrData
from pages.admin.add_product_page import AddProductPage
from pages.admin.admin_panel_page import AdminPanelPage
from pages.admin.admin_products_page import AdminProductPage
from pages.application import Application
from pages.elements.alerts import AlertsMessages
from pages.main_page import MainPage
from pages.register_account_page import RegisterAccountPage

logger = logging.getLogger("test")


@allure.step("Waiting for resource availability {url}")
def wait_url_data(url, timeout=10):
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url:
                return response.content
            else:
                return response.text
    return None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers/"))
    parser.addoption("--url", default="http://192.168.1.43:8081")
    parser.addoption("--executor", action="store", default="192.168.1.43")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--bv")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    base_url = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")

    name = request.node.name
    elements_name = name.split("[")
    request.node.name = elements_name[0]
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))
    if executor == "local":
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
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "screenResolution": "1280x720",
            "name": "Nyusha",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableLog": logs
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            # 'goog:chromeOptions': {}
        }
        options = Options()
        if browser == "opera":
            options.add_experimental_option('w3c', True)

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
            options=options
        )

    def finalizer():
        if request.node.status != 'passed':
            allure.attach(
                body=driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
        driver.quit()

    driver.maximize_window()
    request.addfinalizer(finalizer)
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
