# author：wuziwei   
# @time:2020-07-18 11:52
# coding:-*- utf-8 -*-

from selenium import webdriver
from auto.Task.Task006.settings import DRIVERPATH, URL


class Driver:
    """浏览器驱动工具类"""
    # 初始化为 None
    driver = None

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

        return cls.driver

    @classmethod
    def login_free(cls):
        cookies = [
            {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/',
             'secure': False, 'value': '1595062125'},
            {'domain': '127.0.0.1',  'httpOnly': False,
             'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/',
             'secure': False, 'value': '1595062125'},
            {'domain': '127.0.0.1',  'httpOnly': True, 'name': 'beegosessionID', 'path': '/',
             'secure': False, 'value': '282cef6935d2fb34bf94c1191c14f0f7'}]
        cls.driver.delete_all_cookies()
        for cookie in cookies:
            cls.driver.add_cookie(cookie)
