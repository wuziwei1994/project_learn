# author：wuziwei   
# @time:2020-07-18 16:53
# coding:-*- utf-8 -*-

'''
http://vip.ytesting.com/q.do?a&id=ff80808172521d82017256aa835501cc
实现一个  免登陆的 po框架
'''

from selenium import webdriver
from time import sleep
from auto.Task.Task006.settings import DRIVERPATH, URL
from auto.Task.Task006.loginPage import Login


class Driver:
    """浏览器驱动工具类"""
    # 初始化driver对象为 None
    driver = None
    # 初始化cookies对象为 None
    cookies = None

    @classmethod
    def get_driver(cls, browser_name="Chrome"):
        '''
        获取浏览器对象，最大化浏览器并访问默认网页
        Args:
            browserNname: 默认为空，可填写浏览器类型，目前只支持Chrome

        Returns:
        '''
        # 判断driver对象是否为空
        if cls.driver is None:
            # 如果driver对象为空时，判断浏览器名称，并赋值新的driver对象
            if browser_name == 'Chrome':
                cls.driver = webdriver.Chrome(DRIVERPATH['Chrome'])
            # 浏览器最大化
            cls.driver.maximize_window()
            # 浏览器访问地址
            cls.driver.get(URL)
            # 调用免登陆对象
            cls.login_free()
            sleep(1)
            # 调用刷新
            cls.driver.refresh()
            sleep(1)
            cls.driver.quit()
        return cls.driver

    @classmethod
    def get_cookie(cls):
        """获取cookies，并返回cookies"""
        cls.cookies = Login().login()
        return cls.cookies

    @classmethod
    def login_free(cls):
        """获取cookies，删除原cookies，添加新cookies"""
        # 判断cookie是否为空，如果是则调用获取cookies方法
        if cls.cookies is None:
            # 调用cookies获取方法
            cls.get_cookie()
            # 删除原本的cookies
            cls.driver.delete_all_cookies()
        # 循环添加cookies
        for cookie in cls.cookies:
            cls.driver.add_cookie(cookie)


if __name__ == '__main__':
    Driver().get_driver()
