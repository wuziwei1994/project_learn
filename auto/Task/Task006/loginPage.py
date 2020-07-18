# author：wuziwei   
# @time:2020-07-18 16:00
# coding:-*- utf-8 -*-

from auto.Task.Task006.basePage import BasePage
from auto.Task.Task006.settings import USERNAME, PASSWORD
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage(BasePage):
    def __init__(self):
        # 执行父类的构造方法
        super().__init__()

        # 账号框
        self.usernameInputBox = (By.NAME, 'username')
        # 密码框
        self.passwordInputBox = (By.NAME, 'password')
        # 登录按钮
        self.loginBotton = (By.CSS_SELECTOR, '.btn-block')

    def loginUserName(self):
        """用户名输入框获取"""
        return self.get_element(self.usernameInputBox)

    def loginPassWord(self):
        """密码输入框元素定位"""
        return self.get_element(self.passwordInputBox)

    def loginButton(self):
        """登录按钮元素定位"""
        return self.get_element(self.loginBotton)


class Login(LoginPage):
    def login(self):
        self.loginUserName().send_keys(USERNAME)
        self.loginPassWord().send_keys(PASSWORD)
        self.loginButton().click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    Login().login()
