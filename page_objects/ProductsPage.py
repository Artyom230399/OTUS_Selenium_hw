import time
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductsPageElements:
    add_button = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a.btn.btn-primary > i")
    Product_name_field = (By.CSS_SELECTOR, "#input-name1")
    Meta_Tag = (By.CSS_SELECTOR, "#input-meta-title1")
    Data_button = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a")
    Model_field = (By.CSS_SELECTOR, "#input-model")
    Save_button = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button > i")
    Alert = (By.CSS_SELECTOR, "#content > div.container-fluid > div.alert.alert-success.alert-dismissible")
    Choice_button = (By.CSS_SELECTOR, "#form-product > div > table > tbody > tr:nth-child(1)"
                                      " > td:nth-child(1) > input[type=checkbox]")
    Delete_button = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger")


class ProductsPage(BasePage):

    def add_product(self, products_name, Meta_Tag, Model):
        self.logger.info(f"Click on the add button")
        self.find_element(locator=ProductsPageElements.add_button, time=2).click()
        self.logger.info(f"Input products name")
        self.find_element(locator=ProductsPageElements.Product_name_field, time=2).send_keys(products_name)
        self.logger.info(f"Input Meta tag")
        self.find_element(locator=ProductsPageElements.Meta_Tag, time=2).send_keys(Meta_Tag)
        self.logger.info(f"Click on the data button")
        self.find_element(locator=ProductsPageElements.Data_button, time=2).click()
        self.logger.info(f"Input Model")
        self.find_element(locator=ProductsPageElements.Model_field, time=2).send_keys(Model)
        self.logger.info(f"Click on the save button")
        self.find_element(locator=ProductsPageElements.Save_button, time=2).click()
        self.logger.info(f"Check alert")
        self.find_element(locator=ProductsPageElements.Alert, time=3)
        self.logger.info(f"Add product in the catalog")

    def delete_product(self):
        self.logger.info(f"Click choise button")
        self.find_element(locator=ProductsPageElements.Choice_button, time=2).click()
        self.logger.info(f"Click delete button")
        self.find_element(locator=ProductsPageElements.Delete_button, time=2).click()
        time.sleep(1)
        self.logger.info(f"Check alert")
        self.driver.switch_to.alert.accept()
        self.logger.info(f"Delete product")
