import time

from page_objects.HomePage import HomePage
from page_objects.AdminPage import AdminPage
from page_objects.MacBookPage import MacBookPage
from page_objects.CatalogPage import CatalogPage
from page_objects.RegistrationPage import RegistrationPage
from page_objects.ProductsPage import ProductsPage


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


def test_registration_page_title(browser):
    RegistrationPage(browser).open_registration_page()
    assert RegistrationPage(browser).title_registration_page() == "Register Account"


def test_registration_page_first_name(browser):
    RegistrationPage(browser).open_registration_page()
    RegistrationPage(browser).check_first_name_field()


def test_registration_last_name(browser):
    RegistrationPage(browser).open_registration_page()
    RegistrationPage(browser).check_last_name_field()


def test_registration_email(browser):
    RegistrationPage(browser).open_registration_page()
    RegistrationPage(browser).check_email_field()


def test_registration_telephone(browser):
    RegistrationPage(browser).open_registration_page()
    RegistrationPage(browser).check_telephone_field()


def test_homepage_currency(browser):
    HomePage(browser).check_currency_button()


def test_registration_new_user(browser):
    RegistrationPage(browser).open_registration_page()
    RegistrationPage(browser).registration_new_user(first_name="Artyom", last_name="Agafonov", telephone="+79225464865",
                                                    password="9173")


def test_add_new_product(browser, user_login, user_password):
    AdminPage(browser).open_admin_page()
    AdminPage(browser).Authorization(username=user_login, password=user_password)
    CatalogPage(browser).click_catalog()
    CatalogPage(browser).click_products()
    ProductsPage(browser).add_product(products_name="name", Meta_Tag="tag", Model="model")


def test_delete_product(browser, user_login, user_password):
    AdminPage(browser).open_admin_page()
    AdminPage(browser).Authorization(username=user_login, password=user_password)
    CatalogPage(browser).click_catalog()
    CatalogPage(browser).click_products()
    ProductsPage(browser).delete_product()
