from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class OpencartHomePageElements:
    Desktops_Button = (By.CSS_SELECTOR, "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul"
                                        " > li:nth-child(1) > a")
    Logo = (By.CSS_SELECTOR, "#logo > a > img")
    Search = (By.CSS_SELECTOR, "#search > input")
    Search_Button = (By.CSS_SELECTOR, "#search > span > button")
    Number_Phone = (By.CSS_SELECTOR, "#top-links > ul > li:nth-child(1) > span")
    Currency_Button = (By.CSS_SELECTOR, "#form-currency > div > button")
    Euro_Button = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(1) > button")
    Items_Button = (By.CSS_SELECTOR, "#cart-total")
    Pound_Sterling_Button = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > button")
    Dollar_Button = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3) > button")


class HomePage(BasePage):

    def search_desktop_button(self):
        return self.find_element(locator=OpencartHomePageElements.Desktops_Button, time=2)

    def click_on_the_desktops_button(self):
        return self.find_element(locator=OpencartHomePageElements.Desktops_Button, time=2).click()

    def search_logo(self):
        return self.find_element(locator=OpencartHomePageElements.Logo, time=2)

    def search_field_input_word(self):
        return self._input(locator=OpencartHomePageElements.Search, word="Привет", time=2)

    def click_on_the_search_button(self):
        return self.find_element(locator=OpencartHomePageElements.Search_Button, time=2).click()

    def check_number_phone(self):
        self.driver.maximize_window()
        return str(self.find_element(locator=OpencartHomePageElements.Number_Phone, time=5).get_property("innerText"))

    def check_currency_button(self):
        self.find_element(locator=OpencartHomePageElements.Currency_Button, time=2).click()
        self.find_element(locator=OpencartHomePageElements.Euro_Button, time=2).click()
        items_button = self.find_element(locator=OpencartHomePageElements.Items_Button, time=2)
        assert items_button.get_property("innerText")[-1] == "€"

        self.find_element(locator=OpencartHomePageElements.Currency_Button, time=2).click()
        self.find_element(locator=OpencartHomePageElements.Pound_Sterling_Button, time=2).click()
        items_button2 = self.find_element(locator=OpencartHomePageElements.Items_Button, time=2)
        assert items_button2.get_property("innerText")[12] == "£"

        self.find_element(locator=OpencartHomePageElements.Currency_Button, time=2).click()
        self.find_element(locator=OpencartHomePageElements.Dollar_Button, time=2).click()
        items_button3 = self.find_element(locator=OpencartHomePageElements.Items_Button, time=2)
        assert items_button3.get_property("innerText")[12] == "$"
