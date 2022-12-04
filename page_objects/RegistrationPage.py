from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
import random


class RegistrationPageElement:
    First_Name_field = (By.CSS_SELECTOR, "#input-firstname")
    Last_Name_field = (By.CSS_SELECTOR, "#input-lastname")
    EMail_field = (By.CSS_SELECTOR, "#input-email")
    Telephone_field = (By.CSS_SELECTOR, "#input-telephone")
    Password_field = (By.CSS_SELECTOR, "#input-password")
    Confirm_Password_field = (By.CSS_SELECTOR, "#input-confirm")
    Privacy_Policy_button = (By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)")
    Continue_button = (By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
    Message_before_registration = (By.CSS_SELECTOR, "#content > h1")


class RegistrationPage(BasePage):

    def open_registration_page(self):
        self.logger.info(f"Open registration page")
        self.open_page("/index.php?route=account/register")

    def title_registration_page(self):
        self.logger.info(f"Check title registration page")
        return self.driver.title

    def check_first_name_field(self):
        self.logger.info(f"Check first name field")
        self.find_element(locator=RegistrationPageElement.First_Name_field, time=2)

    def check_last_name_field(self):
        self.logger.info(f"check last name field")
        self.find_element(locator=RegistrationPageElement.Last_Name_field, time=2)

    def check_email_field(self):
        self.logger.info(f"Check email field")
        self.find_element(locator=RegistrationPageElement.EMail_field, time=2)

    def check_telephone_field(self):
        self.logger.info(f"Check telephone field")
        self.find_element(locator=RegistrationPageElement.Telephone_field, time=2)

    def registration_new_user(self, first_name, last_name, telephone, password):
        email = str(random.randint(1, 100000)) + "@mail.ru"
        self.logger.info(f"Filling in fields")
        self.find_element(locator=RegistrationPageElement.First_Name_field, time=2).send_keys(first_name)
        self.find_element(locator=RegistrationPageElement.Last_Name_field, time=2).send_keys(last_name)
        self.find_element(locator=RegistrationPageElement.EMail_field, time=2).send_keys(email)
        self.find_element(locator=RegistrationPageElement.Telephone_field, time=2).send_keys(telephone)
        self.find_element(locator=RegistrationPageElement.Password_field, time=2).send_keys(password)
        self.find_element(locator=RegistrationPageElement.Confirm_Password_field, time=2).send_keys(password)
        self.find_element(locator=RegistrationPageElement.Privacy_Policy_button, time=2).click()
        self.find_element(locator=RegistrationPageElement.Continue_button, time=2).click()
        message = self.find_element(locator=RegistrationPageElement.Message_before_registration, time=2)
        assert message.get_property("innerText") == "Your Account Has Been Created!"
        self.logger.info(f"Registration is completed")
