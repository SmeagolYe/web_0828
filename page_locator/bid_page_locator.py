from selenium.webdriver.common.by import By


class BidPageLocator:
    amount_of_money_box_locator = (By.XPATH, '//input[@class="form-control invest-unit-investinput"]')
    invest_button_locator = (By.XPATH, '//button[text()="投标"]')
    pop_up_locator = (By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')