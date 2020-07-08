# author：wuziwei   
# @time:2020-07-08 20:57
# coding:-*- utf-

from selenium import webdriver

# 创建浏览器对象
driver = webdriver.Chrome(r'D:\project_learn\chromedriver.exe')
# 访问网址
driver.get('http://b.weicantimes.com')

