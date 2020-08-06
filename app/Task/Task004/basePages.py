# author：wuziwei   
# @time:2020-08-06 23:31
# coding:-*- utf-8 -*-
from app.Task.Task004.drivers import Driver


class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()
