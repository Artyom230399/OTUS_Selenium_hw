import time

from page_objects.HomePage import HomePage
from page_objects.AdminPage import AdminPage
from page_objects.MacBookPage import MacBookPage
from page_objects.CatalogPage import CatalogPage
from page_objects.RegistrationPage import RegistrationPage
from page_objects.ProductsPage import ProductsPage


def test_homepage_search_desktops_button(browser):
    homepage = HomePage(browser)

    homepage.search_desktop_button()


def test_homepage_click_desktops_button(browser):
    homepage = HomePage(browser)

    homepage.click_on_the_desktops_button()


def test_homepage_logo(browser):
    homepage = HomePage(browser)

    homepage.search_logo()


def test_homepage_search(browser):
    homepage = HomePage(browser)

    homepage.search_field_input_word()
    homepage.click_on_the_search_button()


def test_homepage_number_phone(browser):
    homepage = HomePage(browser)

    homepage.check_number_phone()


def test_macbookpage_title(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    assert mb_page.title_macbook_page() == "MacBook"


def test_macbookpage_add_in_cart(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    mb_page.add_macbook()


def test_macbookpage_wishlist(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    mb_page.search_add_wishlist_button()


def test_macbookpage_home_button(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    mb_page.search_home_button()


def test_macbook_description_button(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    mb_page.search_description()


def test_admin_open_page(browser):
    admin_page = AdminPage(browser)

    admin_page.open_admin_page()


def test_admin_title(browser):
    admin_page = AdminPage(browser)

    admin_page.open_admin_page()
    assert admin_page.title_adminPage() == "Administration"


def test_admin_username_field(browser):
    admin_page = AdminPage(browser)

    admin_page.open_admin_page()
    admin_page.check_username_field("admin")


def test_admin_password_field(browser):
    admin_page = AdminPage(browser)

    admin_page.open_admin_page()
    admin_page.check_password_field("admin")


def test_admin_login_button(browser):
    admin_page = AdminPage(browser)

    admin_page.Authorization(username="admin", password="admin")


def test_catalog_categories(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_categories()
    assert catalog_page.check_title_catalog() == "Categories"


def test_catalog_products(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_products()
    assert catalog_page.check_title_catalog() == "Products"


def test_catalog_filters(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_filters()
    assert catalog_page.check_title_catalog() == "Filters"


def test_catalog_options(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_options()
    assert catalog_page.check_title_catalog() == "Options"


def test_catalog_downloads(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_downloads()
    assert catalog_page.check_title_catalog() == "Downloads"


def test_registration_page_title(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    assert reg_page.title_registration_page() == "Register Account"


def test_registration_page_first_name(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    reg_page.check_first_name_field()


def test_registration_last_name(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    reg_page.check_last_name_field()


def test_registration_email(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    reg_page.check_email_field()


def test_registration_telephone(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    reg_page.check_telephone_field()


def test_homepage_currency(browser):
    homepage = HomePage(browser)

    homepage.check_currency_button()


def test_registration_new_user(browser):
    reg_page = RegistrationPage(browser)
    reg_page.open_registration_page()
    reg_page.registration_new_user(first_name="Artyom", last_name="Agafonov", telephone="+79225464865",
                                                    password="9173")


def test_add_new_product(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)
    products_page = ProductsPage(browser)

    admin_page.open_admin_page()
    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_products()
    products_page.add_product(products_name="name", Meta_Tag="tag", Model="model")


def test_delete_product(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)
    products_page = ProductsPage(browser)

    admin_page.open_admin_page()
    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_products()
    products_page.delete_product()
