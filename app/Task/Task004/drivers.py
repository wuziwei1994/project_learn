# author：wuziwei   
# @time:2020-08-06 23:31
# coding:-*- utf-8 -*-

from app.Task.Task004.config import boss
from appium import webdriver


class Driver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', boss)
            cls.driver.implicitly_wait(3)
        return cls.driver
