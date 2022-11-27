import pytest
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os.path


# Какие значения передаем через консоль?
def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="browser for test"
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--driver_path", default="C:/Drivers"
    )
    parser.addoption(
        "--url", default="http://192.168.0.100:8081"
    )
    parser.addoption(
        "--firefox_location", default="C:/Program Files/Mozilla Firefox"
    )


@pytest.fixture
def browser(request):
    global driver
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver_path = request.config.getoption("--driver_path")
    url = request.config.getoption("--url")
    FireFox_location = request.config.getoption("--firefox_location")

    if browser_name == "chrome":
        # headless-режим
        options = webdriver.ChromeOptions()
        # Убираем лишние сообщения
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        if headless:
            options.headless = True

        driver = webdriver.Chrome(
            service=Service(f"{driver_path}/chromedriver.exe"),
            options=options
        )

    elif browser_name == "firefox":
        # headless-режим
        options = webdriver.FirefoxOptions()
        options.binary_location = f"{FireFox_location}/firefox.exe"

        if headless:
            options.headless = True

        driver = webdriver.Firefox(
            service=Service(f"{driver_path}/geckodriver.exe"),
            options=options
        )

    elif browser_name == "yandex":
        # headless-режим
        options = webdriver.ChromeOptions()
        # Убираем лишние сообщения
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        if headless:
            options.headless = True

        driver = webdriver.Chrome(
            service=Service(f"{driver_path}/yandexdriver.exe"),
            options=options
        )

    else:
        print('browser not found')

    # Финализатор
    request.addfinalizer(driver.close)

    driver.get(url)

    driver.url = url

    return driver


if os.path.isfile("Login_details.json"):
    path_login = "Login_details.json"

elif os.path.isfile("../Login_details.json"):
    path_login = "../Login_details.json"


@pytest.fixture
def user_login():
    with open(path_login, 'r') as f:
        user = json.load(f)
        login = user['Login']
    return login


@pytest.fixture
def user_password():
    with open(path_login, 'r') as f2:
        user = json.load(f2)
        password = user['Password']
    return password
