from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class OpencartHomePageElements:
    Desktops_Button = (By.CSS_SELECTOR, "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul"
                                       " > li:nth-child(1) > a")
    Logo = (By.CSS_SELECTOR, "#logo > a > img")
    Search = (By.CSS_SELECTOR, "#search > input")
    Search_Button = (By.CSS_SELECTOR, "#search > span > button")
    Number_Phone = (By.CSS_SELECTOR, "#top-links > ul > li:nth-child(1) > span")

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
        return str(self.find_element(locator=OpencartHomePageElements.Number_Phone, time=2).text)
