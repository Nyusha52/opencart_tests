import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from models.user import RegistrData
from pages.admin_panel_page import AdminPanelPage
from pages.app import Application
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
    browser.get(browser.base_url)
    browser.find_element(*MainPage.MY_ACCOUNT).click()
    browser.find_element(*MainPage.REGISTER).click()
    new_person = RegistrData.random()
    browser.find_element(*RegisterAccountPage.FIRSTNAME).send_keys(new_person.name)
    browser.find_element(*RegisterAccountPage.LASTNAME).send_keys(new_person.lastname)
    browser.find_element(*RegisterAccountPage.EMAIL).send_keys(new_person.email)
    browser.find_element(*RegisterAccountPage.TELEPHONE).send_keys("Имqяййц")
    browser.find_element(*RegisterAccountPage.PASSWORD).send_keys(new_person.password)
    browser.find_element(*RegisterAccountPage.PASSWORD_CONFIRM).send_keys(new_person.password)
    browser.find_element(*RegisterAccountPage.BOX_AGREE).click()
    browser.find_element(*RegisterAccountPage.CONTINUE).click()
    assert browser.find_element(*RegisterAccountPage.GOOD_REGISTER).text == "Your Account Has Been Created!"
    fixture = Application(
        driver=browser,
        data=new_person
    )
    yield fixture
    browser.get(browser.base_url + "/admin/")
    browser.find_element(*AdminPanelPage.USER_NAME).send_keys("user")
    browser.find_element(*AdminPanelPage.PASSVORD).send_keys("bitnami")
    browser.find_element(*AdminPanelPage.LOG_IN).click()
    browser.find_element(*AdminPanelPage.CUSTOMERS).click()
    browser.find_element(*AdminPanelPage.CUSTOMERS_1).click()
    browser.find_element(AdminPanelPage.BOX[0],
                         AdminPanelPage.BOX[1].format(f"{new_person.name} {new_person.lastname}")).click()
    browser.find_element(*AdminPanelPage.DELETE).click()
    alert = browser.switch_to.alert
    alert.accept()
    assert browser.find_element(*AdminPanelPage.DELETE_OK).text == "Success: You have modified customers!\n×"
