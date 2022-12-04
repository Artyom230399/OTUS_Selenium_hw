import allure
import pytest

from page_objects.HomePage import HomePage
from page_objects.AdminPage import AdminPage
from page_objects.MacBookPage import MacBookPage
from page_objects.CatalogPage import CatalogPage
from page_objects.RegistrationPage import RegistrationPage
from page_objects.ProductsPage import ProductsPage


@allure.title('Search the desktops button on the Home page')
def test_homepage_search_desktops_button(browser):
    homepage = HomePage(browser)

    homepage.search_desktop_button()


@allure.title('Click the desktops button on the Home page')
def test_homepage_click_desktops_button(browser):
    homepage = HomePage(browser)

    homepage.click_on_the_desktops_button()


@allure.title('Checking the logo on the Home page')
def test_homepage_logo(browser):
    homepage = HomePage(browser)

    homepage.search_logo()


@allure.title('Check the search on the Home page')
def test_homepage_search(browser):
    homepage = HomePage(browser)

    homepage.search_field_input_word()
    homepage.click_on_the_search_button()


@allure.title('Checking the number phone on the Home page')
def test_homepage_number_phone(browser):
    homepage = HomePage(browser)

    homepage.check_number_phone()


@pytest.mark.skip
@allure.title('Checking the title the MacBook Page')
def test_macbookpage_title(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    assert mb_page.title_macbook_page() == "MacBook"


@pytest.mark.skip
@allure.title('Checking add in cart MacBook')
def test_macbookpage_add_in_cart(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    mb_page.add_macbook()


@pytest.mark.skip
@allure.title('Checking wishlist MacBook')
def test_macbookpage_wishlist(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    mb_page.search_add_wishlist_button()


@pytest.mark.skip
@allure.title('Checking the home button on the MacBook Page')
def test_macbookpage_home_button(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    mb_page.search_home_button()


@pytest.mark.skip
@allure.title('Checking the description button on the MacBook Page')
def test_macbook_description_button(browser):
    mb_page = MacBookPage(browser)

    mb_page.open_macbook_page()
    mb_page.search_description()


@allure.title('Opening the admin page')
def test_admin_open_page(browser):
    admin_page = AdminPage(browser)

    admin_page.open_admin_page()


@allure.title('Checking title on the admin page')
def test_admin_title(browser):
    admin_page = AdminPage(browser)

    admin_page.open_admin_page()
    assert admin_page.title_adminPage() == "Administration"


@allure.title('Checking the username field on the admin page')
def test_admin_username_field(browser):
    admin_page = AdminPage(browser)

    admin_page.open_admin_page()
    admin_page.check_username_field("admin")


@allure.title('Checking the password field on the admin page')
def test_admin_password_field(browser):
    admin_page = AdminPage(browser)

    admin_page.open_admin_page()
    admin_page.check_password_field("admin")


@allure.title('Checking the login button on the admin page')
def test_admin_login_button(browser):
    admin_page = AdminPage(browser)

    admin_page.Authorization(username="admin", password="admin")


@allure.title('Checking the title on the  categories page')
def test_catalog_categories(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_categories()
    assert catalog_page.check_title_catalog() == "Categories"


@allure.title('Checking the title on the products page')
def test_catalog_products(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_products()
    assert catalog_page.check_title_catalog() == "Products"


@allure.title('Checking the title on the filters page')
def test_catalog_filters(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_filters()
    assert catalog_page.check_title_catalog() == "Filters"


@allure.title('Checking the title on the options page')
def test_catalog_options(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_options()
    assert catalog_page.check_title_catalog() == "Options"


@allure.title('Checking the title on the downloads page')
def test_catalog_downloads(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)

    admin_page.Authorization(username=user_login, password=user_password)
    catalog_page.click_catalog()
    catalog_page.click_downloads()
    assert catalog_page.check_title_catalog() == "Downloads"


@allure.title('Checking the title on the register account page')
def test_registration_page_title(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    assert reg_page.title_registration_page() == "Register Account"


@allure.title('Checking the first name field on the register account page')
def test_registration_page_first_name(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    reg_page.check_first_name_field()


@allure.title('Checking the last name field on the register account page')
def test_registration_last_name(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    reg_page.check_last_name_field()


@allure.title('Checking the email field on the register account page')
def test_registration_email(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    reg_page.check_email_field()


@allure.title('Checking the telephone field on the register account page')
def test_registration_telephone(browser):
    reg_page = RegistrationPage(browser)

    reg_page.open_registration_page()
    reg_page.check_telephone_field()


@allure.title('Checking the currency on the home page')
def test_homepage_currency(browser):
    homepage = HomePage(browser)

    homepage.check_currency_button()


@allure.title('Checking the registration of a new user')
def test_registration_new_user(browser):
    reg_page = RegistrationPage(browser)

    with allure.step("Opening the registration page"):
        reg_page.open_registration_page()
    with allure.step(f"Entering user data for registration"):
        reg_page.registration_new_user(first_name="Artyom", last_name="Agafonov", telephone="+79225464865",
                                       password="9173")


@allure.title('Checking the addition of a new product')
def test_add_new_product(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)
    products_page = ProductsPage(browser)

    with allure.step("Opening an admin page"):
        admin_page.open_admin_page()
    with allure.step("Entering authorization data"):
        admin_page.Authorization(username=user_login, password=user_password)
    with allure.step("Transition to catalog page"):
        catalog_page.click_catalog()
    with allure.step("Transition to products page"):
        catalog_page.click_products()
    with allure.step("Filling in the required fields and adding the product"):
        products_page.add_product(products_name="name", Meta_Tag="tag", Model="model")


@allure.title('Checking the removal of the product')
def test_delete_product(browser, user_login, user_password):
    admin_page = AdminPage(browser)
    catalog_page = CatalogPage(browser)
    products_page = ProductsPage(browser)

    with allure.step("Opening an admin page"):
        admin_page.open_admin_page()
    with allure.step("Entering authorization data"):
        admin_page.Authorization(username=user_login, password=user_password)
    with allure.step("Transition to catalog page"):
        catalog_page.click_catalog()
    with allure.step("Transition to products page"):
        catalog_page.click_products()
    with allure.step("Removing a product from the catalog"):
        products_page.delete_product()
