from page_object.login_page import LoginPage
from page_object.index_page import IndexPage
from page_object.bid_page import BidPage
from page_object.personal_page import PersonalPage
import unittest
from selenium import webdriver
from test_data.common_data import *
from test_data.bid_page_data import *
import pytest


@pytest.mark.usefixtures("login_env")
@pytest.mark.test_bid
class TestBidPage:
    def test_invest(self, login_env):
        login_env[1].login(global_username, global_password)
        IndexPage(login_env[0]).click_first_invest_button()
        self.bid_page = BidPage(login_env[0])
        money_before_invest = float(self.bid_page.get_left_money_in_input_box(attribute_of_money_box))
        self.bid_page.input_price(invest_price)
        self.bid_page.click_invest_button()
        self.bid_page.click_pop_up_button()
        money_after_invest = float(PersonalPage(login_env[0]).get_left_money())
        assert money_after_invest == money_before_invest - invest_price


