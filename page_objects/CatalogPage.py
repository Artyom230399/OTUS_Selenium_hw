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
        self.logger.info(f"Check title catalog page")
        return self.driver.title

    def click_catalog(self):
        self.logger.info(f"Click on the catalog")
        return self.find_element(locator=CatalogPageElements.catalog_button, time=2).click()

    def click_categories(self):
        self.logger.info(f"Click on the categories")
        return self.find_element(locator=CatalogPageElements.categories_button, time=2).click()

    def click_products(self):
        self.logger.info(f"Click on the product")
        return self.find_element(locator=CatalogPageElements.products_button, time=2).click()

    def click_filters(self):
        self.logger.info(f"Click on the filters")
        return self.find_element(locator=CatalogPageElements.filters_button, time=2).click()

    def click_options(self):
        self.logger.info(f"Click on the options button")
        return self.find_element(locator=CatalogPageElements.options_button, time=2).click()

    def click_downloads(self):
        self.logger.info(f"Click on the download button")
        return self.find_element(locator=CatalogPageElements.downloads_button, time=2).click()
