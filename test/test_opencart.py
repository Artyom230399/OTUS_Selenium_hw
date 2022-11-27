from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    LOGO = (By.CSS_SELECTOR, "#logo")
    Slideshow = (By.CSS_SELECTOR, '#content > div.slideshow.swiper-viewport')
    Slideshow_MacBookAir = (By.CSS_SELECTOR, '#slideshow0 > div > div.swiper-slide.text-center.swiper-slide-active'
                                             ' > img')
    Slideshow_Iphone6 = (By.CSS_SELECTOR,
                         '#slideshow0 > div > div.swiper-slide.text-center.swiper-slide-duplicate.swiper-slide-active'
                         ' > a > img')
    MacBook_Cart = (By.CSS_SELECTOR, '#content > div.row > div:nth-child(1) > div > div.image > a > img')
    SearchField = (By.CSS_SELECTOR, '#search > input')
    Desktops = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(1) > a')
    All_Desktops = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul >'
                                     ' li.dropdown.open > div > a')
    Components = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul >'
                                   ' li:nth-child(3) > a')
    All_Components = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul >'
                                       ' li:nth-child(3) > div > a')
    Software = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(5) > a')
    Phones_PDAs = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul >'
                                    ' li:nth-child(6) > a')
    Laptops = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(2) > a')
    All_Laptops = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(2) >'
                                    ' div > a')


# Наличие лого на HomePage
def test_HomePage_logo(browser):
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(HomePage.LOGO))


# Наличие слайдшоу на HomePage
def test_HomePage_Slideshow(browser):
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(HomePage.Slideshow))


# Наличие картинки макбука на слайдшоу
def test_HomePage_MacBookAir(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(HomePage.Slideshow_MacBookAir))


# Наличие картинки айфона 6 на слайдшоу
def test_HomePage_Iphone6(browser):
    WebDriverWait(browser, 6).until(EC.visibility_of_element_located(HomePage.Slideshow_Iphone6))


# Наличие поле поиска на HomePage
def test_HomePage_SearcField(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.SearchField))


class Opencart_RandomTest:
    Grid_Button = (By.CSS_SELECTOR, '#grid-view')
    Components_TOP = (By.CSS_SELECTOR, '#content > h2')
    Continue_Software = (By.CSS_SELECTOR, '#content > div > div > a')
    Phones_PDAs_SortBy = (By.CSS_SELECTOR, '#content > div:nth-child(2) > div.col-md-4.col-xs-6 > div > label')
    Laptops_Show = (By.CSS_SELECTOR, '#content > div:nth-child(6) > div.col-md-3.col-xs-6')


# Показ товара сеткой в десктопе
def test_Opencart_RandomTest_Desktops_Grid(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.Desktops))
    browser.find_element(*HomePage.Desktops).click()
    browser.find_element(*HomePage.All_Desktops).click()
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Opencart_RandomTest.Grid_Button))


# Проверка наличия заглавия в Components
def test_Opencart_RandomTest_Components(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.Components))
    browser.find_element(*HomePage.Components).click()
    browser.find_element(*HomePage.All_Components).click()
    WebDriverWait(browser, 6).until(EC.visibility_of_element_located(Opencart_RandomTest.Components_TOP))


# Проверка наличия конпки Continue
def test_Opencart_RandomTest_Continue_Software(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.Software))
    browser.find_element(*HomePage.Software).click()
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Opencart_RandomTest.Continue_Software))


# Наличие сортировки в Phones?PDAs/all
def test_Opencart_RandomTest_Phones_PDAs_SortBy(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.Phones_PDAs))
    browser.find_element(*HomePage.Phones_PDAs).click()
    WebDriverWait(browser, 6).until(EC.visibility_of_element_located(Opencart_RandomTest.Phones_PDAs_SortBy))


# Сколько товаров на странице
def test_Opencart_RandomTest_Laptops(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.Laptops))
    browser.find_element(*HomePage.Laptops).click()
    browser.find_element(*HomePage.All_Laptops).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(Opencart_RandomTest.Laptops_Show))


class MacBookCart:
    Name = (By.CSS_SELECTOR, '#content > div > div.col-sm-4 > h1')
    Description = (By.CSS_SELECTOR, '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li.active > a')
    Specification = (By.CSS_SELECTOR, '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li:nth-child(2) > a')
    Reviews = (By.CSS_SELECTOR, '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li:nth-child(3) > a')
    Add_To_Cart = (By.CSS_SELECTOR, '#button-cart')


