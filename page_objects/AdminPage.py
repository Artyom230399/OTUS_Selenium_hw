from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminPageElements:
    message = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-heading")
    username_locator = (By.CSS_SELECTOR, "#input-username")
    password_locator = (By.CSS_SELECTOR, "#input-password")
    login_button = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body"
                                     " > form > div.text-right > button")


class AdminPage(BasePage):

    def title_adminPage(self):
        return self.driver.title

    def open_admin_page(self):
        return self.open_page("/admin")

    def check_username_field(self, text):
        return self.find_element(locator=AdminPageElements.username_locator, time=2).send_keys(text)

    def check_password_field(self, text):
        return self.find_element(locator=AdminPageElements.password_locator, time=2).send_keys(text)

    def Authorization(self, username, password):
        self.open_admin_page()
        self.check_username_field(text=username)
        self.check_password_field(text=password)
        return self.find_element(locator=AdminPageElements.login_button, time=2).click()
