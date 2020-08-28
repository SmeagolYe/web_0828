from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from page_locator.personal_page_locator import PersonalPageLocator
from common.base_page import BasePage


class PersonalPage(PersonalPageLocator, BasePage):
    def get_left_money(self):
        module_name = "PersonalPage::get_left_money"
        self.wait_element(locator=self.left_money_locator, module_name=module_name)
        return self.get_text_of_element(locator=self.left_money_locator, module_name=module_name).strip("元")
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        #     (By.XPATH, self.left_money_locator)))
        # return self.driver.find_element_by_xpath(self.left_money_locator).text.strip("元")