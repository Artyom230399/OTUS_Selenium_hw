import time
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class MacBookPageElements:
    add_button = (By.CSS_SELECTOR, "#button-cart")
    shopping_cart_button = (By.CSS_SELECTOR, "#product-product > div.alert.alert-success.alert-dismissible"
                                             " > a:nth-child(2)")
    product_name_in_cart = (By.CSS_SELECTOR, "#content > form > div > table > tbody > tr > td:nth-child(2) > a")
    add_wishlist_button = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > div.btn-group > button:nth-child(1)")
    alert_wishlist = (By.CSS_SELECTOR, "#product-product > div.alert.alert-success.alert-dismissible")
    home_button = (By.CSS_SELECTOR, "#product-product > ul > li:nth-child(1)")
    description_button = (By.CSS_SELECTOR, "#content > div > div.col-sm-8 > ul.nav.nav-tabs > li.active > a")


class MacBookPage(BasePage):

    def open_macbook_page(self):
        self.logger.info(f"Open MacBook page")
        self.driver.maximize_window()
        self.open_page(_url="/macbook")
        time.sleep(5)

    def title_macbook_page(self):
        self.logger.info(f"Check title page")
        return self.driver.title

    def add_macbook(self):
        self.logger.info(f"Add MacBook in my shopping cart")
        self.find_element(locator=MacBookPageElements.add_button, time=15).click()
        self.find_element(locator=MacBookPageElements.shopping_cart_button, time=15).click()

    def search_add_wishlist_button(self):
        self.logger.info(f"Search add wishlist button")
        self.find_element(locator=MacBookPageElements.add_wishlist_button, time=15).click()

    def search_home_button(self):
        self.logger.info(f"Search home button")
        self.find_element(locator=MacBookPageElements.home_button, time=5).click()

    def search_description(self):
        self.logger.info(f"Search description")
        self.find_element(locator=MacBookPageElements.description_button, time=5)
