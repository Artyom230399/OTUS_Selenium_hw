from page_objects.HomePage import HomePage

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
    browser.maximize_window()
    assert HomePage(browser).check_number_phone() == "123456789"





## Наличие имени в карточке товара и проверка корректности имени
# def test_MacBook_Name(browser):
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MacBookCart.Name))
#    name = browser.find_element(*MacBookCart.Name).text
#    assert name == "MacBook"
#
#
## Проверка наличия Description в карточке товара
# def test_MacBook_Description(browser):
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MacBookCart.Description))
#
#
## Проверка наличия Specification в карточке товара
# def test_MacBook_Specification(browser):
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MacBookCart.Specification))
#
#
## Проверка наличия Reviews в карточке товара
# def test_MacBook_Reviews(browser):
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MacBookCart.Reviews))
#
#
## Проверка наличия кнопки Add to cart
# def test_MacBook_Add_To_Cart(browser):
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(HomePage.MacBook_Cart)).click()
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(MacBookCart.Add_To_Cart))
#
#
# class LogIn_Admin:
#    Username = (By.CSS_SELECTOR, '#input-username')
#    Password = (By.CSS_SELECTOR, '#input-password')
#    Button_Login = (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body > form'
#                                     ' > div.text-right > button')
#    Message = (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-heading > h1')
#    ForgottenPassword = (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body'
#                                          ' > form > div:nth-child(2) > span > a')
#
#
## Наличие поля Username
# def test_LogIn_Admin_Username(browser):
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Username))
#
#
## Наличие поля Password
# def test_LogIn_Admin_Password(browser):
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Password))
#
#
## Наличие кнопки входа
# def test_LogIn_Admin_Button_Login(browser):
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(LogIn_Admin.Button_Login))
#
#
## Наличие сообщения над формой авторизации
# def test_LogIn_Admin_Message(browser):
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Message))
#
#
# Наличие кнопки Forgotten Password
# def test_Login_Admin_ForgottenPassword(browser):
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(LogIn_Admin.ForgottenPassword))
#
#
# class Catalog:
#    Catalog_Navigation = (By.CSS_SELECTOR, '#menu-catalog > a')
#    Categories = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(1) > a')
#    Products = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) > a')
#    Downloads = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(8) > a')
#    Category_Name = (By.CSS_SELECTOR, '#content > div.container-fluid > div > div.panel-heading > h3')
#    Information = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(10) > a')
#
#
## Наличие каталога по категориям
# def test_Catalog_Categories(browser, user_login, user_password):
#    # Авторизация
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Username))
#    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
#    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
#    browser.find_element(*LogIn_Admin.Button_Login).click()
#
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
#    browser.find_element(*Catalog.Catalog_Navigation).click()
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Categories))
#
#
## Наличие Category Name В шапке таблицы
# def test_Catalog_Categories_Category_Name(browser, user_login, user_password):
#    # Авторизация
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(LogIn_Admin.Username))
#    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
#    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
#    browser.find_element(*LogIn_Admin.Button_Login).click()
#
#    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
#    browser.find_element(*Catalog.Catalog_Navigation).click()
#    browser.find_element(*Catalog.Categories).click()
#    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(Catalog.Category_Name))
#
#
## Наличие вкладки Information
# def test_Catalog_Categories_Information(browser, user_login, user_password):
#    # Авторизация
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(LogIn_Admin.Username))
#    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
#    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
#    browser.find_element(*LogIn_Admin.Button_Login).click()
#
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
#    browser.find_element(*Catalog.Catalog_Navigation).click()
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Information))
#
#
## Наличие каталога по продуктам
# def test_Catalog_Products(browser, user_login, user_password):
#    # Авторизация
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Username))
#    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
#    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
#    browser.find_element(*LogIn_Admin.Button_Login).click()
#
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
#    browser.find_element(*Catalog.Catalog_Navigation).click()
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Products))
#
#
## Наличие каталога по Downloads
# def test_Catalog_Downloads(browser, user_login, user_password):
#    # Авторизация
#    browser.get(browser.url + "/admin")
#    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LogIn_Admin.Username))
#    browser.find_element(*LogIn_Admin.Username).send_keys(user_login)
#    browser.find_element(*LogIn_Admin.Password).send_keys(user_password)
#    browser.find_element(*LogIn_Admin.Button_Login).click()
#
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Catalog_Navigation))
#    browser.find_element(*Catalog.Catalog_Navigation).click()
#    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(Catalog.Downloads))
#
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
