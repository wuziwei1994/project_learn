# author：wuziwei
# @time:2020-07-15 22:25
# coding:-*- utf-8 -*-
'''
http://vip.ytesting.com/q.do?a&id=ff80808172480d2501724baa8a7801ca
'''

from selenium import webdriver
from time import sleep


class Login:
    '''登录元素类'''

    def __init__(self):
        '''初始化driver对象'''
        self.driver = webdriver.Chrome(r'D:\project_learn\chromedriver.exe')
        self.driver.get('http://127.0.0.1:8088')
        self.driver.maximize_window()

    def loginUserName(self):
        '''用户名输入框获取'''
        userName = self.driver.find_element_by_name('username')
        return userName

    def loginPassWord(self):
        '''密码输入框元素定位'''
        passWord = self.driver.find_element_by_name('password')
        return passWord

    def loginButton(self):
        button = self.driver.find_element_by_css_selector('.btn-block')
        return button


class LoginPage(Login):
    '''继承登录元素父类'''

    def login(self):
        '''登录'''
        self.loginUserName().send_keys('libai')
        self.loginPassWord().send_keys('opmsopms123')
        self.loginButton().click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    LoginPage().login()
