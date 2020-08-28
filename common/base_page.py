from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
from common.dir_config import *
from common import mylogger
import logging


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element(self, locator, wait_times=10, poll_frequency=0.5, module_name=""):
        try:
            WebDriverWait(self.driver, wait_times, poll_frequency=poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except:
            logging.error("等待元素出现失败")
            self.screenshot(module_name=module_name)
            raise

    def get_element(self, locator, module_name=""):
        self.wait_element(locator)
        try:
            return self.driver.find_element(locator[0], locator[1])
        except:
            logging.error("查找元素失败")
            self.screenshot(module_name=module_name)
            raise

    def click_element(self, locator, module_name=""):
        self.wait_element(locator)
        try:
            self.get_element(locator).click()
        except:
            logging.error("点击元素失败")
            self.screenshot(module_name=module_name)
            raise

    def get_text_of_element(self, locator, module_name=""):
        self.wait_element(locator)
        try:
            return self.get_element(locator).text
        except:
            logging.error("获取元素文本失败")
            self.screenshot(module_name=module_name)
            raise

    def input_element(self, text, locator, module_name=""):
        self.wait_element(locator)
        try:
            self.get_element(locator).send_keys(text)
        except:
            logging.error("输入文本失败")
            self.screenshot(module_name=module_name)
            raise

    def get_attribute_of_element(self, locator, attribute, module_name=""):
        self.wait_element(locator)
        try:
            return self.get_element(locator).get_attribute(attribute)
        except:
            logging.error("获取元素属性失败")
            self.screenshot(module_name=module_name)
            raise

    def screenshot(self, module_name):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        file_path = screenshot_dir + "/{0}_{1}.png".format(module_name, current_time)
        self.driver.get_screenshot_as_file(file_path)