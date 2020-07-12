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

driver.maximize_window()

time.sleep(1)

# 获取所有一级菜单
title_list = driver.find_elements_by_css_selector('.category-list >li')

for category in title_list:
    # 打印一级菜单
    main_category = category.find_element_by_css_selector('a >span').text
    print(f'一级菜单：{main_category}')
    # 鼠标悬停
    ActionChains(driver).move_to_element(category).perform()
    # 匹配每一个二级菜单
    main_category2 = category.find_elements_by_css_selector('li.subcate-item')
    for category2 in main_category2:
        main_category = category2.text
        print(f'\t 二级菜单：{main_category}')
print('=' * 10, '分割符', '=' * 10)

time.sleep(1)
# 向下滚动
driver.execute_script('window.scrollBy(0,1000)')
time.sleep(1)
# 找到每个单品
product = driver.find_elements_by_css_selector('.span-968.fl>ul.grid-list.clearfix >li')

time.sleep(5)
for one in product:
    # 判断标题存不存在
    product_mark = one.find_elements_by_css_selector('.thumb >span')
    if not product_mark:
        continue
    # 获取商品名称
    product_name = one.find_element_by_css_selector('div').text
    # 获取商品价格
    product_prize = one.find_element_by_css_selector('p.grid-price').text
    # 获取标题名称
    product_mark_name = one.find_element_by_css_selector('span').text
    print(f'{product_name}:{product_mark_name},价格{product_prize}')

time.sleep(1.5)
driver.quit()
