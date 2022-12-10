import logging
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    def find_element(self, locator, time):
        # self.logger.info(f"Find element: {locator}")
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def _input(self, locator, time, word):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).send_keys(word)

    def open_page(self, _url):
        self.driver.get(self.driver.url + _url)

    def wait_alert(self, time):
        WebDriverWait(self.driver, time).until(EC.alert_is_present())

    def return_text(self, locator):
        self.driver.find_element(locator).text()
