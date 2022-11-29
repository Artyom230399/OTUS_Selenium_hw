from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time):
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
