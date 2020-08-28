from selenium.webdriver.common.by import By


class IndexPageLocators:
    nick_name_locator = (By.XPATH, '//a[@href="/Member/index.html"]')
    invest_button_locators = (By.XPATH, '//a[text()="抢投标"]')