# Наличие имени в карточке товара и проверка корректности имени
def test_MacBook_Name(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MacBookCart.Name))
    name = browser.find_element(*MacBookCart.Name).text
    assert name == "MacBook"


# Проверка наличия Description в карточке товара
def test_MacBook_Description(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MacBookCart.Description))


# Проверка наличия Specification в карточке товара
def test_MacBook_Specification(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MacBookCart.Specification))


# Проверка наличия Reviews в карточке товара
def test_MacBook_Reviews(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MacBookCart.Reviews))


# Проверка наличия кнопки Add to cart
def test_MacBook_Add_To_Cart(browser):
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(MacBookCart.Add_To_Cart))


class LogIn_Admin:
    Username = (By.CSS_SELECTOR, '#input-username')
    Password = (By.CSS_SELECTOR, '#input-password')
    Button_Login = (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body > form'
                                     ' > div.text-right > button')
    Message = (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-heading > h1')
    ForgottenPassword = (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body'
                                          ' > form > div:nth-child(2) > span > a')


# Наличие поля Username
def test_LogIn_Admin_Username(browser):
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Username))


# Наличие поля Password
def test_LogIn_Admin_Password(browser):
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Password))


# Наличие кнопки входа
def test_LogIn_Admin_Button_Login(browser):
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(LogIn_Admin.Button_Login))


# Наличие сообщения над формой авторизации
def test_LogIn_Admin_Message(browser):
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Message))


# Наличие кнопки Forgotten Password
def test_Login_Admin_ForgottenPassword(browser):
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(LogIn_Admin.ForgottenPassword))


class Catalog:
    Catalog_Navigation = (By.CSS_SELECTOR, '#menu-catalog > a')
    Categories = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(1) > a')
    Products = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) > a')
    Downloads = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(8) > a')
    Category_Name = (By.CSS_SELECTOR, '#content > div.container-fluid > div > div.panel-heading > h3')
    Information = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(10) > a')


# Наличие каталога по категориям
def test_Catalog_Categories(browser, user_login, user_password):
    # Авторизация
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Username))
    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
    browser.find_element(*LogIn_Admin.Button_Login).click()

    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
    browser.find_element(*Catalog.Catalog_Navigation).click()
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Categories))


# Наличие Category Name В шапке таблицы
def test_Catalog_Categories_Category_Name(browser, user_login, user_password):
    # Авторизация
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(LogIn_Admin.Username))
    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
    browser.find_element(*LogIn_Admin.Button_Login).click()

    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
    browser.find_element(*Catalog.Catalog_Navigation).click()
    browser.find_element(*Catalog.Categories).click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Catalog.Category_Name))


# Наличие вкладки Information
def test_Catalog_Categories_Information(browser, user_login, user_password):
    # Авторизация
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(LogIn_Admin.Username))
    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
    browser.find_element(*LogIn_Admin.Button_Login).click()

    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
    browser.find_element(*Catalog.Catalog_Navigation).click()
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Information))


# Наличие каталога по продуктам
def test_Catalog_Products(browser, user_login, user_password):
    # Авторизация
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Username))
    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
    browser.find_element(*LogIn_Admin.Button_Login).click()

    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
    browser.find_element(*Catalog.Catalog_Navigation).click()
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Products))


# Наличие каталога по Downloads
def test_Catalog_Downloads(browser, user_login, user_password):
    # Авторизация
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Username))
    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
    browser.find_element(*LogIn_Admin.Button_Login).click()

    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
    browser.find_element(*Catalog.Catalog_Navigation).click()
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Downloads))


class RegisterAccount:
    First_Name_Field = (By.CSS_SELECTOR, '#input-firstname')
    Password_Field = (By.CSS_SELECTOR, '#input-password')
    Password_Confirm_Field = (By.CSS_SELECTOR, '#input-confirm')
    Privacy_Policy = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    Continue = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')


# Наличие поля для ввода имени в форме регистрации
def test_RegisterAccount_First_Name_Field(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.First_Name_Field))


# Наличие поля для ввода пароля в форме регистрации
def test_RegisterAccount_Password_Field(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.Password_Field))


# Наличие поля для повторного ввода пароля в форме регистрации
def test_RegisterAccount_Password_Confirm_Field(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.Password_Confirm_Field))


# Наличие чекбокса для политики конфиденциальности
def test_RegisterAccount_Privacy_Policy(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.Privacy_Policy))


# Наличие кнопки для продолжения после ввода всех данных
def test_RegisterAccount_Continue(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(RegisterAccount.Continue))
