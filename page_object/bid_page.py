from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from page_locator.bid_page_locator import BidPageLocator
from common.base_page import BasePage


class BidPage(BidPageLocator, BasePage):
    def input_price(self, price):
        module_name = "BidPage::input_price"
        self.wait_element(locator=self.amount_of_money_box_locator, module_name=module_name)
        self.input_element(price, locator=self.amount_of_money_box_locator, module_name=module_name)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        #     (By.XPATH, BidPageLocator.amount_of_money_box_locator)))
        # self.driver.find_element_by_xpath(BidPageLocator.amount_of_money_box_locator).send_keys(price)

    def click_invest_button(self):
        module_name = "BidPage::click_invest_button"
        self.wait_element(locator=self.invest_button_locator, module_name=module_name)
        self.click_element(locator=self.invest_button_locator, module_name=module_name)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        #     (By.XPATH, BidPageLocator.invest_button_locator)))
        # self.driver.find_element_by_xpath(BidPageLocator.invest_button_locator).click()

    def get_left_money_in_input_box(self, attribute):
        module_name = "BidPage::get_left_money_in_input_box"
        self.wait_element(locator=self.amount_of_money_box_locator, module_name=module_name)
        return self.get_attribute_of_element(locator=self.amount_of_money_box_locator, attribute=attribute, module_name=module_name)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        #     (By.XPATH, BidPageLocator.amount_of_money_box_locator)))
        # return self.driver.find_element_by_xpath(BidPageLocator.amount_of_money_box_locator).get_attribute(attribute)

    def get_invest_button_text(self):
        module_name = "BidPage::get_invest_button_text"
        self.wait_element(locator=self.invest_button_locator, module_name=module_name)
        return self.get_text_of_element(locator=self.invest_button_locator, module_name=module_name)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        #     (By.XPATH, BidPageLocator.invest_button_locator)))
        # return self.driver.find_element_by_xpath(BidPageLocator.invest_button_locator).text

    def click_pop_up_button(self):
        module_name = "BidPage::click_pop_up_button"
        self.wait_element(locator=self.pop_up_locator, module_name=module_name)
        self.click_element(locator=self.pop_up_locator, module_name=module_name)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        #     (By.XPATH, BidPageLocator.pop_up_locator)))
        # self.driver.find_element_by_xpath(BidPageLocator.pop_up_locator).click()

