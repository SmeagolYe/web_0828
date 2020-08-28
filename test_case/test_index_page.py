import unittest
from page_object.login_page import LoginPage
from page_object.index_page import IndexPage
from page_object.bid_page import BidPage
from selenium import webdriver
from test_data.common_data import *
from test_data.bid_page_data import *
import pytest


@pytest.mark.usefixtures("login_env")
@pytest.mark.test_index
class TestIndexPage:
    def test_click_fisrt_invest_button(self, login_env):
        login_env[1].login(global_username, global_password)
        IndexPage(login_env[0]).click_first_invest_button()
        text = BidPage(login_env[0]).get_invest_button_text()
        assert text == invest_button_of_bid_page_text
