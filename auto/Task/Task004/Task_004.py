# author：wuziwei   
# @time:2020-07-13 23:16
# coding:-*- utf-8 -*-
'''
http://vip.ytesting.com/q.do?a&id=ff8080817345903c017348c7acac02ec

使用 opms 系统，进入项目管理，新建一个项目
添加成功即可，不需要做其他操作
浏览器访问    127.0.0.1:8088
OPMS开源部署用户登录信息
用户名：libai
密码：opmsopms123
'''

import time
from selenium import webdriver

driver = webdriver.Chrome(r'D:\project_learn\chromedriver.exe')

url = driver.get('http://127.0.0.1:8088')
driver.maximize_window()

driver.implicitly_wait(3)
# 定位账号输入框，输入账号
driver.find_element_by_name('username').send_keys('libai')
# 定位密码输入框，输入密码
driver.find_element_by_name('password').send_keys('opmsopms123')
# 定位登录并提交
driver.find_element_by_css_selector('.btn-block').submit()

# 定位项目管理并点击
time.sleep(3)
driver.find_element_by_css_selector('li >a > .fa-book').click()
# 定位新项目并点击
time.sleep(2)
driver.find_element_by_css_selector('div .pull-right >.btn.btn-success').click()

# 输入项目信息
time.sleep(3)
project = driver.find_elements_by_css_selector('div.form-group >div .form-control')
for one in project:
    if '请填写名称' in one.get_attribute("placeholder"):
        one.send_keys('项目A')
    elif '取个代号' in one.get_attribute('placeholder'):
        one.send_keys('这是一个小项目')
        break
# 点击空白处
driver.find_element_by_css_selector('span.input-group-addon').click()

# 向下滑动
driver.execute_script('window.scrollBy(0,200)')

time.sleep(2)
# 定位到iframe内嵌网页
iframe = driver.find_element_by_css_selector('iframe.ke-edit-iframe')
# 切换到iframe
driver.switch_to.frame(iframe)
# 输入描述
driver.find_element_by_css_selector('.ke-content').send_keys('我是一个描述 哈哈哈啊')
# 退出iframe
driver.switch_to.default_content()

# 点击提交
driver.find_element_by_css_selector('button.btn-primary').click()

time.sleep(3)
driver.quit()
