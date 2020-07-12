# author：wuziwei   
# @time:2020-07-12 21:03
# coding:-*- utf-8 -*-
'''
http://vip.ytesting.com/q.do?a&id=ff8080817238543f01723b6246cc011e

登录 http://www.51job.com
    点击高级搜索
    输入搜索关键词 python
    地区选择 杭州
    职能类别 选 计算机软件 -> 高级软件工程师
    公司性质选 外资 欧美
    工作年限选 1-3 年

搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息

    Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
    Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
    on开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27

'''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r'D:\project_learn\chromedriver.exe')

url = driver.get('http://www.51job.com')
driver.maximize_window()

driver.implicitly_wait(3)

# 点击高级搜索
more_search = driver.find_element_by_css_selector('.more').click()

# 输入搜索关键词 python
input_python = driver.find_element_by_css_selector('.el.on >p.ipt >input').send_keys('python')

# 地区选择 杭州
driver.find_element_by_css_selector('.el.on >p.addbut > input').click()
city_id = driver.find_elements_by_css_selector('.sbar >li')
for id in city_id:
    if 'H' not in id.text:
        continue
    id.click()

city_choose = driver.find_element_by_id(
    'work_position_click_center_right_list_category_220200_080200').click()

subimt = driver.find_element_by_css_selector('#work_position_click_bottom >#work_position_click_bottom_save').click()

# 职能类别 选 计算机软件 -> 高级软件工程师


time.sleep(5)
# quit()
