import logging

import allure
from allure_commons._allure import step
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger("test")


class RegisterAccountPage(BasePage):
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    BOX_AGREE = (By.CSS_SELECTOR, "[name ='agree']")
    CONTINUE = (By.CSS_SELECTOR, ".btn.btn-primary")
    GOOD_REGISTER = (By.CSS_SELECTOR, "h1")
    ASSERT_TEXT = (By.XPATH, '//*[text()="{}"]')

    @step("fill_fields")
    def fill_fields(self, new_person):
        logger.info(f"===> fill_fields")
        with allure.step(
                f"fill fields {new_person.name}, {new_person.lastname}, "
                f"{new_person.email}, {new_person.telephone}, {new_person.password}"):
            firstname = self._find_element(self.FIRSTNAME)
            self._send_keys(element=firstname, text=new_person.name)
            lastname = self._find_element(self.LASTNAME)
            self._send_keys(element=lastname, text=new_person.lastname)
            email = self._find_element(self.EMAIL)
            self._send_keys(element=email, text=new_person.email)
            telephone = self._find_element(self.TELEPHONE)
            self._send_keys(telephone, new_person.telephone)
            self._send_keys(element=self._find_element(self.PASSWORD), text=new_person.password)
            self._send_keys(element=self._find_element(self.PASSWORD_CONFIRM), text=new_person.password)
            self._find_element(self.BOX_AGREE).click()
            self._find_element(self.CONTINUE).click()
        assert self._find_element(self.GOOD_REGISTER).text == "Your Account Has Been Created!"
