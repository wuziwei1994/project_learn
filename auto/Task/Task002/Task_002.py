# author：wuziwei   
# @time:2020-07-12 10:38
# coding:-*- utf-8 -*-

'''
http://vip.ytesting.com/q.do?a&id=ff80808171274e2d01712fd65eff0634

""
访问: https://www.vmall.com/
获取一级菜单下包含哪些二级菜单

然后获取底部，热销单品中所有 顶部 带有 爆款字样的产品名称及价格

打印成这样

补充阅读：
用selenium做自动化，有时候会遇到需要模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键、拖拽等等。而selenium给我们提供了一个类来处理这类事件——ActionChains

ActionChains 类提供了鼠标操作的常用方法：

perform()： 执行操作

context_click()： 右击；

double_click()： 双击；

drag_and_drop()： 拖动；

move_to_element()： 鼠标悬停。
'''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r'D:\project_learn\chromedriver.exe')

url = driver.get('https://www.vmall.com/')

title_list = driver.find_elements_by_css_selector('.category-list')

for one in title_list:
    print(one.find_element_by_css_selector())

time.sleep(1.5)
driver.quit()
