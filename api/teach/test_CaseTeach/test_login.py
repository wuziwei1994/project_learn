# author：xintian   
# time:2020-06-17
#-*- coding: utf-8 -*-
from Lib.ApiLogin import LoginClass
import pytest
import json
import allure
from Lib.GetExcelData import get_excelData
@allure.feature('登录模块')
@allure.story("登录接口")
@allure.title("登录接口用例")
@allure.severity("critical")
@pytest.mark.login(order = 1)#标签--
@pytest.mark.parametrize('inData,repsData',get_excelData('1-登录接口',2,5,6,8))
def test_login(inData,repsData):
    """登录操作"""
    res = LoginClass().api_login(inData,getSession = False)
    assert json.loads(res)['retcode'] == json.loads(repsData)['retcode']#断言
@allure.severity("critical")
@allure.story("登录界面")
@allure.description("这里只是做一个web ui自动化的截图效果")
def test_login_image():
    allure.attach.file(r'../data/test.jpg', '我是附件截图的名字',attachment_type=allure.attachment_type.JPG)
