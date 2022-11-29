from page_objects.HomePage import HomePage
from page_objects.AdminPage import AdminPage
from page_objects.MacBookPage import MacBookPage
from page_objects.CatalogPage import CatalogPage
import time


def test_homepage_search_desktops_button(browser):
    HomePage(browser).search_desktop_button()


def test_homepage_click_desktops_button(browser):
    HomePage(browser).click_on_the_desktops_button()


def test_homepage_logo(browser):
    HomePage(browser).search_logo()


def test_homepage_search(browser):
    HomePage(browser).search_field_input_word()
    HomePage(browser).click_on_the_search_button()


def test_homepage_number_phone(browser):
    assert HomePage(browser).check_number_phone() == "123456789"


def test_macbookpage_title(browser):
    MacBookPage(browser).open_macbook_page()
    assert MacBookPage(browser).title_macbook_page() == "MacBook"


def test_macbookpage_add_in_cart(browser):
    MacBookPage(browser).open_macbook_page()
    MacBookPage(browser).add_macbook()


def test_macbookpage_wishlist(browser):
    MacBookPage(browser).open_macbook_page()
    MacBookPage(browser).search_add_wishlist_button()


def test_macbookpage_home_button(browser):
    MacBookPage(browser).open_macbook_page()
    MacBookPage(browser).search_home_button()


def test_macbook_description_button(browser):
    MacBookPage(browser).open_macbook_page()
    MacBookPage(browser).search_description()


def test_admin_open_page(browser):
    AdminPage(browser).open_admin_page()


def test_admin_title(browser):
    AdminPage(browser).open_admin_page()
    assert AdminPage(browser).title_adminPage() == "Administration"


def test_admin_username_field(browser):
    AdminPage(browser).open_admin_page()
    AdminPage(browser).check_username_field("admin")


def test_admin_password_field(browser):
    AdminPage(browser).open_admin_page()
    AdminPage(browser).check_password_field("admin")


def test_admin_login_button(browser):
    AdminPage(browser).Authorization(username="admin", password="admin")


def test_catalog_categories(browser, user_login, user_password):
    AdminPage(browser).Authorization(username=user_login, password=user_password)
    CatalogPage(browser).click_catalog()
    CatalogPage(browser).click_categories()
    assert CatalogPage(browser).check_title_catalog() == "Categories"


def test_catalog_products(browser, user_login, user_password):
    AdminPage(browser).Authorization(username=user_login, password=user_password)
    CatalogPage(browser).click_catalog()
    CatalogPage(browser).click_products()
    assert CatalogPage(browser).check_title_catalog() == "Products"


def test_catalog_filters(browser, user_login, user_password):
    AdminPage(browser).Authorization(username=user_login, password=user_password)
    CatalogPage(browser).click_catalog()
    CatalogPage(browser).click_filters()
    assert CatalogPage(browser).check_title_catalog() == "Filters"


def test_catalog_options(browser, user_login, user_password):
    AdminPage(browser).Authorization(username=user_login, password=user_password)
    CatalogPage(browser).click_catalog()
    CatalogPage(browser).click_options()
    assert CatalogPage(browser).check_title_catalog() == "Options"


def test_catalog_downloads(browser, user_login, user_password):
    AdminPage(browser).Authorization(username=user_login, password=user_password)
    CatalogPage(browser).click_catalog()
    CatalogPage(browser).click_downloads()
    assert CatalogPage(browser).check_title_catalog() == "Downloads"


#
# class RegisterAccount:
#    First_Name_Field = (By.CSS_SELECTOR, '#input-firstname')
#    Password_Field = (By.CSS_SELECTOR, '#input-password')
#    Password_Confirm_Field = (By.CSS_SELECTOR, '#input-confirm')
#    Privacy_Policy = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
#    Continue = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')
#
#
## Наличие поля для ввода имени в форме регистрации
# def test_RegisterAccount_First_Name_Field(browser):
#    browser.get(browser.url + "/index.php?route=account/register")
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.First_Name_Field))
#
#
## Наличие поля для ввода пароля в форме регистрации
# def test_RegisterAccount_Password_Field(browser):
#    browser.get(browser.url + "/index.php?route=account/register")
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.Password_Field))
#
#
## Наличие поля для повторного ввода пароля в форме регистрации
# def test_RegisterAccount_Password_Confirm_Field(browser):
#    browser.get(browser.url + "/index.php?route=account/register")
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.Password_Confirm_Field))
#
#
## Наличие чекбокса для политики конфиденциальности
# def test_RegisterAccount_Privacy_Policy(browser):
#    browser.get(browser.url + "/index.php?route=account/register")
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.Privacy_Policy))
#
#
## Наличие кнопки для продолжения после ввода всех данных
# def test_RegisterAccount_Continue(browser):
#    browser.get(browser.url + "/index.php?route=account/register")
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.Continue))
#
