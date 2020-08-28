from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_locator.index_page_locators import IndexPageLocators
from common.base_page import BasePage


class IndexPage(IndexPageLocators, BasePage):
    def get_nick_name(self):
        module_name = "IndexPage::get_nick_name"
        self.wait_element(locator=self.nick_name_locator, module_name=module_name)
        return self.get_text_of_element(self.nick_name_locator, module_name=module_name)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        #     (By.XPATH, IndexPageLocators.nick_name_locator)))
        #
        # return self.driver.find_element_by_xpath(IndexPageLocators.nick_name_locator).text

    def click_first_invest_button(self):
        module_name = "IndexPage::click_first_invest_button"
        self.wait_element(locator=self.invest_button_locators, module_name=module_name)
        self.click_element(locator=self.invest_button_locators, module_name=module_name)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        #     (By.XPATH, IndexPageLocators.invest_button_locators)))
        # self.driver.find_element_by_xpath(IndexPageLocators.invest_button_locators).click()