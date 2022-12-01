from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPageElements:
    catalog_button = (By.CSS_SELECTOR, "#menu-catalog > a")
    categories_button = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(1) > a")
    products_button = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    filters_button = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(4) > a")
    options_button = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(6) > a")
    downloads_button = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(8) > a")


class CatalogPage(BasePage):

    def check_title_catalog(self):
        return self.driver.title

    def click_catalog(self):
        return self.find_element(locator=CatalogPageElements.catalog_button, time=2).click()

    def click_categories(self):
        return self.find_element(locator=CatalogPageElements.categories_button, time=2).click()

    def click_products(self):
        return self.find_element(locator=CatalogPageElements.products_button, time=2).click()

    def click_filters(self):
        return self.find_element(locator=CatalogPageElements.filters_button, time=2).click()

    def click_options(self):
        return self.find_element(locator=CatalogPageElements.options_button, time=2).click()

    def click_downloads(self):
        return self.find_element(locator=CatalogPageElements.downloads_button, time=2).click()
