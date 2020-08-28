from selenium.webdriver.common.by import By


class LoginPageLocators:
    # 用户名输入框
    username_box_locator = (By.XPATH, '1//input[@name="phone"]')
    # 密码输入框
    password_box_locator = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_button_locator = (By.XPATH, '//button[@type="button"]')
    # 错误信息提示
    warn_tips_locator = (By.XPATH, '//div[@class="form-error-info"]')

