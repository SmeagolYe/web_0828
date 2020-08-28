import pytest
from selenium import webdriver
from page_object.login_page import LoginPage
from test_data.common_data import *


@pytest.fixture
def login_env():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(login_page_url)
    login_page = LoginPage(driver)

    yield[driver, login_page]

    driver.quit()

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "test_login" # test_login 是标签名
    )