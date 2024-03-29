import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger("test")


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _find_element(self, locator: tuple, wait_time=15):
        element = WebDriverWait(self.browser, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator[1]}",
        )
        return element

    def _find_clickable_element(self, locator: tuple, wait_time=15):
        element = WebDriverWait(self.browser, wait_time).until(
            EC.element_to_be_clickable(locator),
            message=f"Can't find element by locator {locator[1]}",
        )
        return element

    def _send_keys(self, element, text=None):
        element.clear()
        if text:
            element.send_keys(text)
            logger.info(f"===> send text {text}")
            return element

    def get_text(self, element):
        text = element.text
        logger.info(f"===> get text {text}")
        return text

    def get_url(self, uri=None):
        logger.info(f"===> open {self.browser.base_url + uri} page")
        self.browser.get(self.browser.base_url + uri)

    def list_elements(self, locator):
        return self.browser.find_elements(*locator)

    def is_element_visible(self, locator: tuple, wait_time=15):
        element_visible = WebDriverWait(self.browser, wait_time).until(
            EC.invisibility_of_element_located(locator),
            message=f"Can't find element by locator {locator[1]}",
        )
        return element_visible
