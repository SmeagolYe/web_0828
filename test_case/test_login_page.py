from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_object.login_page import LoginPage
from page_object.index_page import IndexPage
from test_data.common_data import *
from test_data.login_page_data import *
import unittest
import pytest


@pytest.mark.test_login
@pytest.mark.usefixtures("login_env")
class TestLoginPage:
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get(login_page_url)
    #     self.login_page = LoginPage(self.driver)

    def test_login_success(self, login_env):
        login_env[1].login(login_success_datas["username"], login_success_datas["password"])
        text = IndexPage(login_env[0]).get_nick_name()
        assert text == login_success_datas["check"]

    @pytest.mark.parametrize("data", login_fail_datas)
    def test_login_fail(self, login_env, data):
        login_env[1].login(data["username"], data["password"])
        text = login_env[1].get_warn_tips()
        assert text == data["check"]

    # def tearDown(self):
    #     self.driver.quit()