from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_locator.login_page_locators import LoginPageLocators
from common.base_page import BasePage


class LoginPage(LoginPageLocators, BasePage):
    def login(self, username, password):
        module_name = "LoginPage::login"
        self.wait_element(self.username_box_locator, module_name=module_name)
        self.input_element(username, locator=self.username_box_locator, module_name=module_name)
        self.input_element(password, locator=self.password_box_locator, module_name=module_name)
        self.click_element(self.login_button_locator, module_name=module_name)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.username_box_locator)))
        # self.driver.find_element_by_xpath(self.username_box_locator).send_keys(username)
        # self.driver.find_element_by_xpath(self.password_box_locator).send_keys(password)
        # self.driver.find_element_by_xpath(self.login_button_locator).click()

    def get_warn_tips(self):
        module_name = "LoginPage::get_warn_tips"
        self.wait_element(self.warn_tips_locator, module_name=module_name)
        return self.get_text_of_element(self.warn_tips_locator, module_name=module_name)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.warn_tips_locator)))
        # return self.driver.find_element_by_xpath(self.warn_tips_locator).text